from tkinter import *             

import random

root = Tk()
root.geometry('400x400')
root.resizable(0, 0)
root.title('Rock,Paper,Scissors Game')
root.config(bg='pink')

Label(root, text='Rock, Paper, Scissor', font='arial 20 bold', bg='orange').pack()
user_take = StringVar()
Label(root, text='choose any one: rock, paper, scissor', font='arial 15 bold', bg='blue').place(x=20, y=70)
Entry(root, font='arial 15', textvariable=user_take, bg='antiquewhite2').place(x=70, y=130)

comp_pick = random.randint(1, 3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick == 2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'

Result = StringVar()


def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('tie, you both select same')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('you loose, computer select paper')
    elif user_pick == 'rock' and comp_pick == 'scissor':
        Result.set('you win, computer select scissor')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('you loose, computer choose rock')
    elif user_pick == 'paper' and comp_pick == 'scissor':
        Result.set('you loose, computer choose scissor')
    elif user_pick == 'scissor' and comp_pick == 'paper':
        Result.set('you win, computer choose paper')
    elif user_pick == 'scissor' and comp_pick == 'rock':
        Result.set('you loose, computer choose rock')
    else:
        Result.set('invalid : choose any one -- rock, paper, scissor')


def Reset():
    Result.set("")
    user_take.set("")


def Exit():
    root.destroy()


Entry(root, font='arial 10 bold', textvariable=Result, bg='antiquewhite2', width=50, ).place(x=25, y=250)

Button(root, font='arial 13 bold', text='PLAY', padx=5, bg='red', command=play).place(x=150, y=190)
Button(root, font='arial 13 bold', text='RESET', padx=5, bg='purple', command=Reset).place(x=70, y=310)
Button(root, font='arial 13 bold', text='EXIT', padx=5, bg='purple', command=Exit).place(x=230, y=310)

root.mainloop()