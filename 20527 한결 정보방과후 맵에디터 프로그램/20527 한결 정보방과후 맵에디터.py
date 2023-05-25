import tkinter as tk

fnt=("맑은 고딕 Semilight",15)
row=12          #가로
col=9            #세로
select_chip=0
map_data=[]



def init_map():
    for y in range(0,col):
        map_data.append([2]*row)

#map_data [y][x]
def draw_map():
    global img,map_data
    for y in range(0,col):
        for x in range(0,row):
            canvas.create_image(x*60+30,y*60+30,image=img[map_data[y][x]],tag="BG")

def set_map(e):
    x=e.x//60
    y=e.y//60

    if 0<=y<row and 0<=x<col:
        map_data[y][x] =select_chip
        canvas.create_image(x*60+30,y*60+30,image=img[select_chip])

def draw_chip():
    for i in range(0,4):
        chip_canvas.create_image(30,i*60+30,image=img[i])

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
                    tk.PhotoImage(file="chip03.png")
                    ]


init_map()
draw_map()
draw_chip()
root.mainloop()

