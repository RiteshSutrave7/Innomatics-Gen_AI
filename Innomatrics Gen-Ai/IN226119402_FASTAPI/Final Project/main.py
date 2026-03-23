from fastapi import FastAPI, Response, status, Query
from pydantic import BaseModel, Field
from typing import Optional, List
import math

app = FastAPI()

# ==========================================
# 1. DATA SETUP
# ==========================================

movies = [
    {"id": 1, "title": "Avengers: Endgame", "genre": "Action", "language": "English", "duration_mins": 181, "ticket_price": 250, "seats_available": 100},
    {"id": 2, "title": "Inception", "genre": "Sci-Fi", "language": "English", "duration_mins": 148, "ticket_price": 300, "seats_available": 50},
    {"id": 3, "title": "Dangal", "genre": "Drama", "language": "Hindi", "duration_mins": 161, "ticket_price": 200, "seats_available": 120},
    {"id": 4, "title": "The Conjuring", "genre": "Horror", "language": "English", "duration_mins": 112, "ticket_price": 220, "seats_available": 0},
    {"id": 5, "title": "Hera Pheri", "genre": "Comedy", "language": "Hindi", "duration_mins": 156, "ticket_price": 150, "seats_available": 80},
    {"id": 6, "title": "Parasite", "genre": "Drama", "language": "Korean", "duration_mins": 132, "ticket_price": 350, "seats_available": 40}
]

bookings = []
booking_counter = 1

holds = []
hold_counter = 1

# ==========================================
# 2. PYDANTIC MODELS (Day 2)
# ==========================================

class BookingRequest(BaseModel):
    customer_name: str = Field(..., min_length=2)
    movie_id: int = Field(..., gt=0)
    seats: int = Field(..., gt=0, le=10)
    phone: str = Field(..., min_length=10)
    seat_type: str = Field(default="standard")
    promo_code: str = Field(default="")

class NewMovie(BaseModel):
    title: str = Field(..., min_length=2)
    genre: str = Field(..., min_length=2)
    language: str = Field(..., min_length=2)
    duration_mins: int = Field(..., gt=0)
    ticket_price: int = Field(..., gt=0)
    seats_available: int = Field(..., gt=0)

class SeatHoldRequest(BaseModel):
    customer_name: str = Field(..., min_length=2)
    movie_id: int = Field(..., gt=0)
    seats: int = Field(..., gt=0)

# ==========================================
# 3. HELPER FUNCTIONS (Day 3)
# ==========================================

def find_movie(movie_id: int):
    for m in movies:
        if m['id'] == movie_id:
            return m
    return None

def calculate_ticket_cost(base_price: int, seats: int, seat_type: str, promo_code: str = ""):
    multiplier = 1.0
    if seat_type.lower() == "premium":
        multiplier = 1.5
    elif seat_type.lower() == "recliner":
        multiplier = 2.0
    
    original_cost = int(base_price * seats * multiplier)
    
    discount_percent = 0
    if promo_code == "SAVE10":
        discount_percent = 10
    elif promo_code == "SAVE20":
        discount_percent = 20
        
    discounted_cost = int(original_cost * (1 - discount_percent / 100))
    return original_cost, discounted_cost

def filter_movies_logic(movie_list: list, genre: str = None, language: str = None, max_price: int = None, min_seats: int = None):
    filtered = movie_list
    if genre is not None:
        filtered = [m for m in filtered if m['genre'].lower() == genre.lower()]
    if language is not None:
        filtered = [m for m in filtered if m['language'].lower() == language.lower()]
    if max_price is not None:
        filtered = [m for m in filtered if m['ticket_price'] <= max_price]
    if min_seats is not None:
        filtered = [m for m in filtered if m['seats_available'] >= min_seats]
    return filtered

# ==========================================
# 4. FIXED ROUTES (Must be placed before variable routes /{id})
# ==========================================

