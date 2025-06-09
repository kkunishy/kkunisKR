langs={'python':0,'C':0,'Java':0,'JS':0}

while True:
    s=input('선호하는 언더(python,C,Java,JS) 또는 종료')
    if s=='종료':
        break
    if s in langs:
        langs[s]+=1
    else:
        print(f'{s}는 존재하지 않습니다.')
for key,value in langs.items():
    print(key,value)

    