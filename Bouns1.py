wieght=float(input("Enter your wieght: "))
hight=float(input("Enter your hight: "))

BMI=wieght/(hight**2)
print(f"Your BMI is {round(BMI,2)}")

if BMI>=25 and BMI<=29.9:
    print("You are overwieght you need to work out more and watch your diet.")
elif BMI>=18 and BMI<=24.9:
    print("You are fit & healthy.")
else:
    print("You are underweight. Watch your health.")        
