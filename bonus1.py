

# Ask the user to provide his wieght.
wieght = int(input("Enter your wieght: "))
# Ask the user to provide hi height.
height = float(input("Enter your wieght: "))

BMI =  wieght / height**2
print(f"your BMI is {BMI}")


# using conditionals tell the user that either :
# You are overwieght you need to work out more and watch your diet.
# You are fit & healthy.
# You are underweight. Watch your health.
if BMI < 18.5:
    print("You are underweight. Watch your health")
elif BMI >= 18.5 and BMI < 24.9:
    print("You are fit & healthy")
elif BMI >= 25 and BMI < 29.9:
    print("You are overwieght you need to work out more and watch your diet")
