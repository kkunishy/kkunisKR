import tkinter as t
import random as r
#변수
bg_timer = 0
fnt = ("휴먼굵은팸체",25)
fnt2 = ("휴먼굵은팸체",50)
scene=0
timer=0
coin=0
score=0
player_x=240
player_y=600
key=""
speed=29
meteo_max=10
meteo_xy=[
                    [0,0] for _ in range(meteo_max)
                    ]
#함수
def init_enemy():
    global meteo_max
    for i in range(0,meteo_max):
        meteo_xy[i][0] = r.randint(0,480)
        meteo_xy[i][1] = r.randint(-640,0)


def draw_enemy():
    global meteo_max,scene
    for i in range(0,meteo_max):
        canvas.create_image(meteo_xy[i][0],meteo_xy[i][1], image = img_meteo,tag = "GAME")
        meteo_xy[i][1]+=60
        if meteo_xy[i][1] >640:
            meteo_xy[i][0] = r.randint(0,480)
            meteo_xy[i][1] = r.randint(-640,0)
        if (meteo_xy[i][0]-player_x)**2 + (meteo_xy[i][1]-player_y)**2 < 36*36:
            scene=2
    
def timer_set():
    global timer
    timer += 1
    root.after(1000,timer_set)
    
def main():
    global bg_timer, scene, coin, timer, key
    bg_timer += 1
    canvas.create_image(240,320+bg_timer%640,image=img_bg,tag="BG")
    canvas.create_image(240, -320+bg_timer%640,image=img_bg,tag="BG")

    if scene == 0:
        canvas.create_text(250,180,text="운석충돌 회피놀이\n<space>를누르시오",font=fnt2,fill=("red"),tag="title")

        if bg_timer%2==0:
            canvas.create_text(240,480,text="동전을 투하하시오.(0/2)",font=fnt2,fill=("pink"),tag="coin0")
            pass

            if coin == 1:
                canvas.delete("coin0")
                canvas.create_text(240,480,text="동전을 투하하시오.(1/2)",font=fnt2,fill=("pink"),tag="coin1")

            if coin == 2:
                canvas.delete("coin0")
                canvas.delete("coin1")
                canvas.create_text(240,480,text="동전을 투하하시오.(2/2)",font=fnt2,fill=("pink"),tag="coin2")

            if coin ==3:
                canvas.delete("coin0")
                canvas.delete("coin1")
                canvas.delete("coin2")
                canvas.create_text(240,480,text="놀음을 시작하시오!",font=fnt2,fill=("red"),tag="play")

            if coin >3:
                canvas.delete("coin0")
                canvas.delete("coin1")
                canvas.delete("coin2")
                canvas.delete("play")
                scene+=1
                timer=0
                init_enemy()
    if scene == 1:
        canvas.delete("title")
        canvas.delete("GAME")
        canvas.create_text(50,50,text="시간 :"+str(timer),font=fnt, fill=("white"),tag="GAME")
        canvas.create_text(250,50,text="혁명점수 :"+str(score),font=fnt, fill=("white"),tag="GAME")
        draw_enemy()
        player_move()
        canvas.create_image(player_x,player_y,image=img_player[timer%2],tag="GAME")
    if scene == 2:
        canvas.delete("GAME")

        canvas.create_text(240,300,text="Game over",font=fnt2,fill=("white"),tag="gameover")
        canvas.create_text(240,480,text="space를 눌러\n다시 시작하세요.",font=fnt2,fill=("white"),tag="gameover")
        coin=0
        if key =="space":
            scene=0

                

    root.after(100, main)

def key_down(e):
    global coin,key
    key=e.keysym
    if e.keysym=="space":
        coin+=1

def player_move():
    global player_x,player_y,key,speed

    if (key=="a" or  key == "A" or key == "Left") and (player_x>30):
        player_x-=speed
    elif (key=="d" or  key == "D" or key == "Right") and (player_x<450):
        player_x+=speed
    elif (key=="w" or  key == "W" or key == "Up") and (player_y>30):
        player_y-=(speed+2)
    elif (key=="s" or  key == "S" or key == "Down") and (player_y<640):
        player_y+=(speed+2)
    key=""
        
#def score_set():
#메인
root = t.Tk()
root.title("샌즈피하기")
root.resizable(False, False)
root.bind("<KeyPress>", key_down)

canvas = t.Canvas(width = 480, height = 640, bg =  "black")
canvas.pack()


img_bg = t.PhotoImage(file="cosmo.png")
img_player = [
                        t.PhotoImage(file="starship0.png"),
                        t.PhotoImage(file="starship1.png")
                        ]
img_meteo = t.PhotoImage(file="meteo.png")
main()
timer_set()
root.mainloop()
