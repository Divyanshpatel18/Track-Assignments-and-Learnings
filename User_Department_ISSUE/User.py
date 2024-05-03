from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    full_name = Column(String(255))
    email = Column(String(255), unique=True)
    password = Column(String(255))
    role = Column(String(255), default="Employee")
    manager_id = Column(Integer, default=1)
    
    # Define ForeignKey reference to 'departments.id'
    department_id = Column(Integer, ForeignKey('departments.dept_id'),nullable=False) 

    department = relationship("Department", backref="users")

    # Establish relationship with Department
    # department = relationship("Department", back_populates="users")
