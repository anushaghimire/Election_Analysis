print("Hello world")

# Add our dependencies
import csv
import os
#Assign a variable to load file from path.
file_to_load = os.path.join("resources", "election_results.csv",)
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")


#open the election results and read the file.
