from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Entities.CreateTables import Department
from configurations.config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME

Base = declarative_base()

# Creating the database connection string
db_uri = f"mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Creating an engine to connect to the MySQL database
engine = create_engine(db_uri)

def add_departments(dept_name, city):
    try:
        new_dept = Department(dept_name=dept_name, city=city)
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(new_dept)
        session.commit()
        session.close()
        return True
    except Exception as e:
        print(f"Error occurred while adding department: {e}")
        return False


def get_all_departments():
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        departments = session.query(Department).all()
        return departments  
    except Exception as e:
        print(f"Error occurred while retrieving departments: {e}")
        return None  
    finally:
        session.close() 

def delete_departments(dept_id):
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        department = session.query(Department).filter_by(dept_id=dept_id).first()
        if department:
            session.delete(department)
            session.commit()
            return True 
        else:
            return False
    
    except Exception as e:
        print(f"Error occurred while deleting department: {e}")
        return False 
    finally:
        session.close()


def get_id_by_department_name(dept_name):
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        department = session.query(Department).filter_by(dept_name=dept_name).first()
        if department:
            return department.dept_id
        else:
            return None  
    except Exception as e:
        print(f"Error occurred while retrieving department ID: {e}")
        return None 
    finally:
        session.close() 

   