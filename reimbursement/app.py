import base64
import logging
import werkzeug
from flask import Flask, jsonify, render_template, request, redirect, session, url_for
from sqlalchemy.orm import sessionmaker, joinedload
from sqlalchemy import and_, create_engine, desc, func, or_
from Entities.CreateTables import Department, Reimbursement, User
from Entities.Department import add_departments, delete_departments, get_all_departments
from Entities.Reimbursement import add_reimbursement, update_user_reimbursement
from Entities.User import add_user, authenticate_user, delete_user, get_user_by_email
from configurations import config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
from configurations.config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Create the database connection string
db_uri = f"mysql://{config.DB_USERNAME}:{config.DB_PASSWORD}@{config.DB_HOST}/{config.DB_NAME}"

# Create an engine to connect to the MySQL database
engine = create_engine(db_uri)

# Create a sessionmaker to interact with the database
Session = sessionmaker(bind=engine)
# --------------------------------------------------------------

# Configure the logging'
log_level=logging.DEBUG
log_file='audit_trail.log'
log_file_mode='a'
log_format='%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(filename=log_file,
                    level=log_level,
                    format=log_format,
                    filemode=log_file_mode)


def log_audit(action, details):
    logging.info(f"Action: {action}, {details}")

# Disable logging of static file requests
werkzeug.serving.WSGIRequestHandler.log_request = lambda *args, **kwargs: None
# ----------------------------------------------------------------

# 1. RENDER LOGIN TEMPLATE AT ROOT
@app.route('/')
def hello():
    try:
        log_audit("API_ROUTE", " route  /  called")
        return render_template('authentication/login.html')
    except Exception as e:
        logging.error(f"Error rendering login template: {e}")
        return render_template('/components/notification.html', notification_title='Error', 
                                    notification_message='Error in rendering Home Page',
                                    notification_type='error',
                                    icon='times',
                                    href='/admin/dashboard')  

