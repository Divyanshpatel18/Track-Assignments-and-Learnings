from io import BytesIO
import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        # initializing a test client
        self.app = app.test_client()

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_login_valid_admin_credentials(self):
        response = self.app.post('/login', data={'email': 'Divyansh@gmail.com', 'password': 'Divyansh123'})
        self.assertEqual(response.status_code, 302)
        print(f"the logged user is a admin,redirected to {response.location}")
        self.assertEqual(response.location, '/admin/dashboard')

    def test_login_valid_manager_credentials(self):
        response = self.app.post('/login', data={'email': 'Xander@gmail.com', 'password': 'Xander123'})
        self.assertEqual(response.status_code, 302)
        print(f"the logged user is a manager,redirected to {response.location}")
        self.assertEqual(response.location, '/manager/dashboard')

    def test_login_valid_employee_credentials(self):
        response = self.app.post('/login', data={'email': 'Adam@gmail.com', 'password': 'Adam123'})
        self.assertEqual(response.status_code, 302)
        print(f"the logged user is an employee,redirected to {response.location}")
        self.assertEqual(response.location, '/employee/dashboard')

    def test_login_invalid_credentials(self):
        response = self.app.post('/login', data={'email': 'Xandeer@gmail.com', 'password': 'Xander123'})
        print(f"code id {response.status_code}")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid Credentials', response.data)
        print("Invalid credentials, user returned to login")

    def get_user_image(self):
        with open('C:/Users/ASUS/Desktop/reimbursement/static/images/manform.jpg', 'rb') as img_file:
            return BytesIO(img_file.read()), 'manform.jpg'

    def test_register_success(self):
        sample_image = self.get_user_image()
        response = self.app.post('/register', data={
            'full_name': 'John Doe',
            'email': 'john.doe2@example.com',
            'password': 'password123',
            'department': '1',  # Assuming '1' is a valid department ID
            'user_image': sample_image
        }, content_type='multipart/form-data', follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'user registered successfully', response.data)

    def test_register_duplicate_email(self):
        sample_image = self.get_user_image()     
        response = self.app.post('/register', data={
            'full_name': 'Dummy',
            'email': 'Dummy@gmail.com',
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
            'employee_id': '18',  
            'manager_id': '4'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Employee-Manager assigned successfully', response.data)

    def test_assign_manager_invalid_manager(self):
        response = self.app.post('/assign_manager', data={
            'employee_id': '27',  
            'manager_id': '999'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Employee or Manager not found', response.data)

    def test_make_manager_success(self):
        #  successful manager assignment
        response = self.app.post('/make_manager', data={"employee_id": '17'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Manager assigned successfully", response.data)
        print(response.data)

    def test_make_manager_employee_not_found(self):
        #  the condition where the employee is not found
        response = self.app.post('/make_manager', data={"employee_id": '27'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Employee not found", response.data)
        print(response.data)

    def test_make_manager_already_a_manager(self):
        # the condition where the employee is already a manager
        response = self.app.post('/make_manager', data={"employee_id": '3'})  
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Employee Already a Manager", response.data)
        # print(response.data)

    
    def test_delete_employee_success(self):
        # Successful employee deletion
        response = self.app.post('/delete_employee', data={"employee_id": '7'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Employee deleted successfully", response.data)
        print(response.data)

    def test_delete_employee_not_found(self):
        # Employee not found
        response = self.app.post('/delete_employee', data={"employee_id": '25'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Employee not found", response.data)
        print(response.data)
    

    def test_add_department(self):
        response=self.app.post('/add_department',data={"dept_name":"Xyz","city":"delhi"})
        self.assertEqual(response.status_code,200)
        self.assertIn(b"department added successfully",response.data)
        print(response.data)

    def test_delete_department_success(self):
        # Successful department deletion
        response = self.app.post('/delete_department', data={"dept_id": 4})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Department deleted successfully", response.data)
        print(response.data)

    def test_delete_department_not_found(self):
        # Department not found
        response = self.app.post('/delete_department', data={"dept_id": 16})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Department not found", response.data)
        print(response.data)

    
    def get_receipt_image(self):
        with open('C:/Users/ASUS/Desktop/reimbursement/static/images/flight3.jpg', 'rb') as img_file:
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
        # successful approvement by admin and valid manager
        with self.app as c:
             with c.session_transaction() as sess:
                 sess['user_id'] = '1'
        response = self.app.post('/approve_reimbursement', data={
            'request_id': '145',
            'comment': 'Approved by admin',
            'userRole': 'admin'  
        })

        self.assertIn(b'Reimbursement Approved successfully', response.data)
        self.assertEqual(response.status_code, 200)
        print(response.data)
        #manager trying to approve the request which is not under him
        with self.app as c:
             with c.session_transaction() as sess:
                 sess['user_id'] = '3'
        response = self.app.post('/approve_reimbursement', data={
            'request_id': '49',
            'comment': 'Approved by manager',
            'userRole': 'manager'  # Note: the key should be 'userRole', not 'user_role'
        })

        self.assertIn(b'You are not authorized to approve this request', response.data)
        self.assertEqual(response.status_code, 200)
        print(response.data)

    def test_reject_reimbursement_manager(self):
        #successful rejectionn by admin and valid manager
        with self.app as c:
             with c.session_transaction() as sess:
                 sess['user_id'] = '1'
        response = self.app.post('/reject_reimbursement', data={
            'request_id': '188',
            'comment': 'Rejected by admin',
            'userRole': 'admin'  
        })

        self.assertIn(b'Reimbursement rejected successfully', response.data)
        self.assertEqual(response.status_code, 200)
        print(response.data)
        
        response = self.app.post('/reject_reimbursement', data={
            'request_id': '188',
            'comment': 'Rejected by admin',
            'userRole': 'admin'  
        })
        # if reimbursement not present
        self.assertIn(b'Error in Reimbursement Rejection', response.data)
        self.assertEqual(response.status_code, 200)
        print(response.data)

        #manager trying to reject the request which is not under him
        with self.app as c:
             with c.session_transaction() as sess:
                 sess['user_id'] = '4'
        response = self.app.post('/reject_reimbursement', data={
            'request_id': '124',
            'comment': 'Rejected by manager',
            'userRole': 'manager' 
        })

        self.assertIn(b'You are not authorized to approve this request', response.data)
        self.assertEqual(response.status_code, 200)
        print(response.data)
          
if __name__ == '__main__':
    unittest.main()
