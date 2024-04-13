import json
from datetime import datetime
import  mysql.connector

# firstly reading the json
file=open("CASE_STUDIES/CASE_1/CASE_1.json","r")
training_data=json.load(file)

# extracting our data from json 
training_name = training_data['name']
training_date_str = training_data['date']
training_date = datetime.strptime(training_date_str, '%B %d, %Y').strftime('%Y-%m-%d')
training_completed = training_data['completed']
instructor_name = training_data['instructor']['name']
instructor_website = training_data['instructor']['website']
participants = training_data['participants']
 
#  connecting to mysql database
connection=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Divi@1321',
    database='python'
)

cursor=connection.cursor()

# creating two tables training session and participants
training_table_query = '''
    CREATE TABLE IF NOT EXISTS training_session (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        date DATE,
        completed BOOLEAN,
        instructor_name VARCHAR(255),
        instructor_website VARCHAR(255)
    )
'''

participants_table_query = '''
    CREATE TABLE IF NOT EXISTS participants (
        id INT AUTO_INCREMENT PRIMARY KEY,
        training_session_id INT,
        name VARCHAR(255),
        email VARCHAR(255),
        FOREIGN KEY (training_session_id) REFERENCES training_session(id)
    )
'''
cursor.execute(training_table_query)
cursor.execute(participants_table_query)


insertion_training_session_query = '''
    INSERT INTO training_session (name, date, completed, instructor_name, instructor_website)
    VALUES (%s, %s, %s, %s, %s)
'''
# note:  MySQL Connector/Python uses %s as the placeholder syntax, not ?.

# inserting data to training session
cursor.execute(insertion_training_session_query, (training_name, training_date, training_completed, instructor_name, instructor_website))
training_session_id = cursor.lastrowid


insertion_participants_query = '''
    INSERT INTO participants (training_session_id, name, email)
    VALUES (%s, %s, %s)
'''
# iterating over participants to get training id,email and name
for participant in participants:
    participant_data = (training_session_id, participant['name'], participant['email'])
    cursor.execute(insertion_participants_query, participant_data)

connection.commit()
connection.close()

print("Training session data successfully stored")