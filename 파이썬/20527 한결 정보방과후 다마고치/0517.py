#다마고치 만들기

import tkinter
import random
fnt=("맑은 고딕 Semilight",15)
pet_list = []

class 죠르디:
    water = 0
    eat = 0
    name =""
    name_entry = 0
    name_window = 0

    def __init__(self):

        self.name_window = tkinter.Toplevel()
        self.name_window.title("이름 짓기")
        self.name_window.geometry("450x230")
        self.name_window.resizable(False, False)
        
        name_label = tkinter.Label ( self.name_window, text ="죠르디의 이름을 지어주세요.", font=("맑은 고딕", 20, "bold"), padx=20,pady = 20)
        name_label.pack()
        
        self.name_entry = tkinter.Entry (self.name_window, font =("맑은 고딕", 20, "bold") )
        self.name_entry.pack()
        
        ok_btn = tkinter.Button ( self.name_window, text = "확인", font =("맑은 고딕", 20, "bold"), command = self.set_name)
        ok_btn.pack()



    def set_name (self):
        self.name = self.name_entry.get()
        self.name_window.destroy()
        
        name_label = tkinter.Label(root, text = "이름 : " + self.name, fg = "green", font = ("맑은 고딕", 15, "bold") )
        name_label.place(x=170,y=430)
        self.select_img()


    def select_img(self):
        global se_1,se_2,se_3

        select_img=tkinter.Toplevel()
        select_img.title("입양할 죠르디 선택")
        select_img.geometry("400x200")

        se1_btn=tkinter.Button(select_img, image=se_1,width=150,height=150,bg="white")
        se1_btn.place(x=20,y=20)

        se2_btn = tkinter.Button(select_img, image=se_2, width=150, height=150, bg="white")
        se2_btn.place(x=40,y=20)

        se3_btn = tkinter.Button(select_img, image=se_3, width=150, height=150, bg="white")
        se3_btn.place(x=60,y=20)


    def eat_water(self):
        self.water +=1
        x = random.randint(20,380)
        y = random.randint(20,380)
        canvas.create_text(x, y, text="water+1",fill= "blue", font = ("맑은 고딕", 15, "bold"), tag = "text")
        water_lb["text"]="물:"+str(self.water)
        root.after(500, self.eraser_text)

    def eat_meat(self):
        self.meat +=1
        x=random.randint(20,380)
        y=random.randint(20,380)
        canvas.create_text(x,y, text="meat+1",fill="red",font=("맑은 고딕", 15, "bold"),tag="text")
        meat_lb["text"]="밥:"+str(self.meat)
        root.after(500,self.eraser_text)

    def eraser_text(self):
         canvas.delete("text")

        

def main():
    canvas.create_image(200,200,image = pet_img[0], tag = "CARACTER")
    water_lb["text"]="물:"+str(pet_list[0].water)
    meat_lb["text"]="고기:"+str(pet_list[0].eat)


def add_pet():
    temp = 죠르디()
    pet_list.append(temp)





    
root = tkinter.Tk()
root.title("죠르디 키우기")
root.geometry("440x550")
root.resizable(False, False)

add_pet()

canvas = tkinter.Canvas(width = 400, height = 400, bg = "white")
canvas.place(x = 20, y = 20)

add_btn = tkinter.Button(text = "추가", bg = "white", fg = "green", font = ("맑은 고딕", 19, "bold"), command=add_pet)
add_btn.place(x = 20, y = 480)

water_img = tkinter.PhotoImage(file ="20527 한결 정보방과후 다마고치/물.png")
water_img = water_img.subsample(6)
water_btn = tkinter.Button ( image = water_img , command = pet_list[0].eat_water)
water_btn.place(x=110,y=480)

meat_img = tkinter.PhotoImage(file ="20527 한결 정보방과후 다마고치/고기.png")
meat_img = meat_img.subsample(6)
meat_btn = tkinter.Button ( image = meat_img )
meat_btn.place(x=180,y=480)


water_lb=tkinter.Label(text="물:",fg="blue",font=fnt)
water_lb.place(x=20,y=460)
meat_lb=tkinter.Label(text="배고픔:",fg="orange",font=fnt)
meat_lb.place(x=20,y=490)

pet_img = [
                    tkinter.PhotoImage(file = "죠르디1.PNG"),
                    tkinter.PhotoImage(file = "죠르디2.PNG"),
                    tkinter.PhotoImage(file = "죠르디3.PNG")
                ]

se_1=tkinter.PhotoImage(file="죠르디1.PNG")
se_1.subsample(6)
se_2=tkinter.PhotoImage(file="죠르디2.PNG")
se_2.subsample(6)
se_3=tkinter.PhotoImage(file="죠르디3.PNG")
se_3.subsample(6)



main()

root.mainloop()









