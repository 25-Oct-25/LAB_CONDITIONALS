weighat = float(input("inter your weight"))
height = float(input("inter your height"))

BMI:float = weighat / (height **2)

print(f"Your BMI is :{BMI:.2}")

if BMI > 25 :
    print("You are fat , you need to do some workout")

elif BMI >=18.5 :
    print("Your weighat is Perfect")

else :
    print("Your weighat is below the normal , add more caloure to your dait")





