import tkinter as tk
import random as rd
import sys

gameMenuListTopic=0
gameMenuList=[["*공격","*행동","*창고","*도망"],["안기","대화하기","노려보기","농담하기"]]
gameMenuNum=0
colorList=["white","black"]     #[0] 하양 [1] 검정

fnt = ("맑은 고딕 Semilight", 15)
fnt2 = ("맑은 고딕 Semilight", 20)
phase=0

myHP=135
enemyHP=100
enemyCarelessRate=1
rdJokeNum=0

moveListNum=0
dialougeNum=0
attackList=["케오는 ",
                    "적에게 마구때리기를 시전하여\n",
                    "적에게 돌진하여\n",
                  "적에게 창을 던져\n",
                  "의 데미지를 상대방에게 주었다!"]
storageList=["오렌지","사과","먹다남은육포","복숭아"]



def gameMenuselect1():
    global gameMenuNum, phase, dialougeNum, moveListNum
    gameMenuNum=1
    dialougeNum=0
    gameTextLabel["text"]="무엇을 하시겠습니까?"
    canvas.delete("char")
    gameMenuLabel1["text"]=gameMenuList[gameMenuListTopic][0]
    gameMenuLabel2["text"]=gameMenuList[gameMenuListTopic][1]
    gameMenuLabel3["text"]=gameMenuList[gameMenuListTopic][2]
    gameMenuLabel4["text"]=gameMenuList[gameMenuListTopic][3]
    canvas.create_image(200,200,image=charMeImg[0],tag="char")
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
    global phase, colorList, moveListNum, dialougeNum, rdJokeNum
    key=e.keysym
    if phase==0 and key=="space":
        phase=1
        gameTextLabel["text"]=""
        gameTextLabelSub["text"]=""
        gameQuestionLabel["fg"]=colorList[0]
        gameMenuselect1()
        
    elif phase==1 or phase==6:
        if key=="Down" and gameMenuNum==1:
            gameMenuselect3()
        elif key=="Down" and gameMenuNum==2:
            gameMenuselect4()
        elif key=="Up" and gameMenuNum==3:
            gameMenuselect1()
        elif key=="Up" and gameMenuNum==4:
            gameMenuselect2()
        elif key=="Left" and gameMenuNum==2:
            gameMenuselect1()
        elif key=="Left" and gameMenuNum==4:
            gameMenuselect3()
        elif key=="Right" and gameMenuNum==1:
            gameMenuselect2()
        elif key=="Right" and gameMenuNum==3:
            gameMenuselect4()
            
        elif key=="Return" and phase==1:
            if gameMenuNum==1:
                gameAttack()
                phase=3
            elif gameMenuNum==2:
                gameMove()
                phase=6
            elif gameMenuNum==3:
                #gameInv()
                print("미구현기능")
                pass
            elif gameMenuNum==4:
                gameFlee()
            
        elif key=="Return" and phase==6:
            if gameMenuNum==1:
                moveListNum=0
                phase=7
                gameMoveReact()
            elif gameMenuNum==2:
                moveListNum=1
                phase=7
                gameMoveReact()
            elif gameMenuNum==3:
                moveListNum=2
                phase=7
                gameMoveReact()
            elif gameMenuNum==4:
                moveListNum=3
                phase=7
                rdJokeNum=rd.randint(0,1)
                gameMoveReact()
        
            
    elif key=="Return" and phase==3:
        gameTextLabel["text"]=""
        phase=4
        gameEnemyAttack()
    elif key=="Return" and phase==4:
        gameTextLabel["text"]=""
        phase=1
        gameMenuselect1()
    elif key=="Return" and phase==7:
        dialougeNum+=1
        gameMoveReact()
    
def gameEnd():
    global phase
    canvas.delete("enemy")
    gameTextLabel["text"]="축하한다! 당신은 승리했다!"
    enemyHPLabel["text"]=""
    phase=2
    sys.exit()
def gameOver():
    global phase
    canvas.delete("char")
    gameTextLabel["text"]="이런... 결국 져버리고 말았다..."
    myHPLabel["text"]=""
    phase=2
    sys.exit()
def gameAttack():
    global attackList, enemyHP, phase, enemyCarelessRate
    rdNum=rd.randint(1,3)
    rdDamage=rd.randint(20,40)
    addedDamage=rdDamage*enemyCarelessRate
    canvas.delete("char")
    
    gameMenuUnavaliable()
    gameTextLabel["text"]=attackList[0]+attackList[rdNum]+str(addedDamage)+attackList[4]
    enemyHP-=addedDamage
    enemyHPLabel["text"]="적 HP: "+str(enemyHP)
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
    myHPLabel["text"]="내 HP: "+str(myHP)
    canvas.create_image(200,200,image=charMeImg[5],tag="char")
    if myHP<0:
        gameOver()

def gameMove():
    global phase, gameMenuListTopic
    gameMenuListTopic=1
    phase=6
    gameMenuselect1()
def gameMoveReset():
    global dialougeNum, gameMenuNum, gameMenuListTopic, phase
    dialougeNum=0
    gameMenuNum=0
    phase=4
    gameMenuListTopic=0
    gameEnemyAttack()
