movi_name = "Frozen"
movi_rating = 3
popularity_score = 72.65

if movi_rating >= 4 and popularity_score > 80:
    print("Highly recommended")

elif movi_rating >= 3 and popularity_score > 70:
    print("I recommended it . It is good")

elif movi_rating <= 2 and popularity_score > 60:
    print("You should check it out!")

else:
    print("Don't watch it. It is a waste of time")