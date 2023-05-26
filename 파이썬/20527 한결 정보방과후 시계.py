
import tkinter
import time

fnt = ("맑은 고딕 Semilight", 40)
count = 0

def key_down(e):        #e가중요
    key_lb2["text"] = "key code ->" + str(e.keycode)
    key_lb3["text"] = "key sbl ->" + str(e.keysym)
def clock():
    clock_lb2["text"] = time.strftime("%H : %M : %S")
    root.after(1000, clock)
def star():
    global count
    count += 1
    print(count)

    if count %2==0:
        star_lb1["text"] = "☆★☆★☆★☆★☆★"
    else:
        star_lb1["text"] = "★☆★☆★☆★☆★☆"
    root.after(1000, star)
    
    


    


root =  tkinter.Tk()
root.title("시계")
root.geometry("800x400")

key_lb1 = tkinter.Label(root, text = "눌려진 키:", font = fnt, fg = 'blue')
key_lb1.place(x=50, y=120)

key_lb2 = tkinter.Label(root, text = "키보드를", font = fnt, fg = 'blue')
key_lb2.place(x=330, y=120)

key_lb3 = tkinter.Label(root, text = "눌러주세요!", font = fnt, fg = 'blue')
key_lb3.place(x=330, y=185)


clock_lb1 = tkinter.Label(root, text = "현재 시각:", font = fnt, fg = 'green')
clock_lb1.place(x=50, y=60)

clock_lb2 = tkinter.Label(root, text = "0 : 0 : 0", font = fnt, fg = 'green')
clock_lb2.place(x=330, y=60)

star_lb1 = tkinter.Label(root, text = "☆", font = fnt, fg = 'red')
star_lb1.place(x=200, y=260)

#이벤트를 넣을때 사용
clock()
star()
root.bind("<KeyPress>", key_down )
root.mainloop()