# Q1: Home Route
@app.get('/')
def home():
    return {'message': 'Welcome to CineStar Booking'}

# Q5: Movie Summary
@app.get('/movies/summary')
def movie_summary():
    if not movies:
        return {"error": "No movies available"}
    
    genre_counts = {}
    for m in movies:
        genre_counts[m['genre']] = genre_counts.get(m['genre'], 0) + 1
        
    cheapest = min(movies, key=lambda x: x['ticket_price'])
    priciest = max(movies, key=lambda x: x['ticket_price'])
    total_seats = sum(m['seats_available'] for m in movies)
    
    return {
        "total_movies": len(movies),
        "most_expensive_ticket": {"title": priciest['title'], "price": priciest['ticket_price']},
        "cheapest_ticket": {"title": cheapest['title'], "price": cheapest['ticket_price']},
        "total_seats_all_movies": total_seats,
        "genre_breakdown": genre_counts
    }

# Q10: Filter Movies
@app.get('/movies/filter')
def filter_movies(
    genre: Optional[str] = None, 
    language: Optional[str] = None, 
    max_price: Optional[int] = None, 
    min_seats: Optional[int] = None
):
    results = filter_movies_logic(movies, genre, language, max_price, min_seats)
    return {"total_found": len(results), "movies": results}

# Q16: Search Movies
@app.get('/movies/search')
def search_movies(keyword: str = Query(..., description="Search title, genre, or language")):
    kw = keyword.lower()
    results = [
        m for m in movies 
        if kw in m['title'].lower() or kw in m['genre'].lower() or kw in m['language'].lower()
    ]
    if not results:
        return {"message": f"No movies found matching '{keyword}'", "total_found": 0, "movies": []}
    return {"total_found": len(results), "movies": results}

# Q17: Sort Movies
@app.get('/movies/sort')
def sort_movies(sort_by: str = "ticket_price", order: str = "asc"):
    valid_sorts = ["ticket_price", "title", "duration_mins", "seats_available"]
    if sort_by not in valid_sorts:
        return {"error": f"Invalid sort_by. Choose from: {valid_sorts}"}
    if order not in ["asc", "desc"]:
        return {"error": "Order must be 'asc' or 'desc'"}
        
    is_desc = (order == "desc")
    sorted_movies = sorted(movies, key=lambda x: x[sort_by], reverse=is_desc)
    
    return {
        "metadata": {"sort_by": sort_by, "order": order},
        "movies": sorted_movies
    }

# Q18: Paginate Movies
@app.get('/movies/page')
def paginate_movies(page: int = Query(1, ge=1), limit: int = Query(3, ge=1, le=10)):
    start = (page - 1) * limit
    end = start + limit
    paginated = movies[start:end]
    total_pages = math.ceil(len(movies) / limit)
    
    return {
        "page": page,
        "limit": limit,
        "total_movies": len(movies),
        "total_pages": total_pages,
        "movies": paginated
    }

# Q20: Combined Browse (Filter -> Sort -> Paginate)
@app.get('/movies/browse')
def browse_movies(
    keyword: Optional[str] = None,
    genre: Optional[str] = None,
    language: Optional[str] = None,
    max_price: Optional[int] = None,
    sort_by: str = "ticket_price",
    order: str = "asc",
    page: int = Query(1, ge=1),
    limit: int = Query(3, ge=1, le=20)
):
    # 1. Filter by keyword
    results = movies
    if keyword:
        kw = keyword.lower()
        results = [m for m in results if kw in m['title'].lower() or kw in m['genre'].lower() or kw in m['language'].lower()]
        
    # 2. Filter by genre/language/price (reusing helper)
    results = filter_movies_logic(results, genre, language, max_price, None)
    
    # 3. Sort
    is_desc = (order == "desc")
    if sort_by in ["ticket_price", "title", "duration_mins", "seats_available"]:
        results = sorted(results, key=lambda x: x[sort_by], reverse=is_desc)
        
    # 4. Paginate
    total_results = len(results)
    start = (page - 1) * limit
    paginated = results[start : start + limit]
    
    return {
        "metadata": {
            "keyword": keyword,
            "filters_applied": {"genre": genre, "language": language, "max_price": max_price},
            "sort_settings": {"sort_by": sort_by, "order": order},
            "pagination": {
                "page": page,
                "limit": limit,
                "total_found": total_results,
                "total_pages": math.ceil(total_results / limit)
            }
        },
        "movies": paginated
    }