def gameMoveReact():
    global moveListNum, enemyCarelessRate, dialougeNum, rdJokeNum
    gameMenuUnavaliable()
    
    dialougeChance="상대방이 입는 데미지가 증가한다!"
    dialouge1=["당신은 병사를 안았다...","깜짝 놀란 그는 방심하는 듯 하다..."]
    dialouge2=["당신은 병사와 대화를 시도했다...","이런, 그는 다른 언어를 쓰는 듯 하다."]
    dialouge3=["당신은 살기를 뿜으며 병사를 노려봤다...","그는 잠시 주춤하는 듯 싶더니, 다시 정신을 차렸다.","병사가 쫄아버린 것 같다..."]
    dialouge4=[
                    ["당신은 병사에게 차가 놀라는 기름이 뭔지 물었다.","병사는 잠시 고민하는 것 같다.",'"카놀라유!"',"...","병사가 화나버렸다..."],
                    ["당신은 병사에게 현재 태어나지 않은게 뭔지 물었다.","병사는 잠시 고민하는 것 같다.","니 여친.","...","이런, 병사의 정곡을 찔러서 화가 난 것 같다..."]

            ]

 
    if moveListNum==0:       #안기
        canvas.delete("char")
        canvas.create_image(200,200,image=charMeImg[6],tag="char")
        if dialougeNum==1:
            gameTextLabel["text"]=dialouge1[0]
        elif dialougeNum==2:
            gameTextLabel["text"]=dialouge1[1]
        elif dialougeNum==3:
            gameTextLabel["text"]=dialougeChance
            enemyCarelessRate+=1
        elif dialougeNum==4:
            gameMoveReset()
            
    elif moveListNum==1:     #대화하기
        canvas.delete("char")
        canvas.create_image(200,200,image=charMeImg[7],tag="char")
        if dialougeNum==1:
            gameTextLabel["text"]=dialouge2[0]
        elif dialougeNum==2:
            gameTextLabel["text"]=dialouge2[1]
        elif dialougeNum==3:
            gameMoveReset()
            
    elif moveListNum==2:     #노려보기
        canvas.delete("char")
        canvas.create_image(200,200,image=charMeImg[8],tag="char")
        if dialougeNum==1:
            gameTextLabel["text"]=dialouge3[0]
        elif dialougeNum==2:
            rdNum=rd.randint(0,1)
            if rdNum==0:
                gameTextLabel["text"]=dialouge3[1]
            elif rdNum==1:
                gameTextLabel["text"]=dialouge3[2]+"\n"+dialougeChance
                enemyCarelessRate+=1
        elif dialougeNum==3:
            gameMoveReset()
            
    elif moveListNum==3:     #농담하기/Joking
        canvas.delete("char")
        canvas.create_image(200,200,image=charMeImg[9],tag="char")
        print(rdJokeNum)
        
        if dialougeNum==1:
            gameTextLabel["text"]=dialouge4[rdJokeNum][0]
        elif dialougeNum==2:
            gameTextLabel["text"]=dialouge4[rdJokeNum][1]
        elif dialougeNum==3:
            gameTextLabel["text"]=dialouge4[rdJokeNum][2]
        elif dialougeNum==4:
            gameTextLabel["text"]=dialouge4[rdJokeNum][3]
        elif dialougeNum==5:
            gameTextLabel["text"]=dialouge4[rdJokeNum][4]
        elif dialougeNum==6:
            gameMoveReset()


#def gameInv():
def gameFlee():
    gameMenuUnavaliable()
    canvas.delete("char")
    gameTextLabel["text"]="쫄아서 튀어버렸다!"
    myHPLabel["text"]=""
    enemyHPLabel["text"]=""
    canvas.create_text(520,265,text="???",font=fnt)
    sys.exit()

    
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

myHPLabel=tk.Label(text="내 HP: "+str(myHP),font=fnt,fg="white",bg="black")
myHPLabel.place(x=150,y=285)
enemyHPLabel=tk.Label(text="적 HP: "+str(enemyHP),font=fnt,fg="white",bg="black")
enemyHPLabel.place(x=500,y=285)

charEnemyImg=tk.PhotoImage(file="리유니온.png")         
charMeImg=[tk.PhotoImage(file="기본.png"),                    #0
                tk.PhotoImage(file="공격1.gif"),                         #1
                tk.PhotoImage(file="공격2.png"),                      #2
                tk.PhotoImage(file="공격3.png"),                      #3
                tk.PhotoImage(file="섭취.png"),                        #4
                tk.PhotoImage(file="피격.png"),                        #5
                tk.PhotoImage(file="안기.png"),                        #6
                tk.PhotoImage(file="대화하기.png"),                 #7
                tk.PhotoImage(file="노려보기.png"),                 #8
                tk.PhotoImage(file="농담하기.png"),                 #9
                tk.PhotoImage(file="섭취성공.png"),                 #10
                tk.PhotoImage(file="섭취실패.png")                  #11
           ]





main()
root.mainloop()
