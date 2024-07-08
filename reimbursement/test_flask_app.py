from io import BytesIO
import unittest
from configurations import config
from app import app, log_audit
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configurations.config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME

class TestApp(unittest.TestCase):
    def setUp(self):
        # initializing a test client
        self.app = app.test_client()


    def test_session_creation(self):
        # creating SQLAlchemy session 
        db_uri = f"mysql://{config.DB_USERNAME}:{config.DB_PASSWORD}@{config.DB_HOST}/{config.DB_NAME}"
        engine = create_engine(db_uri)
        Session = sessionmaker(bind=engine)
        session = Session()

        # checking if the session object is created successfully
        self.assertIsNotNone(session)
        session.close()

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_login_valid_admin_credentials(self):
        response = self.app.post('/login', data={'email': 'divyansh@nucleusteq.com', 'password': 'Divyansh123'})
        self.assertEqual(response.status_code, 302)
        print(f"the logged user is a admin,redirected to {response.location}")
        self.assertEqual(response.location, '/admin/dashboard')

    def test_login_valid_manager_credentials(self):
        response = self.app.post('/login', data={'email': 'xander@nucleusteq.com', 'password': 'Xander123'})
        self.assertEqual(response.status_code, 302)
        print(f"the logged user is a manager,redirected to {response.location}")
        self.assertEqual(response.location, '/manager/dashboard')

    def test_login_valid_employee_credentials(self):
        response = self.app.post('/login', data={'email': 'adam@nucleusteq.com', 'password': 'Adam123'})
        self.assertEqual(response.status_code, 302)
        print(f"the logged user is an employee,redirected to {response.location}")
        self.assertEqual(response.location, '/employee/dashboard')

    def test_login_invalid_credentials(self):
        response = self.app.post('/login', data={'email': 'xandeer@nucleusteq.com', 'password': 'Xander123'})
        print(f"code id {response.status_code}")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid Credentials', response.data)
        print("Invalid credentials, user returned to login")

    def get_user_image(self):
        with open('C:/Users/ASUS/Desktop/NTeq_Assignments_Learning/reimbursement/static/images/manform.jpg', 'rb') as img_file:
            return BytesIO(img_file.read()), 'manform.jpg'

    def test_register_success(self):
        sample_image = self.get_user_image()
        response = self.app.post('/register', data={
            'full_name': 'John Doe',
            'email': 'john.doe3@nucleusteq.com',
            'password': 'password123',
            'department': '1',  # '1' is a valid department ID
            'user_image': sample_image
        }, content_type='multipart/form-data', follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'User registered successfully', response.data)

    def test_register_duplicate_email(self):
        sample_image = self.get_user_image()     
        response = self.app.post('/register', data={
            'full_name': 'Dummy',
            'email': 'dummy@nucleusteq.com',
            'password': 'password123',
            'department': '1',  
            'user_image': (sample_image)
        }, content_type='multipart/form-data')

        self.assertEqual(response.status_code, 200)
        # print(response.data)
        self.assertIn(b'User with this email already exists.', response.data)

    def test_logout(self):
        # adding a user to the session for testing
        with self.app.session_transaction() as sess:
            sess['user_id'] = 1  
        
        response = self.app.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)   
        self.assertIn(b'Login', response.data)
        # checking if the session is cleared
        with self.app.session_transaction() as sess:
            self.assertIsNone(sess.get('user_id'))

    def test_assign_manager_success(self):
        response = self.app.post('/assign_manager', data={
            'employee_id': '38',  
            'manager_id': '4'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Employee-Manager assigned successfully', response.data)

    def test_assign_manager_invalid_manager(self):
        response = self.app.post('/assign_manager', data={
            'employee_id': '35',  
            'manager_id': '999'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Employee or Manager not found', response.data)

    def test_make_manager_success(self):
        #  successful manager assignment
        response = self.app.post('/make_manager', data={"employee_id": '37'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Manager made successfully", response.data)
        # print(response.data)

    def test_make_manager_employee_not_found(self):
        #  the condition where the employee is not found
        response = self.app.post('/make_manager', data={"employee_id": '137'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Employee not found", response.data)
        # print(response.data)

    def test_make_manager_already_a_manager(self):
        # the condition where the employee is already a manager
        response = self.app.post('/make_manager', data={"employee_id": '3'})  
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Employee Already a Manager", response.data)
        # print(response.data)

    
    def test_delete_employee_success(self):
        # Successful employee deletion
        response = self.app.post('/delete_employee', data={"employee_id": '33'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Employee deleted successfully", response.data)
        # print(response.data)

    def test_delete_employee_not_found(self):
        # Employee not found
        response = self.app.post('/delete_employee', data={"employee_id": '133'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Employee not found", response.data)
        # print(response.data)
    

    def test_add_department(self):
        response=self.app.post('/add_department',data={"dept_name":"exam_dept","city":"Pune"})
        self.assertEqual(response.status_code,200)
        self.assertIn(b"department added successfully",response.data)
        # print(response.data)

    def test_delete_department_success(self):
        # Successful department deletion
        response = self.app.post('/delete_department', data={"dept_id": 31})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Department deleted successfully", response.data)
        # print(response.data)

    def test_delete_department_not_found(self):
        # Department not found
        response = self.app.post('/delete_department', data={"dept_id": 16})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Department not found", response.data)
        # print(response.data)

    
    def get_receipt_image(self):
        with open('C:/Users/ASUS/Desktop/NTeq_Assignments_Learning/reimbursement/static/images/flight3.jpg', 'rb') as img_file:
            return BytesIO(img_file.read()), 'manform.jpg'

    def test_submit_reimbursement(self):
          # setting user_id in session
        with self.app as c:
             with c.session_transaction() as sess:
                 sess['user_id'] = '18'

        # get receipt image
        receipt_image=self.get_receipt_image()
        response=self.app.post('/submit_reimbursement',data={
            "requestCategory":"Travel",
            "expenseType":"flight",
            "otherExpenseType":" ",
            "amount":"8100",
            "date":"amount",
            "receipt":receipt_image,
            "userRoleforSubmit":"Employee ", 
        }, content_type='multipart/form-data', follow_redirects=True)
        self.assertEqual(response.status_code,200)
        self.assertIn(b"reimbursement requested successfully",response.data)
        # print(response.data)

    def test_approve_reimbursement_manager(self):
        # successful approval by a valid manager
        with self.app as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 3  # Manager ID

            response = self.app.post('/approve_reimbursement', data={
                'request_id': '47',
                'comment': 'approved by Manager',
                'userRole': 'manager'
            })

            self.assertIn(b'Reimbursement approved successfully.', response.data)
            self.assertEqual(response.status_code, 200)
            print(response.data)

    
    def test_approve_reimbursement_manager_reimbursement_not_found(self):
        response = self.app.post('/approve_reimbursement', data={
            'request_id': '188',
            'comment': 'approved by manager',
            'userRole': 'manager'  
        })
        # if reimbursement not present
        self.assertIn(b'Error approving reimbursement', response.data)
        self.assertEqual(response.status_code, 200)
        print(response.data)

    def test_approve_reimbursement_unAuthorized_manager(self):
        #manager trying to approve the request which is not under him
        with self.app as c:
             with c.session_transaction() as sess:
                 sess['user_id'] = '3'
        response = self.app.post('/approve_reimbursement', data={
            'request_id': '154',
            'comment': 'Approved by manager',
            'userRole': 'manager'  
        })

        self.assertIn(b'You are not authorized to approve this request', response.data)
        self.assertEqual(response.status_code, 200)
        # print(response.data)

    def test_approve_reimbursement_admin(self):
        # successful approvement by admin 
        with self.app as c:
             with c.session_transaction() as sess:
                 sess['user_id'] = '1'
        response = self.app.post('/approve_reimbursement', data={
            'request_id': '49',
            'comment': 'Approved by admin',
            'userRole': 'admin'  
        })

        self.assertIn(b'Reimbursement Approved successfully', response.data)
        self.assertEqual(response.status_code, 200)
        print(response.data)
      
    def test_approve_reimbursement_under_admin_not_found(self):
        response = self.app.post('/reject_reimbursement', data={
            'request_id': '188',
            'comment': 'approved by admin',
            'userRole': 'admin'  
        })
        # if reimbursement not present
        self.assertIn(b'Error in Reimbursement Rejection', response.data)
        self.assertEqual(response.status_code, 200)
        # print(response.data)

    def test_reject_reimbursement_admin(self):
        #successful rejectionn by admin
        with self.app as c:
             with c.session_transaction() as sess:
                 sess['user_id'] = '1'
        response = self.app.post('/reject_reimbursement', data={
            'request_id': '141',
            'comment': 'Rejected by admin',
            'userRole': 'admin'  
        })
        self.assertIn(b'Reimbursement rejected successfully', response.data)
        self.assertEqual(response.status_code, 200)
        # print(response.data)

    def test_reject_reimbursement_under_admin_not_found(self):

        response = self.app.post('/reject_reimbursement', data={
            'request_id': '188',
            'comment': 'Rejected by admin',
            'userRole': 'admin'  
        })
        # if reimbursement not present
        self.assertIn(b'Error in Reimbursement Rejection', response.data)
        self.assertEqual(response.status_code, 200)
        # print(response.data)
            
    def test_reject_reimbursement_manager(self):
        #successful rejectionn by admin
        with self.app as c:
             with c.session_transaction() as sess:
                 sess['user_id'] = '3'
        response = self.app.post('/reject_reimbursement', data={
            'request_id': '47',
            'comment': 'Rejected by Manager',
            'userRole': 'manager'  
        })

        # self.assertIn(b'Reimbursement rejected successfully', response.data)
        # self.assertEqual(response.status_code, 200)
        # print(response.data)

    def test_reject_reimbursement_under_manager_not_found(self):    
        response = self.app.post('/reject_reimbursement', data={
            'request_id': '188',
            'comment': 'Rejected by manager',
            'userRole': 'manager'  
        })
        # if reimbursement not present
        self.assertIn(b'Error rejecting reimbursement', response.data)
        self.assertEqual(response.status_code, 200)
        print(response.data)

    def test_reject_reimbursement_unAuthorized_manager(self):   
        #manager trying to reject the request which is not under him
        with self.app as c:
             with c.session_transaction() as sess:
                 sess['user_id'] = '4'
        response = self.app.post('/reject_reimbursement', data={
            'request_id': '141',
            'comment': 'Rejected by manager',
            'userRole': 'manager' 
        })

        self.assertIn(b'You are not authorized to approve this request', response.data)
        self.assertEqual(response.status_code, 200)
        print(response.data)
    
    def test_employee_dashboard(self):
        with self.app.session_transaction() as session:
          session['user_id'] = 5  # Replace with a valid user ID
        
        # Simulate a request to /employee/dashboard
        with self.app:
            response = self.app.get('/employee/dashboard', follow_redirects=True)
            
        self.assertEqual(response.status_code, 200)
        result = response.data.decode('utf-8')
        # print(result)
        self.assertIn(b'adam@nucleusteq.com', response.data)  
        self.assertIn(b'#158', response.data)  
        self.assertIn(b'#2', response.data)  

    def test_manager_dashboard(self):
        with self.app.session_transaction() as session:
          session['user_id'] = 4 # Replace with a valid user ID
        
        #  a request to /employee/dashboard
        with self.app:
            response = self.app.get('/manager/dashboard', follow_redirects=True)
            
        self.assertEqual(response.status_code, 200)
        result = response.data.decode('utf-8')
        # print(result)
        self.assertIn(b'xander@nucleusteq.com', response.data) 

    def test_admin_dashboard(self):
        with self.app.session_transaction() as session:
          session['user_id'] = 1  
        
        # a request to /employee/dashboard
        with self.app:
            response = self.app.get('/admin/dashboard', follow_redirects=True)
            
        self.assertEqual(response.status_code, 200)
        result = response.data.decode('utf-8')
        # print(result)
        self.assertIn(b'divyansh@nucleusteq.com', response.data)
    
          
    def test_log_audit(self):
        # Call the log_audit function
        action = 'TEST_ACTION'
        details = 'Test details'
        log_audit(action, details)
        
        with open('audit_trail.log', 'r') as log_file:
            log_output = log_file.read()
            expected_log_message = f"Action: {action}, {details}"
            self.assertIn(expected_log_message, log_output)


    def test_update_reimbursement(self):
        
        with self.app.session_transaction() as session:
            session['user_id'] = 18 #  a valid user ID
        # get receipt image
        receipt_image=self.get_receipt_image()
        # request to /update_reimbursement
        with self.app:
            response = self.app.post('/update_reimbursement', data={
                'updateRequestId': '159',  # a valid reimbursement ID
                'updateRequestCategory': 'Travel',
                'updateExpenseType': 'Flight',
                'updateOtherExpenseType': '',
                'updateAmount': '2350',
                'updateDate': '2024-05-31',
                'updateReceipt': receipt_image
            }, follow_redirects=True, content_type='multipart/form-data')

        self.assertEqual(response.status_code, 200)

        self.assertIn(b'Reimbursement updated successfully.', response.data)

    def test_update_reimbursement_reimbursement_not_found(self):
        # Set up session data
        with self.app.session_transaction() as session:
            session['user_id'] = 5  #  valid user ID
          # get receipt image
        receipt_image=self.get_receipt_image()
        #   request to /update_reimbursement with an invalid reimbursement ID
        with self.app:
            response = self.app.post('/update_reimbursement', data={
                'updateRequestId': '999',  # Invalid reimbursement ID
                'updateRequestCategory': 'Travel',
                'updateExpenseType': 'Flight',
                'updateOtherExpenseType': '',
                'updateAmount': '2300',
                'updateDate': '2024-05-31',
                'updateReceipt': receipt_image
            }, follow_redirects=True, content_type='multipart/form-data')

        self.assertEqual(response.status_code, 200)

        self.assertIn(b'Error updating reimbursement.', response.data)
if __name__ == '__main__':
    unittest.main()
