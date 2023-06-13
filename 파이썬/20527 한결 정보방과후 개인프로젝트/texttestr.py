import tkinter as tk

gameMenuList=["*공격","*행동","*창고","*도망"]
gameMenuNum=0
fnt = ("맑은 고딕 Semilight", 15)
fnt2 = ("맑은 고딕 Semilight", 20)
labelFG="white"     #폰트
labelBG="black"     #배경

root=tk.Tk()
root.title("쯔꾸르게임")
root.geometry("720x540")
root.resizable(False,False)

canvas=tk.Canvas(root,width=720,height=540,bg="black")
canvas.pack()

canvas.create_rectangle(0,350,720,360,fill="white")

gameQuestionLabel=tk.Label(text="무엇을 하시겠습니까?",font=fnt2,bg="black",fg=labelFG)
gameQuestionLabel.place(x=50,y=420)

gameMenuLabel1=tk.Label(text=gameMenuList[0],font=fnt,fg=labelFG,bg=labelBG)
gameMenuLabel1.place(x=400,y=400)
gameMenuLabel2=tk.Label(text=gameMenuList[1],font=fnt,fg=labelFG,bg=labelBG)
gameMenuLabel2.place(x=550,y=400)
gameMenuLabel3=tk.Label(text=gameMenuList[2],font=fnt,fg=labelFG,bg=labelBG)
gameMenuLabel3.place(x=400,y=460)
gameMenuLabel4=tk.Label(text=gameMenuList[3],font=fnt,fg=labelFG,bg=labelBG)
gameMenuLabel4.place(x=550,y=460)
