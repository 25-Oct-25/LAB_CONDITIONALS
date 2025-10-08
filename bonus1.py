# Bonus 1
# write a program that Calculates the BMI (body mass index) of the user:

#Ask user
wieght= float(input("Enter your wieght(kg): "))
height= float(input("Enter your height(m): "))

#Calculate BMI
bmi= wieght/(height**2)
#Print BMI to user
print(f"Your body mass index is: {bmi:.2f}")

#Determine the BMI category
if bmi < 18.5:
    print("You are underweight. Watch your health.")
elif  18.5 <= bmi < 25:
    print("You are fit & healthy.")
elif  25 <= bmi < 30:
    print("You are overwieght you need to work out more and watch your diet.")
elif bmi >=30:
    print("You are obese. please consult your doctor.")


