Wieght = float (input("Enter your wieght: "))
Height = float (input("Enter your height in meters: (for example 1.66) "))

BMI = Wieght / (Height**2)

print("your BMI is: " , round(BMI , 2) )

if BMI >= 25:
    print("You are overwieght you need to work out more and watch your diet.")
elif BMI < 18.5:
    print("You are underweight. Watch your health.")
else:
    print("You are fit & healthy.")