#linux vs windows

#C:/users/
#C:\users\

#python은 경로계열이므로 일반슬래쉬 선호

#젇대경로
str="C:/users/"            
print(str)

#상대경로
"/Users/use/"              #현재 디렉토리의 최상위 디렉토리에서 시작
"./temp/"                  #현재 디렉토리
"../week2/"                #현재 디렉토리의 상위 디렉토리\

#파일 열기 모드
#r : 읽기모드
#w : 쓰기 모드
#x : 파일이 없으면 생성하고 쓰기 모드
#a : 추가모드(뒤에 이어쓰기)
try:
    f = open("./20527 클러스터/test.txt", 'x')          #파일 생성
except:
    f = open("./20527 클러스터/test.txt", 'w')          #이미 생성되어 있다면, 쓰기모드로 바뀜
f.write(input())

f.close()