import tkinter

row = 12       #가로
column = 9    #세로
map_data = []
select_chip = 0

#캐릭터 좌표 저장하는 리스트
char_data = [] 

def init_map():
    for y in range ( 0, column ) :
        map_data.append([2]*row)

    #캐릭터 좌표 저장하는 리스트 초기화
    #[-10,-10] 8개
    #캐릭터 4개지만 select_chip으로 접근하기 위해
    #0~7인덱스 생성, 실제 사용 인덱스는 4,5,6,7
    for y in range (0, 8):
        char_data.append( [-10]*2 )




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

        #맵그리는 칩이 선택된 경우
        if select_chip < 4 :
            map_data[y][x] = select_chip
            canvas.create_image(x*60+30, y*60+30, image = img[select_chip])

        #캐릭터 칩이 선택된 경우
        else :
            #캐릭터가 맵에 존재하지 않는 경우
            if char_data[select_chip][0] < 0 or char_data[select_chip][1] < 0:
    
                #클릭한 좌표의 map_data값을 select_chip으로 바꿈.
                map_data[y][x] = select_chip

                #캐릭터 그리기
                canvas.create_image(x*60+30, y*60+30, image = img[select_chip])

                #캐릭터 좌표 리스트에 x좌표, y좌표 값 저장
                char_data[select_chip][0] = x
                char_data[select_chip][1] = y
            
         #캐릭터가 맵에 존재하는 경우       
            else :
                #기존 좌표 이름이 너무 길어서 짧은 이름 변수에 넣음
                c_x = char_data[select_chip][0]
                c_y = char_data[select_chip][1]

                #map_data에서 캐릭터의 기존 좌표에 2번 칩 번호 넣어주고, 그림 그리기
                map_data[c_y][c_x] = 2
                canvas.create_image(c_x*60+30, c_y*60+30, image = img[2])

                #캐릭터 좌표 저장하는 리스트에 현재 좌표 입력해주기, 그림 그리기
                char_data[select_chip][0] = x
                char_data[select_chip][1] = y
                canvas.create_image(x*60+30, y*60+30, image = img[select_chip])


def print_data():

    text.delete("1.0", "end")
    text.insert ( "end","★init_map함수에서 원하는 stage에 붙여 넣으세요!!\n\n")
    
    text.insert ( "end", "map_data = [\n")

    for y in range (0, column) :
        text.insert ( "end", "[") 
        for x in range (0, row):
            text.insert ( "end", str(map_data[y][x]))
            if x < row-1 :
                text.insert ( "end", ", ")
        text.insert ( "end", "],\n" )

    text.insert ( "end", "]\n" )
    text.insert ( "end", "\ncandy = "+str("candy") )

    text2.delete("1.0", "end")
    text2.insert ( "end","★init_map함수의 맨 끝에 붙여 넣으세요!!\n")
    text2.insert ( "end", "\nchar_data.append( "+str(char_data[4])+")")
    text2.insert ( "end", "\nchar_data.append( "+str(char_data[5])+")")
    text2.insert ( "end", "\nchar_data.append( "+str(char_data[6])+")")
    text2.insert ( "end", "\nchar_data.append( "+str(char_data[7])+")")
    

root = tkinter.Tk()
root.title("맵 그림판")
root.geometry("820x830")

canvas = tkinter.Canvas(width = 720, height = 540, bg = "white")
canvas.place(x = 10, y = 10)
canvas.bind("<Button-1>" , set_map )
canvas.bind("<B1-Motion>", set_map ) 

chip_canvas = tkinter.Canvas(width = 60, height = 540, bg = "black")
chip_canvas.place(x=740, y = 10)
chip_canvas.bind("<Button-1>", change_chip )

text = tkinter.Text(width = 40, height = 14, font = ("맑은 고딕", 10, "bold"), fg = "green")
text.place(x=10, y=560)

text2 = tkinter.Text(width = 40, height = 14, font = ("맑은 고딕", 13, "bold"), fg = "green")
text2.place(x=370, y=560)

btn = tkinter.Button(text = "데이터\n출력", font = ("맑은 고딕", 15, "bold"), fg = "blue", command = print_data)
btn.place ( x = 720, y = 650 )

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




