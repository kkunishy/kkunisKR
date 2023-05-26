a = ()
b = (1,)
c = 1,2,3                #이때, 튜플로 저장이 가능
d = (1,2,3)
e = ('a','b',['ab','cd'])


print(e[1])
print(d[0:2])


#e[1] = 'c'                 #error를 출력
#del e[1]                   #''

t1 = d+e
t2 = d * 2

print(t1)
print(t2)