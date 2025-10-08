##نواف البريكان


weight = int(input("Enter your weight in Kg: "))
height = float(input("Enter your height in m: "))
BMI = weight/(height*height)
print(f"Your BMI is {BMI}")
if BMI < 18.5:
    print("You are underweight")
elif BMI >= 18.5 and BMI <= 24.9:
    print("You have a normal weight")
elif BMI >= 25 and BMI <= 29.9:
    print("You are overweight")
elif BMI >=30 and BMI <=39.9:
    print("You have Obesity class 1")
else:
    print("You have Obesity class 2")

