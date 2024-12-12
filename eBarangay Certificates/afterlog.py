import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
import pymysql 

def open_after_login():
    win = tk.Tk()
    win.geometry('1050x650+0+0')
    win.title('eBarangay Certificates')
    win.config(bg='light blue')

    win.iconbitmap(r"C:\Users\Lenovo\Desktop\eBarangay Certificates\logs.ico")

    title_label = tk.Label(
        win, text='eBarangay Certificates',
        font=('Arial', 35, 'bold'),
        border=12, relief=tk.GROOVE,
        bg='light blue', fg='navy blue'
    )
    title_label.pack(side=tk.TOP, fill=tk.X)



    detail_frame = tk.LabelFrame(
        win, text='Enter Details',
        font=('Arial', 15),
        bg='light blue', fg='navy blue',
        border=12, relief=tk.GROOVE
    )
    detail_frame.place(x=20, y=90, width=320, height=550)

    data_frame = tk.Frame(
        win, border=12, bg='light blue', relief=tk.GROOVE
    )
    data_frame.place(x=365, y=90, width=675, height=550)

    or_num = tk.StringVar()
    name = tk.StringVar()
    sitio = tk.StringVar()
    age = tk.StringVar()
    birthdate = tk.StringVar()
    date = tk.StringVar()
    cert = tk.StringVar()
    amt = tk.StringVar()
    search_by = tk.StringVar()
    search_term = tk.StringVar()

    fields = [
        ("OR Number", or_num),
        ("Name", name),
        ("Sitio", sitio),
        ("Age", age),
        ("Date of Birth", birthdate),
        ("Date Issued", date),
        ("Certificate", cert),
        ("Amount", amt)
    ]

    for i, (label, variable) in enumerate(fields):
        tk.Label(detail_frame, text=label, font=('Arial', 10), bg='light blue', fg='navy blue').grid(row=i, column=0, padx=10, pady=10)
        tk.Entry(detail_frame, bd=7, font=('Arial', 10), textvariable=variable).grid(row=i, column=1, padx=10, pady=10)

    def fetch_citizen():
        conn = pymysql.connect(host = 'localhost', user='root',password='',database='barangay')
        curr = conn.cursor()
        curr.execute('SELECT * FROM citizen')
        rows = curr.fetchall()   
        if len(rows)!=0:
            citizen_table.delete(*citizen_table.get_children())
            for row in rows:
                citizen_table.insert('',tk.END,values=row)
            conn.commit()
        conn.close()

    def add_func():
        if  name.get() =='' or cert.get() == '':
            messagebox.showerror('Error','Please fill all the fields!')
        else:
            if messagebox.askyesno("Confirmation","Are you sure to save this record?"):
                conn = pymysql.connect(host='localhost',user='root',password='',database='barangay')
                curr = conn.cursor()
                curr.execute('INSERT INTO citizen VALUES(%s,%s,%s,%s,%s,%s,%s,%s)',
                         (or_num.get(),name.get(),sitio.get(),age.get(),birthdate.get(),date.get(),
                          cert.get(),amt.get()))
                conn.commit()
                conn.close()
                fetch_citizen()
                clear()

    def get_cursor(event):
        cursor_row = citizen_table.focus()
        content = citizen_table.item(cursor_row)
        row = content['values']
        if row:
            or_num.set(row[0])
            name.set(row[1])
            sitio.set(row[2])
            age.set(row[3])
            birthdate.set(row[4])
            date.set(row[5])
            cert.set(row[6])
            amt.set(row[7])

    def clear():
        if messagebox.askyesno("Confirmation", "Are you sure you want to clear all fields?"):
            or_num.set('')
            name.set('')
            sitio.set('')
            age.set('')
            birthdate.set('')
            date.set('')
            cert.set('')
            amt.set('')


    def upd_func():
        if or_num.get() == '':
            messagebox.showerror('Error','Select a record to update!')
        else:
            if messagebox.askyesno("Confirmation","Are you sure you want to update this record?"):
                try:
                    conn = pymysql.connect(host='localhost',user='root',password='',database='barangay')
                    curr = conn.cursor()
                    curr.execute('UPDATE citizen SET name=%s,sitio=%s,age=%s,birthdate=%s,date_issued=%s,certificate=%s,amount=%s WHERE or_num=%s',
                     (name.get(),sitio.get(),age.get(),birthdate.get(),date.get(),
                          cert.get(),amt.get(),or_num.get())) 
                    conn.commit()
                    conn.close()
                    fetch_citizen()
                    clear()
                    messagebox.showinfo('Success',"Record updated successfully!")
                except pymysql.Error as e:
                    messagebox.showerror('Database Error', f"An error occurred: {e}")

    def del_func():
        if or_num.get() == '':
            messagebox.showerror('Error', 'Select a record to delete!')
        else:
            if messagebox.askyesno("Confirmation", "Are you sure you want to delete this record?"):
                conn = pymysql.connect(host='localhost', user='root', password='', database='barangay')
                curr = conn.cursor()
                curr.execute('DELETE FROM citizen WHERE or_num=%s', (or_num.get()))
                conn.commit()
                conn.close()
                fetch_citizen()
                clear()

    def search_func():
        if not search_by.get() or not search_term.get():
            messagebox.showerror('Error', 'Please select a search criteria and enter a search term!')
            return
        
        column_mapping = {
        'OR Number': 'or_num',
        'Name': 'name',
        'Sitio': 'sitio',
        'Age': 'age',
        'Birthdate': 'birthdate',
        'Date': 'date_issued',
        'Certificate': 'certificate',
        'Amount': 'amount'
        }

        column = column_mapping.get(search_by.get())  
        if not column:
            messagebox.showerror('Error', 'Invalid search criterion selected!')
            return
        
        try:
            conn = pymysql.connect(host='localhost', user='root', password='', database='barangay')
            curr = conn.cursor()

            query = f"SELECT * FROM citizen WHERE {column} LIKE %s"
            search_value = '%' + search_term.get() + '%'
            print(f"Executing query: {query} with value: {('%' + search_term.get() + '%',)}")
            curr.execute(query, ('%' + search_term.get() + '%',))
            rows = curr.fetchall()
            print(f"Rows fetched: {rows}")

            citizen_table.delete(*citizen_table.get_children())
            for row in rows:
                citizen_table.insert('', tk.END, values=row)
                conn.close()
        except pymysql.Error as e:
         messagebox.showerror('Database Error', f"An error occurred: {e}")

    def show_all_func():
        fetch_citizen() 

        

    btn_frame = tk.Frame(detail_frame,bg='light blue',bd=10,relief=tk.GROOVE)
    btn_frame.place(x=35,y=418,width=230,height=85)

    add_btn = tk.Button(btn_frame,text='SAVE',font=('arial',10),bg='yellow',fg='black',width=11,command=add_func)
    add_btn.grid(row=0,column=0,padx=4, pady=2)

    upd_bttn = tk.Button(btn_frame,text='UPDATE',font=('arial',10),bg='yellow',fg='black',width=11,command=upd_func)
    upd_bttn.grid(row=0,column=1,padx=3, pady=2)

    dlt_bttn = tk.Button(btn_frame,text='DELETE',font=('arial',10),bg='yellow',fg='black',width=11,command=del_func)
    dlt_bttn.grid(row=1,column=0,padx=4, pady=2)

    clr_bttn = tk.Button(btn_frame,text='CLEAR',font=('arial',10),bg='yellow',fg='black',width=11,command=clear)
    clr_bttn.grid(row=1,column=1,padx=3, pady=2)

    search_frame = tk.Frame(data_frame,bg='light blue',bd=10,relief=tk.GROOVE)
    search_frame.pack(side=tk.TOP,fill=tk.X)

    search_lbl = tk.Label(search_frame,text='Search',bg='light blue',font=('Arial',10))
    search_lbl.grid(row=0,column=0,padx=2,pady=2)

    search_in = ttk.Combobox(search_frame,font=("arial",10),state="readonly",textvariable=search_by)
    search_in['values'] = ('Name','OR Number','Sitio','Age','Birthdate','Date','Certificate','Amount')
    search_in.grid(row=0,column=1,padx=2,pady=2)

    search_entry = tk.Entry(search_frame, textvariable=search_term, font=("Arial", 10), bd=5)
    search_entry.grid(row=0, column=2, padx=2, pady=2)

    search_btn = tk.Button(search_frame,text='Search',font=('arial',10),bd=5,width=10,bg='light blue',command=search_func)
    search_btn.grid(row=0,column=2,columnspan=2,padx=(100,2),pady=2,sticky='e')

    shw_btn = tk.Button(search_frame,text='Show All',font=('arial',10),bd=5,width=10,bg='light blue',command=show_all_func)
    shw_btn.grid(row=0,column=3,columnspan=2,padx=(100,2),pady=2,sticky='e')

    main_frame = tk.Frame(data_frame,bg='light blue',bd=11,relief=tk.GROOVE)
    main_frame.pack(fill=tk.BOTH,expand=True)

    y_scroll = tk.Scrollbar(main_frame,orient=tk.VERTICAL)
    x_scroll = tk.Scrollbar(main_frame,orient=tk.HORIZONTAL)

    citizen_table = ttk.Treeview(main_frame,columns=('OR Number','Name','Sitio','Age','Birthdate','Date','Certification','Amount'),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)
    
    y_scroll.config(command=citizen_table.yview)
    x_scroll.config(command=citizen_table.xview)

    y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
    x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

    for col in citizen_table['columns']:
        citizen_table.heading(col, text=col)
        citizen_table.column(col, width=200)
    
    citizen_table['show'] = 'headings'
    citizen_table.pack(fill=tk.BOTH,expand=True)

    fetch_citizen()

    citizen_table.bind('<ButtonRelease-1>',get_cursor)

    win.mainloop()

if __name__ == "__main__":
    open_after_login()