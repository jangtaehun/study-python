number = 15
if number % 3 == 0:
    print(f"{number}는 3의 배수입니다.")
if number % 5 == 0:
    print(f"{number}는 5의 배수입니다.")


# number가 양수인지, 음수인지, 0인지 출력
'''
positive_condition = number > 0
negative_condition = number < 0
zero_condition = number == 0

if positive_condition:
    print(f'{number}는 양수입니다.')
elif negative_condition:
    print(f'{number}는 음수입니다.')
else:
    print(f'{number}')
'''

# 나이를 입력받은 후 미성년자인지 검사
'''
age = int(input('나이: '))
condition = 0 < age < 20
error_condition = age <= 0

if condition:
    print(f'{age}은 애기')
elif error_condition:
    print(f'잘못 입력')
else:
    print(f'{age}은 성인')
'''

# 두 정수를 입력받은 후 대소 비교
# 선언할 때 초기 값을 모를 경우 초기값을 넣어준다
# 정수: 0
# 실수: 0.0
# 문자열: '' 또는 ""
# 불린: False

# ❤️
# 일괄처리란,
# 각 분기별로 결과를 처리하지 않고
# 모든 분기가 종류 후 한 번에 처리하는 것을 의미한다.
'''
result = ""
num1, num2 = map(int, input("두 정수를 입력하세요: ex)10 20\n").split(' '))

if num1 > num2:
    result = f'{num1}이 더 크다.'
elif num1 == num2:
    result = '같다'
else:
    result = f'{num2}이 더 크다.'

print(result)
'''