
import pandas as pd
import numpy as np
# data=pd.read_excel("C:/Users/ASUS/Downloads/file_example_XLSX.xlsx")

# # 1.
# print(data.head(10))  # Print the first 10 rows

# # 2.
# print(data.tail(10))  # Print the last 10 rows

# # 3.
# print(data.info())    # Print information about the DataFrame
# # output-
# # <class 'pandas.core.frame.DataFrame'>
# # RangeIndex: 5000 entries, 0 to 4999
# # Data columns (total 8 columns):
# #  #   Column      Non-Null Count  Dtype 
# # ---  ------      --------------  ----- 
# #  0   Unnamed: 0  5000 non-null   int64 
# #  1   First Name  5000 non-null   object
# #  2   Last Name   5000 non-null   object
# #  3   Gender      5000 non-null   object
# #  4   Country     5000 non-null   object
# #  5   Age         5000 non-null   int64 
# #  6   Date        5000 non-null   object
# #  7   Id          5000 non-null   int64 
# # dtypes: int64(3), object(5)
# # memory usage: 312.6+ KB
# # None

# # 4.
# data.describe()

# # 5. To check whether value is null or not in a cell
# print(data.isnull())
#     # To check in a column instead of a cell(column wise null values)
# print(data.isnull().sum())


#             #  WORKING WITH DUPLICATES

# data1=pd.read_excel("D:/code data/DummyPandas.xlsx")
# # 6. check the rowise duplicate data
# print(data.duplicated())
# #checks the columnwise duplicate values using true or false
# print(data1['EEID'].duplicated())
# # gives the count of duplicate values according to colummn
# print(data1['EEID'].duplicated().sum())
 
# # 7.dropping the duplicates rows
# print(data1.drop_duplicates())
# # droppping the duplicates based on the column
# print(data1.drop_duplicates("EEID"))
# print(data1["EEID"].drop_duplicates())


#         #    WORKING WITH MISSING DATA
# # gives the count of null values infront of column name
# print(data1.isnull().sum())
# # drops the rows containing null  values whether the null value is in any column
# print(data1.dropna())
# # replace the cell containg null with "Null Value Cell"
# print(data1.replace(np.nan,"null value cell"))
# # replacing the particluar column null value with your value(in nummeric column generally mean value is used)
# data1["Salary"]=data1["Salary"].replace(np.nan,30000)
# data1["Salary"]=data1["Salary"].replace(np.nan,data1["Salary"].mean())
# #filling null values with bfill and ffill
# print(data1.fillna(method="bfill"))
# print(data1.fillna(method="ffill"))
# data1.fillna("hi null cell") # works alike replace

#         # COLUMN TRANSFORMATION
# df=pd.read_excel("D:/code data/ESD.xlsx")
# # conditon basis column transformation
# # if bounus is less than 0 create column GetBonus and write bonus else no bonuss
# df.loc[(df["Bonus %"]==0),"GetBonus"]="no bonus"
# df.loc[(df["Bonus %"])>0,"GetBonus"]="bonus"
# print(df.head(10))

# df1=pd.read_excel("D:/code data/practice_1.xlsx")
# # print(df1)
# #combining two columns into new column
# df1["Full Name"]=df1["First Name"]+" "+df1["Last Name"]
# print(df1)
# df1["Full Name"]=df1["First Name"].str.capitalize()+" "+df1["Last Name"].str.capitalize()
# #creating new column bonus and adding values in them 
# df1["Bonus"]=(df1["Salary"]/100)*20


# def extract(value):
#     return value[0:3]

# data1={"Months":["January","February","March","April"]}
# a=pd.DataFrame(data1)
# a["short_months"]=a["Months"].map(extract)
# print(a)

#                                     #  GROUP BY
# data=pd.read_excel("D:/code data/ESD.xlsx")

# #getting the count of male and females from each department
# gp=data.groupby(["Department","Gender"]).agg({"EEID":"count"})
# print(gp)
# # avg age of country
# gp1=data.groupby("Country").agg({"Age":"mean"})
# gp1=data.groupby("Country").agg({"Annual Salary":"max"})
# gp1=data.groupby(["Country","Gender"]).agg({"Annual Salary":"max"})
# gp1=data.groupby(["Country","Gender"]).agg({"Annual Salary":"max","Age":"min"})



#         #  MERGE , CONCATENATE AND JOIN IN PANDAS

# data1= {"Emp Id":["E01","E02","E03","E04","E05","E06"],
#         "Names":["Ram","Shyam","Rahul","Vishal","Ravi","John"],
#         "Age":[34,56,23,44,32,36]}

# data2={"Emp Id":["E01","E02","E03","E04","E05","E06"],
#         "Salary":[45000,56000,34000,30000,50000,62000]}
# df1=pd.DataFrame(data1)
# df2=pd.DataFrame(data2)
# # print(df1)
# # print()
# # print(df2)
# # merging on Emp Id col
# print(pd.merge(df1,df2,on="Emp Id"))
# # left,inner,right
# print(pd.merge(df1,df2,on="Emp Id",how="left"))


# data1= {"Emp Id":["E01","E02","E03","E04","E05","E06"],
#         "Names":["Ram","Shyam","Rahul","Vishal","Ravi","John"],
#         "Age":[34,56,23,44,32,36]}

# data2={"Emp Id":["E07","E08","E09","E10","E11","E12"],
#         "Names":["bittu","chintu","Pappu","chotu","bunty","golu"],
#         "Age":[34,56,23,44,32,36]}
# df1=pd.DataFrame(data1)
# df2=pd.DataFrame(data2)

# print(pd.concat([df1,df2]))


#     # COMPARE DATAFRMES
# dict={"Fruits":["mango","apples","banana","papaya"],
#       "Price":[100,150,30,35],
#       "Quantity":[15,10,10,3]}
# df1=pd.DataFrame(dict)
# print(df1)

# df2=df1.copy()


# df2.loc[0,"Price"]=120
# df2.loc[1,"Price"]=175
# df2.loc[3,"Price"]=30
# df2.loc[0,"Quantity"]=12
# df2.loc[1,"Quantity"]=15
# df2.loc[3,"Quantity"]=5
# print(df2)

# print(df1.compare(df2))
# print(df1.compare(df2,align_axis=0))
# # print(df1.compare(df2,align_axis=0))
# print(df1.compare(df2,keep_equal=True))
# print(df1.compare(df2,keep_shape=True))


#     # PIVOTING AND MELTING DATAFRAMES
# dict={"keys":["k1","k2","k1","k2"],
# "Names":["John","Ben","David","Peter"],
# "Houses":["red","blue","green","red"],
# "Grades":["3rd","8th","9th","8th"]}

# df=pd.DataFrame(dict)
# print(df)

# # print(df.pivot(index='keys', columns='Names', values='Houses',values="Grades"))
# print(df.pivot_table(index='keys', columns='Names', values=['Houses', 'Grades'], aggfunc='first'))


dict={ "Names":["John","Ben","David","Peter"],
      "Houses":["red","blue","green","red"],
      "Grades":["3rd","8th","9th","8th"]}
df=pd.DataFrame(dict)
print(df)
print(pd.melt(df,id_vars=["Names"],value_vars=["Houses"]))
print(pd.melt(df,id_vars=["Names"],value_vars=["Houses","Grades"]))
print(pd.melt(df,id_vars=["Names"],value_vars=["Houses","Grades"],var_name="Houses&Grades",value_name="values"))