weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)
print("Your BMI is:", bmi)

if bmi > 25:
    print("You are overweight. You need to work out more and watch your diet.")
elif bmi >= 18.5 and bmi <= 25:
    print("You are fit & healthy.")
else:
    print("You are underweight. Watch your health.")
