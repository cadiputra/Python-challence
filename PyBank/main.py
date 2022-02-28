# Import os and csv module
import os
import csv

# Define data source path
csvpath=os.path.join('budget_data_Pybank.csv')

# set list to store changes between rows
Period=[]
PL=[]
Movement=[]

# Open the csv file
with open (csvpath,'r') as csvfile:
    
    csvreader = csv.reader(csvfile,delimiter=',')

    # skip headers
    header = next(csvfile)

    # set variable for previous row value
    previous = 0
    
    # loop through the records in csvreader
    for row in csvreader:
        
        # add period
        Period.append(row[0])

        # add Profit Loss
        Month_PL=int(row[1])
        PL.append(Month_PL)

        # add Changes (difference between rows)
        change = int(row[1]) - previous
        previous = int(row[1])
        Movement.append(change)


# Zip list together
Data = zip(Period, PL,Movement)

# calculate total profit losses
Total_PL=sum(PL)
# print (Total_PL)

# calculate number of months
Row_Count=len(Period)
# print(Row_Count)

# set remove first record in Movement to zero
# calculate number of movements, minus 1 to disregard the first record
Movement[0] = 0
Row_Count_Movement=len(Movement)-1
# print(Row_Count_Movement)

# calculate total movement and average movement
Total_Movement=sum(Movement)
Average_Movement=float(Total_Movement/Row_Count_Movement)
# print(Average_Movement)


#Set variable to ouput file
output_file = os.path.join("Updated_Budget_Data.csv")

#  Open the output file
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    #writer.writerow(["Period", "Profit (Loss)","Movement"])

    # Write in zipped rows
    writer.writerows(Data)

# define source for updated data
csvpath_updated=os.path.join("Updated_Budget_Data.csv")

with open (csvpath_updated,'r') as csvfile_updated:
    csvreader_sorted=csv.reader(csvfile_updated, delimiter=',')
    Sorted_Movement=sorted(csvreader_sorted, key=lambda csvreader_sorted: csvreader_sorted[2], reverse=True)

# identify highest & lowest increase & decrease month & amount
Greatest_Increase_Month=Sorted_Movement[0][0]
Greatest_Increase_Amount=Sorted_Movement[0][2]
Lowest_Decrease_Month=Sorted_Movement[int(Row_Count)-1][0]
Lowest_Decrease_Amount=Sorted_Movement[int(Row_Count)-1][2]

print("Financial Analysis")
print("-------------------------------")
print(f'Total Months: {Row_Count}')
print(f'Total: ${Total_PL}')
print(f'Average Change: ${round(Average_Movement,2)}')
print(f'Greatest Increase in Profits: {Greatest_Increase_Month} (${Greatest_Increase_Amount})')
print(f'Greatest Decrease in Profits: {Lowest_Decrease_Month} (${Lowest_Decrease_Amount})')

# Set variable to output the financial analysis to a txt file
output_txt=os.path.join("Financial_Analysis.txt")

Analysis_Summary_txt = f"""Financial Analysis
----------------------------
Total Months: {Row_Count}
Total: ${Total_PL}
Average Change: ${round(Average_Movement,2)}
Greatest Increase in Profits: {Greatest_Increase_Month} (${Greatest_Increase_Amount})
Greatest Decrease in Profits: {Lowest_Decrease_Month} (${Lowest_Decrease_Amount})"""

with open (output_txt,'w') as text_file:
    text_file.write(Analysis_Summary_txt)
