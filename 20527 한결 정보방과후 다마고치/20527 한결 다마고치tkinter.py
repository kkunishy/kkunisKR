import tkinter as tk
import random as rd
#변수
petList=[]
fnt=("맑은 고딕 Semilight",15)
pet_img=[
                    tk.PhotoImage(file="run.png"),
                    tk.PhotoImage(file="hello2(gif).gif"),
                    tk.PhotoImage(file="hello.png"),
                    tk.PhotoImage(file="hmm.png"),
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
                    tk.PhotoImage(file="fire.png"),
                    tk.PhotoImage(file="bang.png"),
                    tk.PhotoImage(file="hungry.png"),
                    tk.PhotoImage(file="eat.png"),
                    tk.PhotoImage(file="tasty.png"),
                    tk.PhotoImage(file="more.png"),
                    tk.PhotoImage(file="sleep.png"),
                    tk.PhotoImage(file="gn.png")
                ]
                    
#함수
class ceobe:
    petName=""
    petAge=0
    petMeal=0
    petNameEntry=0
    petNameWindow=0
    fnt = ("맑은 고딕 Semilight", 15)

    #실행시키자마자 사용
    def __init__(self):

        self.petNameWindow = tk.Tk()
        self.petNameWindow.title("이름 짓기")
        self.petNameWindow.geometry("450x230")
        self.petNameWindow.resizable(False, False)

        petNameLabel=tk.Label(self.petNameWindow,text="케오의 별명을 지어주세요.",font=fnt,padx=20,pady=20)
        petNameLabel.pack()

        self.petNameEntry=tk.Entry(self.petNameWindow,font=fnt)
        self.petNameEntry.pack()

        btnOK=tk.Button(self.petNameWindow,text="확인",font=fnt,command=self.petNameSet)
        btnOK.pack()

    def petNameSet(self):
        self.petName=self.petNameEntry.get()
        self.petNameWindow.destroy()
        
        petNameLabel=tk.Label(root,text="이름:"+self.petName,fg="green",font=fnt)
        petNameLabel.place(x=170,y=430)
        self.petImageSelect()
        
    def petImageSelect(self):
        


    def peteatMeal(self):
        self.petMeal+=1
        canvas.create_text(100,100,text="meal+1",fill="pink",tag="text")

        root.after(1000,self.petMealDel)

    def peteatWater(self):
        self.petWater += 1
        x = rd.randint(20, 380)
        y = rd.randint(20, 380)
        canvas.create_text(x, y, text="water+1", fill="blue", font=fnt, tag="text")
        root.after(500, self.peteatDel())

    def peteatDel(self):
        canvas.delete("text")
                           

def main():
    canvas.create_image(200,200,file=pet_img[0],tag="pet")


def petAdd():
    temp=ceobe()
    petList.append(temp)

#메인
root=tk.Tk()
root.title("조조 키우기")
root.geometry("440x550")
root.resizable(False,False)

petAdd()

canvas=tk.Canvas(width=400,height=400,bg="white")
canvas.place(x=20,y=20)

add_btn=tk.Button(text="추가",bg="white",fg="green",font=fnt,command=petAdd)
add_btn.place(x=20,y=480)

waterImg=tk.PhotoImage(file="water.png")
waterImg=waterImg.subsample(6)
waterBtn=tk.Button(image=waterImg,command=petList)
waterBtn.place(x=110,y=480)

meatImg=tk.PhotoImage(file="meat.png")
meatImg=waterImg.subsample(6)
meatBtn=tk.Button(image=meatImg)
meatBtn.place(x=180,y=480)

meatBtn=tk.Button(image=meatImg)
meatBtn.place(x=180,y=430)

pet_img=[
                    tk.PhotoImage(file="hmm.png"),
                    tk.PhotoImage(file="hello.png"),
                    tk.PhotoImage(file="ike.png")
                    tk.PhotoImage(file="makaseryo.png"),
                    tk.PhotoImage(file="hello2(gif).gif")
    ]

petPicSelect1=tk.PhotoImage(file="hmm.png")
petPicSelect1.subsample((6))
petPicSelect2=tk.PhotoImage(file="hello.png")
petPicSelect2.subsample((6))
petPicSelect3=tk.PhotoImage(file="ike.png")
petPicSelect3.subsample((6))
petPicSelect4=tk.PhotoImage(file="makaseryo.png")
petPicSelect4.subsample((6))
petPicSelect5=tk.PhotoImage(file="hello2(gif).gif")
petPicSelect5.subsample((6))

main()
root.mainloop()






