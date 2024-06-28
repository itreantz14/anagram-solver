from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import data

root = Tk()
root.title("Frenzy Anagram Solver")

def getx():
	listbox.delete(0,END)
	if(len(entf2_1st.get())>2):
		try:
			for i in data.useAnagram(entf2_1st.get()):
				listbox.insert(END,i)
		except:
			pass
	else:
		messagebox.showwarning("Warning","3 characters up only")

frame1 = Frame(root)
loadImg = ImageTk.PhotoImage(Image.open("images/title.png"))
lblf1_1st = Label(frame1, image=loadImg)
lblf1_1st.grid(row=0,column=0)

frame2 = Frame(root)
lblf2_1st = Label(frame2, text="Starts with :", font="Roboto 25")
lblf2_1st.grid(row=0, column=0)

entf2_1st = Entry(frame2, text="3", width=20, font="Roboto 30")
entf2_1st.grid(row=1, column=0, padx=20)

btnf2_1st = Button(frame2, text="Swish", font="Roboto 20",
                   command=lambda: getx())

btnf2_1st.grid(row=2, column=0, pady=10)

frame3 = Frame(root)

listbox = Listbox(frame3, font="Roboto 20", bg="#10afb2")
listbox.pack(side=LEFT, fill=BOTH, pady=10)

scrollx = Scrollbar(frame3)
scrollx.pack(side=RIGHT, fill=BOTH)

scrollx.config(command=listbox.yview)
listbox.config(yscrollcommand=scrollx.set)

frame1.pack()
frame2.pack()
frame3.pack()

root.mainloop()
