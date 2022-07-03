# Assign a variable for the file to load and the path. 
file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Creating file name 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Opening election results
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)
    print(headers)
 
    