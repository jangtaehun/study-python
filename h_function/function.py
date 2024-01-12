# f(x) = 2x + 1

# def f(x):
#     return 2 * x + 1
#
# f(2)
# result = f(2)
# print(result)


num1 = 2
num2 = 4
# 두 정수의 곱셈 함수
def mul(num1, num2):
    return print(num1 * num2)
mul(num1, num2)


# 두 정수의 나눗셈 후 몫과 나머지 구하는 함수
def div(num1, num2):
    if num2 !=0:
        value, rest = num1 // num2, num1 % num2
        return print(f'몫: {value}, 나머지: {rest}')
    return None
div(num1, num2)


# 1~10까지 print()로 출력하는 함수
num3 = 10
def num(num3):
    range_num = [i + 1 for i in range(num3)]
    return print(range_num)
num(num3)


# 이름을 n번 print()로 출력하는 함수
# n = int(input('몇 번?: '))
# def name(n):
#     call = '장태훈 '
#     return print((call * n))
# name(n)
id = 'jangth'
count = 2
def name(id, count):
    for i in range(count):
        print(id)
name(id, count)

# 1~n까지의 합을 구해주는 함수
n = int(input("숫자: "))
def total_sum(n):
    total = 0
    for i in range(n+1):
        total += i
    return print(total)
total_sum(n)


# 1~100까지 중 n의 배수를 print()로 출력하는 함수
n = int(input("숫자: "))
total = []
def print_1_to_100(n):
    for i in range(100):
        if (i+1) % n ==0:
            total.append(i+1)
    print(total)
print_1_to_100(n)


# 세 정수의 뺄셈 함수
a, b, c = map(int, input("세 정수: ").split(" "))
def minus(a, b, c):
    return print(a - b - c)
minus(a, b, c)


# 문자열을 입력받고 원하는 문자의 개수를 구하는 함수
string = input("문자열 입력: ")
n = input("원하는 문자: ")
def count(string, n):
    total = [i for i in string]
    print(total)
    total_count = total.count(n)
    return print(total_count)
    # return len(i for i in string if i == string)
"""
    for i in string:
        if i == string:
            count += 1
    return print(count)
"""
count(string, n)


"""
    문자열과 문자를 입력받은 뒤 해당 문자가 몇 번째 인덱스에 있는 지 검사하고, 만약 해당 문자가 없으면 -1을 리턴하는 함수
"""
string = input("문자열 입력: ")
n = input("원하는 문자: ")
def count_index(string, n):
    total = [i for i in string]
    if n in total:
        for i in range(len(string)):
            total_index = total.index(n)
            return print(total_index)
    print(-1)
"""
    for i in range(len(string)):
        if string[i] == n: return i
    return -1
"""
count_index(string, n)