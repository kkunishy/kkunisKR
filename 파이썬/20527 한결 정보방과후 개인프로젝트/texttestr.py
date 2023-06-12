import tkinter as tk

gameMenuList=["공격","행동","창고","도망"]
gameMenuNum=0
fnt = ("맑은 고딕 Semilight", 15)

root=tk.Tk()
root.title("쯔꾸르게임")
root.geometry("720x540")
root.resizable(False,False)

canvas=tk.Canvas(root,width=720,height=540,bg="black")
canvas.pack()

gameMenuLabel1=tk.Label(text=gameMenuList[0],font=fnt)
gameMenuLabel1.place(x=180,y=480)
gameMenuLabel2=tk.Label(text=gameMenuList[1],font=fnt)

gameMenuLabel3=tk.Label(text=gameMenuList[2],font=fnt)

gameMenuLabel4=tk.Label(text=gameMenuList[3],font=fnt)
