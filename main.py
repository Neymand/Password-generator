import tkinter as tk
from PIL import ImageTk, Image
import secrets
import pyperclip
import sql
import os

big_OR_mini = 0

win = tk.Tk()
win.title('Генератор паролей')
win.resizable(False, False)
frame1 = tk.Frame(win, width=165, height=330, bg='black')
frame1.pack(fill=tk.BOTH, expand=True)

# Icon
#icon = tk.PhotoImage(file='2023-07-20_23-29-25.png')
#win.iconphoto(False, icon)

userOK = 0  # Проверка был ли уже выполнен вход

""" Picture """

# Получение текущей директории
current_dir = os.getcwd()

# Ninja
imgNINJApath = os.path.join(current_dir, 'images', 'NinjaG.png')
imgFULL = Image.open(imgNINJApath)
image1 = ImageTk.PhotoImage(imgFULL)
background_label1 = tk.Label(frame1, image=image1)

# Systim Shock
img451_path = os.path.join(current_dir, 'images', 'systim shock panel.png')
img451 = Image.open(img451_path)
image2 = ImageTk.PhotoImage(img451)
background_label2 = tk.Label(frame1, image=image2)

# Anonimus
imgANONpath = os.path.join(current_dir, 'images', 'anon.png')
imgAN = Image.open(imgANONpath)
image3 = ImageTk.PhotoImage(imgAN)
background_label3 = tk.Label(frame1, image=image3)

def input_validation():
    length = str(length_var.get())

    if length == 'v':
        password = 'Anonymous'
        result_var.set(password)
        ester_egg2()
        return password

    if length.isdigit() == True:
        length = int(length)
    else:
        password = 'Enter an even number!'
        result_var.set(password)
        return password

    if length == 451:
        password = 'Shodan is watching'
        result_var.set(password)
        ester_egg()
        return password

    if length > 100:
        password = 'Too many characters!'
        result_var.set(password)
        return password

    config_password(length)


def config_password(length):
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    number = '1234567890'
    up_reg = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    symbols = "-=;'[],./~!@#$%^&*()_+{}|<>?"

    use_letters = letters_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()
    use_uppercase = uppercase_var.get()

    if use_uppercase + use_symbols + use_numbers + use_letters == 0:
        password = 'No marks!'
        result_var.set(password)
        return password

    combo = ''

    if use_letters:
        combo += letters
    if use_numbers:
        combo += number
    if use_symbols:
        combo += symbols
    if use_uppercase:
        combo += up_reg

    password = create_password(length, combo)
    result_var.set(password)


def set_mark():
    def close_window():
        child_window1.destroy()

    child_window1 = tk.Toplevel(win)
    child_window1.geometry('170x100')
    child_window1.resizable(False, False)
    child_window1.title('Lable')
    tk.Label(child_window1, text='Set the password label.', width=20, height=2).pack()

    # String
    makeMARK = tk.StringVar(value="")
    MARK_entry = tk.Entry(child_window1, textvariable=makeMARK)

    # Button
    btnMARK = tk.Button(child_window1, text='Enter', command=lambda: [save_password(makeMARK.get()), close_window()])
    MARK_entry.pack()
    btnMARK.pack()
    child_window1.grab_set()


def save_password(makeMARK):

    mark = makeMARK
    password = result_var.get()
    a = sql.add_data(mark, password)

    save_var.delete('1.0', tk.END)
    rows = sql.show_passwords()

    for row in rows:
        save_var.insert(tk.END, 'NAME: \t{} \nPASW: \t{} \nDATE: \t{} \n\n'.format(row[0], row[1], row[2]))
        if big_OR_mini == 1:
            save_var.pack()


def create_password(length, *args):
    password = ''
    for i in range(length):
        password += secrets.choice(''.join(args))
    result_var.set(password)
    return password

def copy_text():
    text = result_var.get()
    pyperclip.copy(text)


def resize_big():
    global big_OR_mini
    win.geometry('330x440')
    background_label1.place(x=0, y=0, relwidth=1, relheight=1)
    frame_s.pack(pady=1, padx=1)
    big_OR_mini = 1

    save_var.delete('1.0', tk.END)
    rows = sql.show_passwords()
    for row in rows:
        save_var.insert(tk.END, 'NAME: \t{} \nPASW: \t{} \nDATE: \t{} \n\n'.format(row[0], row[1], row[2]))
        save_var.pack()



def resize_mini():
    global big_OR_mini
    big_OR_mini = 0
    win.geometry('330x165')
    background_label1.place_forget()
    background_label2.place_forget()
    background_label3.place_forget()


def ester_egg():
    win.geometry('330x440')
    background_label2.place(x=0, y=0, relwidth=1, relheight=1)
    # Forget
    background_label1.place_forget()
    background_label3.place_forget()

def ester_egg2():
    win.geometry('330x440')
    background_label3.place(x=0, y=0, relwidth=1, relheight=1)
    # Forget
    background_label1.place_forget()
    background_label2.place_forget()

