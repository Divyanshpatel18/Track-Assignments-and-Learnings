import pandas as pd
import numpy as np

gods_df=pd.read_csv("D:/code data/greek_gods.csv")
goddess_df=pd.read_csv("D:/code data/greek_goddesses.csv")
print(gods_df)
print()
print(goddess_df)


# QUES1("Merge the data from greek_gods.csv and greek_goddesses.csv")
gods_df=pd.read_csv("D:/code data/greek_gods.csv")
goddess_df=pd.read_csv("D:/code data/greek_goddesses.csv")
# print(gods_df)
print()
# print(goddess_df)
merged_df=pd.merge(gods_df,goddess_df,on="Domain",how="outer",suffixes=('_god','_goddess'))
print(merged_df)
# ____________________________________________________________________________________________________

# QUES2("Filter the merged table to only include gods and goddesses who are older than 8000 years,
#  then sort them based on their ages in descending order.")

# Filter
filtered_df = merged_df[(merged_df['Age_god'] > 8000) | (merged_df['Age_goddess'] > 8000)]

# Sort 
sorted_filtered_df = filtered_df.sort_values(by=['Age_god', 'Age_goddess'], ascending=False)
print(sorted_filtered_df)

# ______________________________________________________________________________________________________

# QUES 3("Join the two tables based on the "Domain" field and calculate the average age of gods and goddesses in each domain.")
gods_df=pd.read_csv("D:/code data/greek_gods.csv")
goddess_df=pd.read_csv("D:/code data/greek_goddesses.csv")

# Merge
merged_df = pd.merge(gods_df, goddess_df, on='Domain', how='outer', suffixes=('_god', '_goddess'))
# average 
average_age_by_domain = merged_df.groupby('Domain')[['Age_god', 'Age_goddess']].mean()
print(average_age_by_domain)
# ______________________________________________________________________________________________________

# QUES 4(".Determine which god/goddess has the highest age, and then find out if they are a god or a goddess.")

merged_df['Age_god'] = merged_df['Age_god'].fillna(0)
merged_df['Age_goddess'] = merged_df['Age_goddess'].fillna(0)
max_age=max(merged_df[['Age_god', 'Age_goddess']].values.flatten())
# or 
# ages = merged_df[['Age_god', 'Age_goddess']].values.flatten()
# # removing nan
# ages_without_nan = ages[~pd.isna(ages)]
# max_age = max(ages_without_nan)

print(max_age)

# check maximum age corresponds to a god or a goddess or not
max_age_god = max(merged_df['Age_god'])
max_age_goddess = max(merged_df['Age_goddess'])

if max_age == max_age_god:
    print("the highest age is a god.")
elif max_age == max_age_goddess:
    print(" highest age is a goddess.")
else:
    print("The highest age does not correspond to any god or goddess.")
# ___________________________________________________________________________________________________

# QUES 5("Create a new column in each table called "Age_Group" and categorize the gods/goddesses into groups such as "Young" (age < 5000), 
# "Middle-aged" (age between 5000 and 8000), and "Old" (age > 8000).")

# print(merged_df)
def categorize(age):
    if age < 5000:
        return "Young"
    elif age >= 5000 and age <= 8000:
        return "Middle-aged"
    else:
        return "Old"

merged_df['Age_Group_god'] = merged_df['Age_god'].apply(categorize)
merged_df['Age_Group_goddess'] = merged_df['Age_goddess'].apply(categorize)
print(merged_df)

# ____________________________________________________________________________________________________

# QUES 6("Compare the average ages of gods and goddesses. Is there a significant age difference between them? If yes,
#  which group tends to be older?")

# calculate average ages of gods and goddesses
avg_age_gods = merged_df['Age_god'].mean()
avg_age_goddesses = merged_df['Age_goddess'].mean()

# compare average ages
if avg_age_gods > avg_age_goddesses:
    print("Gods are older on average.")
elif avg_age_goddesses > avg_age_gods:
    print("Goddesses are older on average.")
else:
    print("The average ages of gods and goddesses are the same.")

# print the average ages
print("Average age of gods:", avg_age_gods)
print("Average age of goddesses:", avg_age_goddesses)

# ___________________________________________________________________________________________________

# QUES 7("Write a Python program using for loop to iterate over the "Age" column of the merged table 
# (after merging the gods and goddesses tables) and print out the names of gods/goddesses who are older than 8000 years.")

# Iterate over the merged table and print names of gods/goddesses older than 8000 years
for index, row in merged_df.iterrows():
    if row['Age_god'] > 8000:
        print("God:", row['Name_god'])
    if row['Age_goddess'] > 8000:
        print("Goddess:", row['Name_goddess'])

# ___________________________________________________________________________________________________

# QUES 8(".Write a Python program to find the oldest god/goddess from the merged table (after merging the gods and goddesses tables)
#  by iterating through the "Age" column using a while loop. Print out the name of the oldest god/goddess and their age.")

# Find the oldest god/goddess using a while loop
oldest_age = 0
oldest_name = None

# Iterate over the merged table to find the oldest god/goddess
index = 0
while index < len(merged_df):
    row = merged_df.iloc[index]
    if row['Age_god'] >= oldest_age:
        oldest_name = row['Name_god']
        oldest_age = row['Age_god']
    if row['Age_goddess'] >= oldest_age:
        oldest_name = row['Name_goddess']
        oldest_age = row['Age_goddess']
    index += 1

# Print the name of the oldest god/goddess and their age
print("The oldest god/goddess is:", oldest_name)
print("Their age is:", oldest_age)

# ___________________________________________________________________________________________________