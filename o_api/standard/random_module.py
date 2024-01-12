import random as r

r.randint(1, 10) #(start, end) -> 마지막 수 포함

#randint(시작값, 끝값)
# 1~10까지 중 랜덤한 값 1개


#확률
# 1. list 선언

# 1 -> 100
# 10 -> 10
단위 = 10
단위_dict = {1: 100, 10: 10}

rating = [0] * 단위_dict[단위]
확률 = 30

# 2. 확률을 계산해서 해당 자리에 1대입
for i in range(확률 // 10):
    rating[i] = 1
# 10개 중 1은 3개있기 떄문에, 1이 나올 확률은 30%이다.
if rating[r.randint(0, len(rating)-1)] == 1:
    print('강화 성공')
