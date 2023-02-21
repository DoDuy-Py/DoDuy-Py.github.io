# - Đăng nhập với tài khoản "admin" mật khẩu "123456aA@" để vào giao diện ADMIN hoặc chạy file display.py
# - Các tài khoản khác sẽ vào giao diện USER hoặc chạy file display_user.py

from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import MySQLdb
import time, datetime
from tkinter.messagebox import showinfo, askyesno
import json
from tkinter.filedialog import asksaveasfile
import webbrowser
import xlsxwriter
from openpyxl import load_workbook
#pip install openpyxl

class EmployeeUser():
    def __init__(self):
        self.root = Tk()
        self.root.title("Employees Manager")
        self.root.geometry("1370x700")
        self.root.resizable(0, 0)
        self.root.iconbitmap("images/bkacad.ico")
        self.name_emp = StringVar()
        self.name_dep = StringVar()
        self.email = StringVar()
        self.gender = StringVar()
        self.age = StringVar()
        self.position = StringVar()
        self.address = StringVar()
        self.filter_var = StringVar()
        self.search_var = StringVar()
        self.font_bold = ('times new roman', 15, "bold")
        self.font_normal = ('times new roman', 13, "normal")
        self.form_right = Frame(self.root, bd = 4, relief=RIDGE)
        self.frame_tree = Frame(self.form_right, bd=4,relief=RIDGE, width=830, height=400)
        self.treev = ttk.Treeview(self.frame_tree, height=19)
        # self.treev2 = ttk.Treeview(frame_bot, height=13)

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

    #Avatar, Logout
    def logout(self):
        answer = askyesno(title='Confirm', message='Do you want delete employee?')
        if answer:
            self.root.destroy()
            import display_first

    def del_form(self):
        try:
            self.name_emp.set("")
            self.name_dep.set("")
            self.email.set("")
            self.gender.set("")
            self.age.set("")
            self.position.set("")
            self.address.set("")
        except Exception as e:
            messagebox.showerror(title="Error", message="Delete Form unsuccessful!")

    def export(self):
        name_emp = self.name_emp.get()
        name_dep = self.name_dep.get()
        email = self.email.get()
        gender = self.gender.get()
        age = self.age.get()
        position = self.position.get()
        address = self.address.get()
        try:
            dic_info = {"Employee Name":name_emp, "Department Name":name_dep, "Email":email, "Gender":gender,
            "Age":age, "Position":position, "Address":address}

            files = [("Json File", "*.json"),
                        ("All Files", "*.*")]
            file = asksaveasfile(filetypes = files, defaultextension = files)
            json.dump(dic_info, file, indent=4)
            file.close()
            messagebox.showinfo(title="Notify", message="Save file successful!")

        except Exception as e:
            print(e)
            pass

    def _exit(self):
        answer = askyesno(title='Confirm', message='Do you want to exit?')
        if answer:
            try:
                self.root.destroy()
            except Exception as e:
                messagebox.showerror(title="Error", message="Error")
    def get_cursor(self, event):
        try:
            cursoror_row = self.treev.focus()
            var = self.treev.item(cursoror_row)
            row=var['values']
            self.name_emp.set(row[0])
            self.name_dep.set(row[1])
            self.email.set(row[2])
            self.gender.set(row[3])
            self.age.set(row[4])
            self.position.set(row[5])
            self.address.set(row[6])
        except Exception as e:
            pass

    def search(self):
        try:
            text = self.search_var.get()
            conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "employees_manager")
            cursor = conn.cursor()
            cursor.execute("SELECT name_emp, name_dep, email, gender, age, position, address FROM employees WHERE name_emp LIKE %s ", ['%'+text+'%'])
            # Có cách fix lỗi ký tự khác = cách nhân đôi ký tự % ('%%%s%%' %search_string)
            info_employees = cursor.fetchall()
            conn.close()
            self.treev.delete(*self.treev.get_children())
            for name_emp, name_dep, email, gender, age, position, address in info_employees:
                self.treev.insert("", 'end',values =(name_emp, name_dep, email, gender,age,position,address))
        except Exception as e:
            messagebox.showerror(title="Error", message="Error")


    def filter(self):
        try:
            text = self.filter_var.get()
            conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "employees_manager")
            cursor = conn.cursor()

            if text in ("Female", "Male", "Other"):
                cursor.execute("SELECT name_emp, name_dep, email, gender, age, position, address FROM employees WHERE gender=%s",[text])
                info_employees = cursor.fetchall()

            elif text in ("Developers", "Tester", "Marketing"):
                cursor.execute("SELECT name_emp, name_dep, email, gender, age, position, address FROM employees WHERE name_dep=%s",[text])
                info_employees = cursor.fetchall()

            conn.close()
            self.treev.delete(*self.treev.get_children())
            for name_emp, name_dep, email, gender, age, position, address in info_employees:
                self.treev.insert("", 'end',values =(name_emp, name_dep, email, gender,age,position,address))
                
        except Exception as e:
            messagebox.showerror(title="Error", message="Error")

    def show_all(self):
        try:
            self.filter_var.set("")
            conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "employees_manager")
            cursor = conn.cursor()
            cursor.execute("SELECT name_emp, name_dep, email, gender, age, position, address FROM employees")
            info_employees = cursor.fetchall()
            conn.close()
            self.treev.delete(*self.treev.get_children())
            for name_emp, name_dep, email, gender, age, position, address in info_employees:
                self.treev.insert("", 'end',values =(name_emp, name_dep, email, gender,age,position, address))
        except Exception as e:
            messagebox.showerror(title="Error", message="Show failed!")


    def saveExcel(self):
        workbook = load_workbook(filename='employees.xlsx')
        sheet=workbook['Sheet1']
        sheet.delete_rows(idx=2, amount=15)
        heading = ("Name", "Department", "Email", "Gender", "Age", "Position", "Address")
        sheet.append(heading)
        for row_id in self.treev.get_children():
            row = self.treev.item(row_id)['values']
            sheet.append(row)
        workbook.save(filename='employees.xlsx')

    def recruitment(self):
        recruitment = Toplevel(self.root)
        recruitment.title("Recruitment Form")
        recruitment.geometry("390x470")
        recruitment.resizable(0,0)

        name_can = StringVar()
        position = StringVar()
        email = StringVar()
        phone = StringVar()
        gender = StringVar()
        age = StringVar()

        def submit():
            name = name_can.get()
            position_ = position.get()
            email_ = email.get()
            phone_ = phone.get()
            gender_ = gender.get()
            age_ = age.get()
            try:
                answer = askyesno(title='Confirm', message='Do you want submit?')
                if answer and name and position and email and phone and gender and age:
                    conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "employees_manager")
                    cursor = conn.cursor()
                    sql = "INSERT INTO candidate(name_can, position, email, phone, gender, age) VALUES (%s,%s,%s,%s,%s,%s)"
                    # Them cac gia tri tuong ung vao cot
                    val = (name, position_, email_, phone_, gender_, age_)
                    cursor.execute(sql, val)
                    conn.commit()
                    conn.close()
                    messagebox.showinfo(title="Notify", message="Submit Successfuly!")
                else:
                    messagebox.showerror(title="Error", message="Please fill in all the information")
            except Exception as e:
                messagebox.showerror(title="Error", message="Submit failed!")

        def _exit_():
            recruitment.destroy()

        text = Label(recruitment, text="Recruitment", fg="green", font=("Times", 20, "bold"))
        text.pack(padx=5)
        can_name = Label(recruitment, text="Name", fg="#4285F4", font=self.font_bold)
        can_name.place(x=10, y=50)
        can_name_text = Entry(recruitment, textvariable=name_can, width=30)
        can_name_text.place(x=150, y=55)

        _position = Label(recruitment, text="Position", fg="#4285F4", font=self.font_bold)
        _position.place(x=10, y=100)
        _position_text = Entry(recruitment, textvariable=position, width=30)
        _position_text.place(x=150, y=105)

        _email = Label(recruitment, text="Email", fg="#4285F4", font=self.font_bold)
        _email.place(x=10, y=150)
        _email_text = Entry(recruitment, textvariable=email, width=30)
        _email_text.place(x=150, y=155)

        _phone = Label(recruitment, text="Phone", fg="#4285F4", font=self.font_bold)
        _phone.place(x=10, y=200)
        _phone_text = Entry(recruitment, textvariable=phone, width=30)
        _phone_text.place(x=150, y=205)

        _gender = Label(recruitment, text="Gender", fg="#4285F4", font=self.font_bold)
        _gender.place(x=10, y=250)
        _gender_box = ttk.Combobox(recruitment, textvariable=gender, width=18, font=self.font_normal)
        _gender_box['values'] = ('Male', 'Female', 'Other')
        _gender_box.place(x=150, y=255)

        _age = Label(recruitment, text="Age", fg="#4285F4", font=self.font_bold)
        _age.place(x=10, y=300)
        _age_text = Entry(recruitment, textvariable=age, width=30)
        _age_text.place(x=150, y=305)


        btn_submit = Button(recruitment, text="Submit", bd=4, bg="green", width=8, font=self.font_normal, command=submit)
        btn_submit.place(x=200, y=400)
        btn_exit_top = Button(recruitment, text="Exit", bd=4, bg="orange", width=8, font=self.font_normal, command=_exit_)
        btn_exit_top.place(x=290, y=400)

    def display_user(self):
        #Create Frame
        form_avt = Frame(self.root, bd = 2, relief=RIDGE)
        form_avt.place(x = 1180, y = 10, width = 170, height = 70)

        form_left = Frame(self.root, bd = 4, relief=RIDGE)
        form_left.place(x = 10, y = 80, width = 450, height = 570)

        form_right = Frame(self.root, bd = 4, relief=RIDGE)
        form_right.place(x = 500, y = 100, width=850, height=500)

        frame_left_bot = Frame(self.root, bd=4, relief=RIDGE)
        frame_left_bot.place(x=480, y=620 , width=400, height=70)

        frame_right_bot = Frame(self.root, bd=4,bg="black", relief=RIDGE)
        frame_right_bot.place(x=950, y=630, width=400, height=60)

        #Form avt, logout
        icon_avt = PhotoImage(file="images/user.png")
        avatar = Button(form_avt, image = icon_avt, width=50, height=50)
        avatar.place(x=15, y=5)
        btn_logout = Button(form_avt, text="Logout", width=7, bd=4, font=("Times", 10, "normal"), command=self.logout)
        btn_logout.place(x=90, y=20)

        #Form Customer Infor
        emp_name = Label(form_left, text="Employee Name", fg="#4285F4", font=self.font_bold)
        emp_name.place(x=10, y=20)
        emp_name_text = Entry(form_left, textvariable=self.name_emp, width=28, state=DISABLED, font=self.font_normal)
        emp_name_text.place(x=180, y=25)

        dep_name = Label(form_left, text="Department Name", fg="#4285F4", font=self.font_bold)
        dep_name.place(x=10, y=80)
        dep_name_text = Entry(form_left, textvariable=self.name_dep, width=28, state=DISABLED, font=self.font_normal)
        dep_name_text.place(x=180, y=85)

        mail = Label(form_left, text="Email", fg="#4285F4", font=self.font_bold)
        mail.place(x=10, y=140)
        mail_text = Entry(form_left, textvariable=self.email, width=28, state=DISABLED, font=self.font_normal)
        mail_text.place(x=180, y=145)

        ngender = Label(form_left, text="Gender", fg="#4285F4", font=self.font_bold)
        ngender.place(x=10, y=200)
        gender_text = Entry(form_left, textvariable=self.gender,width=28, state=DISABLED, font=self.font_normal)
        gender_text.place(x=180, y=205)

        nbirthday = Label(form_left, text="Age", fg="#4285F4", font=self.font_bold)
        nbirthday.place(x=10, y=260)
        nbirthday_text = Entry(form_left, textvariable=self.age, width=28,state=DISABLED, font=self.font_normal)
        nbirthday_text.place(x=180, y=265)

        nposition = Label(form_left, text="Position", fg="#4285F4", font=self.font_bold)
        nposition.place(x=10, y=320)
        nposition_text = Entry(form_left, textvariable=self.position, width=28, state=DISABLED, font=self.font_normal)
        nposition_text.place(x=180, y=325)

        naddress = Label(form_left, text="Address", fg="#4285F4", font=self.font_bold)
        naddress.place(x=10, y=380)
        naddress_text = Entry(form_left, textvariable=self.address, width=28, state=DISABLED, font=self.font_normal)
        naddress_text.place(x=180, y=385)

        #Button Form Custom info
        frame_button_left = Frame(form_left, bd = 2, relief=RIDGE)
        frame_button_left.place(x = 5, y = 470, width=430, height=80)
        custom_info = Label(text="Information", fg="#8B7765", font=self.font_normal).place(x=30, y=68)
        actions = Label(text="Actions Now",fg="#103F91", font=self.font_normal).place(x=30, y=540)

        btn_export = Button(frame_button_left, text="EXPORT", bg="#81C1D0", bd=5, font=("Times", 10, "bold"),
            width=8, command=self.export)
        btn_export.place(x=30, y=25)

        btn_clear = Button(frame_button_left, text="Del Form", bg="#21A366", bd=5, font=("Times", 10, "bold"),
            width=8, command=self.del_form)
        btn_clear.place(x=180, y=25)

        btn_exit = Button(frame_button_left, text="Exit", bg="#CA64EA", bd=5, font=("Times", 10, "bold"),
            width=8, command=self._exit)
        btn_exit.place(x=320, y=25)

        #Button Top Frame Right
        btn_search = Button(form_right, text="Search", bg="#57A5B7", bd=3, font=("Times", 10, "bold"),
            width=8, command=self.search)
        btn_search.place(x = 650, y = 20)

        btn_show_all = Button(form_right, text="Show ALL", bg="#B5B5B5", bd=5, font=("Times",10,"bold"),
            width=8, command=self.show_all)
        btn_show_all.place(x=730, y=17)

        btn_filter = Button(form_right, text="Filter", bg="#C1FFC1", bd=4, font=("Times",10,"bold"),
            width=8, command=self.filter)
        btn_filter.place(x=200, y=20)

        #widget Top Frame Right
        filter_box = ttk.Combobox(form_right, textvariable=self.filter_var, width=15, font=("Times",13,"normal"))
        filter_box["values"] = ("Male", "Female", "Other", "Developers", "Tester", "Marketing")
        filter_box.place(x=30, y=24)

        search_text = Entry(form_right, textvariable=self.search_var, width=20, font=("Times", 13, "normal"))
        search_text.place(x=450, y = 24)
        #Contact
        icon_fb = PhotoImage(file="images/fb.png")
        icon_mes = PhotoImage(file="images/mess1.png")
        icon_ig = PhotoImage(file="images/instagram.png")
        icon_tw = PhotoImage(file="images/tw.png")
        icon_tl = PhotoImage(file="images/telegram.png")
        btn_fb = Button(frame_right_bot, image=icon_fb, width=30, height=30,bd=4, command=self._facebook)
        btn_fb.place(x=15, y=7)
        btn_mes = Button(frame_right_bot, image=icon_mes, width=30, height=30,bd=4, command=self._messager)
        btn_mes.place(x=95, y=7)
        btn_ig = Button(frame_right_bot, image=icon_ig, width=30, height=30,bd=4, command=self._instagram)
        btn_ig.place(x=175, y=7)
        btn_tw = Button(frame_right_bot, image=icon_tw, width=30, height=30,bd=4, command=self._twitter)
        btn_tw.place(x=255, y=7)
        btn_tle = Button(frame_right_bot, image=icon_tl, width=30, height=30,bd=4, command=self._telegram)
        btn_tle.place(x=335, y=7)

        #Button Bottom
        ations_bot = Label(self.root, text="Actions Tree", fg="#103F91", font=self.font_normal)
        ations_bot.place(x=495, y=607)

        contact = Label(self.root, text="Contact Now:", fg="#FF6600", font=self.font_normal)
        contact.place(x=955, y=600)

        btn_recruitment = Button(frame_left_bot, text="Recruitment", bg="gray", bd=4, font=("Times",10,"bold"), width=10, command=self.recruitment)
        btn_recruitment.place(x=200, y=20)

        btn_save_ex = Button(frame_left_bot, text="Save Excel", bg="#FFE595", bd=4, font=("Times",10,"bold"),
            width=8, command=self.saveExcel)
        btn_save_ex.place(x=300, y=20)        

        #Tree View
        frame_tree = Frame(form_right, bd=4,relief=RIDGE, width=830, height=400)
        frame_tree.place(x= 5, y=70)

        self.treev = ttk.Treeview(frame_tree, height=19)
        self.treev.pack()
         
        # Constructing vertical scrollbar
        # with treeview
        yscrlbar = ttk.Scrollbar(frame_tree,orient ="vertical",command = self.treev.yview)
        yscrlbar.place(relx=0.98, rely=0.05, relheight=0.9, relwidth=0.020)
        xscrlbar = Scrollbar(frame_tree, orient="horizontal", command=self.treev.xview)
        xscrlbar.place(relx=0, rely=0.94, relheight=0.050, relwidth=0.99)
        self.treev.configure(yscrollcommand=yscrlbar.set, xscrollcommand=xscrlbar.set)
         
        # Defining number of columns
        self.treev["columns"] = ("Name", "Department", "Email", "Gender", "Age", "Position", "Address")
         
        # Defining heading
        self.treev['show'] = 'headings'
        # scrollbar.grid(row=0, column=1, sticky='ns')
        self.treev.column("Name", width = 170)
        self.treev.column("Department", width = 120)
        self.treev.column("Email", width = 170)
        self.treev.column("Gender", width = 70)
        self.treev.column("Age", width = 50)
        self.treev.column("Position", width = 100)
        self.treev.column("Address", width = 140)

        # define headings
        self.treev.heading('Name', text='Name')
        self.treev.heading('Department', text='Department')
        self.treev.heading('Email', text='Email')
        self.treev.heading('Gender', text='Gender')
        self.treev.heading('Age', text='Age')
        self.treev.heading('Position', text='Position')
        self.treev.heading('Address', text='Address')
        self.treev.bind("<ButtonRelease-1>", self.get_cursor) #Click vào 1 bản ghi tại tree view

        self.root.mainloop()

if __name__ == '__main__':
    obj = EmployeeUser()
    obj.display_user()