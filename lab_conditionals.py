movie = "Taken"

rating = 3

popularityScore = 72.65


if rating >= 4 and popularityScore > 80:
    print("Highly recommended")

elif rating >= 3 and popularityScore > 70:
    print("I recommended it. It is good")

elif rating <= 2 and popularityScore > 60:
    print("You should check it out!")  

else:
    print("Don't watch it. It is a waste of time")