#Creating Variables
movieName:str = "Smurfs"
movieRate:int = 3
popularityScore:float = 72.65

if movieRate >= 4 and popularityScore > 80:
    print("Highly recommended")
elif movieRate >= 3 and popularityScore > 70:
    print("I recommended it . It is good")
elif  movieRate <= 2 and popularityScore > 60:
    print("You should check it out!")
else:
    print("Don't watch it. It is a waste of time")
