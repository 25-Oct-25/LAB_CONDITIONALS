
wieght=input("Plase Enter Your Wieght : ")
height=input("Please Enter Your Heght : ")
height_meter=float(height)/100
BMI=float(wieght)/(height_meter**2)
print(f"Your BMI is : {BMI}")

if BMI < 18.5 :
    print("You are underweight. watch your helth.")
elif BMI >= 18.5 and BMI <= 24.9 :
    print("You are fit & healthy")
elif BMI > 25 and BMI <=29.9:
    print("You are in the weight gain stage . you need to pay attention to your food and work out more")
elif BMI >= 30:
    print("You are overwieght you need to work out more and watch your diet")