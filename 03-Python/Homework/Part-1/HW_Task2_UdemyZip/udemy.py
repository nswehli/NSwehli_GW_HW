import os
import csv

udemy_csv = os.path.join("web_starter.csv")


# Lists to store data
title = []
price = []
subscribers = []
reviews = []
rpercent = []
length = []


with open(udemy_csv, newline="", encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        title.append(row[1])

        # Add price
        price.append(row[4])

        # Add number of subscribers
        subscribers.append(row[5])

        # Add amount of reviews
        reviews.append(row[6])

        # Determine percent of review left to 2 decimal places
        percent=((int(row[6]))/(int(row[5]))*100)
        review_percent=round((percent), 2)
        rpercent.append(review_percent)
        

        # Get length of the course to just a number
        length.append(row[9].split()[0])
# Zip lists together
udemy=zip(title,price,subscribers,reviews,rpercent,length)
print (udemy)

# Set variable for output file
output_file = os.path.join("web_final.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
                     "Percent of Reviews", "Length of Course"])
    # Write in zipped rows
    
    writer.writerows(udemy)
    print (udemy)
