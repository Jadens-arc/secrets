import tkinter as tk # GUI
from crypt import PyCrypt

# declare root window w/ geometry and name
root = tk.Tk()
root.geometry('500x200')
root.title('Shhh')
root.config(bg='black')

def add(password, logWin):
    myCrypt = PyCrypt('logs.json', password=password)
    addWin = tk.Tk()
    addWin.geometry('500x600')
    addWin.title('Hey You Got In :)')
    addWin.config(bg='black')

    textBox = tk.Text(addWin, font='Helvetica 13')
    textBox.config(bg='black', fg='green', highlightbackground='green')
    textBox.place(relx=0.1, rely=0.1, relheight=0.7, relwidth=0.8)

    def save():
        myCrypt.append(textBox.get(1.0, tk.END))
        addWin.destroy()        

    saveBtn = tk.Button(addWin, text="Save",font='Helvetica 22 bold', command=save)
    saveBtn.config(bg='black', fg='green', highlightbackground='green')
    saveBtn.place(relx=0.2, rely=0.85, relheight=0.1, relwidth=0.6)


    addWin.mainloop()


def login(sender=None):
    password = passwordField.get()
    myCrypt = PyCrypt('logs.json', password=password)
    
    logWin = tk.Tk()
    logWin.geometry('500x600')
    logWin.title('Hey You Got In :)')
    logWin.config(bg='black')

    textBox = tk.Text(logWin, bg='black', fg='green', highlightbackground='green', font='Helvetica 22')
    textBox.place(relx=0, rely=0, relwidth=1, relheight=1)

    logs = myCrypt.getAll()
    for log in logs:
        textBox.insert(tk.END, ' > ' + log + '\n')

    textBox.config(state=tk.DISABLED)

    menuBar = tk.Menu(logWin)
    menuBar.add_command(label="Add", command=lambda: add(password, logWin))
    menuBar.add_command(label="Remove")
    menuBar.add_command(label="Edit")
    menuBar.add_command(label="Logout", command=lambda: logWin.destroy())
    logWin.config(menu=menuBar)

    logWin.mainloop()


passwordField = tk.Entry(root, font='Helvetica 22', show='*')
passwordField.config(bg='black', fg='green', highlightbackground='green')
passwordField.place(relx=0.1, rely=0.1, relheight=0.3, relwidth=0.8)
passwordField.bind('<Return>', login)

loginBtn = tk.Button(root, text="Login",font='Helvetica 22 bold', command=login)
loginBtn.config(bg='black', fg='green', highlightbackground='green')
loginBtn.place(relx=0.2, rely=0.5, relheight=0.2, relwidth=0.6)

root.mainloop()
