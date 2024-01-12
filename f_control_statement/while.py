'''
# 이름 10번 출력
count = 0
while count != 10:
    print("이름")
    count += 1
# for문 사용
'''

# 사용자가 입력한 정수가 몇 자리수인지 출력
# 1. 사용자에게 정수를 입력받는다
# 2. 입력받은 정수의 각 자리수를 센다.
# 3. 자리수를 출력한다.
# 힌트: 몫(자리수 출력할 때), 나머지(정수 출력할 때)

message = '정수를 입력하세요.\n'
num = int(input(message))
leng = 0

while num:
    num //= 10
    leng += 1
print(leng)
