'''
Project: Commodity Analysis Final Project
Author: Aman Srinivas Nellutla
Description: This code imports a CSV file and filters the records according to user input for city, commodity, and date. 
The code then plots a bar graph using Plotly, showing the average price of selected commodities in each selected city.
Revisions:
    00 - Importing modules required in the program
    01 - Announced the program and read the CSV file used in the program
    02 - Added comments to explain the code blocks
'''
import csv
from datetime import datetime
import plotly.offline as py
import plotly.graph_objs as go

def average(a):
    length = len(a)
    return 0 if length == 0 else float(sum(a)/length)

print(f'\n{"="*30}\n{"Analysis of Commodity Data":^30}\n{"="*30}\n')


file = csv.reader(open('produce_csv.csv','r')) # Opening the produce csv and reading it
data = [row for row in file] # Iterating each line and storing it as list

modData = [] # Initialize new list to receive data
for row in data: # Traverse the rows
    newRow=list() # Make an empty row to receive values
    for item in row: # Traverse the values in the old row
        if "$" in item: # Test for price string and convert
            newRow.append(float(item.replace("$","")))
        elif "/" in item: # Test for date and convert
            newRow.append(datetime.strptime(item,'%m/%d/%Y')) 
        else: # Otherwise append item (not a date or a price)
            newRow.append(item)  
    modData.append(newRow) # Appending the new list into main list

locations = modData.pop(0)[2:] # Remove header and slice
records = [] # Create empty list for data records
for row in modData: # Traverse each row 
    newRow = row[:2] # First two values are common for all five locations
    for loc, price in zip(locations,row[2:]): # Traverse locations and prices
        records.append(newRow + [loc,price]) # New data is added to record
    
try: # Catching the index exception when user enters an out of bound index
    city=sorted(locations) # Sorting the cities in the file
    commodity = sorted(set([row[0] for row in modData])) # Retrieving and sorting the products
    dates=sorted(set([ row[1] for row in modData ])) # Retreving and sorting the dates
    
    # Dispalying and accepting user input for cities
    for row,item in enumerate(city):
        print(f"<{row+1}> {item}") 
    a=input("Enter location numbers separated by spaces: ").split()
    city_value=[city[int(row)-1] for row in a]
    print("\n")
    
    # Dispalying and accepting user input for products
    for row,item in enumerate(commodity):
        print(f"<{row+1}> {item}")
    b=input("Enter product numbers separated by spaces: ").split()
    commodity_name=[commodity[int(row)-1] for row in b]
    print("\n")
    
    # Dispalying and accepting user input for dates
    for row,item in enumerate(dates):
        print(f"<{row+1}> {str(item).split()[0]}") 
    print(f"Earliest available date is: {min(dates)}")
    print(f"Latest available date is: {max(dates)}")
    c=input("Enter start/end date numbers separated by a space: ").split()
    dates_value=[dates[int(row)-1] for row in c]
    print("\n")
    
    # Creating the final list based on user-selected conditions
    final_list = [row for row in records if((row[0] in commodity_name) and (min(dates_value) <= row[1] <= max(dates_value)) and (row[2] in city_value))]
    # Creating the graph
    final_list_graph = {row:[] for row in city_value} # Creating dictonary where location is the key as it is the filtering condition of graph
    for row in final_list_graph:
            for item in commodity_name:
                final_list_graph[row].append(average([k[3] for k in final_list if k[0] == item and k[2] == row])) # Creating dictonary where location is the key as it is the filtering condition of graph and appending average and other  
    
    graph_value = []
    for city_value,average in final_list_graph.items():
         graph_value.append(go.Bar(x=commodity_name,y=average,name=city_value)) # Creating a bar graph for the selected data
    
    # Printing the values for which graph will be generated
    print("Values for which graph will be generated:\n")     
    print("Selected City :") # Printing the city for which the graph will be generated
    [print(row) for row in city_value]
    print("\nSelected Product :") # Printing the Product for which the graph will be generated
    [print(row) for row in commodity_name]  
    print(f"\nSelected dates range: {min(dates_value)} - {max(dates_value)}\n") # Printing the dates for which the graph will be generated
    
    print(f'{len(final_list)} records have been selected.\n')
    print("RECORDS SELECTED  ....\n")
    [print(f"<{row}> {item}") for row,item in enumerate(final_list)]

    my_dict={} # Creating a empty dictonary
    for loc in final_list: 
        if(loc[0]+"-"+loc[2] in my_dict): # Creating procduct and location as one unit and storing as a key
            my_dict[loc[0]+"-"+loc[2]] = my_dict[loc[0]+"-"+loc[2]] +1 # Incrementing the count if it's already there
        elif(loc[0]+"-"+loc[2] not in my_dict):
            my_dict[loc[0]+"-"+loc[2]] = 1 # Assigning the value as one if it's not there and encountered as 1
    
    for loc in my_dict:
        print(f"{str(my_dict[loc])} prices for {loc.split('-')[0]} in {loc.split('-')[1]}") # Printing the result
 
    
    graph_header = 'Produce Prices from '+datetime.strftime(min(dates_value),"%m-%d-%Y")+' through '+datetime.strftime(max(dates_value),"%m-%d-%Y")
    graph_layout = go.Layout(barmode='group',
                       title=dict(text='<b>'+graph_header+'</b>', x=0.50, xanchor="center"), # Formatting title
                       xaxis=dict(title='Product'), # Formatting x axis
                       yaxis=dict(title='Average Price',tickprefix="$",tickformat=".2f"), # Formatting y axis
                       font=dict(family="sans-serif",size=20,color="#FF0000"), # formatting font
                       paper_bgcolor='rgb(255,255,255)', # Putting screen background color
                       plot_bgcolor='rgba(255,255,255)' # Putting graph background color
                       )
        
    # Plot the graph and save it in an html format
    fig = go.Figure(data=graph_value, layout=graph_layout)
    py.plot(fig, filename='Aman_final_project.html')
    
    print("Final Project Ended\n")

except IndexError: # catching the Index exception
    print("Entered index value is not in list. Please Try again !")