# Child Window
def open_auntification():
    #global enterCODE
    #global child_window

    child_window = tk.Toplevel(win)
    child_window.geometry('170x100')
    child_window.resizable(False, False)
    child_window.title('Login')
    tk.Label(child_window, text='Enter code word.', width=15, height=2).pack()

    # String
    enterCODE = tk.StringVar(value="")
    CODE_entry = tk.Entry(child_window, textvariable=enterCODE)

    def access_check():
        userkey = str(enterCODE.get())
        chek = sql.userkey_check(userkey)

        if chek == 1:
            resize_big()
            child_window.destroy()

    # Button
    btnCODE = tk.Button(child_window, text='Enter', command=access_check)
    CODE_entry.pack()
    btnCODE.pack()
    child_window.grab_set()


def reg_or_log():
    mean = sql.null_or_no()
    if mean == 0:
        open_reg_window()
    else:
        open_auntification()


def open_reg_window():
    global reg_window

    reg_window = tk.Toplevel(win)
    reg_window.geometry('200x160')
    reg_window.resizable(False, False)
    reg_window.title('Reg')

    # String registration

    YOU_CODE_entry = tk.Entry(reg_window, textvariable=enterYOU_CODE)

    YOU_CODE_entry2 = tk.Entry(reg_window, textvariable=enterYOU_CODE2)

    # Button for registration
    btnYOU_CODE = tk.Button(reg_window, text='Enter', command=reg_check)

    tk.Label(reg_window, text='Set your code word', width=20, height=2).pack()
    YOU_CODE_entry.pack()
    tk.Label(reg_window, text='Repeat', width=20, height=2).pack()
    YOU_CODE_entry2.pack()
    btnYOU_CODE.pack()
    reg_window.grab_set()


def reg_check():
    #global big_OR_mini
    key = str(enterYOU_CODE.get())
    key2 = str(enterYOU_CODE2.get())
    if key == key2:
        reg_window.destroy()
        sql.add_userkey(key)
        resize_big()





# Для окна регистрации
enterYOU_CODE = tk.StringVar(value="")
enterYOU_CODE2 = tk.StringVar(value="")


# Window save
frame_s = tk.Frame(win, borderwidth=10, relief=tk.SOLID, bg="black")
save_var = tk.Text(win, width=35, height=7, font="Aria")

label_name = tk.Label(win, text='MARK', bg='black', fg="white")
label_password = tk.Label(win, text='PASSWORD', bg='black', fg='white')
label_date = tk.Label(win, text='DATE', bg='black', fg='white')

# Quik MENU
main_menu = tk.Menu(win)
win.config(menu=main_menu)

r_menu = tk.Menu(main_menu)
main_menu.add_cascade(label='View', menu=r_menu)
r_menu.add_cascade(label='Full', command=reg_or_log)
r_menu.add_cascade(label='Mini', command=resize_mini)


# Количество
length_label = tk.Label(frame1, text="Password long:", bg='black', fg='white', width=15, height=2, font=('Aria', 15, 'bold'))
length_var = tk.StringVar(value="8")
length_entry = tk.Entry(frame1, textvariable=length_var)
length_entry.grid(row=0, column=1)
length_label.grid(row=0, column=0)

# Setting checkboxes
letters_var = tk.BooleanVar(value=True)
letters_check = tk.Checkbutton(frame1, text="Use letters", variable=letters_var, padx=10, pady=10, bg='black', fg='red', font=('Aria', 10, 'bold'))
letters_check.grid(row=3, column=0, sticky='w')

numbers_var = tk.BooleanVar(value=True)
numbers_check = tk.Checkbutton(frame1, text="Use numbers", variable=numbers_var, padx=10, pady=10, bg='black', fg='red', font=('Aria', 10, 'bold'))
numbers_check.grid(row=4, column=0, sticky='w')

symbols_var = tk.BooleanVar(value=True)
synbols_check = tk.Checkbutton(frame1, text="Use symbols", variable=symbols_var, padx=10, pady=10, bg='black', fg='red', font=('Aria', 10, 'bold'))
synbols_check.grid(row=3, column=1, sticky='w')

uppercase_var = tk.BooleanVar(value=True)
uppercase_check = tk.Checkbutton(frame1, text="Use uppercase", variable=uppercase_var, padx=10, pady=10, bg='black', fg='red', font=('Aria', 10, 'bold'))
uppercase_check.grid(row=4, column=1, sticky='w')

# Generate Button
btn1 = tk.Button(frame1, text='Gen', command=input_validation, padx=20, pady=0)
btn1.grid(row=1, column=0, sticky='w')

# Copy Button
btn2 = tk.Button(frame1, text='Copy', command=copy_text, padx=17, pady=0)
btn2.grid(row=1, column=0, sticky='e')

# Save Button
btn3 = tk.Button(frame1, text='Save', command=set_mark, padx=0, pady=0)
btn3.grid(row=1, column=0)

# Password field
result_var = tk.StringVar(value="")
result_entry = tk.Entry(frame1, textvariable=result_var)
result_entry.grid(row=1, column=1)



win.mainloop()



