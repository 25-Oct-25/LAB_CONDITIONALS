wieght = float(input("Enter your weight in kilograms: "))
hieght = float(input("Enter your height in meters (example: 1.75):"))
BMI = wieght / (hieght ** 2)
if BMI < 18.5 :
    print("You are underweight.")
elif 18.5 <= BMI <= 25 :
    print("Your weight is normal.")
else :
    print("You are obese.")
