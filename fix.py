# This file replaces white space in a csv or txt file with commas for csv file manipulation



file_name = 'file_data_copy.csv'
with open(file_name, "r") as f:
    new_lines = f.readlines()

pattern = ", "

with open(file_name, "w") as f:
    for line in new_lines:
        f.write(line.replace(' ', pattern))