# ---------------------------------------------------------------
# 2. ROUTE FOR ADMIN DASHBOARD
@app.route('/admin/dashboard')
def admin_dashboard():
    try:
        log_audit("API_ROUTE", "route /admin/dashboard called") 
        if 'user_id' in session:
            user_id = session['user_id']
            print(f"user id is {user_id}")
        
            # Get user details from database
            db_session = Session()
            user = db_session.query(User).filter_by(id=user_id).first()
            log_audit("ACCESS_DASHBOARD", f"User {user.full_name} accessed the admin dashboard")
            department_name = db_session.query(Department.dept_name).join(User, User.department_id == Department.dept_id).first()[0]
            
            log_audit("ACCESS_DASHBOARD", f"fetching USER count")
            # Get total number of users
            total_users = db_session.query(User.id).count()
            
            log_audit("ACCESS_DASHBOARD", f"fetching DEPARTMENT count")
            # Get total number of departments
            total_departments = db_session.query(Department.dept_id).count()

            log_audit("ACCESS_DASHBOARD", f"fetching PENDING REIMBURSEMENT count")
            # Get total number of pending reimbursements
            total_pending_reimbursements = db_session.query(Reimbursement.id).filter(Reimbursement.status == 'Pending').count()

            log_audit("ACCESS_DASHBOARD", f"fetching APPROVED/REJECTED REIMBURSEMENT count")
            # Get total number of approved/rejected reimbursements
            total_approved_rejected_reimbursements = db_session.query(Reimbursement.id).filter(Reimbursement.status != 'Pending').count()


            log_audit("ACCESS_DASHBOARD", f"fetching UNCHECKED_MANAGERS_REIMBURSEMENT_REQUESTS")
            unchecked_managers_reimbursement_requests = (
                db_session.query(Reimbursement)
                .join(User, Reimbursement.user_id == User.id)  # Joining User table with Reimbursement table
                .options(joinedload(Reimbursement.user))  # Eager loading of associated User data
                .filter(
                    or_(
                        User.role == "manager",  # Filtering for users with role as "manager"
                        User.manager_id == 1  # Filtering for users with manager_id as 1
                    ),
                    Reimbursement.status == 'Pending'  # Filtering for pending reimbursements
                )
                .all()
            )
            log_audit("ACCESS_DASHBOARD", f"fetching CHECKED_MANAGERS_REIMBURSEMENT_REQUESTS")
            checked_managers_reimbursement_requests = (
                db_session.query(Reimbursement)
                .join(User, Reimbursement.user_id == User.id)  # Joining User table with Reimbursement table
                .options(joinedload(Reimbursement.user))  # Eager loading of associated User data
                .filter(
                    or_(
                        User.role == "manager",  # Filtering for users with role as "manager"
                        User.manager_id == 1  # Filtering for users with manager_id as 1
                    ),
                    Reimbursement.status != 'Pending'  # Filtering for reimbursements that are not pending
                )
                .all()
            )
            log_audit("ACCESS_DASHBOARD", f"fetching LATEST_REIMBURSEMENT_REQUESTS")
            latest_reimbursements = db_session.query(Reimbursement).options(joinedload(Reimbursement.user)).order_by(desc(Reimbursement.id)).limit(10).all()

            log_audit("ACCESS_DASHBOARD", f"decoding UNCHECKED_MANAGERS_REIMBURSEMENT_REQUESTS receipt and user images ")
            for reimbursement in unchecked_managers_reimbursement_requests:
                if reimbursement.receipt:
                    reimbursement.receipt = base64.b64encode(reimbursement.receipt).decode('utf-8')
                if reimbursement.user.user_image:
                    if isinstance(reimbursement.user.user_image, bytes):
                        reimbursement.user.user_image = base64.b64encode(reimbursement.user.user_image).decode('utf-8')

            log_audit("ACCESS_DASHBOARD", f"decoding CHECKED_MANAGERS_REIMBURSEMENT_REQUESTS receipt and user images" )
            for reimbursement in checked_managers_reimbursement_requests:
                if reimbursement.receipt:
                    reimbursement.receipt = base64.b64encode(reimbursement.receipt).decode('utf-8')
                if reimbursement.user.user_image:                                
                    if isinstance(reimbursement.user.user_image, bytes):
                        reimbursement.user.user_image = base64.b64encode(reimbursement.user.user_image).decode('utf-8')
                
            log_audit("ACCESS_DASHBOARD", f"decoding LATEST_REIMBURSEMENT_REQUESTS receipt and user images ")   
            # Assuming latest_reimbursements contains all reimbursement requests
            for reimbursement in latest_reimbursements:
                if reimbursement.receipt:
                    if isinstance(reimbursement.receipt, bytes):
                        reimbursement.receipt = base64.b64encode(reimbursement.receipt).decode('utf-8')     
                # Encode user image if it exists
                if reimbursement.user.user_image:
                    if isinstance(reimbursement.user.user_image, bytes):
                        reimbursement.user.user_image = base64.b64encode(reimbursement.user.user_image).decode('utf-8')

            if user.user_image:
                user.user_image = base64.b64encode(user.user_image).decode('utf-8')
            db_session.close()
        
            
            if user:
                log_audit("ACCESS_DASHBOARD", f"passing variables to adminDashboard.html")   
                return render_template('/dashboards/adminDashboard.html',
                                        user=user, department_name=department_name,
                                        total_users=total_users,
                                        total_departments=total_departments,
                                        total_pending_reimbursements=total_pending_reimbursements,
                                        total_approved_rejected_reimbursements=total_approved_rejected_reimbursements,
                                        latest_reimbursements=latest_reimbursements,
                                        max_users=50,
                                        max_departments=8,
                                        max_approved_rejected_reimbursements=100,
                                        max_pending_reimbursements=15,
                                        unchecked_managers_reimbursement_requests=unchecked_managers_reimbursement_requests,
                                        checked_managers_reimbursement_requests=checked_managers_reimbursement_requests,
                                        )
        return redirect(url_for('login'))
    
    except Exception as e:
        logging.error(f"Error rendering admin dashboard: {e}")
        return render_template('/components/notification.html',
                               notification_title='Error',
                               notification_message='Error in rendering Admin Dashboard',
                               notification_type='error',
                               icon='times',
                               href='/login')
# ---------------------------------------------------------------

