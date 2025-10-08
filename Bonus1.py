wieght = int(input("Enter Yore wieght: "))
height = int(input("Enter Yore height: "))

BMI = wieght / (height/100) ** 2
print(BMI)

if BMI < 18.5 :
    print("You are underweight. Watch your health.")
elif BMI >= 18.5 and BMI <= 24.9 :
    print("You are fit & healthy.")
else :
   print( "You are overwieght you need to work out more and watch your diet.")

# Abdulrahman Al-Qahtani