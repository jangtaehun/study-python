import os
import psutil

# process_object = psutil.Process(os.getpid())
# memory_before = process_object.memory_info().rss / 1024 / 1024
#
# data_list = [i ** 2 for i in range(100)]
# print(data_list)
#
#
# memory_after = process_object.memory_info().rss / 1024
#
#
#
# data_generator = (i ** 2 for i in range(100))
# print(data_generator) #대기 중 메모리 사용X
# print(next(data_generator))

#실행중인 프로그램 -> 프로세스

def increas(number: int = 0):
    while True:
        number += 1
        yield number

result = increas()
while True:
    data = input("Y/N >> ")
    if data == 'Y':
        print(next(result))
    else:
        break