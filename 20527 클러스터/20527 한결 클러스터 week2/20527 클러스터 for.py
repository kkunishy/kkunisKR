#   for each

#   c# java javascript
#   for(x=0; x<10; x++)
#
#   x=0
#   while x<10:
#       x+=1

lst = ['one', 'two', 'theree']

for i in lst:
    print(i)

t = [(1,2), (3,4), (5,6)]
for (i,j) in t:
    print(i + j)




#점수를 한명씩 채첨해서 합격과 불합격을 출력해주는 코드
scores = [90, 67, 12, 85, 52]


number = 0
for score in scores:
    number += 1
    if score >= 60:
        print(f"{number}번 수험생은 {score}점, 합격입니다.")
    else:
        print(f"{number}번 수험생은 {score}점, 불합격입니다.")





#continue, break
number = 0
for score in scores:
    number += 1
    if score <= 60:
        continue
    else:
        print(f"{number}번 수험생은 {score}점, 합격입니다. ", end = '')
    print("다음,")



#break를 사용하여 에러 회피
number = 0
scores[2] = -1
for score in scores:
    number += 1
    if score < 0 or score > 100:
        print(f"{number}번 점수가 범위를 벗어났습니다.")
        break
    print(f"{number} PASS")



#range()함수
add = 0
for i in range(1, 11):
    add = add + 1
print(add)

for number in range(len(scores)):
    if scores[number] < 60:
        continue
    print(f"{number+1}번 수험생 합격입니다.")

#다중 루프
#구구단을 출력

#for i in range(2,10):

#리스트 컴프리헨션
#(표현식) for (항목) in (빈복가능객체) if (조건문)
