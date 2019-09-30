import os
import csv

udemy_csv = os.path.join("web_starter.csv")

# Lists to store data
title = []
price = []
subscribers = []
reviews = []
review_percent = []
length = []

# with open(udemy_csv, newline="", encoding='utf-8') as csvfile:
with open(udemy_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        # Add title
        # YOUR CODE HERE

        # Add price
        # YOUR CODE HERE

        # Add number of subscribers
        # YOUR CODE HERE

        # Add amount of reviews
        # YOUR CODE HERE

        # Determine percent of review left to 2 decimal places
        # YOUR CODE HERE

        # Get length of the course to just a number
        # YOUR CODE HERE

# Zip lists together
# YOUR CODE HERE

# Set variable for output file
output_file = os.path.join("web_final.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
                     "Percent of Reviews", "Length of Course"])

    # Write in zipped rows
    # YOUR CODE HERE
