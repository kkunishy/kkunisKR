import random
dice1=random.randint(a=1,b=6)
dice2=random.randint(a=1,b=6)
print(f'주사위1:{dice1}주사위2:{dice2}')

if dice1>dice2:
    print("주사위1 승")

elif dice1<dice2:
    print("주사위2 승")
else:
    print("무승부")

asdfa=random.randint(a=123,b=123123)
print(int(asdfa))