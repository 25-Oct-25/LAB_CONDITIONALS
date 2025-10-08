movie = "UP"
rating :int  = 3 # out of 5
popularity:float = 72.65

if rating >= 4 and popularity > 80 :
    print("Highly recommended")

elif rating >= 3 and popularity > 70 :
    print("I recommended it . It is good")

elif rating <= 2 and popularity > 60 :
    print("You should check it out!")

else :
    rating <= 2 and popularity > 60
    print("Don't watch it. It is a waste of time")

