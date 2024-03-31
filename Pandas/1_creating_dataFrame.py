
# Creating a DataFrame in Python using Pandas is quite straightforward.

# 1. From a Dictionary of Lists/Arrays: You can create a DataFrame from a dictionary where keys are column names
# and values are lists or arrays containing data for each column.
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)
print(df)

# 2.From a List of Dictionaries: You can create a DataFrame from a list of dictionaries, 
# where each dictionary represents a row of data.
data = [{'Name': 'Alice', 'Age': 25, 'City': 'New York'},
        {'Name': 'Bob', 'Age': 30, 'City': 'Los Angeles'},
        {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}]

df = pd.DataFrame(data)
print(df)


# 3.From a NumPy Array: You can create a DataFrame from a NumPy array.
import numpy as np
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

df = pd.DataFrame(data, columns=['A', 'B', 'C'])
print(df)

# 4.reading a csv file
df = pd.read_csv('C:/Users/ASUS/Downloads/states_by_country.csv')  # Read from CSV file
print(df)

# 5. reading a excel file
#  pip install openpyxl
data=pd.read_excel("C:/Users/ASUS/Downloads/file_example_XLSX.xlsx")
print(data)


# 6. reading data from mysql workbench by creating a connection
# pip install pandas mysql-connector-python

import mysql.connector
import pandas as pd

# Establish connection to MySQL database
connection = mysql.connector.connect(
    user="root",
    password="Divi@1321",
    database="sqlpractice"
)

# Query to fetch data from MySQL table
query = "SELECT * FROM emp1"

# Execute query and fetch results
df = pd.read_sql(query, con=connection)

# Close connection
connection.close()

# Display DataFrame
print(df)


print(data.head(10))
print(data.tail(10))