# define the variables: age, weight, gender, cr(creatine_concentration)
# check the variables
# - age < 100
# - 20 < weight 80
# - gender = male or female
# - 0 < cr < 100
#
age = float(input("Please enter your age"))
weight = float(input("Please enter your weight"))
gender = input("Please enter your gender")
cr = float(input("Please enter your creatine concentration"))
if age >= 100:
    print("age must be less than 100 years old")
elif weight <= 20 or weight >= 80:
    print("weight must be between 20 and 80 kg")
elif cr <= 0 or cr >= 100:
    print("creatine concentration must be between 0 and 100 μmol/l")
elif gender not in ["male", "female"]:
    print("gender must be either 'male' or 'female'")
else: 
    crcl = (140 - age) * weight / (72 * weight)
    if gender == "female":
        crcl *= 0.85
    print("Creatine clearance rate (CrCl):", crcl, "ml/min")
    