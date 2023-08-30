import tkinter

row = 12       #가로
column = 9    #세로
map_data = []
select_chip = 0

char_data = []

def init_map():
    for y in range ( 0, column ) :
        map_data.append([2]*row)

    for y in range (0, 8):
        char_data.append([-10,-10])

def draw_map():
    canvas.delete("BG")
    
    for y in range ( 0, column):
        for x in range ( 0, row):
            canvas.create_image ( x*60+30 , y*60+30, image = img[map_data[y][x]], tag = "BG" )

def draw_chip():
    chip_canvas.delete("CHIP")
    
    for i in range(len(img)):
        chip_canvas.create_image (30, i*60+30, image = img[i], tag = "CHIP")
    chip_canvas.create_rectangle(4, 60*select_chip+4, 60-3, 60*(select_chip+1)-3, outline = "red", width = 5, tag = "CHIP")

def change_chip(e):
    global select_chip

    if 0 <= e.y//60 < len(img) :
        select_chip = e.y // 60
        draw_chip()

def set_map(e) :
    global select_chip
    
    x = e.x // 60
    y = e.y // 60

    if 0 <= x < row  and  0 <= y < column :

        if select_chip < 4 :
            map_data[y][x] = select_chip
            canvas.create_image(x*60+30, y*60+30, image = img[select_chip])
        else :
            if char_data[select_chip][0] < 0 and char_data[select_chip][0] < 0:
                map_data[y][x] = 2
                canvas.create_image(x*60+30, y*60+30, image = img[select_chip])

                char_data[select_chip][0] = x
                char_data[select_chip][1] = y

                print(char_data[select_chip][0], char_data[select_chip][1])
            else :
                c_x = char_data[select_chip][0]
                c_y = char_data[select_chip][1]

                map_data[c_y][c_x] = 2
                canvas.create_image(c_x*60+30, c_y*60+30, image = img[2])

                char_data[select_chip][0] = x
                char_data[select_chip][1] = y
                canvas.create_image(x*60+30, y*60+30, image = img[select_chip])
                print(char_data[select_chip][0], char_data[select_chip][1])

def print_data():
    candy = 0
    text.delete("1.0", "end")
    text.insert("end", "[set_map 함수에 넣어서 사용]\n\n")
    text.insert ( "end", "map_data = [\n")

    for y in range (0, column) :
        text.insert ( "end", "[") 
        for x in range (0, row):
            if map_data[y][x] == 3:
                candy += 1
            text.insert ( "end", str(map_data[y][x])+", " )
        text.insert ( "end", "],\n" )

    text.insert ( "end", "]" )
    text.insert ( "end", "\ncandy ="+str(candy) )

    text.insert ( "end", "\nchar_list[0].xy = "+str(char_data[4]))
    text.insert ( "end", "\nchar_list[1].xy = "+str(char_data[5]))
    text.insert ( "end", "\nchar_list[2].xy = "+str(char_data[6]))
    text.insert ( "end", "\nchar_list[3].xy = "+str(char_data[7]))
    

root = tkinter.Tk()
root.title("맵 그림판")
root.geometry("820x980")

canvas = tkinter.Canvas(width = 720, height = 540, bg = "white")
canvas.place(x = 10, y = 10)
canvas.bind("<Button-1>" , set_map )
canvas.bind("<B1-Motion>", set_map ) 

chip_canvas = tkinter.Canvas(width = 60, height = 540, bg = "black")
chip_canvas.place(x=740, y = 10)
chip_canvas.bind("<Button-1>", change_chip )

text = tkinter.Text(width = 40, height = 14, font = ("맑은 고딕", 10, "bold"), fg = "green")
text.place(x=10, y=560)


btn = tkinter.Button(text = "데이터\n출력", font = ("맑은 고딕", 15, "bold"), fg = "blue", command = print_data)
btn.place ( x = 720, y = 600 )

img = [
                tkinter.PhotoImage(file = "chip00.png"),
                tkinter.PhotoImage(file = "chip01.png"),
                tkinter.PhotoImage(file = "chip02.png"),
                tkinter.PhotoImage(file = "chip03.png"),
                tkinter.PhotoImage(file = "pen03.png"),
                tkinter.PhotoImage(file = "red03.png"),
                tkinter.PhotoImage(file = "kuma00.png"),
                tkinter.PhotoImage(file = "seiuchi00.png"),
          ]

init_map()
draw_map()
draw_chip()
                                  
root.mainloop()




