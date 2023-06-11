import os
import qrcode
from tkinter import *
from tkinter import filedialog
def qrcode_creating():
    path = filedialog.askdirectory()
    folder_path.set(path)
    file_name = name_file_entry.get()
    os.chdir(path)
    data = data_entry.get()
    img = qrcode.make(data)
    type(img)
    img.save(f"{file_name}.png")

root = Tk()
folder_path = StringVar()
root.title('QR Creator')
root.geometry('400x120')

data_entry_label = Label(text='Enter text, from what you wanna made  qr code')
data_entry_label.place(x = 10, y = 5)
data_entry = Entry()
data_entry.place(x=10, y= 35, width=200)
name_file_label = Label(text = 'Enter the name of the file')
name_file_label.place(x = 10, y = 60)
name_file_entry = Entry()
name_file_entry.place(x = 10, y = 80)
save_button = Button(text = 'Create QR', command = qrcode_creating)
save_button.place(x = 230, y = 55)

root.mainloop()