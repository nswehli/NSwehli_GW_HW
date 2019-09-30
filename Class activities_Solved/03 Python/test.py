import os
import csv
import math

wrestling_csv= os.path.join('..','Resources','WWE-Data-2016.csv')

def print_percentages(row):
   wrestler=row[0]
   wins=int(row[1])
   losses =int(row[2])
   draws=int(row[3])
   total=wins+losses+draws 
   win_percentage= ((wins/total) *100)
   loss_percentage=((losses/total) *100)
   draws_percentage=((draws/total) *100)
   print(wrestler)
   print (f"wins={win_percentage} %")
   print (f"losses={loss_percentage} %")
   print (f"draws={draws_percentage} %")
   if loss_percentage > 50:
       print ("Jobber")
   else:
       print ("superstar")
       
def stat(row):
            total= int(row[1])+int(row[2])+int(row[3])
            per_win=((int(row[1])/total)*100)
            print (f" win % = {per_win}%")
            per_loss=((int(row[2])/total)*100)
            print (f" loss % = {per_loss}%")
            per_draws=((int(row[3])/total)*100)
            print (f" Draws % = {per_draws}%")
            if per_loss> 50 :
                print ("Looser")

with open(wrestling_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    
    

    # Prompt the user for what wrestler they would like to search for
    name_to_check = input("What wrestler do you want to look for? ")

    # Loop through the data
    for row in csvreader:
        if(name_to_check == row[0]):
            stat(row)
            print ("****\n")
            print_percentages(row)
        
        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
       
            
