from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '?', '*', ',', '.']


# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_pass():
    website = in1.get()
    try:
        with open("passwords.json", 'r') as pass_file:
            data = json.load(pass_file)
        email = data[website]['email']
        password = data[website]['password']
    except FileNotFoundError:
        messagebox.showerror('info request', "No information is saved yet")
    except KeyError:
        messagebox.showerror('info request', f'Website "{website}" not found')
    else:
        pyperclip.copy(password)
        in3.delete(0, END)
        in3.insert(0, password)
        messagebox.showinfo('info request', f'website: {website}\nEmail:{email}\nPassword: {password}\nPassword copied')


def gene_pass():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 3)
    nr_numbers = random.randint(2, 3)

    paa = [random.choice(letters) for _ in range(nr_letters)]
    paa.extend([random.choice(numbers) for _ in range(nr_numbers)])
    paa.extend([random.choice(symbols) for _ in range(nr_symbols)])
    random.shuffle(paa)

    new = ''.join(paa)
    pyperclip.copy(new)
    in3.delete(0, END)
    in3.insert(0, new)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    website = in1.get()
    email = in2.get()
    password = in3.get()

    new_data = {
        website: {
            "email": email,
            'password': password
        }
    }

    if len(in1.get()) == 0 or len(in2.get()) == 0 or len(in3.get()) == 0:
        messagebox.showerror('Error', 'Some entries are empty.\nInfo is not saved.')
        return

    try:
        with open("passwords.json", 'r') as pass_file:
            data = json.load(pass_file)
            data.update(new_data)
    except FileNotFoundError:
        with open("passwords.json", 'w') as pass_file:
            json.dump(new_data, pass_file, indent=4)
    else:
        with open("passwords.json", 'w') as pass_file:
            json.dump(data, pass_file, indent=4)
    in1.delete(0, END)
    in3.delete(0, END)

    messagebox.showinfo('Saved', 'Your information is saved successfully, and copied.')


# ---------------------------- UI SETUP ------------------------------- #
wind = Tk()
wind.title('Password Manager')
wind.config(padx=50, pady=50)

canv = Canvas(width=200, height=200)
img = PhotoImage(file='logo.png')
canv.create_image(100, 100, image=img)
canv.grid(column=1, row=0)

lab1 = Label(text='Website:')
lab2 = Label(text='Email/UserName:')
lab3 = Label(text="Password:")
lab1.grid(column=0, row=1)
lab2.grid(column=0, row=2)
lab3.grid(column=0, row=3)

in1 = Entry(width=33)
in2 = Entry(width=52)
in3 = Entry(width=33)
add_button = Button(text='Add', width=27, command=save_info)
in1.grid(column=1, row=1)
in2.grid(column=1, row=2, columnspan=2)
in2.insert(END, string="my_email@gmail.com")
in3.grid(column=1, row=3)
add_button.grid(column=1, row=4)
in1.focus()

# create generate button
gene_button = Button(text='Generate Password', command=gene_pass)
gene_button.grid(column=2, row=3)

search_button = Button(text='Search Password', width=14, command=search_pass)
search_button.grid(column=2, row=1)


wind.mainloop()
