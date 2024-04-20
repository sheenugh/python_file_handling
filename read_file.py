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
with open('positive_integers.csv', 'r') as file:
    reader = csv.reader(file)
    
    next(reader)
    
    with open('odd_numbers.csv', 'w') as output_file:
        writer = csv.writer(output_file)
        
        header = ['Odd Numbers']
        
        writer.writerow(header)
        
        for line in reader:
            writer.writerow([line[0]])
        
# - For loop code