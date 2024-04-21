# Delima, Sheena Mae Delima
# BSCPE 1-2
# April 21, 2024

# --------------------------------------------

# ========== PSEUDO CODE ===========
# || LIBRARIES \ PACKAGES ||
import csv


# || VARIABLES ||
max_gwa = 1.00
max_student = None


# || ACTUAL CODES ||
# - Open and reading the csv file.
with open('students_grade_info.csv', 'r') as file:
    reader = csv.reader(file)
    
    # Skip the header row
    next(reader)

# - Reading the rows and find the student who has a highest GWA.
    for row in reader:
        name, gwa = row[0], float(row[1])
        if gwa <= max_gwa:
            max_gwa = gwa
            max_student = name

# - Printing the output containing the student name and his/her highest GWA.
print(f'The student with the highest GWA is {max_student} with a GWA of {max_gwa}')