import pandas as pd
# list=[[1,2,3]
#       ,[4,5,6],
#       [7,8,9]]
# df=pd.DataFrame(list,index=["A1","A2","A3"],columns=["col1","col2","col3"])
# print(df)

# D1 = pd.Series(["Virat", "ABD", "Maxwell", "Faf"])
# D2 = pd.Series([32, 33, 34, None])  # Adding a None to represent the missing value
# D3 = pd.Series([130, 200, 200, 150])
# Dict = {"Name": D1, "Age": D2, "StrRate": D3}
# df = pd.DataFrame(Dict)

data={"Name":["Virat", "ABD", "Maxwell", "Faf"],
      "Age":[32, 33, 34, None],
      "StrRate":[130, 200, 200, 150]
}
df = pd.DataFrame(data,index=["R1","R2","R3","R4"])

print(df)

# dataFrame in-built functions
print(df.index) #returns indexes of rows
print(df.axes)#returns rows and col
print(df.dtypes)# returns datatypes
print(df.size)# return size 2*3=6
print(df.shape)#returns(3,2) in tuples
print(df.values)#returns all values in 2 d arr
print(df.empty)#return true if whole df is empty
print(df.T) #transpose of df
print(df.count()) #count non NaN values from each column
print(df.count('columns'))
print(df.count(axis=0))
print(df.count(axis='columns'))

print(df["Name"])#access 1 col
print(df[["Name","Age"]])#access more than 1 col


                            # loc -
 # loc is a method used to access a group of rows and columns by label(s) or a boolean array. 
#  df.loc[row_label, column_label]

#accessing rows
print(df.loc["R1"])#access the single row
print(df.loc[["R2","R3"]])
print(df.loc["R1":"R3":2])#returns rows from R1 to R3 by taking 2 steps 

# #accessing col
print(df.Name)
print(df["Name"])
print(df.loc[:,"Name"])

print(df.loc[:,["Name","Age"]])
print(df.loc[:,'Name':'StrRate':2])

print(df.loc[["R2","R3"],["Name","StrRate"]])
print(df.loc["R2":"R3","Name":"Age"])
 
                        # iloc
# uses index positions instead of labels
# Selecting rows and columns using integer positions
# df.iloc[row_position, column_position]
# # Selecting all rows for specific columns
# df.iloc[:, column_position]
# # Selecting specific rows for all columns
# df.iloc[row_position, :]

print(df.iloc[2:4,1:3])

            # at
# at accessor is used to access a single value in a DataFrame or a Series using row and column labels. 
# For DataFrames
# value = df.at['row_label', 'column_label']
# modifying cell
df.at["R2","Age"]=50
print(df)
print(df[df["Age"]>32])


df["NewCol"]=[1,2,3,4]
df["StrRate"]=[200,212,213,214]


# creating a new col
# 1
df["New2"]=[1,2,3,4]#new col or pass old col name to modify
# 2
df.loc[:,"new"]=90 # not working
# 3
df.at[:,"new"]=90# not working
# 4
df=df.assign(New=[3,3,3,3])#new col
# 5
df.insert(2,"New3",[1,2,3,4])#new col at index 2

# creating new row
# 1.
df.loc["R5"]=["gayle",40,250]#new row4
# 2
df.loc["R6"]=50

# modify cell
df.loc["R3","StrRate"]=300

# del row
df.drop("R4",inplace=True)
df.drop(["R2","R3"],inplace=True)

# del col
# 1.
del df["StrRate"]
# 2
df.pop("Age")
# 3
df.drop("Name",inplace=True,axis=1)
# 4 
df.drop(columns=["Name","Age"],inplace=True)



# rename col
# 1.
df.rename({"Name":"FullName"},axis=1,inplace=True)
# 2
df.rename({"Name":"FullName","Age":"New Age"},axis=1,inplace=True)
# 3. if single column in df
df.columns["new Name"]

# rename rows
# 1
df.rename(index={"R1":"po"},inplace=True)
print(df)