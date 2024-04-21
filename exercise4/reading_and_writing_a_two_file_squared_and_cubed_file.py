# Delima, Sheena Mae D.
# BSCPE 1-2
# April 21, 2024

# ------------------------------------------------------

# ========= PSEUDO CODE =========
# || ACTUAL CODES ||
# - Opening the file and reading the file.
def squared_and_cubed_numbers_from_src():
    with open("integers.txt", "r") as file:
        integers = [int(line.strip()) for line in file.readlines()[:20]]
    
# - Writing a file: double_integers and triple_integers.
    with open("double.txt", "w") as output1, open("triple.txt", "w") as output2:
        for num in integers:
            if num % 2 == 0:
                output1.write(f'{num * num}\n')
                
            
        for num in integers:
            if num % 2 != 0:
                # Write the cube of the number to the triple.txt file
                output2.write(f'{num ** 3}\n')

# Call the function
squared_and_cubed_numbers_from_src()
        

        
