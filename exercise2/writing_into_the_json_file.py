# Delima, Sheena Mae Delima
# BSCPE 1-2
# April 20, 2024

# --------------------------------------------

# ========== PSEUDO CODE ===========
# || LIBRARIES \ PACKAGES ||
import json


# || VARIABLES ||
user_name = input("Enter your name:")
user_age = int(input("Enter your age:"))
user_fav_food = input("Enter your favorite food:")
user_fav_color = input("Enter your favorite color:")
user_role_model = input("Enter your role model/s:")
user_mentor_in_programming = input("Enter who taught you this file handling so early:")


# || ACTUAL CODE ||
# - Stored data of various questions.

life_data = {
    "Name" : user_name,
    "Age" : user_age,
    "Favorite Food" : user_fav_food,
    "Favorite Color" : user_fav_color,
    "Role Model/s:" : user_role_model,
    "Programming Mentor" : user_mentor_in_programming
}

# - Read the 'life_data' 
content = json.dumps(life_data)

print(content)

# - Code for creating a new JSON file
with open("user_info", "w") as output_file:
    output_file()
