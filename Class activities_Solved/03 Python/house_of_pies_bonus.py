pieslist = ["Pecan","Apple Crisp","Bean","Banoffee","Black Bun","Blueberry","Buko", "Burek", "Tamale", "Steak"]
print (" Welcome to the House of Pies! Here are our pies:")
menu =len(pieslist)

Pecan_total=0
Apple_total=0
Bean_total=0
Banoffee_total=0
Black_total=0
Blueberry_total=0
Buko_total=0
Burek_total=0
Tamale_total=0
Steak_total=0

anotherorder = "y"
while anotherorder =="y":
    
    for i in range(menu):
        print("[" + str(i) + "] " + pieslist[i])
        
    selection = input("Whch pie numbner you would like to order?")
    
    if int(selection) == 0:
        pie = "Pecan"
        Pecan_total=Pecan_total+1
           
    if int(selection) == 1:
        pie = "Apple Crisp"
        Apple_total=Apple_total+1
        
    if int(selection) == 2:
        pie = "Bean"
        Bean_total=Bean_total+1
        
    if int(selection) == 3:
        pie = "Banoffee"
        Banoffee_total=Banoffee_total+1
        
    if int(selection) == 4:
        pie = "Black Bun"
        Black_total=Black_total+1
        
    if int(selection) == 5:
        pie = "Blueberry"
        Blueberry_total=Blueberry_total+1
        
    if int(selection) == 6:
        pie = "Buko"
        Buko_total=Buko_total+1
        
    if int(selection) == 7:
        pie = "Burek"
        Burek_total=Burek_total+1 
        
    if int(selection) == 8:
        pie = "Tamale"
        Tamale_total=Tamale_total+1
        
    if int(selection) == 9:
        pie = "Steak"
        Steak_total=Steak_total+1
        
    print (f" great! We'll have that {pie} pie right out for you." )
        
    anotherorder = input ("would you like to make another order ? [y]es or [N]o?")
    
print ("thank you for your order, you total is: ") 

print (f"{Pecan_total} pecan pies ")
print (f"{Apple_total} Apple Crisp pies")
print (f"{Bean_total} Bean pies")
print (f"{Banoffee_total} Banoffee pies")
print (f"{Black_total} Black Bun pies")
print (f"{Blueberry_total} Blueberry pies")
print (f"{Buko_total} Buko pies")
print (f"{Burek_total} Burek pies")
print (f"{Tamale_total} Tamale pies")
print (f"{Steak_total} Steak pies")






