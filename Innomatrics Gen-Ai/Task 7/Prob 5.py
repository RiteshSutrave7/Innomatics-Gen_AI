# 5) Movie Rating Display System
# Create class Movie 
class Movie:
    def __init__(self, movie_name, rating):
        self.name = movie_name
        self.rating = rating
    def show(self):
        print("Movie:", self.name)
        print("Rating:", str(self.rating) + " / 5")

movie_name = input("Movie Name: ")
rating = float(input("Rating: "))

m = Movie(movie_name, rating)
m.show()