#인덱스 슬라이싱
animals = ['dog', 'dog', 'cat', 'bird', 'fish']

#list[inclusive_start=0 : exclusive_end=len(list) : step(default = 1)] -> list
#step => 메모리를 많이 소모해서 거의 안 쓴다.
print(animals[0])
print(animals[0:3])
print(animals[1:4])
print(animals[:2])
print(animals[2:])
print(animals[:])
print(animals[:-1])

food = ['noodle', 'meat', 'bread', 'chicken']
print(food[:3:2])
print(food[2::2])

#역순 출력
print(food[::-1])

number_list = list(range(1, 11))
print(number_list)

# #실습
# #[1,3,5,7,9]
# print(number_list[::2])
#
# #[6,5,4,3,2]
# print(number_list[5:0:-1])
#
# #[2,4,6]
# print(number_list[1:6:2])
#
# #[2,3,4,5,6,7]
# print(number_list[1:7])

animals = ['dog', 'dog', 'cat', 'bird']
zoo = ['panda', 'giraffe']

animals[1:2] = zoo
print(animals)

#기존 값은 뒤로 밀리고 해당 자리에 값이 들어간다.
animals.insert(animals.index('dog')+1, 'giraffe')
print(animals)

#기존 값은 뒤로 밀리고 zoo list 통채로 들어간다.
animals.insert(animals.index('dog')+1, zoo) #list 자체가 들어간다.
print(animals)

#실습
#슬라이싱, insert, del을 사용해 아래의 list 만들기
#['dog', 'hamster', 'fish', 'dog', 'whale', 'bird']
zoo = ['dog', 'hamster', 'fish', 'dog', 'whale', 'bird']
del zoo[1:5]
zoo.insert(zoo.index('dog'), 'dog')
zoo.insert(zoo.index('bird'), 'cat')
print(zoo)
# 결과 => animals = ['dog', 'dog', 'cat', 'bird']

animals = ['dog', 'dog', 'cat', 'bird']
del animals[animals.index('cat')]
print(animals)
animals[-2:-3:-1] = ['whale']

animals[1:3] = ['hamster', 'fish', 'dog', 'whale', 'bird']
print(animals)