# 3.ROUTE FOR EMPLOYEE DASHBOARD
@app.route('/employee/dashboard')
def employee_dashboard():
    try:
        log_audit("API_ROUTE", "route /employee/dashboard called") 
        if 'user_id' in session:
            user_id = session['user_id']
            # Get user details from database
            db_session = Session()
            user = db_session.query(User).filter_by(id=user_id).first()
            
            log_audit("ACCESS_DASHBOARD", f"User {user.full_name} accessed the employee dashboard")
            department_name = db_session.query(Department.dept_name).join(User, User.department_id == Department.dept_id).first()[0]
            
            log_audit("ACCESS_DASHBOARD", f"fetching PENDING REIMBURSEMENT REQUESTS")
            emp_unchecked_reimbursement_requests=db_session.query(Reimbursement).join(User).filter(User.id==user_id).filter(Reimbursement.status=='pending').all()
            
            log_audit("ACCESS_DASHBOARD", f"fetching APPROVED/REJECTED_REIMBURSEMENT_REQUESTS")
            emp_checked_reimbursement_requests=db_session.query(Reimbursement).join(User).filter(User.id==user_id).filter(or_(Reimbursement.status=='approved',Reimbursement.status=='rejected')).all()
            
            log_audit("ACCESS_DASHBOARD", f"decoding REIMBURSEMENT_REQUESTS receipt and user images ")  
            for reimbursement in  emp_unchecked_reimbursement_requests:
                reimbursement.receipt = base64.b64encode(reimbursement.receipt).decode('utf-8')

            for reimbursement in emp_checked_reimbursement_requests:
                reimbursement.receipt = base64.b64encode(reimbursement.receipt).decode('utf-8')
            
            if user.user_image:
                user.user_image = base64.b64encode(user.user_image).decode('utf-8')

            db_session.close()
        
            if user:
                log_audit("ACCESS_DASHBOARD", f"passing variables to employeeDashboard.html")
                return render_template('/dashboards/employeeDashboard.html', 
                                    user=user,
                                    department_name=department_name,
                                    emp_unchecked_reimbursement_requests=emp_unchecked_reimbursement_requests,
                                    emp_checked_reimbursement_requests=emp_checked_reimbursement_requests)
        return redirect(url_for('login'))
    
    except Exception as e:
        logging.error(f"Error rendering employee dashboard: {e}")
        return render_template('/components/notification.html',
                               notification_title='Error',
                               notification_message='Error in rendering Employee Dashboard',
                               notification_type='error',
                               icon='times',
                               href='/login')

# ---------------------------------------------------------------

# 4. ROUTE FOR MANAGER DASHBOARD
@app.route('/manager/dashboard')
def manager_dashboard():
    try:
        log_audit("API_ROUTE", "route /manager/dashboard called") 
        if 'user_id' in session:
            user_id=session['user_id']
            print(f'userID is {user_id} ')
            db_session=Session()
            user=db_session.query(User).filter_by(id=user_id).first()

            log_audit("ACCESS_DASHBOARD", f"User {user.full_name} accessed the manager dashboard")
            log_audit("ACCESS_DASHBOARD", f"fetching PENDING REIMBURSEMENT REQUESTS")
            Unchecked_reimbursement_requests = db_session.query(Reimbursement).options(joinedload(Reimbursement.user)).join(User).filter(
                and_(
                    User.manager_id == user_id,
                    Reimbursement.status == 'Pending'
                )
            ).all()

            
            log_audit("ACCESS_DASHBOARD", f"fetching APPROVED/REJECTED_REIMBURSEMENT_REQUESTS")
            # Query for checked reimbursement requests with user details
            checked_reimbursement_requests = db_session.query(Reimbursement).options(joinedload(Reimbursement.user)).join(User).filter(
                (User.manager_id == user_id),
                User.id != user_id,  # Exclude the manager's own requests
                or_(Reimbursement.status == 'Approved', Reimbursement.status == 'Rejected')
            ).all()

            log_audit("ACCESS_DASHBOARD", f"fetching SELF_REIMBURSEMENT_REQUESTS")
            self_reimbursement_requests= db_session.query(Reimbursement).options(joinedload(Reimbursement.user)).join(User).filter(
                (User.id == user_id)  # Fetch reimbursements where the user ID matches the manager's ID
            ).all()
            department_name = db_session.query(Department.dept_name).join(User, User.department_id == Department.dept_id).first()[0]
            
            log_audit("ACCESS_DASHBOARD", f"fetching EMPLOYEES_UNDER_MANAGER ")
            employees_under_manager = db_session.query(User).options(joinedload(User.department)).filter(User.manager_id == user_id).all()
           
            log_audit("ACCESS_DASHBOARD", f"decoding REIMBURSEMENT_REQUESTS receipt and user images ")
            for reimbursement in Unchecked_reimbursement_requests:
                reimbursement.receipt = base64.b64encode(reimbursement.receipt).decode('utf-8')

            for reimbursement in checked_reimbursement_requests:
                reimbursement.receipt = base64.b64encode(reimbursement.receipt).decode('utf-8')
            
            for reimbursement in self_reimbursement_requests:
                reimbursement.receipt = base64.b64encode(reimbursement.receipt).decode('utf-8')

            for employee in employees_under_manager:
                employee.user_image=base64.b64encode(employee.user_image).decode('utf-8')
            
            if user.user_image:
                user.user_image = base64.b64encode(user.user_image).decode('utf-8')       
            print(f'user is {user}')
            db_session.close()
            if user:
                log_audit("ACCESS_DASHBOARD", f"passing variables to managerDashboard.html")
                return render_template('/dashboards/managerDashboard.html',
                                    department_name=department_name,
                                    user=user,Unchecked_reimbursement_requests=Unchecked_reimbursement_requests,
                                    checked_reimbursement_requests=checked_reimbursement_requests,
                                    self_reimbursement_requests=self_reimbursement_requests,
                                    employees_under_manager=employees_under_manager)
        return redirect(url_for('login')) 
      
    except Exception as e:
        logging.error(f"Error rendering Manager dashboard: {e}")
        return render_template('/components/notification.html',
                               notification_title='Error',
                               notification_message='Error in rendering Manager Dashboard',
                               notification_type='error',
                               icon='times',
                               href='/login')

