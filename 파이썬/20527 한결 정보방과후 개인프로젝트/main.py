import tkinter as tk
import random as rd

gameMenuList=["*공격","*행동","*창고","*도망"]
gameMenuNum=0
fnt = ("맑은 고딕 Semilight", 15)
fnt2 = ("맑은 고딕 Semilight", 20)
colorList=["white","black"]     #[0] 하양 [1] 검정
phase=0
myHP=100
enemyHP=100
#storage=["



def gameMenuselect1():
    global gameMenuNum
    gameMenuNum=1
    if phase==1:
        gameMenuLabel1["bg"]=colorList[0]
        gameMenuLabel1["fg"]=colorList[1]
        gameMenuLabel2["bg"]=colorList[1]
        gameMenuLabel2["fg"]=colorList[0]
        gameMenuLabel3["bg"]=colorList[1]
        gameMenuLabel3["fg"]=colorList[0]
        gameMenuLabel4["bg"]=colorList[1]
        gameMenuLabel4["fg"]=colorList[0]
def gameMenuselect2():
    global gameMenuNum
    gameMenuNum=2
    if phase==1:
        gameMenuLabel1["bg"]=colorList[1]
        gameMenuLabel1["fg"]=colorList[0]
        gameMenuLabel2["bg"]=colorList[0]
        gameMenuLabel2["fg"]=colorList[1]
        gameMenuLabel3["bg"]=colorList[1]
        gameMenuLabel3["fg"]=colorList[0]
        gameMenuLabel4["bg"]=colorList[1]
        gameMenuLabel4["fg"]=colorList[0]
def gameMenuselect3():
    global gameMenuNum
    gameMenuNum=3
    if phase==1:
        gameMenuLabel1["bg"]=colorList[1]
        gameMenuLabel1["fg"]=colorList[0]
        gameMenuLabel2["bg"]=colorList[1]
        gameMenuLabel2["fg"]=colorList[0]
        gameMenuLabel3["bg"]=colorList[0]
        gameMenuLabel3["fg"]=colorList[1]
        gameMenuLabel4["bg"]=colorList[1]
        gameMenuLabel4["fg"]=colorList[0]
def gameMenuselect4():
    global gameMenuNum
    if phase==1:
        gameMenuNum=4
        gameMenuLabel1["bg"]=colorList[1]
        gameMenuLabel1["fg"]=colorList[0]
        gameMenuLabel2["bg"]=colorList[1]
        gameMenuLabel2["fg"]=colorList[0]
        gameMenuLabel3["bg"]=colorList[1]
        gameMenuLabel3["fg"]=colorList[0]
        gameMenuLabel4["bg"]=colorList[0]
        gameMenuLabel4["fg"]=colorList[1]
def gameMenuUnavaliable():
    gameQuestionLabel["bg"]=colorList[1]
    gameQuestionLabel["fg"]=colorList[1]
    gameMenuLabel1["bg"]=colorList[1]
    gameMenuLabel1["fg"]=colorList[1]
    gameMenuLabel2["bg"]=colorList[1]
    gameMenuLabel2["fg"]=colorList[1]
    gameMenuLabel3["bg"]=colorList[1]
    gameMenuLabel3["fg"]=colorList[1]
    gameMenuLabel4["bg"]=colorList[1]
    gameMenuLabel4["fg"]=colorList[1]
def gameMenuKeypress(e):
    global phase, colorList
    key=e.keysym
    if phase==0 and key=="space":
        phase+=1
        gameStartLabel1["text"]=""
        gameStartLabel2["text"]=""
        gameQuestionLabel["fg"]=colorList[0]
        gameMenuselect1()
    elif key=="Down" and gameMenuNum==1 and phase==1:
        gameMenuselect3()
    elif key=="Down" and gameMenuNum==2 and phase==1:
        gameMenuselect4()
    elif key=="Up" and gameMenuNum==3 and phase==1:
        gameMenuselect1()
    elif key=="Up" and gameMenuNum==4 and phase==1:
        gameMenuselect2()
    elif key=="Left" and gameMenuNum==2 and phase==1:
        gameMenuselect1()
    elif key=="Left" and gameMenuNum==4 and phase==1:
        gameMenuselect3()
    elif key=="Right" and gameMenuNum==1 and phase==1:
        gameMenuselect2()
    elif key=="Right" and gameMenuNum==3 and phase==1:
        gameMenuselect4()
    elif key=="enter" and phase==1:
        if gameMenuNum==1:
            #gameAttack()
            pass
        elif gameMenuNum==2:
            #gameMove()
            pass
        elif gameMenuNum==3:
            #gameInv()
            pass
        elif gameMenuNum==4:
            #gameFlee()
            pass
    else:
        pass

'''
def gameAttack():
    gameMenuUnavaliable()
    canvas.create_text(
def gameMove():
    gameMenuUnavaliable()
def gameInv():
    gameMenuUnavaliable()
def gameFlee():
    gameMenuUnavaliable()
#class charEnemy1():
#class charEnemy2():

'''

def main():
    gameMenuUnavaliable()

    
root=tk.Tk()
root.title("쯔꾸르게임")
root.geometry("720x540")
root.resizable(False,False)
root.bind("<KeyPress>",gameMenuKeypress,)
canvas=tk.Canvas(root,width=720,height=540,bg="black")
canvas.pack()

canvas.create_rectangle(0,350,720,360,fill="white")





gameQuestionLabel=tk.Label(text="무엇을 하시겠습니까?",font=fnt2,bg="black",fg="white")
gameQuestionLabel.place(x=50,y=420)
gameMenuLabel1=tk.Label(text=gameMenuList[0],font=fnt,fg="white",bg="black")
gameMenuLabel1.place(x=400,y=400)
gameMenuLabel2=tk.Label(text=gameMenuList[1],font=fnt,fg="white",bg="black")
gameMenuLabel2.place(x=550,y=400)
gameMenuLabel3=tk.Label(text=gameMenuList[2],font=fnt,fg="white",bg="black")
gameMenuLabel3.place(x=400,y=460)
gameMenuLabel4=tk.Label(text=gameMenuList[3],font=fnt,fg="white",bg="black")
gameMenuLabel4.place(x=550,y=460)

gameStartLabel1=tk.Label(text="앗! 야생의 리유니온 병사들이 나타났다!",font=fnt2,bg="black",fg="white")
gameStartLabel1.place(x=50,y=420)
gameStartLabel2=tk.Label(text="Spacebar를 눌러 시작",font=fnt,bg="black",fg="white")
gameStartLabel2.place(x=50,y=460)

charMeImg=[tk.PhotoImage(file="기본.png"),
                tk.PhotoImage(file="공격1.gif"),
                tk.PhotoImage(file="공격2.png"),
                tk.PhotoImage(file="공격3.png"),
                tk.PhotoImage(file="섭취.png"),
                tk.PhotoImage(file="피격.png")
                ]

main()
root.mainloop()
