import tkinter as tk
import random as rd
gameMenuNum=0

gameMenuList=["공격","행동","창고","도망"]
fnt = ("맑은 고딕 Semilight", 20)

class charMe():         #자기자신
    def charMeKeypress(e):
        key=e.keysym
        if key=="Down" and gameMenuNum=1:
            gameMenuNum=3
        elif key=="Down" and gameMenuNum=2:
            gameMenuNum=4
        elif key=="Up" and gameMenuNum=3:
            gameMenuNum=1
        elif key=="Up" and gameMenuNum=4:
            gameMenuNum=2
        elif key=="Left" and gameMenuNum=2:
            gameMenuNum=1
        elif key=="Left" and gameMenuNum=4
            gameMenuNum=3
        elif key=="Right" and gameMenuNum=1:
            gameMenuNum=2
        elif key=="Right" and gameMenuNum=3:
            gameMenuNum=4
        else:
            pass

class charEnemy1():
class charEnemy2():



def main():
    pass

root=tk.Tk()
root.title("쯔꾸르게임")
root.geometry("720x540")
root.resizable(False,False)
root.bind("<KeyPress>", charMe.charMeKeypress)
canvas=tk.Canvas(root,width=720,height=540,bg="black")
canvas.pack()

charMeImg=[tk.PhotoImage(file="공격1.gif"),
                tk.PhotoImage(file="공격2.png"),
                tk.PhotoImage(file="공격3.png"),
                tk.PhotoImage(file="기본.png"),
                tk.PhotoImage(file="섭취.png"),
                tk.PhotoImage(file="피격.png")
                ]

main()
root.mainloop()