# ---------------------------------------------------------------

# 5. ROUTE FOR REGISTER FORM
@app.route('/register_form')
def register_form():
    try:
        print('in register calling get all departments')
        log_audit("ACCESS_REGISTER_FORM", "Fetching all the departments")
        departments = get_all_departments()
        log_audit("ACCESS_REGISTER_FORM", f"Departments fetched successfully, count: {len(departments)}")

        return render_template('authentication/register.html', departments=departments)
    except Exception as e:
        logging.error(f"Error accessing register form: {e}")
        return render_template('/components/notification.html',
                               notification_title='Error',
                               notification_message='Error in accessing register form',
                               notification_type='error',
                               icon='times',
                               href='/register_form')
# ---------------------------------------------------------------

# 6.  ROUTE TO SUBMIT THE REGISTER FORM
@app.route('/register', methods=['GET', 'POST'])
def register():
    try:
        if request.method == 'POST':
            # Get form data
            full_name = request.form['full_name']
            email = request.form['email']
            password = request.form['password']
            department_id = request.form['department']
            user_image = request.files['user_image'].read() 
            # dept_id=get_id_by_department_name(department)
            # print(f'serarching for dept name is {department}')
            # Convert department ID to an integer
                    # Debugging statement to check the department ID
            print("Department ID:", department_id)
            log_audit("REGISTER_ATTEMPT", f"User {email} is attempting to register")
            # Check for existing user with the same email
            existing_user = get_user_by_email(email)  # Add this function to fetch user by email
            if existing_user:
                log_audit("REGISTER_FAIL", f"Registration failed for {email}: User already exists")
                return render_template('/components/notification.html', notification_title='Error',
                                    notification_message='User with this email already exists.',
                                    notification_type='error',
                                    icon='times',
                                    href='/')
            department_id = int(department_id)
            # Call the add_user function to store user data in the database
            result=add_user(full_name, email, password, department_id,user_image)

            if result:
                log_audit("REGISTER_SUCCESS", f"User {email} registered successfully")
                # Redirect to a success page or any other desired page after registration
                return render_template('/components/notification.html', notification_title='Success',
                                       notification_message='User registered successfully.',
                                       notification_type='success',
                                       icon='check',
                                       href='/login')
            else:
                log_audit("REGISTER_FAIL", f"Registration failed for {email}: Database error")
                return render_template('/components/notification.html', notification_title='Error',
                                       notification_message='Error in registration. Please try again.',
                                       notification_type='error',
                                       icon='times',
                                       href='/register')
                                

        # Render the registration form template
        log_audit("ACCESS_REGISTER_FORM", "Rendering register form")
        return render_template('/components/notification.html', notification_title='Error', 
                                notification_message='Error in registration',
                                notification_type='error',
                                icon='times',
                                href='/register')
    except Exception as e:
        logging.error(f"Error during registration: {e}")
        return render_template('/components/notification.html', notification_title='Error',
                               notification_message='Error in registration process. Please try again later.',
                               notification_type='error',
                               icon='times',
                               href='/register')

# ---------------------------------------------------------------

# 7. ROUTE FOR LOGIN 
@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'POST':
            # Get form data
            email = request.form['email']
            password = request.form['password']

            log_audit("LOGIN_ATTEMPT", f"User {email} is attempting to log in")
            # Authenticate user credentials
            user = authenticate_user(email, password)

            if user:
                session['user_id']=user.id
                log_audit("LOGIN_SUCCESS", f"User {email} logged in successfully")
                if user.role == "admin":
                    return redirect('/admin/dashboard')
                elif user.role == "manager":
                    return redirect('/manager/dashboard')
                else:
                    return redirect('/employee/dashboard')
            else:
                # Return an error message if authentication fails
                log_audit("LOGIN_FAIL", f"Login failed for {email}: Invalid credentials")
                return render_template('/components/notification.html', notification_title='Error', 
                                notification_message='Invalid Credentials',
                                notification_type='error',
                                icon='times',
                                href='/')

        else:
            # Render the login form template
            log_audit("ACCESS_LOGIN_FORM", "Rendering login form")
            return render_template('authentication/login.html')
        
    except Exception as e:
        logging.error(f"Error during login: {e}")
        return render_template('/components/notification.html', notification_title='Error', 
                               notification_message='Error in login process. Please try again later.',
                               notification_type='error',
                               icon='times',
                               href='/login')


# ---------------------------------------------------------------

