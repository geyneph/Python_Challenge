""""
This python analyze budget_data.csv, this is a profit /looses by months csv file
"""

#importing modules
import pandas as pd
import csv
import os
import statistics as st 


def financial_Analysis():
    #inicializing the variables
    total_months = 0
    total = 0
    average_change = 0 
    Greatest_increase = 0
    gratest_decrease = 0
    list_amounts = []
    list_months = []
    avg_change = []
    dic  = {}

    #Reading the data
    with open('PyBank/Resources/budget_data.csv') as csv_file:
        csvReader = csv.reader(csv_file)
        header = next(csvReader)
        #Looping through row: separating rows into 2 different list, and counting how many months and total amount 
        for rows in csvReader:
            list_amounts.append(int(rows[1]))
            list_months.append(rows[0])
            total = total+int(rows[1])
            total_months+=1
        #Eliminating the first month cause it doest has a change rate 
        list_months.pop(0)
        #calculating the average change while looping in the list_amounts, notice we finished the looping 1 value before it ends
        for i in range(0,len(list_amounts)-1):
            average_change = list_amounts[i+1]-list_amounts[i]
            avg_change.append(average_change)
            #Creating a diccionary with average_change values as keys and every_month as values, so we can search it later
            if average_change  not in dic:
                dic[average_change] = list_months[i]
        #Saving store data on a TXT file
        with open('PyBank/AnalysisFinalReport.txt','w') as Analysis:
            Analysis.write('Financial Analysis \n ')
            Analysis.write('-'*30+'\n ')
            Analysis.write(f'Total Months: {total_months} \n ')
            Analysis.write(f'total: {total} \n ')
            Analysis.write(f'Average Change: ${st.mean(avg_change)} \n ')
            Analysis.write(f'Greates increase in profits: {dic[max(avg_change)]} (${max(avg_change)}) \n ')
            Analysis.write(f'Greatest Decrease in profits: {dic[min(avg_change)]} (${min(avg_change)}) \n ')
        #Terminal checking values 
        print('Financial Analysis \n ')
        print('-'*30)
        print(f'Total Months: {total_months} \n ')
        print(f'total: {total} \n ')
        print(f'Average Change: ${st.mean(avg_change)} \n ')
        print(f'Greates increase in profits: {dic[max(avg_change)]} (${max(avg_change)}) \n ')
        print(f'Greatest Decrease in profits: {dic[min(avg_change)]} (${min(avg_change)}) \n ')
financial_Analysis()

