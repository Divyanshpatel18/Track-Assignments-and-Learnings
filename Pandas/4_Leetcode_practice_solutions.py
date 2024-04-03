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