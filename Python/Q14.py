##Create an empty list.Use a loop to ask user 5 times to enter their favourite movies.
##Add each movie to the list.After all inputs, print the whole list.

favourite_movies = []
for i in range(5):
    movie = input("Enter a favourite movie: ")
    favourite_movies.append(movie)
print("Your favourite movies are:", favourite_movies)