# 8. ROUTE FOR LOGOUT
@app.route('/logout')
def logout():
  try:
    # Clear the session
    session.clear()
    log_audit("LOGOUT_SUCCESS", f"User logged out successfully")
    return redirect(url_for('login'))
  except Exception as e:
        logging.error(f"Error during logout: {e}")
        return render_template('/components/notification.html', notification_title='Error', 
                               notification_message='Error during logout process. Please try again later.',
                               notification_type='error',
                               icon='times',
                               href='/')

# ---------------------------------------------------------------

# 9. ROUTE TO ASSIGN MANAGER TO AN EMPLOYEE
@app.route('/assign_manager', methods=['POST'])
def assign_manager():
    try:
        # Get form data
        employee_id = request.form['employee_id']
        manager_id = request.form['manager_id']
        log_audit("ASSIGN_MANAGER_ATTEMPT", f"Assigning manager {manager_id} to employee {employee_id}")

        # Create a session to interact with the database
        db_session = Session()

        # Fetch the employee and manager from the database
        employee = db_session.query(User).filter_by(id=employee_id).first()
        manager = db_session.query(User).filter_by(id=manager_id, role='manager').first()

        if employee and manager:
            # Assign the manager ID to the employee
            employee.manager_id = manager.id

            # Commit the transaction and close the session
            db_session.commit()
            db_session.close()
            log_audit("ASSIGN_MANAGER_SUCCESS", f"Manager {manager_id} assigned to employee {employee_id} successfully")

            return render_template('/components/notification.html', notification_title='Success', 
                                notification_message='Employee-Manager assigned successfully.',
                                notification_type='success',
                                icon='check',
                                href='/admin/dashboard')
        else:
            db_session.close()
            log_audit("ASSIGN_MANAGER_FAIL", "Employee or Manager not found, or the manager ID provided is not a manager")
            # Render failure notification template
            return render_template('/components/notification.html', notification_title='Error', 
                                notification_message='Employee or Manager not found, or the manager ID provided is not a manager. Please try again',
                                notification_type='error',
                                icon='times',
                                href='/admin/dashboard')
    except Exception as e:
        logging.error(f"Error during manager assignment: {e}")
        return render_template('/components/notification.html', notification_title='Error', 
                               notification_message='Error during manager assignment. Please try again later.',
                               notification_type='error',
                               icon='times',
                               href='/admin/dashboard')  
# ---------------------------------------------------------------

# 10. ROUTE TO MAKE AN EMPLOYEE AS MANAGER
@app.route('/make_manager', methods=['POST'])
def make_manager_form():
    try:
        employee_id = request.form['employee_id']
        log_audit("MAKE_MANAGER_ATTEMPT", f"Attempting to make employee {employee_id} a manager")

        db_session = Session()
        employee = db_session.query(User).filter_by(id=employee_id).first()
        if employee:
            # Check if the employee is already a manager
            if employee.role == "manager":
                db_session.close()
                log_audit("MAKE_MANAGER_FAIL", f"Employee {employee_id} is already a manager")

                # Return an error response indicating the employee is already a manager
                return render_template('/components/notification.html', notification_title='Error', 
                                notification_message='Employee Already a Manager',
                                notification_type='error',
                                icon='times',
                                href='/admin/dashboard')

            employee.role = "manager"
            db_session.commit()
            db_session.close()
            # Render success notification template

            log_audit("MAKE_MANAGER_SUCCESS", f"Employee {employee_id} assigned as manager successfully")
            return render_template('/components/notification.html', notification_title='Success', 
                                notification_message='Manager assigned successfully.',
                                notification_type='success',
                                icon='check',
                                href='/admin/dashboard')
        else:
            db_session.close()
            # Render failure notification template
            log_audit("MAKE_MANAGER_FAIL", f"Employee {employee_id} not found")
            return render_template('/components/notification.html', notification_title='Error', 
                                notification_message='Employee not found. Please try again.',
                                notification_type='error',
                                icon='times',
                                href='/admin/dashboard')
    except Exception as e:
        logging.error(f"Error during making employee a manager: {e}")
        return render_template('/components/notification.html', notification_title='Error', 
                               notification_message='Error during making employee a manager. Please try again later.',
                               notification_type='error',
                               icon='times',
                               href='/admin/dashboard')
 # ---------------------------------------------------------------

