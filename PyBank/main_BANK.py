# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 12:44:03 2018

@author: Damita
"""
#Modules
import os
import csv

#Get Path
#budget_csv = os.path.join("../Resources", )
budget_csv = "C:\\Users\\Damita\\GWARL201811DATA3\\02-Homework\\03-Python\\Instructions\\PyBank\\Resources\\budget_data.csv"

#Open and read the file
#with open(budget_csv, newline="", encoding='utf-8') as csvfile
with open(budget_csv, newline="", encoding='utf-8') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   #DO NOT INCLUDE HEADER ROW
   csv_header = next(csvfile)
   
   month_year = []
   profit_or_loss = []
   net_change = []
   totmonths = 0
   totnet = 0
      
   #initialize counters
   i = 0
  
   #Calculate Values              
   for row in csvreader:                  
       month_year.append(row[0])
       
       totmonths = totmonths + 1
       
       totnet = totnet + int(row[1])
  
       #Calculate Monthly Change in Profit or Loss       
       profit_or_loss.append(int(row[1]))       
       if(i > 0):
           net_change.append(profit_or_loss[i] - profit_or_loss[i-1])              
                                      
       #Calculate Average Monthly Change to Total Months               
       avgchange = round(sum(net_change)/totmonths, 2) 

       #Calculate Greatest Increase in Profit or Loss
       gIncreasePL = max(profit_or_loss)
       
       #Determine Month of Greatest Increase of Profit or Loss
       if gIncreasePL == profit_or_loss[i]:
           gmonth_year = (row[0])
 
       #Calculate Greatest Decrease in Profit or Loss
       gDecreasePL = min(profit_or_loss)
       
       #Determine Month of Lowest Increase of Profit or Loss
       if gDecreasePL == profit_or_loss[i]:
           lmonth_year = (row[0])                      
      
       i = i + 1 
      
print(f'Total Months: {totmonths}')
print(f'Total: ${totnet}')         
print(f'Average Change: ${avgchange}')
print((f'Greatest Increase in Profits: {gmonth_year} $({gIncreasePL})'))
print((f'Greatest Decrease in Profits: {lmonth_year} $({gDecreasePL})'))

#Zip lists together into a single tuple.
cleaned_txt = zip(month_year, profit_or_loss, net_change)
#cleaned_txt2 = ()

#Write the contents into a text file.
#Set variable for output file
output_file = "C:\\Users\\Damita\\GWARL201811DATA3\\02-Homework\\03-Python\\Instructions\\PyBank\\Resources\\new_budget_data.txt"

#Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    #Write the header row
    writer.writerow(["Month_Year", "Profit/Loss", "Average Change"])
    
    #Write in zipped rows
    writer.writerows(cleaned_txt)
    
    #Write Summary Data
    writer.writerow(["Total Months:", totmonths, "Total:", totnet, "Average Change:", avgchange, "Greatest Increase in Profits:", gmonth_year, gIncreasePL, "Greatest Decrease in Profits:", lmonth_year, gDecreasePL])    
    
    
    
    