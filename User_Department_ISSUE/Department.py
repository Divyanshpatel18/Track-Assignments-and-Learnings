from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Department(Base):
    __tablename__ = 'departments'

    dept_id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)

    users = relationship("User", backref="department")


    # Establish relationship with User
    # users = relationship("User", back_populates="department")
    # Access users associated with the department
    # users_in_department = department.users
    # for user in users_in_department:
    #     print(user.full_name)