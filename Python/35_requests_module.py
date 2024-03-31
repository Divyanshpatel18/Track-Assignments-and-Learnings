
# The requests module in Python is a powerful HTTP library that allows you to send HTTP requests easily. 
# It provides a simple and elegant API to interact with web services and APIs.
#  You can perform HTTP requests such as GET, POST, PUT, DELETE, and more, and handle responses efficiently.

# 1. making a GET request and getting text as reponse below we get html as response
# import requests
# response=requests.get("https://www.google.com")
# print(response.text)


#2.making a GET request and getting reponse as JSON
# import requests

# # Send a GET request
# response = requests.get('https://jsonplaceholder.typicode.com/posts')

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     data = response.json()  # Convert response to JSON format
#     print(data)
# else:
#     print("Request failed with status code:", response.status_code)


# 3. Making a POST request

#  syntax:
# # Send a POST request with data
# payload = {'key1': 'value1', 'key2': 'value2'}
# response = requests.post('https://api.example.com/post', data=payload)
# if response.status_code == 200:
#     data = response.json()
#     print(data)

# implementation:
# import requests
# # Send a post request
# url="https://jsonplaceholder.typicode.com/posts"
# data={
#     "title":'foo',
#     "body":'bar',
#     "userId":1,
# }
# headers={
#     'Content-type':'application/json;charset=UTF-8'
# }
# response=requests.post(url,headers=headers,json=data)
# print(response.text)

#4. html parsing using beautiful soup
import requests
from bs4 import BeautifulSoup

url="https://www.royalenfield.com/in/en/motorcycles/continental-gt/"
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')
print(soup.prettify())

#finding all the content of h2
for heading in soup.find_all("h2"):
    print(heading.txt)