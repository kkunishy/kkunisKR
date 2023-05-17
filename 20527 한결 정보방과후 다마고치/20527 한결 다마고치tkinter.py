import tkinter as tk
import random as rd
#변수
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
    petWater

    #실행시키자마자 사용
    def __init__(self,new_petName,new_petAge):
        self.petName=new_petName
        self.petAge=new_petAge

    def __del__(self):
        print(self.petName, "를 떠나보냅니다... ㅠㅠ\n")

    def petInfoPrint(self):
        print("이름:",self.petName)
        print("나이:",self.petAge)
        print("[상태]:")

        if self.petMeal==0:
            print("배고픈 상태...\n")
        else:
            print("행복한 상태! \n")
    
    def petMealAdd(self):
        self.petMeal+=1
        canvas.create_text(100,100,text="meal+1",fill="pink",tag="text")

        root.after(1000,self.petMealDel)

    def petMealDel(self):
        canvas.delete("text")

    def petWaterAdd(self):
        self.water+=1
        canvas.create_text(100,100,text="water+1",fill="blue",tag="text")

        root.after(1000,self.petWaterDel)

    def petWaterDel(self):
        canvas.delete("text")
                           

def main():
    canvas.create_image(200,200,file=pet_img[0],tag="pet")



#메인
root=tk.Tk()
root.title("조조 키우기")
root.geometry("440x550")
root.resizable(False,False)

canvas=tk.Canvas(width=400,height=400,bg="white")
canvas.place(x=20,y=20)

add_btn=tk.Button(text="추가",bg="white",fg="green",font=fnt)
add_btn.place(x=20,y=430)

import tk as tk
#변수
fnt=("맑은 고딕 Semilight",15)


#함수

#메인
root=tk.Tk()
root.title("조조 키우기")
root.geometry("440x550")
root.resizable(False,False)

first=ceobe()
canvas=tk.Canvas(width=400,height=400,bg="white")
canvas.place(x=20,y=20)

add_btn=tk.Button(text="추가",bg="white",fg="green",font=fnt,command=first.petWaterAdd)
add_btn.place(x=20,y=430)

water_img=tk.PhotoImage(file="water.png")
water_img=water_img.subsample(6)

water_btn=tk.Button(image=water_img)
water_btn.place(x=100,y=430)

meat_img=tk.PhotoImage(file="meat.png")
meat_img=water_img.subsample(6)

meat_btn=tk.Button(image=meat_img)
meat_btn.place(x=180,y=430)

main()
root.mainloop()






