import tkinter as tk
import random as rd
import sys

gameMenuListTopic=0
gameMenuList=[["*공격","*행동","*창고","*도망"],["안기","대화하기","노려보기","농담하기"]]
gameMenuNum=0

fnt = ("맑은 고딕 Semilight", 15)
fnt2 = ("맑은 고딕 Semilight", 20)
colorList=["white","black"]     #[0] 하양 [1] 검정
phase=0
myHP=100
enemyHP=100
enemyCarelessRate=1
attackList=["케오는 ",
                    "적에게 마구때리기를 시전하여\n",
                    "적에게 돌진하여\n",
                  "적에게 창을 던져\n",
                  "의 데미지를 상대방에게 주었다!"]
storageList=["오렌지","사과","먹다남은 육포","복숭아"]



def gameMenuselect1():
    global gameMenuNum, phase
    gameMenuNum=1
    gameTextLabel["text"]="무엇을 하시겠습니까?"
    canvas.delete("char")
    canvas.create_image(200,200,image=charMeImg[0],tag="char")
    gameMenuLabel1["bg"]=colorList[0]
    gameMenuLabel1["fg"]=colorList[1]
    gameMenuLabel2["bg"]=colorList[1]
    gameMenuLabel2["fg"]=colorList[0]
    gameMenuLabel3["bg"]=colorList[1]
    gameMenuLabel3["fg"]=colorList[0]
    gameMenuLabel4["bg"]=colorList[1]
    gameMenuLabel4["fg"]=colorList[0]
    print(phase)
def gameMenuselect2():
    global gameMenuNum
    gameMenuNum=2
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
        gameTextLabel["text"]=""
        gameTextLabelSub["text"]=""
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
    elif key=="Return" and phase==1:
        if gameMenuNum==1:
            gameAttack()
            phase=3
        elif gameMenuNum==2:
            #gameMove()
            pass
        elif gameMenuNum==3:
            #gameInv()
            pass
        elif gameMenuNum==4:
            #gameFlee()
            pass
    elif key=="Return" and phase==3:
        gameTextLabel["text"]=""
        phase=4
        gameEnemyAttack()
    elif key=="Return" and phase==4:
        gameTextLabel["text"]=""
        phase=1
        gameMenuselect1()

    
def gameEnd():
    global phase
    canvas.delete("enemy")
    gameTextLabel["text"]="축하한다! 당신은 승리했다!"
    phase=2
    sys.exit()
def gameOver():
    global phase
    canvas.delete("char")
    gameTextLabel["text"]="이런... 결국 져버리고 말았다..."
    phase=2
    sys.exit()
def gameAttack():
    global attackList, enemyHP, phase, enemyCarelessRate
    rdNum=rd.randint(1,3)
    rdDamage=rd.randint(20,40)
    canvas.delete("char")
    
    gameMenuUnavaliable()
    gameTextLabel["text"]=attackList[0]+attackList[rdNum]+str(rdDamage*enemyCarelessRate)+attackList[4]
    enemyHP-=rdDamage
    enemyHPLabel["text"]=enemyHP
    if rdNum==1:
        canvas.create_image(200,200,image=charMeImg[1],tag="char")
    elif rdNum==2:
        canvas.create_image(200,200,image=charMeImg[2],tag="char")
    elif rdNum==3:
        canvas.create_image(200,200,image=charMeImg[3],tag="char")
    if enemyHP<0:
        gameEnd()
def gameEnemyAttack():
    global myHP, phase
    rdNum=rd.randint(1,3)
    rdDamage=rd.randint(20,40)
    canvas.delete("char")

    gameTextLabel["text"]="리유니온 병사가 공격하여\n"+str(rdDamage)+" 만큼의 데미지를 입혔다!"
    myHP-=rdDamage
    myHPLabel["text"]=myHP
    canvas.create_image(200,200,image=charMeImg[5],tag="char")
    if myHP<0:
        gameOver()

'''
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
    canvas.create_image(200,200,image=charMeImg[0],tag="char")
    canvas.create_image(550,200,image=charEnemyImg,tag="enemy")
    

    
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
gameMenuLabel1=tk.Label(text=gameMenuList[gameMenuListTopic][0],font=fnt,fg="white",bg="black")
gameMenuLabel1.place(x=400,y=400)
gameMenuLabel2=tk.Label(text=gameMenuList[gameMenuListTopic][1],font=fnt,fg="white",bg="black")
gameMenuLabel2.place(x=550,y=400)
gameMenuLabel3=tk.Label(text=gameMenuList[gameMenuListTopic][2],font=fnt,fg="white",bg="black")
gameMenuLabel3.place(x=400,y=460)
gameMenuLabel4=tk.Label(text=gameMenuList[gameMenuListTopic][3],font=fnt,fg="white",bg="black")
gameMenuLabel4.place(x=550,y=460)

gameTextLabel=tk.Label(text="앗! 야생의 리유니온 병사들이 나타났다!",font=fnt2,bg="black",fg="white")
gameTextLabel.place(x=50,y=420)
gameTextLabelSub=tk.Label(text="Spacebar를 눌러 시작",font=fnt,bg="black",fg="white")
gameTextLabelSub.place(x=50,y=460)

myHPLabel=tk.Label(text=myHP,font=fnt,fg="white",bg="black")
myHPLabel.place(x=20,y=20)
enemyHPLabel=tk.Label(text=enemyHP,font=fnt,fg="white",bg="black")
enemyHPLabel.place(x=20,y=70)

charEnemyImg=tk.PhotoImage(file="리유니온.png")         
charMeImg=[tk.PhotoImage(file="기본.png"),                    #0
                tk.PhotoImage(file="공격1.gif"),                          #1
                tk.PhotoImage(file="공격2.png"),                      #2
                tk.PhotoImage(file="공격3.png"),                      #3
                tk.PhotoImage(file="섭취.png"),                           #4
                tk.PhotoImage(file="피격.png")                        #5
                ]

main()
root.mainloop()
