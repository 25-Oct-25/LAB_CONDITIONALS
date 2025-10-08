print("To calculate your BMT please fill in the needed information")
userWieght = float(input("Enter your Wieght in kilograms: \n"))
userHeight = float(input("Enter your Height in meters: \n"))
bmi = userWieght / (userHeight ** 2)
print (f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight. Watch your health.")
elif bmi < 25:
    print("You are fit & healthy.")
elif bmi < 30:
    print("You are overwieght.")
else:
    print("Obese you need to work out more and watch your diet.")