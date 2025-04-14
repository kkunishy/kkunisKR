#card=""
card_output=""
#age=0
fee_old=41000
fee_sale=0
fee=41000
age_str=""
age_output=""

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print("ㅡㅡㅡ에버랜드 4월 요금표ㅡㅡㅡ")
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
print("성인 요금: ",fee_old,"원")
print("*8세 미만 어린이와 60세 이상 노인은 할인된 가격에 10000원이 추가로 할인됩니다.")
print("현재 할인 카드사:")
print("ㄴ삼성카드 40% 할인")
print("ㄴ네이버페이 30% 할인")
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n\n")

def card_verify():
    global fee, card_output
    while True:
        c=input("카드사를 입력해주십시오: ")
        if c == "삼성카드":
            fee = fee * 0.6
            card_output="삼성카드 사용으로 40% 할인."
            break
        elif c == "네이버페이":
            fee = fee * 0.7
            card_output = "네이버페이 사용으로 30% 할인."
            break
        else:
            print("해당 카드사는 없거나, 저희 놀이공원에서 사용할 수 없는 카드사입니다.")

def age_verify():
    global age_str,age_output,fee
    r = int(input("나이를 입력해주십시오: "))
    if r < 8:
        age_str = "어린이"
        fee = fee - 10000
        age_output='10000원 할인.'
    elif r>60:
        age_str = "노인"
        fee = fee - 10000
        age_output="10000원 할인."
    else:
        age_str = "성인"



print("\n\n에버랜드에 오신 것을 환영합니다.\n\n")
card_verify()
age_verify()
print("==============================")
print("에버랜드 4월 영수증")
print("연령대: ",age_str)
print("==============================")
print("할인: (1) ",card_output)
if age_str=="어린이"or"노인":
    print("할인: (2) ",age_str,"혜텍으로",age_output)
print("==============================")
print("지불금액: ",{int(fee)},"원")
print("할인금액: ",{int(fee_old-fee)},"원")


