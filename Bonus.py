weight = float(input("weight (kg):"))
height = float(input("height (m): "))

bmi = weight / (height ** 2 )
print(f"Your BMI is: {bmi:.2f}")

if bmi >= 25:
    print("You are overwieght you need to work out more and watch your diet")
elif 18.5 <= bmi < 25:
    print("You are fit & healthy.")
elif bmi < 18.5:
    print("You are underweight. Watch your health.")
