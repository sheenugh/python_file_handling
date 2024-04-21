import csv

def process_integers():
    # Open the source file for reading
    with open("positive_integers_file.csv", "r") as f:
        # Create a CSV reader object
        reader = csv.reader(f)

        # Loop through the rows in the CSV file
        integers = [int(row[0]) for row in reader[:20]]

    # Open the output files for writing
    with open("double.csv", "w", newline="") as double_file, open("triple.csv", "w", newline="") as triple_file:
        # Create CSV writer objects
        double_writer = csv.writer(double_file)
        triple_writer = csv.writer(triple_file)

        # Loop through the integers
        for num in integers:
            # Check if the number is even
            if num % 2 == 0:
                # Write the square of the number to the double.csv file
                double_writer.writerow([num ** 2])
            else:
                # Write the cube of the number to the triple.csv file
                triple_writer.writerow([num ** 3])

# Call the function
process_integers()