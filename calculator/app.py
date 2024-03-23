def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
a = calculate_bmi(weight, height)
print(f"Your BMI is: {a}")

if a < 18.5:
    print("You are underweight.")
elif a >= 18.5 and a < 25:
    print("You have a normal weight.")
elif a >= 25 and a < 30:
    print("You are overweight.")
else:
    print("You are obese.")
