# Delima, Sheena Mae Delima
# BSCPE 1-2
# April 20, 2024

# --------------------------------------------

# ========== PSEUDO CODE ===========
# || LIBRARIES \ PACKAGES ||

# || IMPORTS || 
import csv

# || ACTUAL CODES ||
# - FOR ODD NUMBERS
# - Opening the file.
with open('python_file_handling\positive_integers.csv', 'r') as file:
    reader = csv.reader(file)
    
    # - Removing the header while reading the file.
    next(reader) 
    
    # - Creating a csv file for the output.
    with open('odd_numbers.csv', 'w', newline="") as output_file:
        writer = csv.writer(output_file)
        
        header = ['Odd Numbers']
        
        writer.writerow(header)
        
        for line in reader:
            writer.writerow([line[0]])
            
# - FOR EVEN NUMBERS
# - Opening the file.
with open('python_file_handling\positive_integers.csv', 'r') as file:
    reader = csv.reader(file)
    
    # - Removing the header while reading the file.
    next(reader) 
    
    # - Creating a csv file for the output.
    with open('even_numbers.csv', 'w', newline="") as output_file:
        writer = csv.writer(output_file)
        
        header = ['Even Numbers']
        
        writer.writerow(header)
        
        for line in reader:
            writer.writerow([line[1]])
        
        