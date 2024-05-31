from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Entities.CreateTables import Reimbursement
from configurations.config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME

Base = declarative_base()

# Creating the database connection string
db_uri = f"mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Creating an engine to connect to the MySQL database
engine = create_engine(db_uri)
def add_reimbursement(user_id,request_category,expense_type, other_expense_type, amount, date,receipt):
    try:  
        new_reimbursement = Reimbursement(user_id=user_id,request_category=request_category,expense_type=expense_type, other_expense_type=other_expense_type, amount=amount, date=date,receipt=receipt)
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(new_reimbursement)
        session.commit()
        session.close()
        return True
    except Exception as e:
        print(f"Error occurred while adding reimbursement: {e}")
        return False

def update_user_reimbursement(reimbursement_id, request_category, expense_type, other_expense_type, amount, date, receipt):
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
    
        reimbursement = session.query(Reimbursement).filter_by(id=reimbursement_id).first()
        
        if reimbursement:
            reimbursement.request_category = request_category
            reimbursement.expense_type = expense_type
            reimbursement.other_expense_type = other_expense_type
            reimbursement.amount = amount
            reimbursement.date = date
            
            if receipt:
                reimbursement.receipt = receipt
            session.commit()
            session.close()
            return True
        else:
            print("Reimbursement record not found")
            return False
    except Exception as e:
        print(f"Error occurred while updating reimbursement: {e}")
        return False
