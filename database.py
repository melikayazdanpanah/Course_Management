import mysql.connector

# Connect to MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="melika1380"
)

# Create a cursor object to execute SQL queries
with conn.cursor() as cursor:
    # Create the 'uni_management' database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS uni_management3 DEFAULT CHARACTER SET utf8;")

# Connect to the new database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="melika1380",
    database="uni_management3"
)

# Create a cursor object to execute SQL queries
with conn.cursor() as cursor:
    # Create 'accounts' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            id INT(11) NOT NULL AUTO_INCREMENT,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL, 
            PRIMARY KEY (id)
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
    ''')

     # Create 'courses' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            course_id INT(11) NOT NULL AUTO_INCREMENT,
            course_name VARCHAR(255) NOT NULL,
            instructor_id INT(11) NOT NULL,
            PRIMARY KEY (course_id),
            FOREIGN KEY (instructor_id) REFERENCES accounts(id)
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
    ''')

    # Create 'sections' table related to 'courses'
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sections (
            section_id INT(11) NOT NULL AUTO_INCREMENT,
            section_name VARCHAR(255) NOT NULL,
            course_id INT(11) NOT NULL,
            PRIMARY KEY (section_id),
            FOREIGN KEY (course_id) REFERENCES courses(course_id)
        ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
    ''')

    # Create 'enrollment' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS enrollment (
        enrollment_id INT(11) NOT NULL AUTO_INCREMENT,
        student_id INT(11) NOT NULL,
        section_id INT(11) NOT NULL,
        PRIMARY KEY (enrollment_id),
        FOREIGN KEY (student_id) REFERENCES accounts(id),
        FOREIGN KEY (section_id) REFERENCES sections(section_id)
    ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
''')

# Create 'grades' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades (
        grade_id INT(11) NOT NULL AUTO_INCREMENT,
        enrollment_id INT(11) NOT NULL,
        grade_value INT(11) NOT NULL,
        PRIMARY KEY (grade_id),
        FOREIGN KEY (enrollment_id) REFERENCES enrollment(enrollment_id)
    ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
''')

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database 'uni_management3' and table 'accounts' created successfully.")
