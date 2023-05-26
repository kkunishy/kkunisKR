import tkinter

drink = {"아메리카노" : 3000, "라떼" : 3500, "아이스티" : 4000, "레몬에이드" : 4500, "딸기스무디" : 5000}
total_price = 0
order_drink = {}

def select_drink(menu):
    global total_price

    total_price += drink[menu]

    if menu in order_drink:
        order_drink[menu] += 1
    else :
        order_drink[menu]=1

    print_menu()
    print_price()


def print_menu():
    temp = ""

    for i in order_drink:
        temp = temp + i + " X " + str(order_drink[i]) + "\n"

    text.delete("1.0", tkinter.END)
    text.insert(tkinter.INSERT, temp)

def print_price():
    global total_price
    label_price["text"] = str(total_price)+"원"

def end_order():
    global total_price, order_drink

    total_price = 0
    del order_drink

    order_drink = {}
    print_menu()
    print_price()



root = tkinter.Tk()
root.title("주문 프로그램")
root.geometry("600x400+500+300")
root.resizable(False, False)


frame1 = tkinter.Frame(root, width="600", height="10")
frame1.pack(fill="both")
btn_end = tkinter.Button(frame1, text="주문종료",padx=10, pady=10, command = end_order)
btn_end.grid(row=0, column=2, padx=10, pady=10 )
label_price = tkinter.Label(frame1, text = "0원", width = "20", padx =10, pady = 10, fg = "blue")
label_price.grid(row = 0, column=3, padx = 10, pady = 10)

frame2 = tkinter.Frame(root, width="600", height="10")
frame2.pack(fill="both")

frame3 = tkinter.Frame(root, width="600", height="10")
frame3.pack()

photo1 = tkinter.PhotoImage(file = "a.jpg")
photo1 = photo1.subsample(6)
photolb1 = tkinter.Label(frame2, image= photo1)
photolb1.grid(row=0,column=0, padx = 10, pady = 10)


btn_drink1 = tkinter.Button(frame2, text = "아메리카노\n(3000원)", command=lambda:select_drink("아메리카노"), padx= 10, pady =10, width = "10")
btn_drink1.grid(row=1,column =0, padx = 10, pady = 10)


photo2 = tkinter.PhotoImage(file = "a.png")
photo2 = photo1.subsample(6)
photolb2 = tkinter.Label(frame2, image= photo1)
photolb2.grid(row=0,column=1, padx = 10, pady = 10)

btn_drink2 = tkinter.Button(frame2, text = "라떼\n(3500원)", command=lambda:select_drink("라떼"),padx= 10, pady =10, width = "10")
btn_drink2.grid(row=1,column =1, padx = 10, pady = 10)

btn_drink3 = tkinter.Button(frame2, text = "아이스티\n(4000원)", command=lambda:select_drink("아이스티"),padx= 10, pady =10, width = "10")
btn_drink3.grid(row=1,column =2, padx = 10, pady = 10)

btn_drink4 = tkinter.Button(frame2, text = "레몬에이드\n(4500원)", command=lambda:select_drink("레몬에이드"),padx= 10, pady= 10, width = "10")
btn_drink4.grid(row=1,column =3, padx = 10, pady = 10)

btn_drink5 = tkinter.Button(frame2, text = "딸기스무디\n(5000원)", command=lambda:select_drink("딸기스무디"),padx= 10, pady =10, width = "10")
btn_drink5.grid(row=1,column =4, padx = 10, pady = 10)

text = tkinter.Text(frame3, height = "10")
text.pack()

root.mainloop()

