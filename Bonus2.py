weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))
height = height / 100  # convert cm to meters

bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight. Watch your health.")
elif bmi < 25:
    print("You are fit & healthy.")
elif bmi < 30:
    print("You are overweight. You need to work out more and watch your diet.")
else:
    print("You are obese. Consult a doctor for health advice.")
