import tkinter as tk

fnt=("맑은 고딕 Semilight",15)
row=12          #가로
col=9            #세로
select_chip=0
map_data=[]
char_data=[]


def init_map():
    for y in range(0,col):
        map_data.append([2]*row)
    for y in range(0,8):
        char_data.append([-10]*2)

#map_data [y][x]
def draw_map():
    global img,map_data
    for y in range(0,col):
        for x in range(0,row):
            canvas.create_image(x*60+30,y*60+30,image=img[map_data[y][x]],tag="BG")

def set_map(e):
    x=e.x//60
    y=e.y//60

    if 0<=x<row and 0<=y<col:
        map_data[y][x] =select_chip
        canvas.create_image(x*60+30,y*60+30,image=img[select_chip])
    else:
        c_x = char_data[select_chip][0]
        c_y = char_data[select_chip][0]
        map_data[c_y][c_x] = 2
        canvas.create_image(c_x*60+30,c_y*60+30, image=img[2])
        char_data[select_chip][0] = x
        char_data[select_chip][1] = y
        canvas.create_image(x * 60 + 30, y*60+30,image=img[select_chip])

def change_chip(e):
    global select_chip
    if 0<=e.y//60<len(img):
        select_chip=e.y//60
        draw_chip()

def draw_chip():

    chip_canvas.delete("chip")
    for i in range(0,8):
        chip_canvas.create_image(30,i*60+30,image=img[i],tag="chip")

    chip_canvas.create_rectangle(4,60*select_chip+4,60-3,60*(select_chip+1),outline="red",width=5,tag="chip")

def print_data():
    text.delete("1.0","end")

    text.insert("end","map_data=")

    for y in range(0,col):
        text.insert("end","[")
        for x in range(0,row-1):
             text.insert("end",str(map_data[y][x])+",")
        text.insert("end", "],\n")






root=tk.Tk()
root.title("맵 그림판")
root.geometry("820x1000")

canvas=tk.Canvas(width=720,height=540,bg="white")
canvas.place(x=10,y=10)
canvas.bind("<Button-1>",set_map)
canvas.bind("<B1-Motion>",set_map)

chip_canvas=tk.Canvas(width=60,height=540,bg="green")
chip_canvas.place(x=740,y=10)

text=tk.Text(width=40,height=14,font=fnt)
text.place(x=10,y=560)

btn=tk.Button(text="데이터\n출력",font=fnt,fg="blue",command=print_data)
btn.place(x=520,y=600)

img=    [
                    tk.PhotoImage(file="chip00.png"),
                    tk.PhotoImage(file="chip01.png"),
                    tk.PhotoImage(file="chip02.png"),
                    tk.PhotoImage(file="chip03.png"),
                    tk.PhotoImage(file="pen00.png"),
                    tk.PhotoImage(file="red00.png"),
                    tk.PhotoImage(file="kuma00.png"),
                    tk.PhotoImage(file="seiuchi00.png")
                    ]


init_map()
draw_map()
draw_chip()
root.mainloop()

