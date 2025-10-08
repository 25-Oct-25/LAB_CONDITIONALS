wieght:str= input("Please enter your wight: ")
height:str= input("Please enter your hight: ")

wieght:float= int(wieght)
height:float= int(height)

BMI:float= round((wieght/height/height)*10000 ,2)

if BMI <18.5:
    print(f"Your BMI is {BMI}.You are underweight. Watch your health.")

elif BMI >=18.5 and BMI<=24.9:
    print(f"Your BMI is {BMI}. You are fit & healthy.")

else:
    BMI >=25
    print(f"Your BMI is {BMI}. You are overwieght you need to work out more and watch your diet.")