# Q19: Bookings Search, Sort, Page
@app.get('/bookings/search')
def search_bookings(customer_name: str = Query(...)):
    name = customer_name.lower()
    results = [b for b in bookings if name in b['customer_name'].lower()]
    return {"total_found": len(results), "bookings": results}

@app.get('/bookings/sort')
def sort_bookings(sort_by: str = "total_cost", order: str = "asc"):
    if sort_by not in ["total_cost", "seats"]:
        return {"error": "Can only sort bookings by 'total_cost' or 'seats'"}
    is_desc = (order == "desc")
    sorted_b = sorted(bookings, key=lambda x: x[sort_by], reverse=is_desc)
    return {"bookings": sorted_b}

@app.get('/bookings/page')
def paginate_bookings(page: int = Query(1, ge=1), limit: int = Query(3, ge=1)):
    start = (page - 1) * limit
    paginated = bookings[start : start + limit]
    return {
        "page": page,
        "total_pages": math.ceil(len(bookings) / limit) if bookings else 0,
        "bookings": paginated
    }

# ==========================================
# 5. STANDARD & VARIABLE ROUTES
# ==========================================

# Q2: Get all movies
@app.get('/movies')
def get_movies():
    total_seats = sum(m['seats_available'] for m in movies)
    return {"total": len(movies), "total_seats_available": total_seats, "movies": movies}

# Q11: Add a new movie
@app.post('/movies', status_code=status.HTTP_201_CREATED)
def add_movie(movie: NewMovie, response: Response):
    if any(m['title'].lower() == movie.title.lower() for m in movies):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": f"Movie '{movie.title}' already exists"}
        
    new_id = max((m['id'] for m in movies), default=0) + 1
    new_movie = {"id": new_id, **movie.model_dump()}
    movies.append(new_movie)
    return {"message": "Movie added", "movie": new_movie}

# Q3: Get movie by ID
@app.get('/movies/{movie_id}')
def get_movie(movie_id: int, response: Response):
    movie = find_movie(movie_id)
    if not movie:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "Movie not found"}
    return movie

# Q12: Update movie
@app.put('/movies/{movie_id}')
def update_movie(movie_id: int, response: Response, ticket_price: Optional[int] = None, seats_available: Optional[int] = None):
    movie = find_movie(movie_id)
    if not movie:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "Movie not found"}
        
    if ticket_price is not None:
        movie['ticket_price'] = ticket_price
    if seats_available is not None:
        movie['seats_available'] = seats_available
        
    return {"message": "Movie updated", "movie": movie}

# Q13: Delete movie
@app.delete('/movies/{movie_id}')
def delete_movie(movie_id: int, response: Response):
    movie = find_movie(movie_id)
    if not movie:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "Movie not found"}
        
    # Check if movie has active bookings
    if any(b['movie_id'] == movie_id for b in bookings):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "Cannot delete movie. Active bookings exist."}
        
    movies.remove(movie)
    return {"message": f"Movie '{movie['title']}' deleted successfully"}

# Q4: Get all bookings
@app.get('/bookings')
def get_bookings():
    total_revenue = sum(b['total_cost'] for b in bookings)
    return {"total": len(bookings), "total_revenue": total_revenue, "bookings": bookings}

