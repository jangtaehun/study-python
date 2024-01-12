# Comprehension: (어떤 뜻을) 내포하고 있다.
# 반복하거나 특정 조건을 만족하는 list를 쉽게 만들어 내기 위한 방법

#List Comprehensioon
#   [표현식 for 항목 in iterator (if 조건)]
"""
num_list = [1, 2, 3, 4]
result_list = [number * 3 for number in num_list]
print(result_list)

number_list = [1, 2, 3, 4]
#[6, 12]
result_list = [number * 3 for number in number_list if number % 2 == 0]

[표현식 if 조건 else 표현식 for 항목 in iterator
[1, 6, 3, 12]
number_list = [1, 2, 3, 4]
result_list = [number * 3 if number % 2 == 0 else number for number in number_list]
print(result_list)
"""

"""
#실습
# 아래의 list에서 '양수'만 추출한 뒤 새로운 List에 담기
number_list = [10, 20, 30, -20, -3, 50, 70]
new_list = []
[new_list.append(number) if number > 0 else 0 for number in number_list]
print(new_list)

new_list1 = [number for number in number_list if number > 0]
print(new_list1)

# n개의 0으로만 채워진 list
length = int(input("숫자 입력: "))
# new_list1 = [0 for i in range(length)]
new_list1 = [0] * length
print(new_list1)

# 제곱의 결과가 10보다 큰 결과만 담은 list
number_list = [1, -2, 3, -4, 5]
new_list2 = [number for number in number_list if number ** 2 > 10]
print(new_list2)

# 0~9까지 중 3의 배수만 담은 list
new_list3 = [number for number in range(1, 10) if number % 3 == 0]
print(new_list3)
"""