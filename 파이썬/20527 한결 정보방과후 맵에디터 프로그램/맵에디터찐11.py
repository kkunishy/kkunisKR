import tkinter as tk

col=12
row=9

char_list=[]
map_data=[]
candy=0
stage=1

def set_map():
    global stage, map_data

    if stage==1:
        map_data = [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2],
                    [0, 5, 2, 2, 2, 2, 2, 2, 0, 0, 0, 2],
                    [0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2],
                    [0, 4, 0, 2, 2, 2, 0, 0, 0, 0, 0, 2],
                    [0, 2, 0, 2, 0, 2, 0, 2, 2, 2, 0, 2],
                    [0, 2, 2, 2, 0, 2, 0, 2, 0, 2, 0, 2],
                    [0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 0, 2],
                    [0, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                        ]

        if stage==2:
            map_data = [
                    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
                    [2, 2, 2, 3, 3, 3, 3, 3, 3, 2, 2, 0],
                    [2, 2, 2, 3, 0, 1, 1, 1, 0, 0, 2, 0],
                    [2, 2, 2, 0, 0, 2, 4, 2, 0, 1, 2, 0],
                    [2, 2, 0, 0, 2, 2, 2, 0, 1, 2, 2, 0],
                    [2, 2, 0, 2, 2, 2, 0, 1, 2, 2, 2, 0],
                    [2, 0, 0, 2, 2, 0, 1, 2, 2, 2, 2, 0],
                    [2, 0, 0, 2, 0, 0, 5, 2, 2, 2, 2, 0],
                    [2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0]
                        ]
            candy=8

def draw_map():
    global row,col,map_data
    

    for y in range(0,row):
        for x in range(0,col):
            if map_data[y][x]>3:
                canvas.create_image(x*60+30,y*60+30,image=img_chip[2],tag = "BG")
            else:
                canvas.create_image(x*60+30,y*60+30,image=img_chip[map_data[y][x]],tag = "BG")
            


    

def main():
    set_map()
    draw_map()




root=tk.Tk()
root.title("펭귄게임")
root.geometry("720x540")
root.resizable(False,False)

canvas=tk.Canvas(width=720,height=540,bg="white")
canvas.pack()

img_pen=[
                    tk.PhotoImage(file="pen00.png"),
                    tk.PhotoImage(file="pen01.png"),
                    tk.PhotoImage(file="pen02.png"),
                    tk.PhotoImage(file="pen03.png"),
                    tk.PhotoImage(file="pen04.png"),
                    tk.PhotoImage(file="pen05.png"),
                    tk.PhotoImage(file="pen06.png"),
                    tk.PhotoImage(file="pen07.png"),
                    tk.PhotoImage(file="pen08.png"),
                    tk.PhotoImage(file="pen09.png"),
                    tk.PhotoImage(file="pen10.png"),
                    tk.PhotoImage(file="pen11.png")
                     ]
                    
img_red=[
                    tk.PhotoImage(file="red00.png"),
                    tk.PhotoImage(file="red01.png"),
                    tk.PhotoImage(file="red02.png"),
                    tk.PhotoImage(file="red03.png"),
                    tk.PhotoImage(file="red04.png"),
                    tk.PhotoImage(file="red05.png"),
                    tk.PhotoImage(file="red06.png"),
                    tk.PhotoImage(file="red07.png"),
                    tk.PhotoImage(file="red08.png"),
                    tk.PhotoImage(file="red09.png"),
                    tk.PhotoImage(file="red10.png"),
                    tk.PhotoImage(file="red11.png")
                        ]

img_seiuchi=[
                    tk.PhotoImage(file="seiuchi00.png"),
                    tk.PhotoImage(file="seiuchi01.png"),
                    tk.PhotoImage(file="seiuchi02.png")
                    ]

img_title=tk.PhotoImage(file="title.png")

img_chip=[
                tk.PhotoImage(file="chip00.png"),
                tk.PhotoImage(file="chip01.png"),
                tk.PhotoImage(file="chip02.png"),
                tk.PhotoImage(file="chip03.png")
                    ]
main()
root.mainloop()
