#디지털 배열

arr = [[1,2,3,4,5], [6,7,8,9,10]]

print(arr[0][1])

n = 1
for i in arr:
    for j in i:
        print(j, end = " ")
    print("|", end = " ")

#i가 첫번째 동작시에 i == [1,2,3,4,5]
#j에 i의 각각의 원소[1,2,3,4,5]를 넣어줌
print("\n")
print("\n")

arr3 = [[[1,2,3],[4,5,6,]],[[7,8,9],[10,11,12]]]

for i in arr3:
    for j in i:
        for k in j:
            print(k, end = " ")
        print("|", end = "")
    print("/", end = "")

print("\n")
print("\n")

def add(x,y):
    return x + y

function = add
print(function(1,4))

lambdaFunc = lambda x,y: x+y
print(lambdaFunc(1,7))