from tkinter import *
from PIL import ImageTk, Image
from random import *

##### Config window ##### 

root = Tk()
root.geometry("300x100")
root.title("MathX")
root.resizable(width=False, height=False)
root.iconbitmap('mathx.ico')

##### Function #####

def calcul():
	user = e.get()

	if user == str(gen_numb):
		result.config(text=f"👏🏻 {user}", fg="#09EE73")
		generate()

	else:
		result.config(text=f"invalid: {gen_numb}", fg="red")
		generate()

def generate():
	global gen_numb
	a = randint(1, 9)
	b = randint(1, 9)
	gen_numb = a * b
	cal.config(text=f"{a}*{b}")

def fiche():

	##### config 2e windows #####

	rev = Toplevel()
	rev.geometry("1024x756")
	rev.title('Fiche')
	rev.iconbitmap('mathx.ico')
	rev.resizable(width=False, height=False)

	##### Font #####

	table = Image.open("asset/table.png")
	resize_table = table.resize((1024, 756), Image.ANTIALIAS)
	new_table = ImageTk.PhotoImage(resize_table)

	tablefont = Label(rev, image=new_table, borderwidth=0)
	tablefont.pack()

	rev.mainloop()

##### Frame #####

frame_left = Frame(root)
frame_left.pack(side=LEFT)

frame_right = Frame(root)
frame_right.pack(side=RIGHT)

##### Label ##### 

title = Label(root, text="MathX training", font=(2))
title.pack(side=TOP)
version = Label(frame_left, text="v1.0", fg="red")
version.pack(side=TOP)
cal = Label(root, text="Calcul")
cal.pack(side=TOP)

##### Input ##### 

e = Entry(root)
e.pack()

##### Label ##### 

result = Label(root, text=" ")
result.pack(expand=YES)

##### Button #####

gen = Button(frame_right, text="  ↻  ", fg="#0035FE", font=(2), command=generate)
gen.pack()
valid = Button(frame_right, text="Valider", fg="#09EE73", command=calcul)
valid.pack()
note = Button(frame_left, text="fiche", fg="#FE7E00", command=fiche)
note.pack()

root.mainloop()