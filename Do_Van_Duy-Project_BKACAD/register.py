from tkinter import *
from tkinter import messagebox, ttk
import os
import MySQLdb

def login_():
	window_register.destroy()
	import login

def check_info_dangky(info_name, info_pass, info_repass, info_email, info_phone, info_check):
	db = MySQLdb.connect(host="localhost", user="root", passwd="", db="employees_manager")
	cursor = db.cursor()
	#Truy van du lieu
	cursor.execute("SELECT user_name, email FROM accounts")
	list_name = []
	list_mail = []
	data = cursor.fetchall()
	for x, y in data:
		list_name.append(str(x))
		list_mail.append(str(y))
	db.close()
	error = ""
	check_true = 0
	if len(info_name) > 3 and ' ' not in info_name and info_name not in list_name:
		check_true += 1
	else:
		error = "User Name must be more than three characters or\nAccount already exists!"
		messagebox.showerror("Error", error)
		return

	if len(info_pass) > 4 and ' ' not in info_name:
		check_true += 1
	else:
		error = "Password must be more than five characters!"
		messagebox.showerror("Error", error)
		return

	if info_repass == info_pass:
		check_true += 1
	else:
		error = "Two passwords are not the same!"
		messagebox.showerror("Error", error)
		return

	if '@' in info_email and info_email not in list_mail:
		check_true += 1
	else:
		error = "Wrong email or\nEmail already exists!"
		messagebox.showerror("Error", error)
		return

	if len(info_phone) == 10 and info_phone.isdigit():
		check_true += 1
	else:
		error = "Phone must be ten number!"
		messagebox.showerror("Error", error)
		return
	
	if info_check == 1:
		check_true += 1
	else:
		error = "You do not agree to the terms?"
		messagebox.showerror("Error", error)
		return

	if check_true == 6:
		return True

def save_db_acc(info_name, info_pass, info_email, info_phone, info_gender, cursor, db):
	# Tao cau truy van
	sql = "INSERT INTO accounts(user_name, password, email, phone, gender) VALUES (%s,%s,%s,%s,%s)"
	# Them cac gia tri tuong ung vao cot
	val = (info_name, info_pass, info_email, info_phone, info_gender)
	#Them du lieu vao trong bang account
	cursor.execute(sql, val)
	db.commit()

def register_():
	info_name = t_user.get(1.0, END).strip("\n")
	info_pass = t_pass.get().strip("\n")
	info_repass = t_repass.get().strip("\n")
	info_email = t_email.get(1.0,END).strip("\n")
	info_phone = t_phone.get(1.0,END).strip("\n")
	info_gender = var_gender.get()
	info_check = check_button_dk.get()
	account = check_info_dangky(info_name, info_pass, info_repass, info_email, info_phone, info_check)
	if account == True:
		db = MySQLdb.connect(host="localhost", user="root", passwd="", db="employees_manager")
		cursor = db.cursor()
		save_db_acc(info_name, info_pass, info_email, info_phone, info_gender, cursor,db)
		db.close()
		messagebox.showinfo("Notify","Register Successfuly")
		window_register.destroy()
		import login

window_register = Tk()
window_register.geometry("390x470")
#Lấy đường dẫn tuyệt đối đến file hiện tại và thêm "images/icon.ico" vào đường dẫn
abs_icon_path = os.path.abspath("images/icon.ico")
window_register.iconbitmap(abs_icon_path)
window_register.title('Dang ky')
window_register.resizable(0,0)
# print(abs_icon_path, type(abs_icon_path))

var_gender = StringVar()
check_button_dk = IntVar()
#show = '*' để text hiển thị thành *

user_name = Label(window_register, text = "User Name")
user_name.place(x = 30, y = 50)
password = Label(window_register, text = "Password")
password.place(x = 30, y = 100)
repassword = Label(window_register, text = "Re-Enter Password")
repassword.place(x = 30, y = 150)
email = Label(window_register, text = "Email").place(x = 30, y = 200)
phone = Label(window_register, text = "Number Phone").place(x = 30, y = 250)
gender = Label(window_register, text = "Gender").place(x=30, y=300)

t_user = Text(window_register, width = 25, height = 1)
t_user.place(x = 150, y = 50)
t_pass = Entry(window_register, show = '*', width = 33)
t_pass.place(x = 150, y = 100)
t_repass = Entry(window_register, show = '*', width = 33)
t_repass.place(x= 150, y = 150)
t_email = Text(window_register, width = 25, height = 1)
t_email.place(x = 150, y = 200)
t_phone = Text(window_register, width = 25, height = 1)
t_phone.place(x = 150, y = 250)

values_gender = {'Male':'male',
		'Female':'female',
		'Others': 'others'}
x = 120
for text, val in values_gender.items():
	Radiobutton(window_register, text=text, value = val, variable=var_gender).place(x=x, y=300)
	x += 80
var_gender.set('male')

button_dk = Checkbutton(window_register, text = "You agree to our terms?", 
                      	variable = check_button_dk,
                      	onvalue = 1,
                      	offvalue = 0,
                      	height = 1,
                    	width = 20)
button_dk.place(x = 100, y = 350)

btn_register = Button(window_register, width = 7, height = 1, text = "Submit", command = register_)
btn_register.place(x = 240, y = 400)
btn_login = Button(window_register, width = 7, height = 1, text = "Login", command = login_)
btn_login.place(x = 320, y = 400)

window_register.mainloop()