print("Hello")

number=3
string="Python"
list=['one',2,'three',4]
dictionary={'name':'john','phone':111111}
tuple=('a',1,'b',2)
set={'apple','banana','orange'}
bool=True

#if
money=True

if money:
    print("돈이 없다.")
else:
    print("돈이 없다.")
'''
score=int(input("점수 입력:"))
print(type(score))

if score>=80:
    print("A")
elif score >= 70:
    print("B")
else:
    print("C")
'''
#while
count=3
while count>0:
    print(f"count:{count}")
    count-=1

#for
students=[{'name':'Park','score':70},{'name':'Lee','score':80},{'name':'Han','score':60}]

for student in students:
    if student["score"]>=80:
        print(f"{student['name']}:A")
    elif student["score"] >= 70:
        print(f"{student['name']}:B")
    else:
        print(f"{student['name']}:C")


for count in range(1,6):
    print(f"cooldown,{count}")

#func

def funcname():
    print("Hello function")


funcname()

funcname()

funcname()

def add(arg1,arg2):
    return arg1+arg2

print(add(5,6))


#절대경로
"C:/users/..."

#상대경로
"/users/..."     #최상위디렉토리
"./folders/..."  #현재 디렉토리
"../Workspace/folders/..." #상위 디렉토리
"D:/Programs/Project/Workspace/folders/week00"

# PS D:/Programs/Project/Workspace>