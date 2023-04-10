#입력
#str = input()
#print(type(str))            #<class 'type'>를 출력


#real_number = int(input("숫자를 입력하세요:"))
#print(type(real_number))

#출력
print("life""is""too short")
tmp1 = "life" "is" "too short"              #콤마 X
tmp2 = "life", "is", "too short"            #콤마 O
cat_str = "life" + "is" + "too short"

print(cat_str)
print(tmp1)
print(tmp2)
print("life", "is", "too short")

print("save key", "ctrl", "C", sep = "|", end = "ABCD")
print("save key", end = "|")
print("Ctrl", "C")

def add(x,y=7):
    return x + y

print(add(1))

