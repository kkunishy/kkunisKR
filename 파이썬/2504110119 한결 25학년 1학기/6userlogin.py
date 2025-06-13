def val_id(user_id):
    if len(user_id) < 5:
        return False
    
    alpha_count = sum(c.isalpha() for c in user_id)
    digit_count = sum(c.isdigit() for c in user_id)
    
    return alpha_count > 0 and digit_count > 0

def val_pw(password):
    if len(password) < 5:
        return False
    
    alpha_count = sum(c.isalpha() for c in password)
    digit_count = sum(c.isdigit() for c in password)
    special_count = sum(not c.isalnum() for c in password)
    
    return alpha_count > 0 and digit_count > 0 and special_count > 0

def adduser():
    while True:
        user_id = input("ID(5자 이상 문자+숫자 조합): ")
        if not val_id(user_id):
            print("유효하지 않은 ID 형식입니다. 다시 입력해주세요.")
            continue
        if user_id in id:
            print("이미 존재하는 ID입니다. 다시 입력해주세요.")
            continue
        break
    
    while True:
        password = input("PW(5자 이상 문자+숫자+특수문자 조합): ")
        if not val_pw(password):
            print("유효하지 않은 비밀번호 형식입니다. 다시 입력해주세요.")
            continue
        break
    
    id.append(user_id)
    pw.append(password)
    print("user가 추가되었습니다.")

def moduser():
    while True:
        search_id = input("수정할 ID를 입력하세요: ")
        if search_id in id:
            idx = id.index(search_id)
            while True:
                new_pw = input("새로운 비밀번호를 입력하세요: ")
                if val_pw(new_pw):
                    pw[idx] = new_pw
                    print("비밀번호가 수정되었습니다.")
                    return
                else:
                    print("유효하지 않은 비밀번호 형식입니다. 다시 입력해주세요.")
        else:
            print("해당 ID를 찾을 수 없습니다. 다시 입력해주세요.")

def deluser():
    while True:
        search_id = input("삭제할 ID를 입력하세요: ")
        if search_id in id:
            idx = id.index(search_id)
            id.pop(idx)
            pw.pop(idx)
            print("user가 삭제되었습니다.")
            break
        else:
            print("해당 ID를 찾을 수 없습니다. 다시 입력해주세요.")

def seruser():
    while True:
        search_id = input("검색할 ID를 입력하세요: ")
        if search_id in id:
            idx = id.index(search_id)
            print(f"ID: {id[idx]}, PW: {pw[idx]}")
            break
        else:
            print("해당 ID를 찾을 수 없습니다. 다시 입력해주세요.")

def prtuser():
    print("SHELL\n")
    for i in range(len(id)):
        print(f"ID: {id[i]}, PW: {pw[i]}")

id = []
pw = []


for i in range(0,5):
    adduser()

while True:
    print("\n1: user 추가")
    print("2: user 수정")
    print("3: user 삭제")
    print("4: user 검색")
    print("5: user 목록 출력")
    print("6: 종료")
    
    choice = input("원하는 작업을 선택하세요 (1-5): ")
    
    if choice == '1':
        if len(id) >= 5:
            print("최대 5명까지만 등록 가능합니다.")
            continue
        adduser()
    elif choice == '2':
        moduser()
    elif choice == '3':
        deluser()
    elif choice == '4':
        seruser()
    elif choice == '5':
        prtuser()
    elif choice == '6':
        print("종료합니다.")
        break
    else:
        print("잘못된 선택입니다.")