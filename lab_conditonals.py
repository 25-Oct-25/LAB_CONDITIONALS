move = "Lord of the rings"
rating = 3
poprularity:float = 72.65
if rating >= 4 and poprularity > 80 :
   print("Highly recommended") 
elif rating >= 3 and poprularity > 70 :
   print("I recommended it . It is good")
elif rating <= 2 and poprularity > 60 :
   print("You should check it out!")
elif rating <= 2 and poprularity < 50 :
   print("Don't watch it. It is a waste of time")