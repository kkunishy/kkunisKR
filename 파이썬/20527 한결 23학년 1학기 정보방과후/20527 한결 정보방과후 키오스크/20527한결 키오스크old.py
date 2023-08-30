import tkinter

price = 0
drink_menu = {"아메리카노" : 3000, "라떼" : 3500, "아이스티" : 4000, "레몬에이드" : 4500, "딸기라떼" : 5000}

def select_menu(menu):
    global drink_menu, price

    price += drink_menu[menu]
    price_lb["text"] = str(price) + "원"
    print(drink_menu[menu])


root =  tkinter.Tk()
root.title("키오스크")
root.geometry("660x400+500+300")    #구역을 나눌때 +를 사용


frame1 = tkinter.Frame(root, width = "600", height = "10")
frame1.pack(fill = "both")

end_btn = tkinter.Button(frame1, text = "주문종료", font = 15, fg = "blue", bg = "white", padx = 20, pady = 10)
end_btn.grid(row = 0, column = 0, padx = 10, pady = 10)

price_lb = tkinter.Label(frame1, text = "0원", fg = "blue")
price_lb.grid(row = 0, column = 1)


frame2 = tkinter.Frame(root, width = "600", height = "10")
frame2.pack(fill = "both")

menu_btn1 = tkinter.Button(frame2, command = lambda:select_menu("아메리카노"), text = "아메리카노\n(3000원)", font = 15, fg = "blue", bg = "white", padx = 20, pady = 10)
menu_btn1.grid(row = 0, column = 0, padx = 5, pady = 10)

menu_btn2 = tkinter.Button(frame2, command = lambda:select_menu("라떼"), text = "라떼\n(3500원)", font = 15, fg = "blue", bg = "white", padx = 20, pady = 10)
menu_btn2.grid(row = 0, column = 1, padx = 5, pady = 10)

menu_btn3 = tkinter.Button(frame2, command = lambda:select_menu("아이스티"), text = "아이스티\n(4000원)", font = 15, fg = "blue", bg = "white", padx = 20, pady = 10)
menu_btn3.grid(row = 0, column = 2, padx = 5, pady = 10)

menu_btn4 = tkinter.Button(frame2, command = lambda:select_menu("레몬에이드"), text = "레몬에이드\n(4500원)", font = 15, fg = "blue", bg = "white", padx = 20, pady = 10)
menu_btn4.grid(row = 0, column = 3, padx = 5, pady = 10)

menu_btn5 = tkinter.Button(frame2, command = lambda:select_menu("딸기라떼"), text = "딸기라떼\n(5000원)", font = 15, fg = "blue", bg = "white", padx = 20, pady = 10)
menu_btn5.grid(row = 0, column = 4, padx = 5, pady = 10)


frame3 = tkinter.Frame(root, width = "600", height = "10")
frame3.pack(fill = "both")

text = tkinter.Text(frame3, pady = 20, height = "10")
text.pack()

root.mainloop()
