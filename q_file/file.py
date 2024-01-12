#절대 경로 => 대한민국 서울시 강남구 역삼동 ....
#어떤 위치에 있든 상관없이 찾아갈 수 있는 경로
#C:/a/b, D:/User/ted, ...

#상대 경로 => 직진해서 좌회전 후 오른쪽 건물
#현재 위치에 따라 변경되는 경
#./: 현재 경로, ../: 이전 경로, ./src/images, ../../a/b, src/images

#파일 생성하기
# file = open('food.txt', 'w', encoding='UTF-8')
# file.write('오늘 점심 뭐 먹지\n')
# file.write('부대찌개')
# file.close()

#파일 추가
# file = open('food.txt', 'a', encoding='utf-8')
# file.write('\n햄버거')
# file.close()

#파일 읽기
try:
    file = open("food.txt", "r", encoding='utf-8')
    print(file.readlines())

    # for i in range(4):
    #     print(file.readline())
    #     #빈 문자열 출력

    line = None
    while line != '':
        line = file.readline()
        print(line)
    file.close()

except FileNotFoundError:
    print('경로 확인!')


#with를 사용하면 자동으로 file이 close된다.
with open('food.txt', 'r', encoding='utf-8') as file:
    print(file.readlines())
print()

#수정
#외부 파일을 담을 수 있는 공간
content = ''
with open('food.txt', 'r', encoding='utf-8') as file:
    line = None
    #전체 내용을 한 줄씩 읽어오기
    while line != "":
        #한 줄을 line에 담기
        line = file.readline()
        #담은 내용이 찾고 있는 것일 경우
        if line == '부대찌개햄버거':
            #content에 치킨으로 변경해서 담기
            content += '치킨\n'
            continue
        #수정 대상이 아닌 줄은 그대로 content에 담기
        content += line
    #수정 완료된 문자열 값 확인
    print(content)

#기존의 내용을 수정 완료된 문자열로 덮어쓰기
with open('food.txt', 'w', encoding='utf-8') as file:
    file.write(content)

#원본 파일 내용 확인
with open('food.txt', 'r', encoding='utf-8') as file:
    print(file.readlines())

"""
# 외부 파일에 있는 내용을 담아줄 변수
content = ""
with open('food.txt', 'r', encoding='utf-8') as file:
    line = None
    # 전체 내용을 한 줄씩 읽어오기
    while line != '':
        # 한 줄을 line에 담기
        line = file.readline()
        # 담은 내용이 찾고 있는 햄버거일 경우
        if line == '햄버거\n':
            # content에 치킨으로 변경해서 담기
            content += '치킨\n'
            continue

        # 수정 대상이 아닌 줄은 그대로 content에 담기
        content += line

    # 수정 완료된 문자열 값 확인
    print(content)

# 기존의 내용을 수정 완료된 문자열로 덮어쓰기
with open('food.txt', 'w', encoding='utf-8') as file:
    file.write(content)

# 원본 파일의 내용 확인
with open('food.txt', 'r', encoding='utf-8') as file:
    print("".join(file.readlines()))
"""