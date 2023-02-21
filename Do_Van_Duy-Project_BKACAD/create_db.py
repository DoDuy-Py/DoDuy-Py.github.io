import mysql.connector

# create connection to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "employees_manager"
)
mycursor = mydb.cursor()

sql_string_1 = """CREATE TABLE IF NOT EXISTS accounts (
                id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                user_name VARCHAR(20),
                password VARCHAR(20),
                email VARCHAR(150) UNIQUE,
                phone VARCHAR(10) UNIQUE,
                gender VARCHAR(10)
                )
                """

sql_string_2 = """CREATE TABLE IF NOT EXISTS departments (
                id_dep INT NOT NULL PRIMARY KEY,
                name_dep VARCHAR(20) NOT NULL
                )
                """

sql_string_3 = """CREATE TABLE IF NOT EXISTS employees (
                id_emp INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                id_dep INT NOT NULL,
                name_emp VARCHAR(20) NOT NULL,
                name_dep VARCHAR(20) NOT NULL,
                email VARCHAR(150) NOT NULL UNIQUE,
                phone VARCHAR(10) NOT NULL UNIQUE,
                gender VARCHAR(10) NOT NULL,
                age INT NOT NULL,
                position VARCHAR(20) NOT NULL,
                salary INT(150) NOT NULL,
                address VARCHAR(150) NOT NULL
                -- FOREIGN KEY (id_dep) REFERENCES departments(id_dep)
                )
                """
sql_string_4 = """CREATE TABLE IF NOT EXISTS contracts (
                id_con INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                id_emp INT NOT NULL,
                name_con VARCHAR(20) NOT NULL,
                name_emp VARCHAR(20) NOT NULL,
                date_create DATE NOT NULL,
                end_date DATE NOT NULL
                -- FOREIGN KEY (id_con) REFERENCES employees(id_emp)
                )
                """
sql_string_5 = """CREATE TABLE IF NOT EXISTS candidate (
                id_can INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                name_can VARCHAR(150) NOT NULL,
                position VARCHAR(20) NOT NULL,
                email VARCHAR(20) NOT NULL,
                phone VARCHAR(10) NOT NULL,
                gender VARCHAR(10) NOT NULL,
                age INT(20) NOT NULL
                )
                """

mycursor.execute(sql_string_1)
mycursor.execute(sql_string_2)
mycursor.execute(sql_string_3)
mycursor.execute(sql_string_4)
mycursor.execute(sql_string_5)
# disconnect from MySQL
mydb.close()
print("Tao bang thanh cong!")
# cursor.execute("INSERT INTO account(id, user_name, password, email, phone, gender) VALUES(1, 'admin', '1234aA@', 'admin@gmail.com', '0987654321', 'male');")
# cursor.execute(sql, val)
# print("ADD thanh cong!")