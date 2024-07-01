from tkinter import *
import base64
from tkinter import messagebox
import tkinter.font as font

# Encoding Function
def encode(key, msg):
    enc = []
    for i in range(len(msg)):
        list_key = key[i % len(key)]
        list_enc = chr((ord(msg[i]) + ord(list_key)) % 256)
        enc.append(list_enc)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

# Decoding Function
def decode(key, code):
    dec = []
    enc = base64.urlsafe_b64decode(code).decode()
    for i in range(len(enc)):
        list_key = key[i % len(key)]
        list_dec = chr((256 + ord(enc[i]) - ord(list_key)) % 256)
        dec.append(list_dec)
    return "".join(dec)

# Function that executes on clicking Show Message function
def Result():
    msg = Message.get()
    k = key.get()
    i = mode.get()
    if i == 1:
        Output.set(encode(k, msg))
    elif i == 2:
        Output.set(decode(k, msg))
    else:
        messagebox.showinfo('', 'Please choose either Encryption or Decryption. Try again.')

# Function that executes on clicking Reset function
def Reset():
    Message.set("")
    key.set("")
    mode.set(0)
    Output.set("")

# Function to toggle key visibility
def toggle_key_visibility():
    if key_entry.cget('show') == '*':
        key_entry.config(show='')
    else:
        key_entry.config(show='*')

wn = Tk()
wn.geometry("500x400")
wn.configure(bg='lightblue')
wn.title("Text Encryption and Decryption")

Message = StringVar()
key = StringVar()
mode = IntVar()
Output = StringVar()

headingFrame1 = Frame(wn, bg="lightgray", bd=5)
headingFrame1.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

headingLabel = Label(headingFrame1, text="Encryption and Decryption System", fg='black', font=('Courier', 13, 'bold'))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

main_frame = Frame(wn, bg='lightblue')
main_frame.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.7)

label1 = Label(main_frame, text='Enter the Message:', font=('Courier', 10), bg='lightblue')
label1.grid(row=0, column=0, pady=10, padx=10, sticky=E)

msg = Entry(main_frame, textvariable=Message, width=35, font=('calibre', 10, 'normal'))
msg.grid(row=0, column=1, pady=10, padx=10)

label2 = Label(main_frame, text='Enter the Key:', font=('Courier', 10), bg='lightblue')
label2.grid(row=1, column=0, pady=10, padx=10, sticky=E)

key_entry = Entry(main_frame, textvariable=key, width=35, font=('calibre', 10, 'normal'), show='*')
key_entry.grid(row=1, column=1, pady=10, padx=10)

toggle_btn = Button(main_frame, text='Show/Hide Key', command=toggle_key_visibility)
toggle_btn.grid(row=1, column=2, padx=10)

label3 = Label(main_frame, text='Choose Mode:', font=('Courier', 10), bg='lightblue')
label3.grid(row=2, column=0, pady=10, padx=10, sticky=E)

Radiobutton(main_frame, text='Encrypt', variable=mode, value=1, bg='lightblue').grid(row=2, column=1, pady=10, padx=10, sticky=W)
Radiobutton(main_frame, text='Decrypt', variable=mode, value=2, bg='lightblue').grid(row=2, column=1, pady=10, padx=10, sticky=E)

label4 = Label(main_frame, text='Result:', font=('Courier', 10), bg='lightblue')
label4.grid(row=3, column=0, pady=10, padx=10, sticky=E)

res = Entry(main_frame, textvariable=Output, width=35, font=('calibre', 10, 'normal'))
res.grid(row=3, column=1, pady=10, padx=10)

ShowBtn = Button(main_frame, text="Show Message", bg='lavender', fg='black', width=15, height=1, command=Result)
ShowBtn['font'] = font.Font(size=12)
ShowBtn.grid(row=4, column=1, pady=10, padx=10, sticky=E)

ResetBtn = Button(main_frame, text='Reset', bg='lightgreen', fg='black', width=15, height=1, command=Reset)
ResetBtn['font'] = font.Font(size=12)
ResetBtn.grid(row=4, column=0, pady=10, padx=10, sticky=E)

QuitBtn = Button(main_frame, text='Exit', bg='lightcoral', fg='black', width=15, height=1, command=wn.destroy)
QuitBtn['font'] = font.Font(size=12)
QuitBtn.grid(row=4, column=2, pady=10, padx=10)

wn.mainloop()
