e = [3, 2, ["a","b","c"]]

#인덱싱과 슬라이싱 
'''
print(e[0])
print(e[1])
print(e[2])


print(e[0:2])
print(e[-1][1:])
'''
#numbers 숫자          정수, 실수, 복소수
#sequence 시퀸스        문자열, 리스트, 튜플
#apping  매핑          딕셔너리, 집합


#수정 삭제
del e[1]
print(e)

del e[-1][1:]
print(e)

'''
append
sort
insert
remove
pop 
extend

count
index
'''

list_shityourself = [1, 2, "A","a",["life", "is", "too"]]
str = ["short"]


#list.append ([4, 3])

#append ?
# list_shityourself.sort(reverse = TRUE)
#print(list_shityourself)

list_shityourself.insert(3, '8')
print(list_shityourself)

list_shityourself.remove('a')
print(list_shityourself)

#list.pop(4)
#print(list_shityourself)

list_shityourself.extend([1, 2, 5])
print(list_shityourself)

list.reverse()
print(list_shityourself)