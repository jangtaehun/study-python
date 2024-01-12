# 1~15까지 출력
for i in range(15):
    print(i+1, end=" ")
    if i == 14:
        print()

# 30~1까지 출력
for i in range(30):
    print(30 - i, end=" ")
    if i == 29:
        print()

# 1~100까지 홀수 출력
for i in range(50):
    print(i*2+1, end=" ")
    if i == 49:
        print()


# 1~10까지 합 출력
sum = 0
for i in range(10):
    sum += (i+1)
    print(sum, end=" ")
    if i == 9:
        print()


# 1~n까지 합 출력
sum = 0
n = int(input('정수를 입력하세요: '))
for i in range(1, n+1):
    sum += i
    print(sum, end=" ")
    if i == n:
        print()
print(sum)


# 3 4 5 6 3 4 5 6 3 4 5 6 출력
for i in range(3):
    for i in range(4):
        print(i+3, end=" ")
    if i == 3:
        print()

for i in range(12):
    print(i % 4 + 3, end=" ")
print()


# '1,235,500'를 1235500으로 출력
string = '1,235,500'
result = ''
for i in string:
    if i != ',':
        result += i
result = int(result)
print(result)