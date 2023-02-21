# - Đăng nhập với tài khoản "admin" mật khẩu "123456aA@" để vào giao diện ADMIN hoặc chạy file display.py
# - Các tài khoản khác sẽ vào giao diện USER hoặc chạy file display_user.py

from tkinter import *
from tkinter import messagebox, ttk
import os
import webbrowser
from PIL import ImageTk, Image

window = Tk()
window.title("Display Main")
window.geometry("900x600")
icon_path = os.path.abspath("images/bkacad.ico")
window.iconbitmap(icon_path)
window.resizable(0,0)

#back ground
bg_image = Image.open("images/python-logo-4k-i6.png")
render = ImageTk.PhotoImage(bg_image)
img = Label(window, image=render)
img.place(x=0, y=0)

text_first = Label(text="Hello Friend !\nPlease login to continue.", font=(30), fg="orange")
text_first.place(x= 370, y=290)

def _login():
	window.destroy()
	import login
def _register():
	window.destroy()
	import register

#Button Contact
def _facebook(self):
    link_fb = 'https://www.facebook.com/duy552.py'
    webbrowser.open_new_tab(link_fb)
def _messager(self):
    link_mess = 'https://www.facebook.com/messages/t/duy552.py'
    webbrowser.open_new_tab(link_mess)
def _instagram(self):
    link_ig = 'https://www.instagram.com/dovanduy552/'
    webbrowser.open_new_tab(link_ig)
def _twitter(self):
    link_tw = 'https://twitter.com/?lang=vi'
    webbrowser.open_new_tab(link_tw)
def _telegram(self):
    link_tele = 'https://web.telegram.org/z/'
    webbrowser.open_new_tab(link_tele)

frame = Frame(window, bd=4,bg="black", relief=RIDGE)
frame.place(x=480, y=530, width=400, height=60)

icon_fb = PhotoImage(file="images/fb.png")
icon_mes = PhotoImage(file="images/mess1.png")
icon_ig = PhotoImage(file="images/instagram.png")
icon_tw = PhotoImage(file="images/tw.png")
icon_tl = PhotoImage(file="images/telegram.png")

btn_fb = Button(frame, image=icon_fb, width=30, height=30,bd=4, command=_facebook)
btn_fb.place(x=15, y=7)
btn_mes = Button(frame, image=icon_mes, width=30, height=30,bd=4, command=_messager)
btn_mes.place(x=95, y=7)
btn_ig = Button(frame, image=icon_ig, width=30, height=30,bd=4, command=_instagram)
btn_ig.place(x=175, y=7)
btn_tw = Button(frame, image=icon_tw, width=30, height=30,bd=4, command=_twitter)
btn_tw.place(x=255, y=7)
btn_tle = Button(frame, image=icon_tl, width=30, height=30,bd=4, command=_telegram)
btn_tle.place(x=335, y=7)

btn_login = Button(window, width = 7, height = 1, text = "Login", command = _login)
btn_login.place(x = 750, y = 15)
btn_register = Button(window, width = 7, height = 1, text = "Register", command = _register)
btn_register.place(x = 820, y = 15)

window.mainloop()