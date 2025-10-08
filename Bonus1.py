wieght = int(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = wieght / (height ** 2)

if bmi < 18.5:
    print("You are underweight. Watch your health")
elif 18.5 <= bmi < 25:
    print("You have a normal weight. Good job!")
elif 25 <= bmi < 30:
    print("You are overwieght you need to work out more and watch your diet")
    