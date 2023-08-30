def int_enter(a,p):                                     #자료의 값을 입력받는 함수
    a=list()
    for i in range(1,p+1):
        a.append(int(input()))
    return a
def average(k,a_average,k1,p):                      #평균값을 구하는 함수
    for i in range(0,k):
        a_average=sum(k1)/p
        return a_average

#a값
k=int(input("자료 가짓수(26이하):"))               #자료의 가짓수 입력
p=int(input("자료 개수:"))                             #자료의 개수 입력
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','v','z']
k1=list()
for i in range(0,k):		                              #자료의 값 저장- 2차원 배열
    print(alphabet[i])
    k1.append(int_enter(alphabet[i],p))
    print(k1[i])
#평균
average_value=list()
for i in range(0,k):
    average_value.append(average(k,alphabet[i]+'평균',k1[i],p))
print('평균값:',average_value)
#편차
n=list()
m=list()
for h in range(0,k):
    for i in range(0,p):
        n.append(k1[h][i]-average_value[h])         #리스트n에 편차-1차원 배열
    m.append(n[h*p:(h+1)*p])                        #리스트m에 편차-2차원 배열
print('n;',n)
print('m;',m)



# 오류1-a의 편차가 0이 되는 경우- 분모가 0이라 연산 불가

while int(m[0].count(0))>0:                     # 기준자료a의 편차에 0이 있는지 확인
    e=m[0].index(0)                                # 0이 있는 위치 e에 저장
    el= list()
    el.append(e)                                    # e의 값을 리스트el에 저장
    for i in range(1,k):                             # 기준 자료a제외 자료에서 확인
        if m[i][e]==0:                             # 2가지 경우-0/0
            m[0][e]=1                               # 임의로 a의 0인 편차에 1대입-추후 제외
            m[i][e]=1                                # 임의로 a이외 다른 자료의 0인 편차에 1대입
            r=list()                                   # 동일 위치 편차 사이 비율-m?/n?-일차원
            R=list()                                  # 동일 위치 편차 사이 비율-m?/n?-이차원
            for h in range(1,k):                    # r에 값 입력
                for j in range(0,p):
                    r.append(m[h][j]/m[0][j])
                R.append(r[(h-1)*p:h*p])         # R에 값 입력
                Rm = sum(R[i-1])                 # R의 값의 평균측정
                R[i-1][e]=(Rm-1)/(p-1)           # 0/0인 경우 제외하고 계산
        else:                                         # 2가지 경우-실수/0
            m[0][e]=1/3                            # 임의로 a의 0인 편차에 수치 대입-2차시 때
            r=list()                                  # 동일 위치 편차 사이 비율-m?/n?-일차원
            R=list()                                 # 동일 위치 편차 사이 비율-m?/n?-이차원
            for h in range(1,k):                   # r에 값 입력
                for j in range(0,p):
                    r.append(m[h][j]/m[0][j])
                R.append(r[(h-1)*p:h*p])        # R에 값 입력
                Rm = sum(R[i-1])                 # R의 값의 평균측정
                R[i-1][e]=(Rm-1)/(p-1)

# 출력
print("k1=",k1)
print("a;",k1[0])

for i in range(1,k):
    print(alphabet[i],";",k1[i])
for i in range(0,k):
    print(alphabet[i],"average_value;",average_value[i])
for i in range(0,k):
    print(alphabet[i],"편차;",m[i])

print("a?,b? => a?가 a평균값에서 1 멀어질때 b?는 m?/n?의 평균 만큼 멀어진다")
print("r;",r)
print("R;",R)

# 예측
for j in range(0,p):
    at = int(input("test a;"))
    for i in range(1,k):
        print(alphabet[i],";", average_value[i]+(at-average_value[0])*sum(R[i-1])/5)
