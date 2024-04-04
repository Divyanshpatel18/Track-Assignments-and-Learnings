#QUESTION
# Consider a scenario where you're developing a system to manage training sessions for 
# a software development company. The JSON snippet provided represents one such training session named 
# 'Python Training.' In this scenario, you have multiple training sessions with different instructors, 
# dates, and participants. For this you need to handle booleans, integers, strings, floats a lists and 
# dictionaries.
# JSON
training_session = {
    "name": "Python Training",
    "date": "April 19, 2024",
    "completed": True,
    "instructor": {
        "name": "XYZ",
        "website": "http://pqr.com/"
    },
    "participants": [
        {
            "name": "Participant 1",
            "email": "email1@example.com"
        },
        {
            "name": "Participant 2",
            "email": "email2@example.com"
        }
    ]
}

# Accessing the fields
session_name = training_session["name"]
session_date = training_session["date"]
session_completed = training_session["completed"]
instructor_name = training_session["instructor"]["name"]
instructor_website = training_session["instructor"]["website"]
participant1_name = training_session["participants"][0]["name"]
participant1_email = training_session["participants"][0]["email"]
participant2_name = training_session["participants"][1]["name"]
participant2_email = training_session["participants"][1]["email"]

# Printing the valuesvalues
print("Session Name:", session_name)
print("Session Date:", session_date)
print("Session Completed:", session_completed)
print("Instructor Name:", instructor_name)
print("Instructor Website:", instructor_website)
print("Participant 1 Name:", participant1_name)
print("Participant 1 Email:", participant1_email)
print("Participant 2 Name:", participant2_name)
print("Participant 2 Email:", participant2_email)