# Q8 & Q9: Create a booking
@app.post('/bookings', status_code=status.HTTP_201_CREATED)
def create_booking(req: BookingRequest, response: Response):
    global booking_counter
    movie = find_movie(req.movie_id)
    
    if not movie:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "Movie not found"}
        
    if movie['seats_available'] < req.seats:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": f"Not enough seats. Only {movie['seats_available']} available."}
        
    # Calculate costs
    orig_cost, final_cost = calculate_ticket_cost(
        base_price=movie['ticket_price'],
        seats=req.seats,
        seat_type=req.seat_type,
        promo_code=req.promo_code
    )
    
    # Deduct seats
    movie['seats_available'] -= req.seats
    
    booking_record = {
        "booking_id": booking_counter,
        "customer_name": req.customer_name,
        "movie_id": movie['id'],
        "movie_title": movie['title'],
        "seats": req.seats,
        "seat_type": req.seat_type,
        "promo_code": req.promo_code,
        "original_cost": orig_cost,
        "total_cost": final_cost,
        "status": "confirmed"
    }
    
    bookings.append(booking_record)
    booking_counter += 1
    
    return {"message": "Booking successful", "booking": booking_record}

# ==========================================
# 6. SEAT HOLD WORKFLOW (Q14 & Q15)
# ==========================================

# Q14: Create a seat hold
@app.post('/seat-hold', status_code=status.HTTP_201_CREATED)
def create_seat_hold(req: SeatHoldRequest, response: Response):
    global hold_counter
    movie = find_movie(req.movie_id)
    
    if not movie:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "Movie not found"}
        
    if movie['seats_available'] < req.seats:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": "Not enough seats available to hold."}
        
    # Temporarily deduct seats
    movie['seats_available'] -= req.seats
    
    hold_record = {
        "hold_id": hold_counter,
        "customer_name": req.customer_name,
        "movie_id": movie['id'],
        "movie_title": movie['title'],
        "seats": req.seats,
        "status": "held"
    }
    
    holds.append(hold_record)
    hold_counter += 1
    
    return {"message": "Seats held successfully", "hold": hold_record}

# Q14: View all holds
@app.get('/seat-hold')
def get_holds():
    return {"total_holds": len(holds), "holds": holds}

# Q15: Confirm Hold -> Booking
@app.post('/seat-confirm/{hold_id}', status_code=status.HTTP_201_CREATED)
def confirm_seat_hold(hold_id: int, response: Response):
    global booking_counter
    
    # Find the hold
    hold_record = next((h for h in holds if h['hold_id'] == hold_id), None)
    if not hold_record:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "Hold record not found"}
        
    movie = find_movie(hold_record['movie_id'])
    
    # Create booking (seats are already deducted)
    orig_cost, final_cost = calculate_ticket_cost(movie['ticket_price'], hold_record['seats'], "standard")
    
    new_booking = {
        "booking_id": booking_counter,
        "customer_name": hold_record['customer_name'],
        "movie_id": hold_record['movie_id'],
        "movie_title": hold_record['movie_title'],
        "seats": hold_record['seats'],
        "seat_type": "standard",
        "promo_code": "",
        "original_cost": orig_cost,
        "total_cost": final_cost,
        "status": "confirmed"
    }
    
    bookings.append(new_booking)
    booking_counter += 1
    
    # Remove from holds list
    holds.remove(hold_record)
    
    return {"message": "Hold confirmed and converted to booking", "booking": new_booking}

# Q15: Release Hold (Cancel)
@app.delete('/seat-release/{hold_id}')
def release_seat_hold(hold_id: int, response: Response):
    hold_record = next((h for h in holds if h['hold_id'] == hold_id), None)
    if not hold_record:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "Hold record not found"}
        
    # Return seats to available pool
    movie = find_movie(hold_record['movie_id'])
    if movie:
        movie['seats_available'] += hold_record['seats']
        
    holds.remove(hold_record)
    
    return {"message": f"Hold {hold_id} released. Seats added back to availability."}