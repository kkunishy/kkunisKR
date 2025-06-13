employee_num = 3
total = 0
for i in range(employee_num):
    rank = int(input('직급: '))
    basic_salary = int(input('본봉: '))
    if rank >= 2:
        bonus = basic_salary * 0.3
    else:
        bonus = basic_salary * 0.2
    salary = basic_salary + bonus
    total += salary
    print(f'본봉: {basic_salary}원')
    print(f'보너스: {bonus}원')
    print(f'총 급여: {salary}원')
    
print('\n전체 월급총액:', total, '원')