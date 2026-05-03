# ===== 1. create a new python class =====
class food_item(object):
    def __init__(self, name, calories, protein, carbohydrate, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrate = carbohydrate
        self.fat = fat

# ===== 2. write a function to take the food list =====
def daily_intake(food_list):
    total_calories = 0
    total_protein = 0
    total_carbohydrate = 0
    total_fat = 0
    for food in food_list:
        total_calories += food.calories
        total_protein += food.protein
        total_carbohydrate += food.carbohydrate
        total_fat += food.fat

    # print the total intake
    print("Total calories:", total_calories, "calories")
    print("Total protein:", total_protein, "g")
    print("Total carbohydrate:", total_carbohydrate, "g")
    print("Total fat:", total_fat, "g")
        
        # warning
    if total_calories > 2500:
        print("Warning: calorie intake is above 2500 calories.")

    if total_fat > 90:
        print("Warning: fat intake is above 90 g.")

# ===== 3. an example to use the class and function =====
apple = food_item("apple", 60, 0.3, 15, 0.5)
rice = food_item("rice", 200, 4, 45, 0.4)
chicken = food_item("chicken", 300, 30, 0, 8)
today_food = [apple, rice, chicken]
daily_intake(today_food)