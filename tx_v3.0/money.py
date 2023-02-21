from tkinter import *
from tkinter import messagebox, ttk
import os
import MySQLdb


class Money():
	"""docstring for Money"""
	def __init__(self, user_name, so_tien):
		self.user_name = user_name
		self.so_tien = so_tien
		

	def nap_tien(self):
		so_du = self.show_sodu()
		conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "sicbo")
		cursor = conn.cursor()
		cursor.execute("UPDATE accounts SET so_du = %s" %(so_du[0][0]+self.so_tien))
		conn.commit()
		conn.close()

	def rut_tien(self):
		so_du = self.show_sodu()
		if so_du[0][0] - self.so_tien > 50000:
			conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "sicbo")
			cursor = conn.cursor()
			cursor.execute("UPDATE accounts SET so_du = %s" %(so_du[0][0]-self.so_tien))
			conn.commit()
			conn.close()
		else:
			messagebox.showerror("Erorr","Số tiền còn lại\nphải lớn hơn 50K")

	def show_sodu(self):
		conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "sicbo")
		cursor = conn.cursor()
		cursor.execute("SELECT so_du FROM accounts WHERE user_name=%s",[self.user_name])
		so_du = cursor.fetchall()
		conn.close()
		return so_du