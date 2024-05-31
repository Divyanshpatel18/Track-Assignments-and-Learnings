from sqlalchemy import create_engine, Column, String, Integer,LargeBinary, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from configurations.config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    full_name = Column(String(255))
    user_image=Column(LargeBinary, nullable=True)
    email = Column(String(255), unique=True)
    password = Column(String(255))
    role = Column(String(255), default="Employee")
    manager_id = Column(Integer, default=1)
    department_id = Column(Integer, ForeignKey('department.dept_id'))


    department = relationship("Department", back_populates="users")
    reimbursements = relationship("Reimbursement", back_populates="user", cascade="all, delete-orphan")

class Department(Base):
    __tablename__='department'
    dept_id=Column(Integer,primary_key=True)
    dept_name=Column(String(255),unique=True)
    city=Column(String(255))

    users = relationship("User", back_populates="department")

class Reimbursement(Base):
    __tablename__ = 'reimbursement'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)  # Ensure CASCADE is set in the ForeignKey
    request_category = Column(String(255), nullable=False)
    expense_type = Column(String(255), nullable=False)
    other_expense_type = Column(String(255), nullable=True)
    amount = Column(Integer, nullable=False)
    date = Column(String(255), nullable=False)
    receipt = Column(LargeBinary, nullable=False)
    status = Column(String(20), default="Pending")
    manager_comment = Column(String(255), nullable=True)

    # define a relationship with the User table
    user = relationship("User", back_populates="reimbursements")

# Creating the database connection string
db_uri = f"mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Creating an engine to connect to the MySQL database
engine = create_engine(db_uri)

# Create the tables in the database
Base.metadata.create_all(engine)



