


money = True            #변수
if money:
    print("택시를 타고 간다")
else:
    print("걸어간다.")



if money:
#'''
#여러줄 이상 주석           # <- #지울시 문자열로 인식하여 작동되지 않음. '''''' 쓸시 주의.
#'''
    print("택시를 타고 간다")
        #print("2번 택시")                   # <- #지울시 unexpected indent 출력
else:
    print("걸어간다.")

#들여쓰기가 중요!!



# > < <= >= == != 
#이때, ==와 =는 다른 의미를 가지고 있음.
x = 4
y = 4
print(4 > 1)            #true를 출력
print(x != y)           #false를 출력



#and or not
money = 2000
card = True
if money >= 3000 or card:         #money는 조건을 충족하지 않지만 card를 소유하고 있으므로 조건에 충족함.
    print("택시를 타고 걸어간다.") #or연산자를 사용하므로 둘 중 하나의 조건만 충족해도 됨.
else:
    print("걸어간다.")



#in /not in
a = [1,2,3]
print(1 in a)

con = True
if con:
    pass            #조건에 충족하므로 아무 행동 없이 건너뜀
else:
    print("패스안함")



#조건문
score = 90         
if score >= 80:
    print("합격입니다.")        
elif score >= 70:
    print("재시험입니다.")
elif score >= 60:
    print("불합격입니다.")
else:
    print("발닦고 잠이나 자세요.")



#조건부 표현식
message = "합격" if score >= 70 else "불합격"           #이때, print를 써주지 않으면 출력되지가 않음.

print(message)

