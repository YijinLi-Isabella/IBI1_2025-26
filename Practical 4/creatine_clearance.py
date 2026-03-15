# 1. define the variables: age, weight, gender, cr(creatine_concentration)
# 2. check the variables
#   - age < 100
#   - 20 < weight 80
#   - gender = male or female
#   - 0 < cr < 100
# 3. calculate crcl
age = float(input("Please enter your age (in years):"))
weight = float(input("Please enter your weight (in kg):"))
gender = input("Please enter your gender (male or female):")
cr = float(input("Please enter your creatine concentration (in μmol/l):"))
if age >= 100:
    print("age must be less than 100 years old")
elif weight <= 20 or weight >= 80:
    print("weight must be between 20 and 80 kg")
elif cr <= 0 or cr >= 100:
    print("creatine concentration must be between 0 and 100 μmol/l")
elif gender not in ["male", "female"]:
    print("gender must be either 'male' or 'female'")
else: 
    crcl = (140 - age) * weight / (72 * cr)
    if gender == "female":
        crcl *= 0.85
    print("Creatine clearance rate (CrCl):", crcl, "ml/min")
