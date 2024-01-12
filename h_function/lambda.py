# 람다(lambda): 이름이 없는 함수, 일회성
# lambda 매개변수, ...: 리턴값

#일반 함수
def add(num1, num2):
    return num1 + num2

#익명 함수
lambda num1, num2: num1 + num2


# map = 바꿀려고 사용한다. map(함수, iterable) => map(어떻게 바꿀 것인가, list/tuple)
# num1, num2 = map(int, input("두 정수를 입력하세요\nex)1, 3\n", ).split(','))
# print(num1 * num2)
print(list(map(lambda num: num+2, [1, 2, 3, 4])))
print()

#실습
# 아래의 list의 각 요소에 2를 곱하여 변경
datas = [2, 4, 6, 8]
print(list(map(lambda num: num*2, datas)))

# 각 경로 앞에 '/app'을 붙여준다
urls = ['/game', '/news', '/fashion', '/ranking']
print(list(map(lambda str: '/app' + str, urls)))


#fillter(function, iteratar)
#1~10까지 중 짝수만 출력
print(list(filter(lambda num: num % 2 == 0, [i + 1 for i in range(10)])))

# 바꿀 때 map
# 추려낼 때 filter

# 'game': 서비스를 제공하는 경로 찾기
urls = ['/app/game', '/app/news', '/app/fashion', '/app/ranking']
print(list(filter(lambda str: 'game' in str, urls)))
print(list(filter(lambda str: str.split('/')[-1] == 'game', urls)))