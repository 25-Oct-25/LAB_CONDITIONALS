#Calculater of BMI
wieght = float(input("Enter your wieght in meters :"))
height = float(input("Enter your height in meters :"))
bmi = wieght / (height**2)

if bmi >= 30:
    print("You are overwieght ," \
    "you need to work out more and watch your diet. ")
elif  bmi <= 29.9 and bmi >= 25 :
    print("You have gained weight, " \
    "you should take more care of your health")
elif  bmi <= 24.9 and bmi >= 18.5:
    print("You are fit & health.")
elif bmi<= 18.5: 
    print("You are underweight ,and watch your health.")