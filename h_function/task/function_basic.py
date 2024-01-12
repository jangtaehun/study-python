# 회원의 주문 금액(pay)과 회원의 쿠폰 할인율과 개수(coupon, count)를 전달받은 뒤
# 회원이 보유한 쿠폰의 할인율을 주문 금액에 순차 적용하는 함수 제작
# 할인율이 적용된 주문 금액이 정수로 리턴된다.
# 쿠폰의 할인율은 백분율로 되어있다.
# 쿠폰의 개수는 주문 개수보다 많을 수 있다.
# comprehension을 사용한다.


# 쿠폰 종류는 단 1개, 쿠폰 할인율은 40과 같은 1~100사이의 정수
#
# coupon=40
# count=5
#
# 아래와 같이 무조건 1개 종류의 쿠폰 여러 장이다.
# 40%쿠폰 5개
#
# 아래와 같은 상황은 없다.
# 10%쿠폰 1개, 20%쿠폰 2개


# 회원의 주문 금액(pay)과 회원의 쿠폰 할인율과 개수(coupon, count)를 전달받은 뒤
# 회원이 보유한 쿠폰의 할인율을 주문 금액에 순차 적용하는 함수 제작
# 할인율이 적용된 주문 금액이 정수로 리턴된다.
# 쿠폰의 할인율은 백분율로 되어있다.
# 쿠폰의 개수는 주문 개수보다 많을 수 있다.
# comprehension을 사용한다.

# 입력 예시1
# [2000, 4000, 5000]
# coupon=50
# count=2

# 출력 예시1
# [1000, 2000]


# 입력 예시2
# [1000, 4000, 5000]
# coupon=30
# count=100

# 출력 예시2
# [700, 2800, 3500]


input_price = [1000, 1000, 5000, 2000, 1000]
def sale_price1(*args, **kwargs):
    """
    가격 리스트, 쿠폰 할인율, 쿠폰 개수를 입력받아 할인율을 계산한 가격 리스트를 반환하는 함수
    :param args: packing된 가격을 전달 받는다.
    :param kwargs: input_count인 쿠폰의 개수, input_coupon인 할인율을 받는다.
    :return: 리스트에서 쿠폰의 개수만큼 할인율이 계산된 가격만 반환한다.
    """
    total = [] #빈리스트를 만든다.
    count = kwargs["input_count"] #kwargs로 받은 input_count 즉, 쿠폰의 개수를 count에 저장
    money = [i for i in args[0]] #args로 받은 list형식의 input_price를 list형식으로 추출하기 위해 args의 첫 번째 요소를 money에 저장
    for i in money[:count]:
        pay = int(i * (1 - kwargs["input_coupon"] / 100))
        total.append(pay)
    return print(total)
    #money에 저장된 값을 슬라이싱 연산을 이용해 처음부터 쿠폰 갯수만큼 가져오기 위해 for을 이용했다.
    #money list에 저장된 값이 쿠폰보다 많으면 쿠폰만큼 가져오고 적으면 list에 저장된 값만 가져온다.
    #가져온 각각의 money를 input_coupon에 저장된 할인율만큼 계산한 후 pay에 저장하고 빈 리스트 total에 저장한다.

def sale_price2(*args, **kwargs):
    """
    가격 리스트, 쿠폰 할인율, 쿠폰 개수를 입력받아 할인율을 계산한 가격 리스트를 반환하는 함수
    :param args: packing된 가격을 전달 받는다.
    :param kwargs: input_count인 쿠폰의 개수, input_coupon인 할인율을 받는다.
    :return: 리스트에서 쿠폰의 개수만큼 할인율이 계산된 가격만 반환한다.
    """
    # money = [i for i in args[0]] #args로 받은 list형식의 input_price를 list형식으로 추출하기 위해 args의 첫 번째 요소를 money에 저장
    # return print([int(pay * (1 - kwargs["input_coupon"] / 100)) for pay in money[:kwargs["input_count"]]])
    return print([int(pay * (1 - kwargs["input_coupon"] / 100)) for pay in args[0][:kwargs['input_count']] ])
    #money list에 슬라이싱 연산을 이용해 매개변수로 입력받은 input_count 즉, 쿠폰의 개수만큼 list에서 가져와 pay에 저장한다.
    #pay에 저장된 값을 백분율 계산을 한 후 반환한다.

sale_price1(input_price, input_coupon=30, input_count=1)
sale_price1(input_price, input_coupon=30, input_count=100)
help(sale_price1)
sale_price2(input_price, input_coupon=30, input_count=100)
sale_price2(input_price, input_coupon=30, input_count=1)


def use_coupon(*pay, **kwargs):
    '''
    :param pay: 주문 금액들
    :param kwargs: {coupon: 할인율, count: 쿠폰의 개수}
    :return: 할인율이 적용된 주문 금액들
    '''
    if 'coupon' in kwargs:
        return [int((1 - kwargs.get('coupon') * 0.01) * pay[i]) for i in range(kwargs.get('count') if kwargs.get('count') <= len(pay) else len(pay))]

    return None


help(use_coupon)
result = use_coupon(1000, 2000, 3000, coupon=50, count=100)

if result:
    print(result)
else:
    print('쿠폰이 없습니다.')