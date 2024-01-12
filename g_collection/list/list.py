# animals = ['dog', 'cat', 'bird', 'fish']
#
# print(animals)
# print(type(animals))
#
# print(animals[0])
# print(animals[-1])
# print(animals[-2])
# #인덱스 0부터 시작 -> 시작 주소를 담고 있기 때문이다.
# #음수 인덱스 가능(가장 마지막부터 순서대로 앞으로 이동한다)
#
# #len()
# print(len(animals))
#
# #append()
# animals.append("hamster")
# print(len(animals))
# print(animals)
# animals.append('cat') # list는 중복 가능
# print(animals)
#
# #insert()
# animals.insert(1, 'dog')
# print(animals)
#
# #remove()
# animals.remove('fish')
# print(animals)
#
# #del()
# del(animals[1])
# print(animals)
# # del animals[1]
#
# #clear()
# # animals.clear()
# # print(animals)
#
# #index()
# print(animals.index('bird'))
# # print(animals.index('tiger')) 오류
#
# #수정
# animals[animals.index('bird')] = 'lion'
# print(animals)
#
# #그 외
# animals = ['dog', 'cat', 'bird', 'fish']
# print(animals*2) #안에 있는 요소가 반복
#
# print("dog" in animals)
# print("tiger" in animals)
#
# for i in animals:
#     print(i)

#실습
'''
# 1~90까지 list에 담고 출력
num_list = []
for i in range(90):
    num_list.append(i+1)
print(num_list)

# 1_100까지 중 짝수만 list에 담고 출력
num_list = [0] * 50
for i in range(len(num_list)):
    num_list[i] = (i +1)*2
print(num_list)

# 1~10까지 list에 담은 후 짝수만 출력
num_list = []
even_list = []
for i in range(10):
    num_list.append(i + 1)
for i in range(len(num_list)):
    if num_list[i] % 2 == 0:
        even_list.append(num_list[i])
print(even_list)

# 4명의 회원 정보를 list에 담은 뒤 두 번째 회원의 이름을 변경하고 마지막 회원은 삭제
num_list = ['철수', '영희', '맹구', '짱구']
num_list[num_list.index('영희')] = '훈이'
#num_list[1] = '훈이'

del num_list[-1]
#num_list.remove(num_list[-1])
print(num_list)
'''

# "189,000 원"을 189000으로 변경, 제너레이터 사용
s = "189,000 원"
b = ''.join(i for i in s if '0' <= i <= '9') #문자열 안의 정수 -> 조건식에서 자동으로 정수로 바뀐다. => 아스키코드로 형변환된다.
print(b)

# list 안에 list
number_list = [[1, 3, 5], [2, 4, 6]]
#한 번 접근 -> 주소 / 두 번 접근 -> 값
print(number_list[0][0])
print(number_list[0][2])
print(len(number_list))
print()

for i in range(len(number_list)):
    for j in range(len(number_list[i])):
        print(number_list[i][j])