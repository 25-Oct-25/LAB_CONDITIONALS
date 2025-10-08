

def calculatesBMI ():
    
    print("Calculates the BMI")

    # You must be enter a float number 
    # or printing an error masseg 
    wieght = float(input("Enter your wieght in kilograms (kg): ")) 
    hight = float(input("Enter your hight in meters (m) : "))

    # If user enter an input of wieght and hight == 0.0
    # Will print an error massge and ratern to the same calculater
    if wieght <= 0.0 or hight <= 0.0 :
        print("Please Enter a vaild wight and hight")
        return calculatesBMI()

    # Calculates the BMI    
    bmi = ( wieght / (hight ** 2) )
    print(f"Your bmi is : {bmi:.2f}\n")

    # Your BMI is :
    if bmi < 18.5:
        print("You are underweight. Watch your health.")
    elif 18.5 <= bmi < 24.9:
        print("You are fit & healthy.")
    elif 25 <= bmi < 29.9:
        print("You are overwieght you need to work out more and watch your diet.")

# To call the function
calculatesBMI()    