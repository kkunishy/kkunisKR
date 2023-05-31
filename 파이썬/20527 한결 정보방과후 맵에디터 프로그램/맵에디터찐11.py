import tkinter as tk

row = 12       
col = 9    
map_data = []
select_chip = 0
candy=0
stage=1
timer=0

char_data = []
char_list=[]



class mob:
    name=""
    xy=[]
    img=""
    img_num=0

    def __init__(self,name,img,img_num):
        self.name=name
        self.img=img
        self.img_num=img_num
        print(name,"생성")

def init_char():
    temp=mob("blue",img_pen,3)
    char_list.append(temp)
    
    temp=mob("red",img_red,3)
    char_list.append(temp)
    
    temp=mob("kuma",img_kuma,0)
    char_list.append(temp)
    
    temp=mob("seiuchi",img_seiuchi,0)
    char_list.append(temp)

    

def set_map():
    global stage, map_data

    if stage==1:
        map_data = [
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
                                [0, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 0, ],
                                [0, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 0, ],
                                [0, 2, 2, 2, 3, 1, 1, 3, 3, 2, 2, 0, ],
                                [0, 2, 2, 2, 3, 3, 3, 3, 3, 2, 2, 0, ],
                                [0, 0, 2, 2, 2, 3, 2, 2, 2, 2, 2, 0, ],
                                [2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, ],
                                [2, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, ],
                                [2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, ],
                                ]
        candy =10
        char_list[0].xy = [2, 2]
        char_list[1].xy = [8, 6]
        char_list[2].xy = [-10, -10]
        char_list[3].xy = [-10, -10]
    

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
    

    for y in range(0,col):
        for x in range(0,row):
            if map_data[y][x]>3:
                canvas.create_image(x*60+30,y*60+30,image=img_chip[2],tag = "BG")
            else:
                canvas.create_image(x*60+30,y*60+30,image=img_chip[map_data[y][x]],tag = "BG")
            
    for i in char_list:
        if i.xy[0]>=0 and i.xy[1]>=0:
            canvas.create_image(i.xy[0]*60+30,i.xy[1]*60+30,image=i.img[i.img_num+timer],tag="BG")
            print(i.xy)
        
    timer=(timer+1)%3

    root.after(1000,draw_map)
        

def main():
    init_char()
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
img_kuma=[
                    tk.PhotoImage(file="kuma00.png"),
                    tk.PhotoImage(file="kuma01.png"),
                    tk.PhotoImage(file="kuma02.png")
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
