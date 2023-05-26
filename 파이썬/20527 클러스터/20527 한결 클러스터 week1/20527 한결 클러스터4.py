sI = set([1,2,3])
sII = set("hello")

#print(sI, sII)

sIII = set([2,3,4,7])
sIV = set([0,2,4,6,8])

print(sIII & sIV)               # == sIII.intersection(sIV)

print(sIII | sIV)               # == sIII.union(sIV)

print(sIV - sIII)               # == sIV.difference(sIII)

#관련 함수

sIII.add(11)
sIII.update([13,17])
sIII.remove(4)

print(sIII)
