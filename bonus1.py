wieght = float(input("Enter your weight in kg: "))
height_cm = float(input("Enter your height in meters: "))

height = height_cm / 100
bmi = wieght / (height ** 2)

print("Your BMI is:", round(bmi, 2))

if bmi > 25:
    print("You are overweight. You need to work out more and watch your diet.")
elif bmi >= 18.5:
    print("You are fit & healthy.")
else:
    print("You are underweight. Watch your health.")