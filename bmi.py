
wieght = float(input("Enter your wieght wiegth :"))
height = float(input("Enter your  height :"))

bmi = wieght / (height ** 2)
print("Your BMI is:", round(bmi, 1)) 

if bmi > 25 :
    print("You are overwieght you need to work out more and watch your diet .")
elif 18.5 <= bmi <= 25 :
    print("You are fit & healthy .")
else:
    print("You are underweight. Watch your health .")





