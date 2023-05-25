dict = {"name":"jun","phone":"010-0101-0101","birth":"0120"}            #정의가 중복될시 뒤에 오는 dict는 무시됨, 권고하지 않음


#임시로 문자열화
'''
a = {0: 0}
b = {1: 'b'}
c = {"c":[1,2,3]}

a['a'] = 1
b[1] = 'b'
del c['c'][1]


print (a,b,c)

print(dict["name"])
'''


#dict함수

print(list(dict.keys()))

print(list(dict.items()))


#dict.clear()                #클리어
#print(dict)

#dict.get("tele")           #none을 출력
#dict["tele"]               #에러를 출력
#print(dict.get("tele"))    #''
#print(dict['tele'])        #'' 

print(dict[dict.get("tele", "phone")])                  #A가 없으면 B를 배출
print('name' in dict)  #true                                 #bool형으로 배출
print('tele' in dict)  #false                                #''

