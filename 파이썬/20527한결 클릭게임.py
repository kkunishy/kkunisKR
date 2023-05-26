'''
import tkinter
def click() :
    name = en1.get()
    en2.delete(0,tkinter.END)
    en2.insert(0, name)


#font = 15
#font = 나눔고딕 
root = tkinter.Tk()
root.geometry("400x200")
root.title("방과후")

lb1 = tkinter.Label(root, text = "ID", font = 15, bg = "white", fg = "red")
lb1.pack()

en1 = tkinter.Entry(root, font = 30)
en1.pack()

lb2 = tkinter.Label(root, text = "PASSWORD", font = 15, bg = "white", fg = "red")
lb2.pack()

en2 = tkinter.Entry(root, font = 30)
en2.pack()

bt1 = tkinter.Button(root, text = "enter", font = 15, bg = "skyblue", fg = "white", command = click)
bt1.pack()

root.mainloop()
'''

import tkinter
count = 0

def click() :
    global count
    count = count + 1
    clickBt1["text"] = "버튼 클릭 수 : " + str(count)
    if count == 100:
        count = 0

root = tkinter.Tk()
root.title("클릭 게임")
root.geometry("2000x1000")

mainLabel = tkinter.Label(root, text = "클릭하세요")
mainLabel.pack()

clickBt1 = tkinter.Button(root, text = "클릭!", bg = "green", width = 180, height = 30, command = click)
clickBt1.pack()

clickBt2 = tkinter.Button(root, text = "리셋!", bg = "red", width = 180, height = 30)
clickBt2.pack()
