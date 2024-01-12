#정렬
num_list= [5, 3, 7, 9, 1]

# 1. sort() -> 원본을 바꾼다.
# num_list.sort() # 오름차순
# num_list.sort(reverse=True) # 내림차순
# print(num_list)
# print(num_list[::-1])

# 2. sorted() -> 원본은 유지되고 새로운 list가 만들어 진다.
sorted_num_list = sorted(num_list)
print(sorted_num_list)
sorted_num_list = sorted(num_list, reverse=True) #내림차순
print(sorted_num_list)

