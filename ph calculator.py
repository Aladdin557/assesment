import math

def calculate_bmi(weight_kg, height_m):
    ''' Workout MBI takes two parameters: weight and height.and returns bmi value and category'''

    while height_m <= 0:
        return None, "Error: Height must be positive."

    bmi_value = weight_kg / (math.pow(height_m, 2))

    if bmi_value < 18.5:
        category ="Underweight"
    elif 18.5 <= bmi_value < 25:
        category ="Normal"
    elif 25 <=bmi_value < 30:
        category ="Overweight"
    else:
        category ="Obesity"


    return bmi_value, category
weight =float(input("Enter your weight in kg: "))
height =float(input("Enter your height in m: "))

bmi, status = calculate_bmi(weight, height)

if bmi is not None:
    print(f"For a weight of {weight}kg and height of {height}m:")
    print(f"BMI: {bmi:.2f}")
    print(f"Status: {status}")
else:
    print(status)



