# 중복이 없고, 순서가 없다.
# 중복 제거할 때 사용
world_set = {'korea', 'america', 'japan', 'china'}
print(type(world_set))
print(len(world_set))
# print(world_set[0]) # 에러

world_set.add("korea")
print(world_set)

# 자료 가져오기
#   다른 자료형으로 변환한 후 가져온다.

datas = [1, 1, 2, 3, 2, 1, 3, 4, 5, 2, 1, 5, 3, 1, 1]
print(list(set(datas)))
# 자동으로 정렬이 된다.