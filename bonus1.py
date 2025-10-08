#Bodu mass index calculator


weight:str = input("Type your weight: ")

height:str = input("Type your height: ")


bmi = ( int(weight) * 10000 / int(height) **2 )

print(f"Your BMI is: {bmi}")

if bmi <=18:
    print("You are underweight!")

elif 25 > bmi > 18:
    print("Healthy")

else:
    print("You are overweight!") 