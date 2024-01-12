# input("이름: ") => 값, 문자열
'''
name = input("이름: ")
print(name + "님 환영합니다.")
formatting = f'{name}님 환영합니다.'
print(formatting)
'''

# 문자열끼리만 연결이 가능하다. / (+) 연산, 연결 구분
'''
data = 3
print('안 ' + str(data))
'''

# 제 이름은 ???, 키는 ???cm 입니다.
'''
name = input("이름: ")
height = input("키: ")
formatting1 = f'제 이름은 {name}입니다. 키는 {height}cm 입니다.'
print(formatting1)
'''

# 두 정수를 입력받은 후 곱셈 결과 출력
'''
first_num = input("first_num: ")
second_num = input("second_num: ")
result = f'{int(first_num) * int(second_num)}'
print(result)
'''

"""
map = 바꿀려고 사용한다. map(함수, iterable) => map(어떻게 바꿀 것인가, list/tuple)
num1, num2 = map(int, input("두 정수를 입력하세요\nex)1, 3\n", ).split(','))
print(num1 * num2)
# 함수도 값이다.
# split -> list
print('a,b,c'.split(',')[0])
a, b, c = 'a,b,c'.split(',')
print(a, b, c)
"""

"""
message = '두 정수를 입력하세요'
example_message = '예) 1, 3'
num1, num2 = map(int, input(message + "\n" + example_message + "\n" ).split(', '))
result = num1 * num2
formatting3 = f'{num1} * {num2} = {result}'
print(formatting3)
"""

# 실습
# 현재 시간을 입력하고 시와 분으로 분리하여 출력
message = '현재 시간을 입력하세요'
example_message = '예) 12:45'
time, min = map(int, input(message + "\n" + example_message + "\n").split(':'))
formatting4 = f'시간: {time}시, 분: {min}분\n'
print(formatting4)

# 핸드폰 번호를 -(하이픈)과 함께 입력받은 뒤 각 자리의 번호를 분리해서 출력
message = '핸드폰 번호를 입력해주세요'
example_message = '예) 010-1234-5678'
fir, sec, thir = map(str, input(message + "\n" + example_message + "\n").split("-"))
formatting5 = f'default: {fir}, 앞 번호: {sec}, 뒷 번호: {thir}\n'
print(formatting5)

# 이름과 나이를 한 번에 입력받은 뒤 "000님의 나이는 000살" 형식으로 출력
message = '이름, 나이'
example_message = '예) 이름, 나이'
name, age = input(message + "\n" + example_message + "\n").split(", ")
formatting6 = f'{name}님의 나이는 {age}살\n'
print(formatting6)

# 3개의 정수를 입력받은 뒤 덧셈 결과 출력
message = '세 개 정수'
example_message = '예) 1 2 3'
fir, sec, thir = map(int, input(message + "\n" + example_message + "\n").split(" "))
formatting7 = f'{fir} + {sec} + {thir} = {fir + sec + thir}\n'
print(formatting7)