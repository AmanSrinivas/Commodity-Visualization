# Commodity-Visualization
This Python script provides an intuitive and interactive way to analyze commodity price data across various cities and dates.
The tool leverages a CSV file containing commodity prices, enabling users to filter data based on specific criteria, such as city, commodity type, and date range.
The filtered dataset is then visualized using Plotly, a popular graphing library, to display the average price of selected commodities in each chosen city through a bar graph.

How It Works:
Data Preparation: The script reads commodity price data from a CSV file and performs necessary transformations to prepare it for analysis. This includes converting price strings to float values and parsing dates.
User Input: Through a series of prompts, the user selects cities, commodities, and a date range for analysis. The script dynamically adjusts to user choices, offering sorted lists of options based on the data.
Data Filtering: Based on user input, the script filters the dataset to include only the relevant records matching the selected criteria.
Visualization: The script calculates the average price for each selected commodity in each city within the specified date range. These averages are then visualized in a bar graph, with commodities on the x-axis and average prices on the y-axis.
Output: The final bar graph is saved as an HTML file, which can be viewed in any web browser. This interactive visualization allows users to explore the data in depth.
