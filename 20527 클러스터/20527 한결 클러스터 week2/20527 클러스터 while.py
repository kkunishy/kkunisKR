#while for 
#C# java for each

#반복 for: for each
"""
#반복문
score = 70
x = 0
while x < 10:                        #반복될때마다 x를 1씩 추가하여,
    x += 1                          #x가 10에 도달할경우 루프를 멈춤.
    print("실행 {x}번.")
    if x == 10:
        print("실행 끝.")           #들여쓰기를 한번 더.

"""

#x의 값을 임의로 계속 더해주는 코드
option ="""
    1.add
    2.exit
"""

select = 0                                  # :happythoughts:
x = 0               
while select != 2:                          #select가 2가 아닐때까지 반복
    print(f"\nx = {x}")                     #x의 값을 출력
    print(option)                           #menu 출력
    select = int(input())                   #메뉴를 입력받아 select에 저장
    if select == 1:                         #입력받은 select가 1이면
        x = x + 1                           #x에 1을 더해 저장함
    elif select != 2:                       #입력받은 select가 1과 2가 아니면
        print("not on the menu")            #메뉴에 없다고 표시.



                    #number = x + y + calculate(x,y)

                    
#while 
'''
while True:
    print("1")          #ctrl+c로 빠져나오기
'''
