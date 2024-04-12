import pandas as pd
                                # Data FILTERING
#1 Big Countries

def big_countries(world: pd.DataFrame) -> pd.DataFrame:

    filtered_df= world[ (world["area"]>=3000000) | (world["population"]>=25000000)]
    result_df=filtered_df[["name","population","area"]]
    return result_df


#2 Recyclable and Low Fat Products

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    
    filter_df=products[(products["low_fats"]=='Y') & (products["recyclable"]=='Y')]
    result_df=filter_df[["product_id"]]
    return result_df

#3 Customers Who Never Order
 
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    join_df=pd.merge(customers,orders,how='left',left_on='id',right_on='customerId')
    # the rows where customerId is null, indicating that the customer never ordered anything
    row_df=join_df[join_df["customerId"].isnull()]
    # selecting the name column
    result=row_df[["name"]]
    # changing column name
    result.rename({"name":'Customers'},axis=1,inplace=True)
    # result.columns=["Customers"]
    return result

#4 Article Views I

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where author_id matches viewer_id
   rows_df=views[views["author_id"]==views['viewer_id']]
   #get author_id column
   id_df=rows_df[['author_id']]
   #remove duplicates id from that column
   distinct_df=id_df.drop_duplicates()
   #sort the values
   result=distinct_df.sort_values(by='author_id',ascending=True)
#    remove duplicate and sort in one line 
#    result=id_df.drop_duplicates().sort_values(by='author_id')
   #rename the column
   result.columns=["id"]
   return result

                                # STRING METHODS
#6 Invalid Tweets
def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
   # Filter the DataFrame based on the length of the content
    rows_df=tweets[tweets['content'].str.len()>15]
    
    # the tweet_id column
    result=rows_df[['tweet_id']]
    return result

#7 Calculate Special Bonus


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # creating new column and keeping bonus as 0
    employees['bonus']=0
    # modifying each cell based on condition
    employees.loc[(employees['employee_id']%2==1) & (employees['name'].str[0]!='M'),'bonus']=employees['salary']
   
    # using numpy where
    # employees['bonus'] = pd.np.where((employees['employee_id'] % 2 == 1) & (employees['name'].str[0] != 'M'), employees['salary'], 0)

    result=employees[['employee_id','bonus']].sort_values(by='employee_id')

    return result

#8 Fix Names in a Table

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
   users['name']=users["name"].str.capitalize()
   return users.sort_values(by='user_id')

#9 Find Users With Valid E-Mails
def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    result=users[users['mail'].str.contains(r'^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$')]
    return result

# Patients With a Condition


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    # Adding \b before and after "DIAB1" ensures that only the whole word "DIAB1" is matched, and not parts of larger words
    # \S* matches zero or more non-whitespace characters.
    result=patients[patients['conditions'].str.contains(r'\bDIAB1\S*')]
    return result


                        # DATA MANIPULATION

# 177. Nth Highest Salary

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if N <= 0:
      return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    sorted_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    if N <= len(sorted_salaries):
        nth_highest = sorted_salaries.iloc[N - 1]
        result = pd.DataFrame({f'getNthHighestSalary({N})': [nth_highest]})
    else:
        result = pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    return result

# def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
#     if N <= 0:
#         return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
#     sorted_salaries = employee.drop_duplicates().sort_values(by="salary", ascending=False)
#     unique_salaries = sorted_salaries["salary"].unique()
#     print(unique_salaries)
    
#     if len(unique_salaries) >= N:
#         nth_highest = unique_salaries[N - 1]
#         return pd.DataFrame({f'getNthHighestSalary({N})': [nth_highest]})
#     else:
#         return pd.DataFrame({f'getNthHighestSalary({N})': [None]})

# 176. Second Highest Salary

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorted_salaries=employee['salary'].drop_duplicates().sort_values(ascending=False)
    if len(sorted_salaries) <2:
          return  pd.DataFrame({'SecondHighestSalary':[None]})
    else:
         result = sorted_salaries.iloc[1]
         return pd.DataFrame({'SecondHighestSalary':[result]})
    
# 184. Department Highest Salary
import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merge_df=pd.merge(employee,department,how='inner',left_on='departmentId',right_on='id')
    max_salary=merge_df.groupby('name_y')['salary'].max().reset_index()
    max_salary.columns=['Department','Salary']
    result=pd.merge(merge_df,max_salary,how='inner',left_on=['name_y','salary'],right_on=['Department','Salary'])
    result=result[["Department",'name_x','salary']]
    result.columns=['Department','Employee','Salary']
    return result
    # merge_df=pd.merge(employee,department,how='inner',left_on='departmentId',right_on='id')
    # max_salary = merge_df.groupby('name_y')['salary'].max().reset_index()
    # max_salary.columns=['Department','Salary']
    # result = pd.merge(merge_df, max_salary, how='inner', left_on=['name_y', 'salary'], right_on=['Department', 'Salary'])      # Select required columns
    # result = result[['Department', 'name_x', 'Salary']]
    
    # # Rename columns
    # result.columns = ['Department', 'Employee', 'Salary']
    # print(result)
    # return result



# 178. Rank Scores
def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # sort scores in descending order
    scores_sorted = scores.sort_values(by='score', ascending=False) 
    # ascending=False higher score will get lower ranks
    scores_sorted['rank'] = scores_sorted['score'].rank(method='dense', ascending=False).astype(int)

    return scores_sorted[['score', 'rank']]

# 196. Delete Duplicate Emails

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id', ascending=True, inplace=True)
    # subset='email':
    # This parameter specifies the column or columns to consider when identifying duplicates. 
    person.drop_duplicates(subset='email', keep='first', inplace=True)

# 1795. Rearrange Products Table
import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
   new_products = pd.melt(products, id_vars=['product_id'], var_name='store', value_name='price')
   new_products = new_products.dropna(subset=['price'])
   return new_products

# 1741. Find Total Time Spent by Each Employee
import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time']=employees['out_time']-employees['in_time']
    result=employees.groupby(['event_day','emp_id'])['total_time'].sum().reset_index()
    result.rename({'event_day':'day'},axis=1,inplace=True)
    print(result)
    return result


# 511. Game Play Analysis I
import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    result = activity.groupby('player_id')['event_date'].min().reset_index()
    result.rename({'event_date':'first_login'},axis=1,inplace=True)
    print(result)
    return result

# 2356. Number of Unique Subjects Taught by Each Teacher

import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    # 'nunique gives unique count'
    result=teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()
    result.rename({'subject_id':'cnt'},axis=1,inplace=True)
    return result


# 596. Classes More Than 5 Students
def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    # group by class and count the number of students in each class
    class_counts = courses.groupby('class').size().reset_index(name='count')
    # filter out classes with less than 5 students
    result = class_counts[class_counts['count'] >= 5]
    result = result[['class']] 
    return result

# 586. Customer Placing the Largest Number of Orders
import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    result=orders.groupby('customer_number').size().reset_index(name='count')
    maxcount=result['count'].max()
    result1=result[result['count']==maxcount]['customer_number']
    return pd.DataFrame({"customer_number":result1})

# 1484. Group Sold Products By The Date
import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    result = activities.groupby(['sell_date', 'product']).size().reset_index(name='count')
    
    # Group the result by sell_date and aggregate the products into a sorted list
    result = result.groupby('sell_date').apply(lambda x: pd.Series({
        'num_sold': len(x),
        'products': ','.join(sorted(x['product'].unique()))
    })).reset_index()
    
    return result