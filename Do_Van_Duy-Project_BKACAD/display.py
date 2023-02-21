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

class Employee():
    def __init__(self):
        self.root = Tk()
        self.root.title("Employees Manager")
        self.root.geometry("1370x700")
        self.root.resizable(0, 0)
        self.root.iconbitmap("images/bkacad.ico")
        self.id_emp = StringVar()
        self.id_dep = StringVar()
        self.name_emp = StringVar()
        self.name_dep = StringVar()
        self.email = StringVar()
        self.phone = StringVar()
        self.gender = StringVar()
        self.age = StringVar()
        self.position = StringVar()
        self.salary = StringVar()
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

    def update(self):
        try:
            conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "employees_manager")
            cursor = conn.cursor()
            cursor.execute("UPDATE employees SET id_dep='" +
                   self.id_dep.get() + "', name_emp='" +
                   self.name_emp.get() + "', name_dep='" +
                   self.name_dep.get() + "', email='" +
                   self.email.get() + "', phone='" +
                   self.phone.get() + "', gender='" +
                   self.gender.get() + "', age='" +
                   self.age.get() + "', position='" +
                   self.position.get() + "', salary='" +
                   self.salary.get() + "', address='" +
                   self.address.get() + "' WHERE id_emp='" +
                   self.id_emp.get() + "' ")
            conn.commit()
            conn.close()
            messagebox.showinfo(title="Notify", message="Update employee Successfuly!")
        except ValueError:
            messagebox.showerror(title="Error", message="Update employee failed!")


    def del_form(self):
        try:
            self.id_emp.set("")
            self.id_dep.set("")
            self.name_emp.set("")
            self.name_dep.set("")
            self.email.set("")
            self.phone.set("")
            self.gender.set("")
            self.age.set("")
            self.position.set("")
            self.salary.set("")
            self.address.set("")
        except Exception as e:
            messagebox.showerror(title="Error", message="Delete Form unsuccessful!")

    def add_emp(self):
        id_dep = self.id_dep.get()
        name_emp = self.name_emp.get()
        name_dep = self.name_dep.get()
        email = self.email.get()
        phone = self.phone.get()
        gender = self.gender.get()
        age = self.age.get()
        position = self.position.get()
        salary = self.salary.get()
        address = self.address.get()
        if id_dep and name_emp and name_dep and email and phone and gender and age and position and salary and address:
            try:
                conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "employees_manager")
                cursor = conn.cursor()
                # Tao cau truy van
                sql = "INSERT INTO employees(id_dep, name_emp, name_dep, email, phone, gender, age, position, salary, address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                # Them cac gia tri tuong ung vao cot
                val = (id_dep, name_emp, name_dep, email, phone, gender, age, position, salary, address)
                cursor.execute(sql, val)
                conn.commit()
                conn.close()
                messagebox.showinfo(title="Notify", message="Add employee Successfuly!")
            except ValueError:
                messagebox.showerror(title="Error", message="Add employee failed!")
        else:
            messagebox.showerror(title="Error", message="Add employee failed!")

    def del_emp(self):
        try:
            answer = askyesno(title='Confirm', message='Do you want delete employee?')
            id_emp = self.id_emp.get()
            if answer:
                conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "employees_manager")
                cursor = conn.cursor()
                sql = "DELETE FROM employees WHERE id_emp = %s"
                adr = (id_emp)
                cursor.execute(sql, adr)
                conn.commit()
                conn.close()
                messagebox.showinfo(title="Notify", message="Delete employee Successfuly!")
        except Exception as e:
            messagebox.showerror(title="Error", message="Delete employee failed!")

    def export(self):
        id_emp = self.id_emp.get()
        id_dep = self.id_dep.get()
        name_emp = self.name_emp.get()
        name_dep = self.name_dep.get()
        email = self.email.get()
        phone = self.phone.get()
        gender = self.gender.get()
        age = self.age.get()
        position = self.position.get()
        salary = self.salary.get()
        address = self.address.get()
        try:
            dic_info = {"Employee Code":id_emp, "Department Code":id_dep, "Employee Name":name_emp,
            "Department Name":name_dep, "Email":email, "Phone":phone, "Gender":gender, "Age":age,
            "Position":position, "Salary":salary, "Address":address}

            files = [("All Files", "*.*"),
                    ("Json File", "*.json"),
                    ("Text Document", "*.txt")]
            file = asksaveasfile(filetypes = files, defaultextension = files)
            json.dump(dic_info,file, indent=4)
            file.close()
            messagebox.showinfo(title="Notify", message="Save file successful!")

        except Exception as e:
            messagebox.showerror(title="Error", message="Error")

    def _exit(self):
        answer = askyesno(title='Confirm', message='Do you want to exit?')
        if answer:
            try:
                self.root.destroy()
            except Exception as e:
                messagebox.showerror(title="Error", message="Error")

    def search(self):
        try:
            text = self.search_var.get()
            conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "employees_manager")
            cursor = conn.cursor()
            cursor.execute("SELECT id_emp, name_emp, name_dep, email, phone, gender, age, position, salary, address FROM employees WHERE name_emp LIKE %s ", ['%'+text+'%'])
            # Có cách fix lỗi ký tự khác = cách nhân đôi ký tự % ('%%%s%%' %search_string)
            info_employees = cursor.fetchall()
            conn.close()
            self.treev.delete(*self.treev.get_children())
            for id_emp, name_emp, name_dep, email, phone, gender, age, position, salary, address in info_employees:
                self.treev.insert("", 'end',values =(id_emp, name_emp, name_dep, email, phone,gender,age,position,salary,address))
        except Exception as e:
            print(e)
            messagebox.showerror(title="Error", message="Error")


    def filter(self):
        try:
            text = self.filter_var.get()
            conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "employees_manager")
            cursor = conn.cursor()

            if text in ("Female", "Male", "Other"):
                cursor.execute("SELECT id_emp, name_emp, name_dep, email, phone, gender, age, position, salary, address FROM employees WHERE gender=%s",[text])
                info_employees = cursor.fetchall()

            elif text in ("Developers", "Tester", "Marketing"):
                cursor.execute("SELECT id_emp, name_emp, name_dep, email, phone, gender, age, position, salary, address FROM employees WHERE name_dep=%s",[text])
                info_employees = cursor.fetchall()

            conn.close()
            self.treev.delete(*self.treev.get_children())
            for id_emp, name_emp, name_dep, email, phone, gender, age, position, salary, address in info_employees:
                self.treev.insert("", 'end',values =(id_emp, name_emp, name_dep, email, phone,gender,age,position,salary,address))
                
        except Exception as e:
            messagebox.showerror(title="Error", message="Error")

    def show_all(self):
        try:
            self.filter_var.set("")
            conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "employees_manager")
            cursor = conn.cursor()
            cursor.execute("SELECT id_emp, name_emp, name_dep, email, phone, gender, age, position, salary, address FROM employees")
            info_employees = cursor.fetchall()
            conn.close()
            self.treev.delete(*self.treev.get_children())
            for id_emp, name_emp, name_dep, email, phone, gender, age, position, salary, address in info_employees:
                self.treev.insert("", 'end',values =(id_emp, name_emp, name_dep, email, phone,gender,age,position,salary,address))
        except Exception as e:
            messagebox.showerror(title="Error", message="Show failed!")

    def show_contract(self):
        pass

    def make_contract(self):
        pass

    def get_cursor(self, event):
        try:
            cursoror_row = self.treev.focus()
            var = self.treev.item(cursoror_row)
            row=var['values']
            self.id_emp.set(row[0])
            self.name_emp.set(row[1])
            self.name_dep.set(row[2])
            self.email.set(row[3])
            self.phone.set(row[4])
            self.gender.set(row[5])
            self.age.set(row[6])
            self.position.set(row[7])
            self.salary.set(row[8])
            self.address.set(row[9])
            conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "employees_manager")
            cursor = conn.cursor()
            sql = "SELECT id_dep FROM employees WHERE id_emp = %s"
            cursor.execute(sql, str(row[0]))
            id_dep = cursor.fetchall()
            conn.close()
            self.id_dep.set(id_dep)
        except Exception as e:
            pass

    def saveExcel(self):
        workbook = load_workbook(filename='employees.xlsx')
        sheet=workbook['Sheet1']
        sheet.delete_rows(idx=2, amount=15)
        heading = ("ID", "Name", "Department", "Email", "Phone", "Gender", "Age", "Position", "Salary", "Address")
        sheet.append(heading)
        for row_id in self.treev.get_children():
            row = self.treev.item(row_id)['values']
            sheet.append(row)
        workbook.save(filename='employees.xlsx')

    def candidate(self):
        candidate = Toplevel(self.root)
        candidate.title("Candidate TreeViews")
        candidate.geometry("850x500")
        candidate.resizable(0,0)
        can_del = StringVar()

        def exit_():
            candidate.destroy()
        #Method TopLevel
        def refresh():
            try:
                conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "employees_manager")
                cursor = conn.cursor()
                cursor.execute("SELECT id_can, name_can, position, email, phone, gender, age FROM candidate")
                info_candidate = cursor.fetchall()
                conn.close()
                treev2.delete(*treev2.get_children())
                for id_can, name_can, position, email, phone, gender, age in info_candidate:
                    treev2.insert("", 'end',values =(id_can, name_can, position, email, phone,gender,age))
            except Exception as e:
                messagebox.showerror(title="Error", message="Refresh failed!")

        #Create Frame
        frame_top = Frame(candidate, bd=2, relief=RIDGE)
        frame_top.place(x=10,y=10, width=820, height=70)

        frame_bot = Frame(candidate, bd=4, relief=RIDGE)
        frame_bot.place(x=10, y=85, width=820, height=320)

        frame_actions = Label(candidate, bd=3,relief=RIDGE)
        frame_actions.place(x=30,y=420, width=780, height=70)

        logo = Label(frame_top, text = "DMOUSE CANDIDATE", fg="orange", font=("Bauhaus 93", 30, "bold"))
        logo.pack()

        #Button Actions
        btn_refresh = Button(frame_actions, text="Refresh",bd=4, bg="#0097EE", font=("Times",10,"bold"),
            width=8, command=refresh) #command=self.show_all
        btn_refresh.place(x=680, y=20)

        btn_delete = Button(frame_actions, text="Delete",bd=4, bg="#57D558", font=("Times",10,"bold"),
            width=8) #command=self.delete
        btn_delete.place(x=380, y=20)

        btn_exit = Button(frame_actions, text="Exit",bd=4, bg="#E53E31", font=("Times",10,"bold"),
            width=8, command=exit_)
        btn_exit.place(x=25, y=20)

        # treeview initialization
        treev2 = ttk.Treeview(frame_bot, height=13)
        treev2.place(x=5, y=10, width=790)

        # scrollbars
        vsb = Scrollbar(frame_bot, orient="vertical", command=treev2.yview)
        vsb.place(relx=0.978, rely=0.07, relheight=0.83, relwidth=0.020)

        hsb = Scrollbar(frame_bot, orient="horizontal", command=treev2.xview)
        hsb.place(relx=0.0, rely=0.95, relheight=0.05, relwidth=1.0)

        treev2.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        treev2["columns"] = ("ID", "Name","Position", "Email", "Phone", "Gender", "Age")
        # scrollbar.grid(row=0, column=1, sticky='ns')
        treev2.column("ID", width = 20)
        treev2.column("Name", width = 120)
        treev2.column("Position", width = 90)
        treev2.column("Email", width = 120)
        treev2.column("Phone", width = 120)
        treev2.column("Gender", width = 40)
        treev2.column("Age", width = 35)

        treev2['show'] = 'headings'
        # define headings
        treev2.heading('ID', text='ID')
        treev2.heading('Name', text='Name')
        treev2.heading('Position', text='Position')
        treev2.heading('Email', text='Email')
        treev2.heading('Phone', text='Phone')
        treev2.heading('Gender', text='Gender')
        treev2.heading('Age', text='Age')
        treev2.bind("<ButtonRelease-1>")
        # treev.insert("", 'end',values =("1", "F", "F", "12","M","22","A"))
        conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "employees_manager")
        cursor = conn.cursor()
        cursor.execute("SELECT id_can, name_can, position, email, phone, gender, age FROM candidate")
        info_candidate = cursor.fetchall()
        conn.close()
        for id_can, name_can, position, email, phone, gender, age in info_candidate:
            treev2.insert("", 'end',values =(id_can, name_can, position, email, phone,gender,age))


    def display_admin(self):
        #Create Frame
        form_avt = Frame(self.root, bd = 2, relief=RIDGE)
        form_avt.place(x = 1180, y = 10, width = 170, height = 70)

        form_left = Frame(self.root, bd = 4, relief=RIDGE)
        form_left.place(x = 10, y = 80, width = 450, height = 570)

        form_right = Frame(self.root, bd = 4, relief=RIDGE)
        form_right.place(x = 500, y = 100, width=850, height=500)

        frame_left_bot = Frame(self.root, bd=4, relief=RIDGE)
        frame_left_bot.place(x=480, y=620 , width=400, height=70)

        frame_right_bot = Frame(self.root, bd=4, bg="black", relief=RIDGE)
        frame_right_bot.place(x=950, y=630, width=400, height=60)

        #Form avt, logout
        icon_avt = PhotoImage(file="images/admin.png")
        avatar = Button(form_avt, image = icon_avt, width=50, height=50)
        avatar.place(x=15, y=5)
        btn_logout = Button(form_avt, text="Logout", width=7, bd=4, font=("Times", 10, "normal"), command=self.logout)
        btn_logout.place(x=90, y=20)

        #Form Customer Infor
        emp_code = Label(form_left, text = "Employee Code", fg = "#4285F4", font=self.font_bold)
        emp_code.place(x = 10, y = 7)
        emp_id_text = Entry(form_left, textvariable=self.id_emp, width=28, font = self.font_normal,
            state=DISABLED) #state để không cho người dùng có thể sửa text
        emp_id_text.place(x=180, y=10)

        emp_dep = Label(form_left, text = "Department Code", fg = "#4285F4", font=self.font_bold)
        emp_dep.place(x = 10, y = 47)
        emp_dep_text = Entry(form_left, textvariable=self.id_dep, width=28, font = self.font_normal)
        emp_dep_text.place(x=180, y=50)

        emp_name = Label(form_left, text="Employee Name", fg="#4285F4", font=self.font_bold)
        emp_name.place(x=10, y=87)
        emp_name_text = Entry(form_left, textvariable=self.name_emp, width=28, font=self.font_normal)
        emp_name_text.place(x=180, y=90)

        dep_name = Label(form_left, text="Department Name", fg="#4285F4", font=self.font_bold)
        dep_name.place(x=10, y=127)
        dep_name_text = Entry(form_left, textvariable=self.name_dep, width=28, font=self.font_normal)
        dep_name_text.place(x=180, y=130)

        mail = Label(form_left, text="Email", fg="#4285F4", font=self.font_bold)
        mail.place(x=10, y=167)
        mail_text = Entry(form_left, textvariable=self.email, width=28, font=self.font_normal)
        mail_text.place(x=180, y=170)

        nphone = Label(form_left, text="Phone Numbers", fg="#4285F4", font=self.font_bold)
        nphone.place(x=10, y=207)
        nphone_text = Entry(form_left, textvariable=self.phone, width=28, font=self.font_normal)
        nphone_text.place(x=180, y=210)

        ngender = Label(form_left, text="Gender", fg="#4285F4", font=self.font_bold)
        ngender.place(x=10, y=247)
        gender_box = ttk.Combobox(form_left, textvariable=self.gender, width=26, font=self.font_normal)
        gender_box['values'] = ('Male', 'Female', 'Other')
        gender_box.place(x=180, y=250)

        nbirthday = Label(form_left, text="Age", fg="#4285F4", font=self.font_bold)
        nbirthday.place(x=10, y=287)
        nbirthday_text = Entry(form_left, textvariable=self.age, width=28, font=self.font_normal)
        nbirthday_text.place(x=180, y=290)

        nposition = Label(form_left, text="Position", fg="#4285F4", font=self.font_bold)
        nposition.place(x=10, y=327)
        nposition_text = Entry(form_left, textvariable=self.position, width=28, font=self.font_normal)
        nposition_text.place(x=180, y=330)

        nsalary = Label(form_left, text="Salary", fg="#4285F4", font=self.font_bold)
        nsalary.place(x=10, y=367)
        nsalary_text = Entry(form_left, textvariable=self.salary, width=28, font=self.font_normal)
        nsalary_text.place(x=180, y=370)

        naddress = Label(form_left, text="Address", fg="#4285F4", font=self.font_bold)
        naddress.place(x=10, y=407)
        naddress_text = Entry(form_left, textvariable=self.address, width=28, font=self.font_normal)
        naddress_text.place(x=180, y=410)

        #Button Form Custom info
        frame_button_left = Frame(form_left, bd = 2, relief=RIDGE)
        frame_button_left.place(x = 5, y = 470, width=430, height=80)
        custom_info = Label(text="Information", fg="#8B7765", font=self.font_normal).place(x=30, y=68)
        actions = Label(text="Actions Now",fg="#103F91", font=self.font_normal).place(x=30, y=540)

        btn_add = Button(frame_button_left, text="ADD New", bg="orange", bd=5, font=("Times", 10, "bold"),
            command=self.add_emp)
        btn_add.place(x=5, y=25)

        btn_update = Button(frame_button_left, text="Update", bg="#3CC58A", bd=5, font=("Times", 10, "bold"),
            width=8, command=self.update)
        btn_update.place(x=90, y=25)

        btn_export = Button(frame_button_left, text="EXPORT", bg="#81C1D0", bd=5, font=("Times", 10, "bold"),
            width=8, command=self.export)
        btn_export.place(x=175, y=25)

        btn_clear = Button(frame_button_left, text="Del Form", bg="#21A366", bd=5, font=("Times", 10, "bold"),
            width=8, command=self.del_form)
        btn_clear.place(x=260, y=25)

        btn_exit = Button(frame_button_left, text="Exit", bg="#CA64EA", bd=5, font=("Times", 10, "bold"),
            width=8, command=self._exit)
        btn_exit.place(x=345, y=25)

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
        contact.place(x=950, y=600)

        btn_del = Button(frame_left_bot, text="Delete", bg="#F03442", bd=4, font=("Times",10,"normal"),
            width=8, command=self.del_emp)
        btn_del.place(x=5, y=20)

        btn_save_ex = Button(frame_left_bot, text="Save Excel", bg="#FFE595", bd=4, font=("Times",10,"normal"),
            width=8, command=self.saveExcel)
        btn_save_ex.place(x=82, y=20)

        btn_contract = Button(frame_left_bot, text="Contract", bg="#C82A6D", bd=4, font=("Times",10,"normal"),
            width=8, command=self.show_contract)
        btn_contract.place(x=160, y=20)

        mk_contract = Button(frame_left_bot, text="Make Con", bg="#1474F2", bd=4, font=("Times",10,"normal"),
            width=8, command=self.make_contract)
        mk_contract.place(x=240, y=20)         

        btn_candidate = Button(frame_left_bot, text="Candidate", bg="#C1FFC1", bd=4, font=("Times",10,"normal"),
            width=8, command=self.candidate)
        btn_candidate.place(x=315, y=20)

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
        self.treev["columns"] = ("ID", "Name", "Department","Email","Phone","Gender","Age","Position","Salary","Address")
         
        # Defining heading
        self.treev['show'] = 'headings'
        # scrollbar.grid(row=0, column=1, sticky='ns')
        self.treev.column("ID", width = 30)
        self.treev.column("Name", width = 120)
        self.treev.column("Department", width = 75)
        self.treev.column("Email", width = 150)
        self.treev.column("Phone", width = 110)
        self.treev.column("Gender", width = 50)
        self.treev.column("Age", width = 35)
        self.treev.column("Position", width = 90)
        self.treev.column("Salary", width = 70)
        self.treev.column("Address", width = 70)

        # define headings
        self.treev.heading('ID', text='ID')
        self.treev.heading('Name', text='Name')
        self.treev.heading('Department', text='Department')
        self.treev.heading('Email', text='Email')
        self.treev.heading('Phone', text='Phone')
        self.treev.heading('Gender', text='Gender')
        self.treev.heading('Age', text='Age')
        self.treev.heading('Position', text='Position')
        self.treev.heading('Salary', text='Salary')
        self.treev.heading('Address', text='Address')
        self.treev.bind("<ButtonRelease-1>",self.get_cursor) #Click vào 1 bản ghi tại tree view

        self.root.mainloop()

if __name__ == '__main__':
    obj = Employee()
    obj.display_admin()