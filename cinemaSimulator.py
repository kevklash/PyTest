movies = {
    "Batman V Superman": [16, 5],
    "The Hateful Eight": [16, 5],
    "Alien": [16, 5],
    "The Croods": [8, 5]
}

while True:
    movie = input("What movie would you like to watch?").strip().title()
    # Check if the movie is in the list
    if movie in movies:
        # Check if the age is met
        age = int(input("What's your age?").strip())
        if age >= movies[movie][0]:
            # Check if there are enough tickets
            if movies[movie][1] > 0:
                print("Enjoy the movie!")
                movies[movie][1] = movies[movie][1] - 1
            else:
                print("Sorry, we're sold out!")
        else:
            print("Sorry, you're too young for that movie")
    else:
        print("Sorry, we don't have that movie")