def bmi(weight, height):
    bmi = weight / (height*height)
    result = bmi
    if result <= 18.5:
        print("Underweight")
    if result <= 25.0:
        print("Normal")
    if result <= 30.0:
        print("Overweight")
    if result > 30:
        print("Obese")
bmi(70, 57)