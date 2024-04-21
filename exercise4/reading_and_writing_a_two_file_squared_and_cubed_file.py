# Delima, Sheena Mae D.
# BSCPE 1-2
# April 21, 2024

# ------------------------------------------------------

# ========= PSEUDO CODE =========
# || LIBRARIES / PACKAGES ||
import csv

# || VARIABLES || 

# || FUNCTIONS ||

# || ACTUAL CODES ||
# - Opening the file and reading the file.
with open("C:/Users/Myline/Desktop/OOP/Assignment 4/python_file_handling/exercise4/positive_integers_file.csv", "r") as file:
    reader = csv.reader(file)

# - Writing a file: squared_integers and cubed_integers.
    with open("triple.csv", "w", newline="") as output1, open("doubled.csv", "w", newline="") as output2:
        tripled_file = csv.writer(output1)
        doubled_file = csv.writer(output2)
        

        
