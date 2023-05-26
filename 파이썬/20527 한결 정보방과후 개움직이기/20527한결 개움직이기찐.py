import tkinter

bg_x1 = 240
bg_x2 = -240
bg_y = 150
timer = 0
x=0

def draw():
    global x, img_bg, timer

    x += 1


    canvas.delete("BG")
    canvas.create_image(x%480-240, 150, image = img_bg, tag = "BG")
    canvas.create_image(x%480+240, 150, image = img_bg, tag = "BG")
    canvas.create_image(240, 150, image = img_dog[timer%4], tag = "BG")
    
    root.after(50, draw)

def dog_move():
    global timer
    
    timer += 1
    root.after(5, dog_move)

def bg_move():
    global bg_x1, bg_x2

    bg_x1 += 1
    bg_x2 += 1
    
    if bg_x1 == 720:
        bg_x1 = -240
    elif bg_x2== 720:
        bg_x2 = -240
    root.after(5, bg_move)



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#실행시키지 말것
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#def dog_move_old():
#    global bg_x, bg_y, dog_pic1, dog_pic2, dog_pic3, dog_pic4, cntdog
#
#    print(cntdog)
#    cntdog += 1
#    if cntdog %4==0:
#        canvas.create_image(bg_x1, bg_y, image = dog_pic1, tag = "DP1")
#        canvas.delete("DP4")
#    elif cntdog %4==1:
#        canvas.create_image(bg_x1, bg_y, image = dog_pic2, tag = "DP2")
#        canvas.delete("DP1")
#    elif cntdog %4==2:
#        canvas.create_image(bg_x1, bg_y, image = dog_pic3, tag = "DP3")
#        canvas.delete("DP2")
#    elif cntdog %4==3:
#        canvas.create_image(bg_x1, bg_y, image = dog_pic4, tag = "DP4")
#        canvas.delete("DP3")
#
#    root.after(1, dog_move)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



root = tkinter.Tk()
root.title("강아지 산책")

canvas = tkinter.Canvas(width = 480, height = 300, bg = "white")
canvas.pack()


img_bg = tkinter.PhotoImage(file = "park.png")
img_dog = [
                        tkinter.PhotoImage(file = "dog0.png"), #img_dog[0]
                        tkinter.PhotoImage(file = "dog1.png"), #img_dog[1]
                        tkinter.PhotoImage(file = "dog2.png"), #img_dog[2]
                        tkinter.PhotoImage(file = "dog3.png") #img_dog[3]
                        ]

bg_move()
draw()
dog_move()
#dog_move_old()

root.mainloop()
