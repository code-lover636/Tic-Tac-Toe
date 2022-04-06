# IMPORTS
from tkinter import *
from tkinter import messagebox

count = 0
b = []
root = Tk()
root.title('TIC TAC TOE ')


# CREATING LABELS
label1 = Label(root, text='PLAYER 1:X', fg='blue', bg='grey', font=('gabriola', 15, 'normal'))
label1.grid(row=0, column=0)
label2 = Label(root, text='PLAYER 2:O', fg='black', bg='white', font=('gabriola', 15, 'normal'))
label2.grid(row=0, column=1)


# CREATING FUNCTIONS FOR BUTTONS
def refresh():
    global count, b
    but1.config(text=" ", state='normal', bg='Black')
    but2.config(text=" ", state='normal', bg='Black')
    but3.config(text=" ", state='normal', bg='Black')
    but4.config(text=" ", state='normal', bg='Black')
    but5.config(text=" ", state='normal', bg='Black')
    but6.config(text=" ", state='normal', bg='Black')
    but7.config(text=" ", state='normal', bg='Black')
    but8.config(text=" ", state='normal', bg='Black')
    but9.config(text=" ", state='normal', bg='Black')
    count = 0
    b = []
    label1.config(fg='blue', bg='grey')
    label2.config(fg='black', bg='white')


def undo():
    global b, count, last
    if len(b) > 0:
        last = b[-1]
        last.config(text=" ", state='normal')
        count -= 1
        if len(b) >= 1:
            label1['fg'], label2['fg'] = label2['fg'], label1['fg']
            label1['bg'], label2['bg'] = label2['bg'], label1['bg']
        b.pop()


def click(button):
    global count, b
    b.append(button)
    if count % 2 == 0:
        label2.config(fg='blue', bg='grey')
        label1.config(fg='black', bg='white')
        symbol = button["text"] = "X"
        button['state'] = 'disabled'
        count += 1
    elif count % 2 != 0:
        label1.config(fg='blue', bg='grey')
        label2.config(fg='black', bg='white')
        symbol = button["text"] = "O"
        button['state'] = 'disabled'
        count += 1
    if but1['text'] == but2['text'] == but3['text'] == button['text']:
        but1['bg'] = but2['bg'] = but3['bg'] = 'red'
        messagebox.showinfo('congratulations', f"congrats!!!\n{button['text']} won the game")
        refresh()
    elif but4['text'] == but5['text'] == but6['text'] == button['text']:
        but4['bg'] = but5['bg'] = but6['bg'] = 'red'
        messagebox.showinfo('congratulations', f"congrats!!!\n{button['text']} won the game")
        refresh()
    elif but7['text'] == but8['text'] == but9['text'] == button['text']:
        but7['bg'] = but8['bg'] = but9['bg'] = 'red'
        messagebox.showinfo('congratulations', f"congrats!!!\n{button['text']} won the game")
        refresh()
    elif but1['text'] == but4['text'] == but7['text'] == button['text']:
        but1['bg'] = but4['bg'] = but7['bg'] = 'red'
        messagebox.showinfo('congratulations', f"congrats!!!\n{button['text']} won the game")
        refresh()
    elif but2['text'] == but5['text'] == but8['text'] == button['text']:
        but2['bg'] = but5['bg'] = but8['bg'] = 'red'
        messagebox.showinfo('congratulations', f"congrats!!!\n{button['text']} won the game")
        refresh()
    elif but3['text'] == but6['text'] == but9['text'] == button['text']:
        but3['bg'] = but6['bg'] = but9['bg'] = 'red'
        messagebox.showinfo('congratulations', f"congrats!!!\n{button['text']} won the game")
        refresh()
    elif but1['text'] == but5['text'] == but9['text'] == button['text']:
        but1['bg'] = but5['bg'] = but9['bg'] = 'red'
        messagebox.showinfo('congratulations', f"congrats!!!\n{button['text']} won the game")
        refresh()
    elif but3['text'] == but5['text'] == but7['text'] == button['text']:
        but3['bg'] = but5['bg'] = but7['bg'] = 'red'
        messagebox.showinfo('congratulations', f"congrats!!!\n{button['text']} won the game")
        refresh()
    elif len(b) == 9:
        messagebox.showinfo('no one wins', f"     TIE!!!\n no one won the game")
        refresh()


def exit_file():
    msg1 = messagebox.askquestion('tic tac toe', 'Are you sure you want to exit?')
    if msg1 == "yes":
        root.quit()


# creating menu
menu_bar = Menu(root)
root.config(menu=menu_bar)
filemenu = Menu(menu_bar)
filemenu.add_command(label="new game", command=refresh)
filemenu.add_separator()
filemenu.add_command(label="Undo", command=undo)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_file)
menu_bar.add_cascade(label="▼", menu=filemenu)

num = 13

# CREATING BUTTONS
but1 = Button(root, text=" ", command=lambda: click(but1), padx=50, pady=50, fg='white', bg='black', font=('Consolas', num, 'bold'))
but1.grid(row=1, column=0)
but2 = Button(root, text=" ", command=lambda: click(but2), padx=50, pady=50, fg='white', bg='black', font=('Consolas', num, 'bold'))
but2.grid(row=1, column=1)
but3 = Button(root, text=" ", command=lambda: click(but3), padx=50, pady=50, fg='white', bg='black', font=('Consolas', num, 'bold'))
but3.grid(row=1, column=2)
but4 = Button(root, text=" ", command=lambda: click(but4), padx=50, pady=50, fg='white', bg='black', font=('Consolas', num, 'bold'))
but4.grid(row=2, column=0)
but5 = Button(root, text=" ", command=lambda: click(but5), padx=50, pady=50, fg='white', bg='black', font=('Consolas', num, 'bold'))
but5.grid(row=2, column=1)
but6 = Button(root, text=" ", command=lambda: click(but6), padx=50, pady=50, fg='white', bg='black', font=('Consolas', num, 'bold'))
but6.grid(row=2, column=2)
but7 = Button(root, text=" ", command=lambda: click(but7), padx=50, pady=50, fg='white', bg='black', font=('Consolas', num, 'bold'))
but7.grid(row=3, column=0)
but8 = Button(root, text=" ", command=lambda: click(but8), padx=50, pady=50, fg='white', bg='black', font=('Consolas', num, 'bold'))
but8.grid(row=3, column=1)
but9 = Button(root, text=" ", command=lambda: click(but9), padx=50, pady=50, fg='white', bg='black', font=('Consolas', num, 'bold'))
but9.grid(row=3, column=2)

root.mainloop()
