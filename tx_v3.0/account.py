#Form login logout

from tkinter import *
from tkinter import messagebox, ttk
import os
import MySQLdb

def _login():
	window_login = Tk()
	window_login.geometry("390x200")
	window_login.iconbitmap("data_server/images/icon.ico")
	window_login.resizable(0,0)
	window_login.config(background="#444444")
	window_login.title('Login')

	user_name = Label(window_login, text = "User Name", fg = "white", bg = "#444444")
	user_name.place(x = 30, y = 50)
	password = Label(window_login, text = "Password", fg = "white", bg = "#444444")
	password.place(x = 30, y = 100)

	t_user = Text(window_login, width = 25, height = 1)
	t_user.place(x = 150, y = 50)
	t_pass = Entry(window_login, show = '*', width = 33)
	t_pass.place(x = 150, y = 100)

	btn_login = Button(window_login, width = 7, height = 1, text = "Login", bd=5)
	btn_login.place(x = 300, y = 160)

	window_login.mainloop()

def check_login():
	info_name = t_user.get(1.0, END).strip("\n")
	info_pass = t_pass.get().strip("\n")
	conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "sicbo")
	cursor = conn.cursor()
	cursor.execute("SELECT user_name, password FROM accounts")
	info_acc = cursor.fetchall()
	conn.close()
	if (info_name, info_pass) in info_acc:
		return True
	else:
		return False

def _register():
	window_register = Tk()
	window_register.geometry("390x400")
	window_register.iconbitmap("data_server/images/icon.ico")
	window_register.resizable(0,0)
	window_register.config(background="#444444")
	window_register.title('Register')

	t_user = Text(window_register, width = 25, height = 1)
	t_user.place(x = 150, y = 50)
	t_pass = Entry(window_register, show = '*', width = 33)
	t_pass.place(x = 150, y = 100)
	t_repass = Entry(window_register, show = '*', width = 33)
	t_repass.place(x= 150, y = 150)
	t_email = Text(window_register, width = 25, height = 1)
	t_email.place(x = 150, y = 200)
	check_button_dk = IntVar()

	user_name = Label(window_register, text = "User Name", fg = "white", bg = "#444444")
	user_name.place(x = 30, y = 50)
	password = Label(window_register, text = "Password", fg = "white", bg = "#444444")
	password.place(x = 30, y = 100)
	repassword = Label(window_register, text = "Re-Enter Password", fg = "white", bg = "#444444")
	repassword.place(x = 30, y = 150)
	email = Label(window_register, text = "Email", fg = "white", bg = "#444444").place(x = 30, y = 200)

	button_dk = Checkbutton(window_register, text = "You agree to our terms?",
                  	variable = check_button_dk,
                  	onvalue = 1,
                  	offvalue = 0,
                  	height = 1,
                	width = 20)
	button_dk.place(x = 100, y = 250)

	btn_register = Button(window_register, width = 7, height = 1, text = "Submit", bd=5, command=obj.register)
	btn_register.place(x = 240, y = 320)
	btn_login = Button(window_register, width = 7, height = 1, text = "Login", bd=5)
	btn_login.place(x = 320, y = 320)

	window_register.mainloop()

def check_form(info_name, info_pass, info_repass, info_email, info_phone, info_check):
	error = ""
	check_true = 0
	if len(info_name) > 3 and ' ' not in info_name:
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

	if '@' in info_email:
		check_true += 1
	else:
		error = "Wrong email or\nEmail already exists!"
		messagebox.showerror("Error", error)
		return
	
	if info_check == 1:
		check_true += 1
	else:
		error = "You do not agree to the terms?"
		messagebox.showerror("Error", error)
		return

	if check_true == 5:
		return True

class Account():
	"""docstring for Account"""
	def __init__(self, user_name, password, email):
		self.window_register = Tk()
		self.user_name = user_name
		self.password = password
		self.email = email
		# self.so_du = 0
	def _login(self):
		info_name = self.t_user.get(1.0, END).strip("\n")
		info_pass = self.t_pass.get().strip("\n")
		check = self.check_login(info_name, info_pass)
		if check:
			messagebox.showinfo("Notify","Login Successfuly")
			self.window_register.destroy()
			self.user_name = info_name
			return
		else:
			messagebox.showerror("Error","Incorrect account or password")

	def login(self):
		pass


	def logout(self):
		pass

	def register(self):
		account = check_form()
		if account:
			try:
				db = MySQLdb.connect(host="localhost", user="root", passwd="", db="sicbo")
				cursor = db.cursor()
				sql = "INSERT INTO accounts(user_name, password, email, so_du) VALUES (%s,%s,%s,%s)"
				# Them cac gia tri tuong ung vao cot
				val = (info_name, info_pass, info_email, 0)
				#Them du lieu vao trong bang account
				cursor.execute(sql, val)
				db.commit()
				db.close()
				messagebox.showinfo("Notify","Register Successfuly")
				self.window_register.destroy()
			except Exception as e:
				messagebox.showerror("Erorr", e)
class Money(Account):
	"""docstring for Money"""
	def nap_tien(self):
		pass
	
	def rut_tien(self):
		pass

	def show_sodu(self):
		pass

if __name__ == '__main__':
	obj = Account('a', 'b', 'c')
	obj.register()
	# obj.login()

	# obj_2 = Money('a', 'b', 'c')
	_login()