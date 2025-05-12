employee_num=3
total=0

for i in range(employee_num):
    rank=int(input('직급: '))
    basic_salary=int(input('본봉: '))
    if rank>=2:
        bonus=basic_salary*0.3
    else:
        bonus=basic_salary*0.2
    salary=basic_salary+bonus
    total+=salary
print('월급총액: ',total)
