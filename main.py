# Start 9:25 PM 8/29/2022
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import sys

con = sqlite3.connect('TODO.db')

con.execute("""CREATE TABLE IF NOT EXISTS TODO
	(ID INT PRIMARY KEY,
	NAME TEXT)""")

cur = con.cursor()

#cur.execute("INSERT INTO TODO (ID,NAME) VALUES (4, 'karimi')")

cur = con.execute("SELECT ID,NAME FROM TODO")

con.commit()

def dark(envert):
	label.config(image=icon1)
	window.config(bg='#333333')
	menubar.config(background='#333333')
	list_box.config(bg='#333333',fg='#F0F0F0',bd=0)
	btn.config(image=Photo2,bd=0,activebackground='#333333')
	btn3.config(image=Photo4,bd=0,activebackground='#333333')

def light(envert):
	label.config(image=icon)
	window.config(bg='#F0F0F0')
	menubar.config(background='#F0F0F0')
	list_box.config(bg='#F0F0F0',fg='#333333',bd=0)
	btn.config(image=Photo,bd=0,activebackground='#F0F0F0')
	btn3.config(image=Photo3,bd=0,activebackground='#F0F0F0')


def Help():
	messagebox.showinfo('Help','Change Color with F1,F2')

def version():
	messagebox.showinfo('ToDo','ToDo\nversion 1.0.0\nauthor Satrap18')

def new():
	def add():
		try:
			con = sqlite3.connect('TODO.db')
			cur = con.cursor()
			data = [e1.get() , e2.get()]
			cur.execute("INSERT INTO TODO VALUES (?,?)",data)
			con.commit()
			root.destroy()
			messagebox.showinfo('Add','Add ToDo Successfully!')
		except sqlite3.IntegrityError:
			messagebox.showinfo('Error','is ID Available Select another ID')


	root = Tk()
	root.title('Add New Todo')
	lbl = Label(root,text='ID',font=('arial',15))
	lbl.pack()
	e1 = Entry(root,font=('arial',15))
	e1.pack()
	lbl2 = Label(root,text='Add Your ToDo',font=('arial',15))
	lbl2.pack()
	e2 = Entry(root,font=('arial',15))
	e2.pack()
	btn2 = ttk.Button(root,text='Add',command=add)
	btn2.pack(pady=5)
	root.mainloop()

def remove():
	def delete():
		con = sqlite3.connect('TODO.db')
		cur = con.cursor()
		cur.execute(f"DELETE FROM TODO WHERE id == {int(e3.get())}")
		con.commit()
		messagebox.showinfo('Delete','Delete Successfully!')
		Toplevel.destroy()

	Toplevel = Tk()
	Toplevel.title('Delete ToDo')
	lbl3 = Label(Toplevel,text='ENTER ID',font=('arial',15))
	lbl3.pack()
	e3 = Entry(Toplevel,font=('arial',15))
	e3.pack()
	ttk.Button(Toplevel,text='Delete',command=delete).pack()
	Toplevel.mainloop()

window = Tk()
window.title('Todo')
window.geometry('400x400')


icon = PhotoImage(file='3-light.png')

icon1 = PhotoImage(file='3.png')

Photo = PhotoImage(file='add.png')
Photo2 = PhotoImage(file='add_dark.png')
Photo3 = PhotoImage(file='remove.png')
Photo4 = PhotoImage(file='remove-dark.png')


window.iconphoto(True,icon)

label = Label(window,image=icon,bd=0)
label.pack()

btn = Button(window,image=Photo,command=new,bd=0)
btn.place(x=0,y=90)

btn3 = Button(window,image=Photo3,bd=0,command=remove)
btn3.place(x=370,y=100)
#-----------------------Menu------------------------
menubar = Menu(window,bg='#000000')

filemenu = Menu(menubar,tearoff=0)

menubar.add_cascade(label='Color',command=Help)
menubar.add_cascade(label='Help',menu=filemenu)
filemenu.add_command(label='About',command=version)

window.config(menu=menubar)
#----------------------------------------------------
#-----------------------------listbox----------------
list_box = Listbox(window,width=50,height=30,bg='#F0F0F0',fg='black',font=('arial',13),bd=0)#,selectmode=SINGLE)
list_box.pack()

for i in cur.fetchall():
        list_box.insert(i[0],f'{i[0]}                              {i[1]}')
#----------------------------------------------------
#-------------color-------------------
window.bind('<F1>',dark)
window.bind('<F2>',light)
#-------------------------------------
window.mainloop()