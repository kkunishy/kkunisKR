#고객데이터:리스트
customers = []

#메뉴구성:딕셔너리
#메뉴함수:종료0,정보입력1,정보수정2,정보삭제3,정보출력4
menu = {
    0: "종료",
    1: "고객정보입력",
    2: "고객정보수정",
    3: "고객삭제",
    4: "고객정보출력"
}

def reg_cm():
    print("\n=== 고객정보입력 ===")
    name = input("이름: ")
    password = input("암호: ")
    while True:
        gender = input("성별 (1:남성, 2:여성): ")
        if gender in ['1', '2']:
            gender = int(gender)
            break
        print("잘못된 입력입니다. 1 또는 2를 입력하세요.")
    birth = input("생년월일 (YYYYMMDD): ")
    phone = input("전화번호: ")
    address = input("주소: ")

    # 리스트 형식으로 저장
    customer = [name, password, gender, birth, phone, address]
    customers.append(customer)
    print("고객 정보가 등록되었습니다.")

def mod_cm():
    print("\n=== 고객정보수정 ===")
    if not customers:
        print("등록된 고객이 없습니다.")
        return
    
    name = input("수정할 고객의 이름을 입력하세요: ")
    for customer in customers:
        if customer[0] == name:  # 이름0
            password = input("암호를 입력하세요: ")
            if password == customer[1]:  # 암호1
                customer[0] = input("새 이름: ")
                customer[1] = input("새 암호: ")
                while True:
                    gender_input = input("새 성별 (1:남성, 2:여성): ")
                    if gender_input in ['1', '2']:
                        customer[2] = int(gender_input)  # 성별 2
                        break
                    print("잘못된 입력입니다. 1 또는 2를 입력하세요.")
                customer[3] = input("새 생년월일 (YYYYMMDD): ")  # 생년월일 3
                customer[4] = input("새 전화번호: ")  # 전화번호4
                customer[5] = input("새 주소: ")  # 주소 5
                print("고객 정보가 수정되었습니다.")
                return
            else:
                print("암호가 일치하지 않습니다.")
                return
    print("해당 이름의 고객을 찾을 수 없습니다.")

def del_cm():
    print("\n=== 고객삭제 ===")
    if not customers:
        print("등록된 고객이 없습니다.")
        return
    
    name = input("삭제할 고객의 이름을 입력하세요: ")
    for i, customer in enumerate(customers):
        if customer[0] == name:  # 이름0
            password = input("암호를 입력하세요: ")
            if password == customer[1]:  # 암호1
                del customers[i]
                print("고객 정보가 삭제되었습니다.")
                return
            else:
                print("암호가 일치하지 않습니다.")
                return
    print("해당 이름의 고객을 찾을 수 없습니다.")

def prt_cm():
    print("\n=== 고객정보출력 ===")
    if not customers:
        print("등록된 고객이 없습니다.")
        return
    
    for customer in customers:
        print("\n고객 정보:")
        print(f"이름: {customer[0]}")
        print(f"성별: {'남성' if customer[2] == 1 else '여성'}({customer[2]})")
        print(f"생년월일: {customer[3]}")
        print(f"전화번호: {customer[4]}")
        print(f"주소: {customer[5]}")

def main():
    while True:
        print("\n=== 고객 관리 프로그램 ===")
        for key, value in menu.items():
            print(f"{key}. {value}")
            
        select = int(input("메뉴를 선택하세요: "))
        
        if menu.get(select) == "종료":
            print("프로그램을 종료합니다.")
            break
        elif menu.get(select) == "고객정보입력":
            reg_cm()
        elif menu.get(select) == "고객정보수정":
            mod_cm()
        elif menu.get(select) == "고객삭제":
            del_cm()
        elif menu.get(select) == "고객정보출력":
            prt_cm()
        else:
            print("잘못된 메뉴 선택입니다.")

main()