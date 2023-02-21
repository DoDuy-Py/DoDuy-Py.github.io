from tkinter import* 
from tkinter import messagebox, ttk
import random
from PIL import Image, ImageTk

root = Tk()
root.title('Permutation Cipher - Group 2')
root.iconbitmap('icon.ico')
root.geometry('900x600')

#back ground
image = Image.open('humg.png')
render = ImageTk.PhotoImage(image)
img = Label(root, image=render)
img.place(x=0, y=0)

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÁÀÃẠẢĂẮẰẴẲẶÂẤẦẪẨẬĐÉÈẼẺẸÊẾỀỄỂỆÍÌĨỈỊÓÒÕỎỌÔỐỒỖỔỘƠỚỜỠỞỢÚÙŨỦỤƯỨỪỮỬỰÝỲỸỶỴ'
def make_key():
	try:
		khoa = {}
		k = list(LETTERS)
		random.shuffle(k)
		key =''.join(k)
		key = list(key)
		for i in range(len(LETTERS)):
			khoa[LETTERS[i]] = key[i]
		list_kytu = ['`','!','@','#','$','%','^','&','*','(',')','-','_','=','+','~','1','2','3','4',
		'5','6','7','8','9','0',',',"'",'.','<','>',':',';','"','{','}','[',']',' ','?','/','|',"\n"]
		for i in list_kytu:
			khoa[i] = i
		key_txt = ''
		for x in khoa.values():
			key_txt += x
		with open('key.txt', 'w', encoding='utf-8') as file:
			file.write(key_txt)
		res = messagebox.showinfo("Thông báo","Tạo Khóa Thành công!\nKhóa đã được lưu vào file key.txt")
	except Exception as e:
		raise e

#buttom
btn_1 = Button(root, width = 10, text='Make Key', bd = 4, bg ='#93AEF3', font = (('Goudy Stout'), 10, 'bold'), command=make_key)
btn_1.pack(pady = 10)

#Entry
box_1 = Text(root, width=85, height=6, font = ('Times new roman', 15), bg = '#F5DEB3')
box_1.pack(pady=10)

box_2 = Text(root, width=85, height=6, font = ('Times new roman', 15), bg = '#EEE0E5')
box_2.pack(pady=100)

def cipher():
	try:
		khoa = {}
		with open('key.txt', 'r', encoding='utf-8') as file:
			key = file.read()
		for i in range(len(LETTERS)):
			khoa[LETTERS[i]] = key[i]
		list_kytu = ['`','!','@','#','$','%','^','&','*','(',')','-','_','=','+','~','1','2','3','4',
		'5','6','7','8','9','0',',',"'",'.','<','>',':',';','"','{','}','[',']',' ','?','/','|',"\n"]
		for i in list_kytu:
			khoa[i] = i

		user_input = box_1.get(1.0,END)
		user_input = user_input.upper()
		text = ''
		for i in user_input:
			text += khoa[i]
		box_2.delete(1.0, END)	
		box_2.insert(END, text)
		res = messagebox.showinfo("Thông báo","Mã Hóa Thành công!")
	except ValueError as e:
		res = messagebox.showerror("Error", str(e))

def decryp():
	try:
		khoa = {}
		with open('key.txt', 'r', encoding='utf-8') as file:
			key = file.read()
		for i in range(len(LETTERS)):
			khoa[key[i]] = LETTERS[i]
		list_kytu = ['`','!','@','#','$','%','^','&','*','(',')','-','_','=','+','~','1','2','3','4',
		'5','6','7','8','9','0',',',"'",'.','<','>',':',';','"','{','}','[',']',' ','?','/','|',"\n"]
		for i in list_kytu:
			khoa[i] = i

		user_input = box_1.get(1.0,END)
		user_input = user_input.upper()
		text = ''
		for i in user_input:
			text += khoa[i]
		box_2.delete(1.0, END)	
		box_2.insert(END, text)
		res = messagebox.showinfo("Thông báo","Giải Mã Thành công!")
	except Exception as e:
		raise e

def clear():
	box_1.delete(1.0,END)
	box_2.delete(1.0,END)

#Label
label_1 = Label(root, text = 'Input:', font=(('Time New Roman', 20, 'bold')), bg ='#AACEEE')
label_1.place(x=5, y = 20)
label_2 = Label(root, text = 'Output:', font=(('Time New Roman'), 20, 'bold'), bg = '#A39D81')
label_2.place(x=5, y=260)

#buttom
btn_2 = Button(root, width = 10, text='Cipher', bd=4, bg='white', fg='blue', font=(('Cascadia Code'), 10, 'bold'), command=cipher)
btn_2.place(x = 300, y = 210)
btn_3 = Button(root, width=10, text='Decryp', bd=4, bg = 'white',fg='green', font=(('Showcard Gothic'), 10, 'bold'), command=decryp)
btn_3.place(x = 500, y = 210)
btn_3=ttk.Button(root, text="Clear Text", command = clear)
btn_3.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)

root.mainloop()