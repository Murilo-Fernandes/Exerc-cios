# BMI Calculator with interpretations 
weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("You're underweight.")
elif bmi >= 18.5 and bmi < 25:
    print("Congrats, you have a normal weight.")
else: 
    print("You're overweight.")