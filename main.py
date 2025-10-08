##نواف البريكان

movie ="Inception"
rating = int(3)
popularity = 72.65
if rating >=4 and popularity> 80:
    print(f"{movie} is Highly recommended")
elif rating >=3 and popularity > 70:
    print("I recommend it . Its good")
elif rating <=2 and popularity > 60:
    print("You should cheeck it out!")
else:
    print("Don't watch it. It is a waste of time")