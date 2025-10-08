movie = "Enola Holmes"
rate:int = 3
popularityScore:float = 72.65

if rate >= 4 and popularityScore > 80:
    print("Highly recommended")
elif rate >=3 and popularityScore > 70:
    print("I recommended it. It is good") 
elif rate <=2 and popularityScore > 60:
    print("You should check it out!")
else:
    print("Don't Watch it. It is a waste of time")