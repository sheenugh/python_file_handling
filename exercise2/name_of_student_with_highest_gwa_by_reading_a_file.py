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
with open('python_file_handling\exercise2\students_grade_info.csv', 'r') as file:
    reader = csv.reader(file)
# - Reading the rows and find the student who has a highest GWA.
# - Printing the output containing the student name and his/her highest GWA.