import tkinter

bg_x1 = 240
bg_x2 = -240
bg_y = 150

count = 0
cntdog = 0


def bg_move():
    global bg_x1, bg_y, bg_x2, img_bg, count
    count += 1
    bg_x1 += 1
    bg_x2 += 1
    canvas.delete("BG")
    canvas.delete("BG2")
    canvas.create_image(bg_x1+(count%480), bg_y, image = img_bg, tag = "BG")
    canvas.create_image(bg_x2+(count%480), bg_y, image = img_bg, tag = "BG2")
    
    root.after(50, bg_move)


'''
def dog_move():
    global bg_x, bg_y, dog_pic1, dog_pic2, dog_pic3, dog_pic4, cntdog

    print(cntdog)
    cntdog += 1
    if cntdog %4==0:
        canvas.create_image(bg_x1, bg_y, image = dog_pic1, tag = "DP1")
        canvas.delete("DP4")
    elif cntdog %4==1:
        canvas.create_image(bg_x1, bg_y, image = dog_pic2, tag = "DP2")
        canvas.delete("DP1")
    elif cntdog %4==2:
        canvas.create_image(bg_x1, bg_y, image = dog_pic3, tag = "DP3")
        canvas.delete("DP2")
    elif cntdog %4==3:
        canvas.create_image(bg_x1, bg_y, image = dog_pic4, tag = "DP4")
        canvas.delete("DP3")

    root.after(1, dog_move)
'''   
root = tkinter.Tk()
root.title("강아지 산책")

canvas = tkinter.Canvas(width = 480, height = 300, bg = "white")
canvas.pack()

img_bg = tkinter.PhotoImage(file = "park.png")

dog_pic1 = tkinter.PhotoImage(file = "dog0.png")
dog_pic2 = tkinter.PhotoImage(file = "dog1.png")
dog_pic3 = tkinter.PhotoImage(file = "dog2.png")
dog_pic4 = tkinter.PhotoImage(file = "dog3.png")

bg_move()
#dog_move()
root.mainloop()
