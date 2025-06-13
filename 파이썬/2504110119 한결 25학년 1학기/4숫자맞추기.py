import random

print('1부터 100까지의 수 하나가 정해졌습니다')
print('이 수를 맞추시오')

answer=random.randint(1,100)
times=0

while True:
    user=int(input('1~100 입력'))
    times+=1
    if user==answer:
        break
    elif user<answer:
        print(f'{user}보다 큽니다.')
    else:
        print(f'{user}보다 작습니다.')
print(f'정답입니다! {times} 안에 맞혔습니다.')