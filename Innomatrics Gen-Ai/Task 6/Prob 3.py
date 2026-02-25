# 3) Movie Theatre Seat Occupancy Analyzer

def theatre_occupancy(total_seats, booked_seats):
    booked = len(booked_seats)
    occupancy = (booked / total_seats) * 100

    print(f"Occupancy: {int(occupancy)}%")

    if occupancy == 100:
        print("Show Status: Housefull")
    elif occupancy >= 75:
        print("Show Status: Almost Full")
    else:
        print("Show Status: Seats Available")


theatre_occupancy(200, [1]*150)
     