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
def process_integers():
    with open("positive_integers_file.cs", "r") as file:
        reader = csv.reader(file)
    
    # Loop through the rows in the CSV file
        integers = [int(row[0]) for row in reader[:20]]

# - Writing a file: squared_integers and cubed_integers.
    with open("triple.csv", "w", newline="") as output1, open("doubled.csv", "w", newline="") as output2:
        tripled_file = csv.writer(output1)
        doubled_file = csv.writer(output2)
        
# Loop through the integers
        for num in integers:
            # Check if the number is even
            if num % 2 == 0:
                # Write the square of the number to the double.csv file
                doubled_file.writerow([num ** 2])
            else:
                # Write the cube of the number to the triple.csv file
                tripled_file.writerow([num ** 3])v

# Call the function
process_integers()
        
        

        
