mass=int(input("enter your weight : "))
height=int(input("enter your height in centimetre : "))

bmi=mass/pow(height/100,2)

print("your BMI is ",'%.2f'%bmi)