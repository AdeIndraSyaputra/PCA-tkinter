from tkinter import*
from PIL import ImageTk,Image
from tkinter import filedialog


root = Tk()
root.title('Belajar Tkinter')

root.filename = filedialog.askopenfilename(initialdir="/gui/images", title="Select A File", filetypes=(("jpg file", " *.jpg"),("all files", "*.*")))
my_label = Label(root, text=root.filename).pack()



root.mainloop()

