import tkinter as tk
import random as rd

gameMenuList=["*공격","*행동","*창고","*도망"]
gameMenuNum=0
fnt = ("맑은 고딕 Semilight", 15)
fnt2 = ("맑은 고딕 Semilight", 20)
colorList=["white","black"]     #[0] 하양 [1] 검정
labelFG1=""
labelFG2=""
labelFG3=""
labelFG4=""
labelBG1=""
labelBG2=""
labelBG3=""
labelBG4=""


def gameMenuKeypress(e):
    key=e.keysym
    if key=="Down" and gameMenuNum==1:
        gameMenuNum=3
    elif key=="Down" and gameMenuNum==2:
        gameMenuNum=4
    elif key=="Up" and gameMenuNum==3:
        gameMenuNum=1
    elif key=="Up" and gameMenuNum==4:
        gameMenuNum=2
    elif key=="Left" and gameMenuNum==2:
        gameMenuNum=1
    elif key=="Left" and gameMenuNum==4:
        gameMenuNum=3
    elif key=="Right" and gameMenuNum==1:
        gameMenuNum=2
    elif key=="Right" and gameMenuNum==3:
        gameMenuNum=4
    else:
        pass

        
#class charEnemy1():
#class charEnemy2():



def main():
    pass

def gameMenuselect1():
    global gameMenuNum, labelFG1, labelFG2, labelFG3, labelFG4, labelBG1, labelBG2, labelBG3, labelBG4, colorList
    gameMenuNum=1
    labelFG1=colorList[1]
    labelFG2=colorList[0]
    labelFG3=colorList[0]
    labelFG4=colorList[0]
    labelBG1=colorList[1]
    labelBG2=colorList[0]
    labelBG3=colorList[0]
    labelBG4=colorList[0]
def gameMenuselect2():
    gameMenuNum=2
    labelFG1=colorList[0]
    labelFG2=colorList[1]
    labelFG3=colorList[0]
    labelFG4=colorList[0]
    labelBG1=colorList[0]
    labelBG2=colorList[1]
    labelBG3=colorList[0]
    labelBG4=colorList[0]
def gameMenuselect3():
    gameMenuNum=3
    labelFG1=colorList[0]
    labelFG2=colorList[0]
    labelFG3=colorList[1]
    labelFG4=colorList[0]
    labelBG1=colorList[0]
    labelBG2=colorList[0]
    labelBG3=colorList[1]
    labelBG4=colorList[0]
def gameMenuselect4():
    gameMenuNum=4
    labelFG1=colorList[0]
    labelFG2=colorList[0]
    labelFG3=colorList[0]
    labelFG4=colorList[1]
    labelBG1=colorList[0]
    labelBG2=colorList[0]
    labelBG3=colorList[0]
    labelBG4=colorList[1]
    
root=tk.Tk()
root.title("쯔꾸르게임")
root.geometry("720x540")
root.resizable(False,False)
root.bind("<KeyPress>",gameMenuKeypress)
canvas=tk.Canvas(root,width=720,height=540,bg="black")
canvas.pack()

canvas.create_rectangle(0,350,720,360,fill="white")

gameQuestionLabel=tk.Label(text="무엇을 하시겠습니까?",font=fnt2,bg="black",fg="white")
gameQuestionLabel.place(x=50,y=420)

gameMenuLabel1=tk.Label(text=gameMenuList[0],font=fnt,fg=labelFG1,bg=labelBG1)
gameMenuLabel1.place(x=400,y=400)
gameMenuLabel2=tk.Label(text=gameMenuList[1],font=fnt,fg=labelFG2,bg=labelBG2)
gameMenuLabel2.place(x=550,y=400)
gameMenuLabel3=tk.Label(text=gameMenuList[2],font=fnt,fg=labelFG3,bg=labelBG3)
gameMenuLabel3.place(x=400,y=460)
gameMenuLabel4=tk.Label(text=gameMenuList[3],font=fnt,fg=labelFG4,bg=labelBG4)
gameMenuLabel4.place(x=550,y=460)


charMeImg=[tk.PhotoImage(file="공격1.gif"),
                tk.PhotoImage(file="공격2.png"),
                tk.PhotoImage(file="공격3.png"),
                tk.PhotoImage(file="기본.png"),
                tk.PhotoImage(file="섭취.png"),
                tk.PhotoImage(file="피격.png")
                ]

main()
root.mainloop()
