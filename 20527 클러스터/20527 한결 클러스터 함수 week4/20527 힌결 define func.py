'''
def function(매개변수):
    #내용
    return #리턴
'''

def add(x,y):
    return x+y

print(add(7,6))         #프린트

def welcome():
    return "hello world!"

print(welcome())

def printAdd(x,y):
    print(f"{x}+{y}={x+y}")

printAdd(3,9)


'''             #에러를 일으킴
1 = [1,2,3]
for i in 1:
    x=1

print(x)
'''

def listsum(args):
    sum = 0
    for i in args:
        sum += 1
    return sum


#tmplist[]
