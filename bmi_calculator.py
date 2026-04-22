height_cm = float(input("Enter your height in centimetres: "))
weight_kg = float(input("Enter your weight in kilograms: "))

height_m = height_cm / 100
bmi = weight_kg / (height_m ** 2)
rounded_bmi = round(bmi, 1)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Your BMI is {rounded_bmi}")
print(f"Category: {category}")
