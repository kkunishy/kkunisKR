import tkinter as t

#변수
x1 = 50
y1 = 50
w1 = 120
h1 = 60

x2 = 300
y2 = 100
w2 = 120
h2 = 160

#함수
def mouse_movingman(e):
    canvas.delete("RECT_I")

    ex1 = e.x-w1/2
    ey1 = e.y-h1/2

    col = "blue"
    if hit_check(e) == True:
        col = "black"
        
    canvas.create_rectangle(ex1, ey1, ex1+w1, ey1+h1, fill = col, tag = "RECT_I")

def hit_check(e):

    #절대값 함수 abs(숫자 또는 식)
    #abs(dx-dy)
    dx = abs(350-e.x)
    dy = abs(150-e.y)

    if dx <= 115 and dy <= 130:
        return True
    else:
        return False




#메인
root = t.Tk()
root.title("충돌체크")

canvas = t.Canvas(width = 600, height = 400,  bg = "pink")
canvas.pack()
canvas.bind("<Motion>", mouse_movingman)

canvas.create_rectangle(x1, y1, x1+w1, y1+h1, fill = "black", tag = "RECT_I")
canvas.create_rectangle(x2, y2, x2+w2, y2+h2, fill = "black", tag = "RECT_II")


root.mainloop()
