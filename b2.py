import streamlit as st
import mysql.connector
from mysql.connector import Error


# MySQL Connection Setup
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='12345',
            database='sql_db'  # Replace with your database name
        )
        if connection.is_connected():
            return connection
    except Error as e:
        st.error(f"Error connecting to MySQL: {e}")
        return None


# Create Customer_Data table if it doesn't exist
def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Customer_Data (
                id INT AUTO_INCREMENT PRIMARY KEY,
                Name VARCHAR(255),
                Age INT,
                Profession VARCHAR(255),
                City VARCHAR(255)
            )
        """)
        connection.commit()
    except Error as e:
        st.error(f"Error creating table: {e}")
    finally:
        cursor.close()


# Insert customer data into the table
def insert_customer_data(connection, name, age, profession, city):
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO Customer_Data (Name, Age, Profession, City) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (name, age, profession, city))
        connection.commit()
        st.success('Customer Data inserted successfully!')
    except Error as e:
        st.error(f"Error inserting data: {e}")
    finally:
        cursor.close()

# Create Customer_Data table if it doesn't exist
def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Customer_Data (
                id INT AUTO_INCREMENT PRIMARY KEY,
                Name VARCHAR(255),
                Age INT,
                Profession VARCHAR(255),
                City VARCHAR(255)
            )
        """)
        connection.commit()
    except Error as e:
        st.error(f"Error creating table: {e}")
    finally:
        cursor.close()

# Insert customer data into the table
def insert_customer_data(connection, name, age, profession, city):
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO Customer_Data (Name, Age, Profession, City) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (name, age, profession, city))
        connection.commit()
        st.success('Customer Data inserted successfully!')
    except Error as e:
        st.error(f"Error inserting data: {e}")
    finally:
        cursor.close()


# Create Business_Customer_Data table if it doesn't exist
def create_business_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Business_Customer_Data (
                id INT AUTO_INCREMENT PRIMARY KEY,
                Name VARCHAR(255),
                Age INT,
                Industry VARCHAR(255),
                Date_of_Incorporation DATE,
                Annual_Turnover FLOAT,
                City VARCHAR(255)
            )
        """)
        connection.commit()
    except Error as e:
        st.error(f"Error creating table: {e}")
    finally:
        cursor.close()

# Insert business customer data into the table
def insert_business_customer_data(connection, name, age, industry, incorporation_date, turnover, city):
    try:
        cursor = connection.cursor()
        sql = """
        INSERT INTO Business_Customer_Data (Name, Age, Industry, Date_of_Incorporation, Annual_Turnover, City)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (name, age, industry, incorporation_date, turnover, city))
        connection.commit()
        st.success('Business Customer Data inserted successfully!')
    except Error as e:
        st.error(f"Error inserting data: {e}")
    finally:
        cursor.close()
# Main Streamlit App
st.title('GBMS Bank Mumbai, India')

# Sidebar options
option = st.sidebar.selectbox('Home', ('About us', 'Mission', 'Vision', 'Management', 'Awards', 'Contact', 'Social'))
option1 = st.sidebar.selectbox('Open an Account', ('Savings Account', 'Current Account'))
option2 = st.sidebar.selectbox('Bank with us', ('Personal Loan', 'Credit Card', 'Business Loan', 'Home Loan', 'Two Wheeler Loan', 'Car Loan'))
option3 = st.sidebar.selectbox('Trading with us', ('Demat Account', 'Securities Trading'))
option4 = st.sidebar.selectbox('Investor Relations', ('AGMs', 'Reports', 'Grievances'))
option5 = st.sidebar.selectbox('Support', ('Feedback', 'Customer Support'))

st.write("Welcome to GBMS Bank")

# Loan Calculator as earlier (skipped for brevity)
# ...

# If user selects 'Savings Account' from sidebar
if option1 == 'Savings Account':
    st.subheader('Open a Savings Account')

    # User inputs
    name = st.text_input('Enter your Name')
    age = st.number_input('Enter your Age', min_value=18, max_value=100)
    profession = st.text_input('Enter your Profession')
    city = st.text_input('Enter your City')

    # Button to submit form
    if st.button('Submit'):
        # Connect to MySQL
        connection = create_connection()
        if connection:
            # Create the table if it doesn't exist
            create_table(connection)

            # Insert user data into the table
            insert_customer_data(connection, name, age, profession, city)

            # Close the connection
            connection.close()
if option1 == 'Current Account':
    st.subheader('Open a Current Account')

    # User inputs for Business Customers
    name = st.text_input('Enter your Name')
    age = st.number_input('Enter your Age', min_value=18, max_value=100)
    industry = st.text_input('Enter your Industry')
    incorporation_date = st.date_input('Enter Date of Incorporation')
    turnover = st.number_input('Enter your Annual Turnover', min_value=0.0)
    city = st.text_input('Enter your City')

    # Button to submit form
    if st.button('Submit'):
        # Connect to MySQL
        connection = create_connection()
        if connection:
            # Create the Business_Customer_Data table if it doesn't exist
            create_business_table(connection)

            # Insert business customer data into the table
            insert_business_customer_data(connection, name, age, industry, incorporation_date, turnover, city)

            # Close the connection
            connection.close()


# Rest of your app code like loan calculator, etc.