# 11. ROUTE TO DELETE AN EMPLOYEE
@app.route('/delete_employee',methods=['POST'])
def delete_employee():
    try:
        employee_id=request.form['employee_id']
        log_audit("DELETE_EMPLOYEE_ATTEMPT", f"Attempting to delete employee {employee_id}")

        if employee_id:
            result=delete_user(employee_id)
            if result:
                log_audit("DELETE_EMPLOYEE_SUCCESS", f"Employee {employee_id} deleted successfully")
                return render_template('/components/notification.html', notification_title='Success', 
                                    notification_message='Employee deleted successfully.',
                                    notification_type='success',
                                    icon='check',
                                    href='/admin/dashboard')
            else:
                log_audit("DELETE_EMPLOYEE_FAIL", f"Employee {employee_id} not found")
                return render_template('/components/notification.html', notification_title='Error', 
                                    notification_message='Employee not found. Please try again.',
                                    notification_type='error',
                                    icon='times',
                                    href='/admin/dashboard')
    except Exception as e:
        logging.error(f"Error during employee deletion: {e}")
        return render_template('/components/notification.html', notification_title='Error', 
                               notification_message='Error during employee deletion. Please try again later.',
                               notification_type='error',
                               icon='times',
                               href='/admin/dashboard')
# ---------------------------------------------------------------
 
# 12.ROUTE TO ADD DEPARTMENT 
@app.route('/add_department',methods=['GET','POST'])
def add_department():
    try:
        dept_name=request.form['dept_name']
        city=request.form['city']
        log_audit("ADD_DEPARTMENT_ATTEMPT", f"Attempting to add department: {dept_name} in city: {city}")

        result=add_departments(dept_name,city)
        if result:
            log_audit("ADD_DEPARTMENT_SUCCESS", f"Department added successfully: {dept_name}")
            return render_template('/components/notification.html', notification_title='Success', 
                                notification_message='department added successfully.',
                                notification_type='success',
                                icon='check',
                                href='/admin/dashboard')
        else:
            log_audit("ADD_DEPARTMENT_FAIL", f"Error in adding Department: {dept_name}")
            return render_template('/components/notification.html', notification_title='Error', 
                                notification_message='Error in adding Department',
                                notification_type='error',
                                icon='times',
                                href='/admin/dashboard')
    except Exception as e:
        logging.error(f"Error during department addition: {e}")
        return render_template('/components/notification.html', notification_title='Error', 
                               notification_message='Error during department addition. Please try again later.',
                               notification_type='error',
                               icon='times',
                               href='/admin/dashboard')
# ---------------------------------------------------------------

# 13. ROUTE TO DELETE A DEPARTEMENT
@app.route('/delete_department',methods=['POST'])
def delete_department():
    try:
        dept_id=request.form['dept_id']
        if dept_id:
            result=delete_departments(dept_id)
            if result:
                log_audit("DELETE_DEPARTMENT_SUCCESS", f"Department with ID {dept_id} deleted successfully")
                return render_template('/components/notification.html', notification_title='Success', 
                                    notification_message='department deleted successfully.',
                                    notification_type='success',
                                    icon='check',
                                    href='/admin/dashboard')
            else:
                log_audit("DELETE_DEPARTMENT_FAIL", f"Department with ID {dept_id} not found")
                return render_template('/components/notification.html', notification_title='Error', 
                                    notification_message='Department not found',
                                    notification_type='error',
                                    icon='times',
                                    href='/admin/dashboard')
        else:
                log_audit("DELETE_DEPARTMENT_ERROR", "Error in deleting Department: No department ID provided")
                return render_template('/components/notification.html', notification_title='Error', 
                                    notification_message='Error in deleting Department',
                                    notification_type='error',
                                    icon='times',
                                    href='/admin/dashboard')
    except Exception as e:
        logging.error(f"Error during department deletion: {e}")
        return render_template('/components/notification.html', notification_title='Error', 
                               notification_message='Error during department deletion. Please try again later.',
                               notification_type='error',
                               icon='times',
                               href='/admin/dashboard')

  # ---------------------------------------------------------------

#   14. ROUTE TO SUBMIT THE REIMBURSEMENT
@app.route('/submit_reimbursement',methods=['POST'])
def submit_reimbursement():
    try:
        print(request.form)
        requestCategory = request.form['requestCategory']
        expenseType = request.form['expenseType']
        otherExpenseType = request.form['otherExpenseType']
        amount = request.form['amount']
        date = request.form['date']
        receipt = request.files['receipt'].read()  # Read the uploaded file as binary data'
        image_size = len(receipt)
        print("Image size in bytes:", image_size)
    
        user_id = session['user_id']
        # print(f'receipt is {receipt}' )
        result=add_reimbursement(user_id,requestCategory, expenseType, otherExpenseType, amount, date, receipt)
        role=request.form['userRoleforSubmit']
        if result:
            if role=="Employee":
                log_audit("SUBMIT_REIMBURSEMENT_SUCCESS", "Reimbursement requested successfully by an employee")
                return render_template('/components/notification.html', notification_title='Success', 
                                    notification_message='reimbursement requested successfully.',
                                    notification_type='success',
                                    icon='check',
                                    href='/employee/dashboard')
            else:
                log_audit("SUBMIT_REIMBURSEMENT_SUCCESS", "Reimbursement requested successfully by a manager")
                return render_template('/components/notification.html', notification_title='Success', 
                                notification_message='reimbursement requested successfully',
                                notification_type='success',
                                icon='check',
                                href='/manager/dashboard')
        else:
            log_audit("SUBMIT_REIMBURSEMENT_ERROR", "Error occurred while submitting reimbursement request")
            return render_template('/components/notification.html', notification_title='Error', 
                                notification_message='reimbursement request not sent',
                                notification_type='error',
                                icon='times',
                                href='/')
        
    except Exception as e:
        logging.error(f"Error submitting reimbursement request: {e}")
        return render_template('/components/notification.html', notification_title='Error', 
                               notification_message='Error submitting reimbursement request. Please try again later.',
                               notification_type='error',
                               icon='times',
                               href='/')
