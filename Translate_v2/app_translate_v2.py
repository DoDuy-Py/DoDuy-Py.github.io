from tkinter import *
from tkinter.ttk import Combobox
from tkinter import ttk
from PIL import Image, ImageTk
from googletrans import Translator
import googletrans

#Tao window
root = Tk()
root.title('Google Translate')
root.geometry('700x600')
root.iconbitmap('data/logo.ico')

image = Image.open('data/background.png')
render = ImageTk.PhotoImage(image)
img = Label(root, image=render)
img.place(x = 0, y = 0)

#Combobox
languages = ('english', 'vietnames', 'korean', 'chinese', 'japanese', 'russian', 'french')
dic_languages = {'english':'en', 'vietnames':'vi', 'korean':'ko', 'chinese':'zh-cn', 'japanese':'ja',
	'russian':'ru', 'french':'fr'}
var=StringVar()
var.set('english')
cbx=Combobox(root, values=languages, width = 30, textvariable = var)
cbx.place(x=250, y=65)
# from_lang = var.get()

var2=StringVar()
var2.set('vietnames') #Set giá trị mặc định cho combobox
cbx2=Combobox(root, values=languages, width = 30, textvariable = var2)
cbx2.place(x=250, y=335)
cbx2.current(1)
# to_lang = var2.get()

lang_option1 = Label(root, text = 'Languages: ',font=(('Times New Roman'), 13, 'bold'), fg = 'white', bd = 0, bg = '#031520')
lang_option1.place(x=150, y=65)
lang_option2 = Label(root, text = 'Languages: ',font=(('Times New Roman'), 13, 'bold'), fg = 'white', bd = 0, bg = '#031520')
lang_option2.place(x=150, y=335)

name = Label(root, text = 'Translator', fg = 'white', bd = 0, bg = '#031520')
name.config(font = ('Transformers Movie', 30))
name.pack(pady = 10)

box = Text(root, width = 25, height = 8, font = ('Times new roman', 15))
box.pack(pady = 20)

button_frame = Frame(root).pack(side="bottom")

def clear():
	box.delete(1.0,END)
	box1.delete(1.0,END)
def translate():
	from_lang = var.get() #Lấy giá trị mà combobox đang trỏ tới
	to_lang = var2.get()
	user_input = box.get(1.0,END)
	box1.delete(1.0,END)
	for check in user_input:
		if check.isalpha() or check.isalnum():
			t = Translator()
			a = t.translate(user_input, src = dic_languages[from_lang], dest = dic_languages[to_lang])
			text = a.text
			box1.insert(END,text)
			break

clear_button = ttk.Button(root, text="Clear Text", command = clear)
clear_button.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)
trans_button = Button(button_frame,width=15, text = 'TRANSLATE', font=(('Arial'), 10, 'bold'), fg = 'white', bg = 'black', command=translate)
trans_button.place(x = 290, y = 290)

box1 = Text(root, width = 25, height = 8, font = ('Times New Roman', 15))
box1.pack(pady = 70)

root.mainloop()