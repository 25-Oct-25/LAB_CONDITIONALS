weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters (example: 1.75):"))
BMI = weight / height **2
print(f"your BMI is: {BMI} " )
if BMI < 18.5 :
    print("You are underweight.")
elif 18.5 <= BMI <= 25 :
    print("Your weight is normal.")
else :
    print("You are obese.")
