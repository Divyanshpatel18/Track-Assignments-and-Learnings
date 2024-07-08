import bcrypt
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Entities.CreateTables import User
from configurations.config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME

Base = declarative_base()

# Creating the database connection string
db_uri = f"mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Creating an engine to connect to the MySQL database
engine = create_engine(db_uri)

def add_user(full_name, email, password, department_id, user_image):
    try:
        # converting password to array of byte
        bytes_password=password.encode('UTF-8')
        # generating the salt 
        salt=bcrypt.gensalt()
        # Hashing the password 
        hashed_password=bcrypt.hashpw(bytes_password,salt)
        new_user = User(full_name=full_name, email=email, password=hashed_password, department_id=department_id, user_image=user_image)
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(new_user)
        session.commit()
        session.close()
        return True
    except Exception as e:
        print(f"Error occurred while adding user: {e}")
        return False
    

def delete_user(id):
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        user = session.query(User).filter_by(id=id).first()
        if user:
            session.delete(user)
            session.commit()
            return True
        else:
            return False 
    except Exception as e:
        print(f"Error occurred while deleting user: {e}")
        return False 
    finally:
        session.close() 
        

def authenticate_user(email, password):
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        user = session.query(User).filter_by(email=email).first()
        # encoding entered user password 
        entered_password=password.encode('UTF-8')
        #fetching db password
        db_password=user.password.encode('UTF-8')
        result=bcrypt.checkpw(entered_password,db_password)
        if user and result:
           return user 
    except Exception as e:
        print(f"Error occurred while authenticating user: {e}")
        return None  
    finally:
        session.close()  

def get_user_by_Id(userId):
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        user = session.query(User).filter_by(id=userId).first()
        if user:
            return user
        else:
            return None  
    except Exception as e:
        print(f"Error occurred while retrieving user: {e}")
        return None 
    finally:
        session.close() 

def get_user_by_email(userEmail):
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        user = session.query(User).filter_by(email=userEmail).first()
        if user:
            return user
        else:
            return None  
    except Exception as e:
        print(f"Error occurred while retrieving user: {e}")
        return None 
    finally:
        session.close() 