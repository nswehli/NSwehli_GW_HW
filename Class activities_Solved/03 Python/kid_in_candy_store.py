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
    candyCart.append(candyList[int(choice)]) 
    
        
    allowance = allowance - 1
    
print (f"These are your choices : {candyCart}")


