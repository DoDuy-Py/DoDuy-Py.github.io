import mysql.connector

# create connection to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "sicbo"
)

mycursor = mydb.cursor()

sql_string_1 = """CREATE TABLE IF NOT EXISTS accounts (
                id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                user_name VARCHAR(20) UNIQUE,
                password VARCHAR(20),
                email VARCHAR(150) UNIQUE,
                so_du INT(50)
                )
                """

mycursor.execute(sql_string_1)
# disconnect from MySQL
mydb.close()
print("Tao bang thanh cong!")