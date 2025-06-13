prices={'아메리카노':2000,'라떼':3000,'녹차':2500}
sum=0

while True:
    s=input('음료 종류 또는 종료: ')
    if s=='종료':
        break
    if s in prices:
        n=int(input(f'{s} 주문 수량: '))
        sum+=prices[s]*n
    else:
        print('잘못된 입력입니다.')
print(f'총 금액: {sum}원')