# ---------------------------------------------------------------

def is_authorized_manager(session, manager_id, request_id):
    # Query the reimbursement request from the database
    reimbursement = session.query(Reimbursement).filter_by(id=request_id).first()

    # Check if the reimbursement exists and if the manager_id matches
    if reimbursement and reimbursement.user.manager_id == manager_id:
        return True
    else:
        return False
    


# 15. ROUTE TO APPROVE REIMBURSEMENT
@app.route('/approve_reimbursement',methods=['POST'])
def approve_reimbursement():
    try:
        if 'user_id' in session:
            user_id = session['user_id']
        request_id=request.form['request_id']
        print(f"request id is {request_id} ","\n")
        comment=request.form['comment']
        role=request.form["userRole"]
        db_session=Session()
        if role == "manager":
            # Check if the manager is authorized to approve the request
            if is_authorized_manager(db_session, user_id, request_id):
                reimbursement = db_session.query(Reimbursement).filter_by(id=request_id).first()
                if reimbursement:
                    reimbursement.status = 'approved'
                    reimbursement.manager_comment = comment
                    db_session.commit()
                    db_session.close()

                    log_audit("APPROVE_REIMBURSEMENT", f"Reimbursement {request_id} approved by manager {user_id}")
                    return render_template('/components/notification.html', notification_title='Success', 
                                            notification_message='Reimbursement approved successfully.',
                                            notification_type='success',
                                            icon='check',
                                            href='/manager/dashboard')
                else:
                    db_session.close()
                    log_audit("APPROVE_REIMBURSEMENT_ERROR", f"Reimbursement {request_id} not found")
                    return render_template('/components/notification.html', notification_title='Error', 
                                            notification_message='Error in Reimbursement approvement',
                                            notification_type='error',
                                            icon='times',
                                            href='/manager/dashboard')
            else:
                db_session.close()
                log_audit("APPROVE_REIMBURSEMENT_UNAUTHORIZED", f"Unauthorized attempt to approve reimbursement {request_id} by manager {user_id}")
                return render_template('/components/notification.html', notification_title='Error', 
                                        notification_message='You are not authorized to approve this request',
                                        notification_type='error',
                                        icon='times',
                                        href='/manager/dashboard')
        elif role=="admin":
                reimbursement=db_session.query(Reimbursement).filter_by(id=request_id).first()
                if reimbursement:
                    reimbursement.status='approved'
                    reimbursement.manager_comment=comment
                    db_session.commit()
                    db_session.close()
                    log_audit("APPROVE_REIMBURSEMENT", f"Reimbursement {request_id} approved by admin {user_id}")
                    return render_template('/components/notification.html', notification_title='Success', 
                                        notification_message='Reimbursement Approved successfully.',
                                        notification_type='success',
                                        icon='check',
                                        href='/admin/dashboard')
                else:
                    log_audit("APPROVE_REIMBURSEMENT_ERROR", f"Reimbursement {request_id} not found")
                    return render_template('/components/notification.html', notification_title='Error', 
                                        notification_message='Error in Reimbursement approvement',
                                        notification_type='error',
                                        icon='times',
                                        href='/admin/dashboard')
                
    except Exception as e:
        logging.error(f"Error approving reimbursement: {e}")
        return render_template('/components/notification.html', notification_title='Error', 
                               notification_message='Error approving reimbursement. Please try again later.',
                               notification_type='error',
                               icon='times',
                               href='/')

# ---------------------------------------------------------------

