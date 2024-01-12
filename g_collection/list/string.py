# print(list("ABC"))

# for i in "ABC":
#     print(i)

#upper(), lower()
print("Apple123~@#".upper())
print("Apple123~@#".lower())

# split()
data = "사과, 바나나, 파인애들, 포토, 복숭아"
data = data.split(",", maxsplit=2) # 두 번째까지만 구분한다.
print(data)

print("A B C D E F G H I J K".split())
print("A             B".split())
print("A       \n     B".split())
print("A             B".split(" "))

#join()
print(":".join(['a', 'b', 'c']))
print("".join(['a', 'b', 'c']))

#replace('기존 값', '새로운 값')
print("A b C d".replace(" ", ""))
print("안녕! 반가워~!".replace("!", "?"))

#strip(), lstrip(), rstrip()
print("       a        b           c     ".strip())
print("     a        b           c     ".lstrip(" "))
print("      a        b           c     ".rstrip(" "))
print("apple".strip("p"))
print("apple".strip("a")) #맨 앞, 맨 뒤에 해당 공백/문자 제거
print("apple".strip("e"))

#index
print("ABC".index("A"))
# print("ABC".index("Z")) -> 오류

#find: 찾고자 하는 값이 없으면 -1을 출력 / 찾는 것이 목적
print("ABC".find("A"))
print("ABC".find("Z"))

#in: 있는지 없는지 확인 목적 / 없으면 False 출력
print("A" in "ABC")

#count(): 전달한 값이 몇 개인지 검사
print("asjdfnskfhsfdhksjfsdfladoeoofroeigjrkdsn\n\n".count("o"))

price_list = [1,2,3,4,5,6,6,7,8]
price = 4
min =1
max = 8
[price for price in price_list if min <= price <= max]
