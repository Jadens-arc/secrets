import tkinter as tk # GUI
from crypt import PyCrypt

# declare root window w/ geometry and name
root = tk.Tk()
root.geometry('500x200')
root.title('Shhh')
root.config(bg='black')

def login(sender=None):
    myCrypt = PyCrypt('logs.json', password=passwordField.get())
    
    logWin = tk.Tk()
    logWin.geometry('500x600')
    logWin.title('Hey You Got In :)')
    logWin.config(bg='black')

    textBox = tk.Text(logWin, bg='black', fg='green',
                      highlightbackground='green', font='Helvetica 22')
    textBox.place(relx=0, rely=0, relwidth=1, relheight=1)

    logs = myCrypt.getAll()
    for log in logs:
        textBox.insert(tk.END, '• ' + log + '\n')

    textBox.config(state=tk.DISABLED)
    
    logWin.mainloop()


passwordField = tk.Entry(root, font='Helvetica 22', show='*')
passwordField.config(bg='black', fg='green', highlightbackground='green')
passwordField.place(relx=0.1, rely=0.1, relheight=0.2, relwidth=0.8)
passwordField.bind('<Return>', login)

loginBtn = tk.Button(root, text="Login",font='Helvetica 22 bold', command=login)
loginBtn.config(bg='black', fg='green', highlightbackground='green')
loginBtn.place(relx=0.2, rely=0.4, relheight=0.2, relwidth=0.6)

root.mainloop()
