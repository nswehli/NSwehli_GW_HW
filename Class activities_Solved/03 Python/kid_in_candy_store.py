# The list of candies to print to the screen
candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish",
             "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candyCart = []

# Print out options
for i in range(len(candyList)):
    print("[" + str(i) + "] " + candyList[i])

while allowance < 6 and allowance >0:
    choice = input (" what is the index number of the candy you want? you have " + str(allowance)+ " choices")
    if int(choice) == 0 :
        candyCart.append("Snickers")
    if int(choice) == 1 :
        candyCart.append("Kit Kat")
    if int(choice) == 2 :
        candyCart.append("Sour Patch Kids")
    if int(choice) == 3 :
        candyCart.append("Juicy Fruit")    
    if int(choice) == 4:
        candyCart.append("Swedish Fish")
    if int(choice) == 5 :
        candyCart.append("Skittles")
    if int(choice) == 6 :
        candyCart.append("Hershey Bar")
    if int(choice) == 7 :
        candyCart.append("Starbursts")
    if int(choice) == 7 :
        candyCart.append("M&Ms")
        
    allowance = allowance - 1
    
    
print (f"These are your choices : {candyCart}")


