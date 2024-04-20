# Delima, Sheena Mae Delima
# BSCPE 1-2
# April 20, 2024

# --------------------------------------------

# ========== PSEUDO CODE ===========
# || LIBRARIES \ PACKAGES ||

# || IMPORTS || 
import csv

# || VARIABLES || 

# || FUNCTIONS

# || ACTUAL CODES ||
# - Opening the file.
with open('python_file_handling\positive_integers.csv', 'r') as file:
    reader = csv.reader(file)
    
    next(reader)
    
    with open('odd_numbers.csv', 'w') as output_file:
        writer = csv.writer(output_file)
        
        
# - For loop code