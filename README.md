University Management System
This is a basic University Management System implemented using Flask and MySQL. The system allows users to register, log in, enroll in courses, and view grades. MySQL is used to store user accounts, courses, sections, enrollment information, and grades.

Getting Started
Prerequisites
Python 3.x
Flask
MySQL
mysql-connector-python
Installation
Install Python 3.x: Download Python

Install Flask:

bash
Copy code
pip install flask
Install mysql-connector-python:

bash
Copy code
pip install mysql-connector-python
Setting up the Database
Create a MySQL database named uni_management3.

Update the MySQL connection details in app.py and createdatabases.py:

python
Copy code
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'uni_management3'
Run createdatabases.py to create the necessary tables:

bash
Copy code
python createdatabases.py
Running the Application
Run the Flask application:

bash
Copy code
python app.py
The application will be accessible at http://localhost:5000/.

Usage
Visit http://localhost:5000/ to access the main page.
Register a new account or log in if you already have one.
Explore the features of the University Management System.
Structure
app.py: Main Flask application with user registration, login, and basic routes.
init_db.py: Script to initialize the MySQL database and create tables.
templates/: HTML templates for the application.
