movie = "interstellar"
rating = int(input("Enter your rating (1-5): "))
score = float(input("Enter your score (0-100): "))

if rating >= 4 and score > 80:
    print("Highly recommended")
elif rating >= 3 and score > 70:
    print("I recommend it. it's good")
elif rating <= 2 and score < 50:
    print("Don't watch it. it is a waste of time")  
