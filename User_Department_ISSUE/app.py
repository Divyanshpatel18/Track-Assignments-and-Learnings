from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Department import Base as DepartmentBase, Department
from User import Base as UserBase, User
from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME

# initialize Flask application
app = Flask(__name__)

# Create the database connection string
db_uri = f"mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
engine = create_engine(db_uri)

# Create all tables in the engine
DepartmentBase.metadata.create_all(engine)
UserBase.metadata.create_all(engine)


# sessionmaker to interact with the database
Session = sessionmaker(bind=engine)
session=Session()

@app.route('/')
def hello():
    return "Hello, World!"

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
