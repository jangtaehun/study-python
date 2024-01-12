# mutable: 변할 수 있는
data_list1 = [1, 2, 3, 4]
data_list2 = data_list1
data_list2[0] = 10
print(data_list1)
print(data_list2)
print()
print()


# immutable: 변할 수 없는
data_tuple1 = (1, 2, 3, 4)
data_tuple2 = data_tuple1

# data_tuple2[0] = 10 # 에러
# tuple을 list로 바꿔서 바꾼다.
# tuple -> 추가 가능
test = list(data_tuple2)
test[0] = 10
print(test)
print()
print()


data_tuple2 = data_tuple1 + (5, 6)
print(data_tuple2)

datas = 1, 2
print(type(datas))
print(datas[0])

#파이썬 상수 선언 => 대문자로 (약속)
ERROR_CODE = 1,
print(type(ERROR_CODE))
print(ERROR_CODE[0])
print()
print()

a = (1,2,3,4) + (1,2,3)
print(id(a))
b = (5,6,7,8)
print(a)
print(id(a))