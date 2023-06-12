import os
import qrcode
from tkinter import *
from tkinter import filedialog

def qrcode_creating():
    global qrcode
    global qr_flag
    path = filedialog.asksaveasfilename(filetypes=(('PNG File', '*.png'), ('All files', '*.*')))
    path_split = path.split('/')
    filename = path_split[-1]
    path_split.pop(-1)
    new_path = '/'.join(path_split)
    os.chdir(new_path)
    data = data_entry.get()
    img = qrcode.make(data)
    type(img)
    img.save(f"{filename}.png")
root = Tk()
root.title('QR Creator')
root.geometry('400x120')
root.resizable(width=False, height=False)

data_entry_label = Label(text='Enter the text you want to make a qr code from')
data_entry_label.place(x = 10, y = 5)
data_entry = Entry()
data_entry.place(x=10, y= 35, width=200)
save_button = Button(text = 'Create QR', command = qrcode_creating)
save_button.place(x = 230, y = 32)
root.mainloop()