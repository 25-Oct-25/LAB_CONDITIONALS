
move = 'amazing spider man'
rating:int = 3
popularity:float = 72.65
print("")

if rating >= 4 and popularity >= 80 :
    print("Highly recommended")
    print(f"Move name : {move} \nMove rating : {rating} Out of 5 \nMove popularity : % {popularity}")
elif rating >= 3 and popularity >= 70 :
    print("I recommended it . It is good")
    print(f"Move name : {move} \nMove rating : {rating} Out of 5 \nMove popularity : % {popularity}")
elif rating >= 2 and popularity >= 60 :
    print("You should check it out!")
    print(f"Move name : {move} \nMove rating : {rating} Out of 5 \nMove popularity : % {popularity}")
else:
    print("Don't watch it. It is a waste of time")