# 16. ROUTE TO REJECT REIMBURSEMENT
@app.route('/reject_reimbursement',methods=['POST'])
def reject_reimbursement():
    try:
        if 'user_id' in session:
            user_id = session['user_id']
        request_id=request.form['request_id']
        comment=request.form['comment']
        role=request.form["userRole"]
        db_session=Session()
        if role=="manager":
            # Check if the manager is authorized to reject the request
            if is_authorized_manager(db_session, user_id, request_id):
                reimbursement=db_session.query(Reimbursement).filter_by(id=request_id).first()
                if reimbursement:
                    reimbursement.status='rejected'
                    reimbursement.manager_comment=comment
                    db_session.commit()
                    db_session.close()

                    log_audit("REJECT_REIMBURSEMENT", f"Reimbursement {request_id} rejected by manager {user_id}")
                    return render_template('/components/notification.html', notification_title='Success', 
                                        notification_message='Reimbursement rejected successfully.',
                                        notification_type='success',
                                        icon='check',
                                        href='/manager/dashboard')
                else:
                    db_session.close()
                    log_audit("REJECT_REIMBURSEMENT_ERROR", f"Reimbursement {request_id} not found")
                    return render_template('/components/notification.html', notification_title='Error', 
                                        notification_message='Error in Reimbursement Rejection',
                                        notification_type='error',
                                        icon='times',
                                        href='/manager/dashboard')
            else:
                db_session.close()
                log_audit("REJECT_REIMBURSEMENT_UNAUTHORIZED", f"Unauthorized attempt to reject reimbursement {request_id} by manager {user_id}")
                return render_template('/components/notification.html', notification_title='Error', 
                                        notification_message='You are not authorized to approve this request',
                                        notification_type='error',
                                        icon='times',
                                        href='/manager/dashboard')
        elif role=="admin":
            reimbursement=db_session.query(Reimbursement).filter_by(id=request_id).first()
            if reimbursement:
                reimbursement.status='rejected'
                reimbursement.manager_comment=comment
                db_session.commit()
                db_session.close()

                log_audit("REJECT_REIMBURSEMENT", f"Reimbursement {request_id} rejected by admin {user_id}")
                return render_template('/components/notification.html', notification_title='Success', 
                                    notification_message='Reimbursement rejected successfully.',
                                    notification_type='success',
                                    icon='check',
                                    href='/admin/dashboard')
            else:
                db_session.close()
                log_audit("REJECT_REIMBURSEMENT_ERROR", f"Reimbursement {request_id} not found")
                return render_template('/components/notification.html', notification_title='Error', 
                                    notification_message='Error in Reimbursement Rejection',
                                    notification_type='error',
                                    icon='times',
                                    href='/admin/dashboard')
    except Exception as e:
        logging.error(f"Error rejecting reimbursement: {e}")
        return render_template('/components/notification.html', notification_title='Error', 
                               notification_message='Error rejecting reimbursement. Please try again later.',
                               notification_type='error',
                               icon='times',
                               href='/')    
# --------------------------------------------------------------
# 17. ROUTE TO UPDATE REIMBURSEMENT
@app.route('/update_reimbursement', methods=['POST','GET'])
def update_reimbursement():
    print("in update reimburesement","\n")
    try:
        # Parse request data
        print("in try")
        reimbursement_id = request.form['updateRequestId'] 
        print(reimbursement_id)
        requestCategory = request.form['updateRequestCategory']
        expenseType = request.form['updateExpenseType']
        otherExpenseType = request.form['updateOtherExpenseType']
        amount = request.form['updateAmount']
        date = request.form['updateDate']
        receipt = request.files['updateReceipt'].read()  # Read the uploaded file as binary data'
        # image_size = len(receipt)
        print(f"result is :","\n")
        print(f"result is :","\n")  
        # Call function to update reimbursement
        result = update_user_reimbursement(reimbursement_id, requestCategory, expenseType, otherExpenseType, amount, date, receipt)
        print(f"result is {result} :","\n")
        print(f"result is {result}:","\n") 
        # Handle result and return response
        if result:
            log_audit("UPDATE_REIMBURSEMENT_SUCCESS", "Reimbursement updated successfully")
            return render_template('/components/notification.html', notification_title='Success', 
                                   notification_message='Reimbursement updated successfully.',
                                   notification_type='success',
                                   icon='check',
                                   href='/employee/dashboard')  
        else:
            log_audit("UPDATE_REIMBURSEMENT_ERROR", "Error occurred while updating reimbursement")
            return render_template('/components/notification.html', notification_title='Error', 
                                   notification_message='Error updating reimbursement.',
                                   notification_type='error',
                                   icon='times',
                                   href='/employee/dashboard') 
        
    except Exception as e:
        logging.error(f"Error updating reimbursement: {e}")
        return render_template('/components/notification.html', notification_title='Error', 
                               notification_message='Error updating reimbursement. Please try again later.',
                               notification_type='error',
                               icon='times',
                               href='/employee/dashboard') 

#  Run the Flask app
if __name__ == '__main__':
    # init_db()
    app.run(debug=True)
