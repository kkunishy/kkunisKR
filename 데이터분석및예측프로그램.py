def int_enter(a,p):
    a=list()
    for i in range(1,p+1):
        a.append(int(input()))
    return a
def average(k,a_average,k1,p):
    for i in range(0,k):
        a_average=sum(k1)/p
        return a_average
#a값
k=int(input("자료 가짓수(26이하):"))
p=int(input("a값 개수:"))
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','v','z']
k1=list()
for i in range(0,k):
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
        n.append(k1[h][i]-average_value[h]) 
    m.append(n[h*p:(h+1)*p]) 
print('n;',n) 
print('m;',m)
#오류1-a의 편차가 0이되는경우 
while(int(m[0].count(0))>0): 
    e=int(m[0].index(0)) 
    for i in range(1,k): 
        if (m[i][e]==0): 
            m[0][e]=1 
            m[i][e]=1 
        else: 
            m[0][e]=1/3 
