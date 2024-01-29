# 'aPPle', 'BananA', 'meLON'을 모두 소문자로 변경
string = ['aPPle', 'BananA', 'meLON']
print(list(map(lambda string: string.lower(), string)))


# 입력받은 한글을 정수로 변경
# 입력 예: 삼오일구
# 출력 예: 3519
hangul = "공일이삼사오육칠팔구"
data = "삼오일구"
print(int("".join(list(map(lambda s: str(hangul.index(s)), data)))))

# 입력받은 정수를 한글로 변경
# 입력 예: 3519
# 출력 예: 삼오일구
# hangul = "공일이삼사오육칠팔구"
# data = 3519
# print("".join(list(map(lambda s: hangul[int(s)], str(data)))))
# print("".join(list(map(lambda s: hangul[ord(s) - 48], str(data)))))



# 'user/join', 'user/login', 'post/write', 'order/pay', 'order/list', 'post/read'
# 위 경로 중 회원 서비스가 아닌 경로만 추출
# 1. 서비스명(user, post, order)으로 변경(map)
# 2. 서비스명 중 'user'가 아닌 경로만 추출(filter)
# 출력 예시
# ['post', 'order', 'order', 'post']

urls = ['user/join', 'user/login', 'post/write', 'order/pay', 'order/list', 'post/read']
print(list(map(lambda urls: urls.split('/')[0], urls)))
print(list(map(lambda url: url[:url.index("/")], urls)))

print(list(filter(lambda urls: urls.split('/')[0] != 'user', urls)))

print(list(filter(lambda service: service != 'user', list(map(lambda urls: urls.split('/')[0], urls)))))

urls = [1,2,3,4,5,6,7]

result = [i for i in range(0, len(urls)) if urls[i] > 4]
print(result)
for i in range(0, len(urls)):
    print(urls[i] > 4)