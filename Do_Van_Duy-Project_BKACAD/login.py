# - Đăng nhập với tài khoản "admin" mật khẩu "123456aA@" để vào giao diện ADMIN hoặc chạy file display.py
# - Các tài khoản khác sẽ vào giao diện USER hoặc chạy file display_user.py

from tkinter import *
from tkinter import ttk, messagebox
import os
import MySQLdb

def register():
	try:
		ws.destroy()
		import register
	except Exception as e:
		print(e)

def check_info_acc(info_name, info_pass):
	conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "employees_manager")
	cursor = conn.cursor()
	cursor.execute("SELECT user_name, password FROM accounts")
	info_acc = cursor.fetchall()
	conn.close()
	if (info_name, info_pass) in info_acc:
		return True
	else:
		return False

def login():
	info_name = text_name.get(1.0, END).strip("\n")
	info_pass = text_pass.get().strip("\n")
	check = check_info_acc(info_name, info_pass)
	if check == True:
		messagebox.showinfo("Notify","Login Successfuly")
		ws.destroy()
		if info_name == "admin":
			from display import Employee
			obj = Employee()
			obj.display_admin()
		else:
			from display_user import EmployeeUser
			user = EmployeeUser()
			user.display_user()
	else:
		messagebox.showerror("Error","Incorrect account or password")

ws = Tk()
ws.title('Login')
#Lấy đường dẫn tuyệt đối đến file hiện tại và thêm "images/icon.ico" vào đường dẫn
abs_icon_path = os.path.abspath("images/icon.ico")
ws.iconbitmap(abs_icon_path)
ws.geometry('330x180')
ws.resizable(0, 0) # Khong cho zoom tab

ws.columnconfigure(1, weight=1)
ws.columnconfigure(2, weight=2)

user_name = Label(ws, text="User Name").grid(column=1, row = 1)
user_pass = Label(ws, text="Password").grid(column=1, row = 2)

text_name = Text(ws, width = 20, height=1)
text_name.grid(column=2,row=1, padx = 5, pady = 10)
text_pass = Entry(ws, show = '*', width = 27)
text_pass.grid(column=2,row=2, padx = 5, pady = 10)

btn_login = Button(ws, text="Login", command = login)
btn_login.grid(column=2, row=3, pady = 20, sticky=W) # sticky bám dính theo hướng đông tây nam bắc
btn_f_pass = Button(ws, text="Forgot password")
btn_f_pass.place(x = 150, y = 100)
btn_register = Button(ws, text="Register", command = register)
btn_register.place(x = 260, y = 100)

ws.mainloop()