import tkinter

root = tkinter.Tk()
root.title("맵 그림판")
root.geometry("820x980")

canvas = tkinter.Canvas(width = 720, height = 540, bg = "white")
canvas.place(x = 10, y = 10)

chip_canvas = tkinter.Canvas(width = 60, height = 540, bg = "black")
chip_canvas.place(x=740, y = 10)

text = tkinter.Text(width = 40, height = 14, font = ("맑은 고딕", 15, "bold"), fg = "green")
text.place(x=10, y=560)

btn = tkinter.Button(text = "데이터\n출력", font = ("맑은 고딕", 15, "bold"), fg = "blue")
btn.place ( x = 520, y = 600 )

root.mainloop()




