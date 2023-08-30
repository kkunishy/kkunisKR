
import tkinter as tk
import random as rd

# 변수
fnt = ("맑은 고딕 Semilight", 15)


# 함수
class Ceobe:
    petName = ""
    petAge = 0
    petMeat = 0
    petWater = 0
    petNameEntry = 0
    petNameWindow = 0
    petPicNum = 0
    fnt = ("맑은 고딕 Semilight", 15)

    # 실행시키자마자 사용
    def start(self):
        self.petNameWindow = tk.Toplevel()
        self.petNameWindow.title("이름 짓기")
        self.petNameWindow.geometry("450x230")
        self.petNameWindow.resizable(False, False)

        petNameLabel = tk.Label(self.petNameWindow, text="케오의 별명을 지어주세요.", font=fnt, padx=20, pady=20)
        petNameLabel.pack()

        self.petNameEntry = tk.Entry(self.petNameWindow, font=fnt)
        self.petNameEntry.pack()

        btnOK = tk.Button(self.petNameWindow, text="확인", font=fnt, command=self.petNameSet)
        btnOK.pack()

    def petNameSet(self):
        self.petName = self.petNameEntry.get()
        self.petNameWindow.destroy()

        petNameLabel = tk.Label(root, text="이름:" + self.petName, fg="green", font=fnt)
        petNameLabel.place(x=170, y=430)
        self.petPicSelect()

    def petPicSelect(self):
        global petPicSelect1, petPicSelect2, petPicSelect3, petPicSelect4, petPicSelect5

        self.petNameWindow = tk.Toplevel()
        self.petNameWindow.title("입양할 케오 선택")
        self.petNameWindow.geometry("1100x200")

        petPicSelect1 = tk.PhotoImage(file="hmm.png")
        petPicSelect1.subsample((6))
        petPicSelect2 = tk.PhotoImage(file="hello.png")
        petPicSelect2.subsample((6))
        petPicSelect3 = tk.PhotoImage(file="ike.png")
        petPicSelect3.subsample((6))
        petPicSelect4 = tk.PhotoImage(file="makaseryo.png")
        petPicSelect4.subsample((6))
        petPicSelect5 = tk.PhotoImage(file="hello2(gif).gif")
        petPicSelect5.subsample((6))

        petPicSelect1Btn = tk.Button(self.petNameWindow, image=petPicSelect1, width=150, height=150, bg="white",command=lambda: self.petPicSetup(0))
        petPicSelect1Btn.place(x=20, y=20)
        petPicSelect2Btn = tk.Button(self.petNameWindow, image=petPicSelect2, width=150, height=150, bg="white",command=lambda: self.petPicSetup(1))
        petPicSelect2Btn.place(x=220, y=20)
        petPicSelect3Btn = tk.Button(self.petNameWindow, image=petPicSelect3, width=150, height=150, bg="white",command=lambda: self.petPicSetup(2))
        petPicSelect3Btn.place(x=420, y=20)
        petPicSelect4Btn = tk.Button(self.petNameWindow, image=petPicSelect4, width=150, height=150, bg="white",command=lambda: self.petPicSetup(3))
        petPicSelect4Btn.place(x=620, y=20)
        petPicSelect5Btn = tk.Button(self.petNameWindow, image=petPicSelect5, width=150, height=150, bg="white",command=lambda: self.petPicSetup(4))
        petPicSelect5Btn.place(x=820, y=20)

    def petPicSetup(self, select_num):
        self.petPicNum = select_num
        self.petNameWindow.destroy()
        main()

    def petEatWater(self):
        self.petWater += 1
        x = rd.randint(20, 380)
        y = rd.randint(20, 380)
        canvas.create_text(x, y,text="water+1",fill="blue", font=fnt, tag="text")
        petWaterLb["text"] = "물" + str(self.petWater)
        root.after(500, self.peteatDel())

    def petEatMeat(self):
        self.petMeat += 1
        x = rd.randint(20, 380)
        y = rd.randint(20, 380)
        canvas.create_text(x, y, text="meat+1", fill="red", font=fnt, tag="text")
        petMeatLb["text"] = "밥" + str(self.petMeat)
        root.after(500, self.peteatDel)

    def peteatDel(self):
        canvas.delete("text")


def main():
    global ceobe
    canvas.create_image(200, 200, image=petIdleImg[ceobe.petPicNum], tag="CHARACTER")
    petWaterLb["text"] = "물:" + str(ceobe.petWater)
    petMeatLb["text"] = "고기:" + str(ceobe.petMeat)






# 메인
root = tk.Tk()
root.title("조조 키우기")
root.geometry("440x550")
root.resizable(False, False)

canvas = tk.Canvas(width=400, height=400, bg="white")
canvas.place(x=20, y=20)

ceobe=Ceobe()



ButtonSet = tk.Button(text="추가", bg="white", fg="green", font=fnt,command=ceobe.petNameSet)
ButtonSet.place(x=20, y=480)

petWaterImg = tk.PhotoImage(file="water.png")
petWaterImg = petWaterImg.subsample(6)
petWaterBtn = tk.Button(image=petWaterImg, command=ceobe.petEatWater)
petWaterBtn.place(x=110, y=480)
petWaterLb = tk.Label(text="물", fg="blue", font=fnt)
petWaterLb.place(x=20, y=460)

petMeatImg = tk.PhotoImage(file="meat.png")
petMeatImg = petMeatImg.subsample(6)
petMeatBtn = tk.Button(image=petMeatImg, command=ceobe.petEatMeat)
petMeatBtn.place(x=180, y=480)
petMeatLb = tk.Label(text="배고픔:", fg="orange", font=fnt)
petMeatLb.place(x=20, y=490)



petIdleImg = [
    tk.PhotoImage(file="hmm.png"),
    tk.PhotoImage(file="hello.png"),
    tk.PhotoImage(file="ike.png"),
    tk.PhotoImage(file="makaseryo.png"),
    tk.PhotoImage(file="hello2(gif).gif")
]
ceobe.start()

petShowImg = [
    tk.PhotoImage(file="hmm.png"),
    tk.PhotoImage(file="hello2(gif).gif"),
    tk.PhotoImage(file="hello.png"),
    tk.PhotoImage(file="run.png"),
    tk.PhotoImage(file="ilysm.png"),
    tk.PhotoImage(file="please.png"),
    tk.PhotoImage(file="grooming.png"),
    tk.PhotoImage(file="makaseryo.png"),
    tk.PhotoImage(file="ok.png"),
    tk.PhotoImage(file="ike.png"),
    tk.PhotoImage(file="cry.png"),
    tk.PhotoImage(file="shatter.png"),
    tk.PhotoImage(file="happy.png"),
    tk.PhotoImage(file="thumbsup.png"),
    tk.PhotoImage(file="fire.gif"),
    tk.PhotoImage(file="bang.png"),
    tk.PhotoImage(file="hungry.png"),
    tk.PhotoImage(file="eat.png"),
    tk.PhotoImage(file="tasty.png"),
    tk.PhotoImage(file="more.png"),
    tk.PhotoImage(file="sleep.png"),
    tk.PhotoImage(file="gn.png")
]


root.mainloop()



