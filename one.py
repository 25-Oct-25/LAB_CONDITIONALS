movie = "Home Alone"
riting = 3
popularity = 72.65

if riting >= 4 and popularity > 80:
    print("Highly recommended")
elif riting >= 3 and popularity > 70:
    print("I recommended it. It is good")
elif riting <= 2 and popularity > 60:
    print("You should check it out!")
elif riting <= 2 and popularity < 50:
    print("Don't watch it. It is a waste of time")