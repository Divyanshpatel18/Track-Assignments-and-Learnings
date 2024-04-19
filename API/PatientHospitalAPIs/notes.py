
# REQUIREMENTS.TXT DEPENDENCIES

# 1.uvicorn: Uvicorn is a lightning-fast ASGI server implementation, using uvloop and httptools.

# 2.fastapi[all]~=0.104.1: FastAPI is a modern, fast (high-performance), web framework for building APIs with
#  Python 3.7+ based on standard Python type hints. The [all] extra installs additional dependencies 
#  for things like database support, etc. Version 0.104.1 is being used here.

# 3.mongoengine: MongoEngine is a Python Object-Document Mapper (ODM) for working with MongoDB. It provides 
# a Pythonic way of interacting with MongoDB through objects.

# 4.pymongo~=4.6.0: PyMongo is the official Python driver for MongoDB. This specifies version 4.6.0 or any 
# compatible version within the 4.x.x series.

# 5.sqlalchemy==1.4.17: SQLAlchemy is a SQL toolkit and Object-Relational Mapping (ORM) library for Python.
#  This specifies version 1.4.17 specifically.

# 6.pydantic~=2.5.1: Pydantic is a data validation and settings management library, which provides runtime
#  checking and validation of data against a data schema using Python type annotations. Version 2.5.1 is 
#  being used here.

# COMMANDS USED
# COMMAND1 
# pip install -r .\requirements.txt  : to install all the dependencies in requirements.txt

# COMMAND2
# uvicron main:app --reload 

# uvicorn: This is the command-line interface (CLI) for running ASGI applications, such as those built 
# with FastAPI.
# main:app: This specifies the location of your FastAPI application. In this case, it's telling Uvicorn
# to look for an object named app in a file named main.py 
# --reload: This flag tells Uvicorn to enable auto-reloading. When this flag is set, Uvicorn will monitor
# your Python files for changes, and automatically restart the server when it detects modifications. This 
# is very useful during development asit saves you from manually restarting the server every time you
# make changes to your code.

# COMMAND3(STEP3)
# COPY THE LOCAL ADDRESS
# PASTE ON BROWSER
# AND ADD 
# /docs to check the api's on swagger 