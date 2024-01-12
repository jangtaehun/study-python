#fish.txt
#사용자에게 입력 받은 물고기를 fish.txt에 작성한다.
#사용자가 a에 입력하면, fish.txt의 전체 내용을 삭제한다.
#사용자가 r을 입력하면, fish.txt의 전체 내용을 큰 솥에 출력한다.

# title = 'q(삭제), r(출력)'
#
# while True:
#     fish = input('물고기 입력: ')
#
#     with open('fish.txt', 'w', encoding='utf-8') as file:
#         file.write(fish + '\n')
#
#     word = input(title)
#     if word == 'q':
#         with open('fish.txt', 'a', encoding='utf-8') as file:
#             pass
#     else:
#         try:
#             with open('fish.txt', 'r', encoding='utf-8') as file:
#                 for line in file.readlines():
#                     print(line, end="")
#                     break
#         except FileNotFoundError:
#             print('error')


# title = 'q: 삭제, r: 읽기'
# message = '물고기: '
#
# while True:
#     path = input('경로: ')
#     fish = input(title + '\n' + message)
#
#     if fish == 'q':
#         with open(path, 'w', encoding='utf-8') as file:
#             pass
#
#     elif fish == 'r':
#         try:
#             with open(path, 'r', encoding='utf-8') as file:
#                 for line in file.readlines():
#                     print(line, end='')
#             break
#         except FileNotFoundError:
#             print('경로를 다시 확인해주세요.')
#
#     else:
#         with open(path, 'a', encoding='utf-8') as file:
#             file.write(fish + '\n')


# 고등어를 참치로 수정하기
content = ''
with open('fish.txt', 'r', encoding='utf-8') as file:
    line = None
    while line != '':
        line = file.readline()
        if line == '고등어':
            content += '참치'
            continue
        content += line

with open('fish.txt', 'w', encoding='utf-8') as file:
    file.write(content)
with open('fish.txt', 'r', encoding='utf-8') as file:
    print(file.readlines())