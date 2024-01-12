def set_key(key):
    formatting = ''

    # 클로저
    def set_value(value):
        nonlocal formatting # 바꿀 때 필요
        formatting = f'{key}: {value}'
        return formatting

    return set_value

set_name = set_key('이름')
formatting_name = set_name("장태훈")
print(formatting_name)
print()


# '나이: 00살'
set_name = set_key('나이')
formatting_age = set_name("20살")
print(formatting_age)
print()

print(f'{formatting_name} : {formatting_age}')
print('\n')


###############

# 이름(name) 또는 주제(topic) 및 요약(point), 둘 중 하나를 전달할 수 있다.
# 제작하는 함수는 각각 아래와 같은 형식의 문자열로 변환한다.
# 함수1. "name, 전달받은 이름"
# 함수2. "전달받은 주제, 전달받은 요약"
# 구분점은 기본 값이 ', '이고 원하는 구분점을 전달받아서 변경할 수 있다.
# 함수1과 함수2를 합쳐서 하나의 함수로 만든다.
# 구분점은 각 함수에서 전달받는다.

def set_topic(**kwargs):
    formatting = ''

    if 'name' in kwargs:
        def set_point(comma= ','):
            # nonlocal formatting
            formatting = f'name {comma} {kwargs["name"]}'
            return formatting

    else:
        def set_point(comma= ','):
            # nonlocal formatting
            formatting = f'{kwargs["topic"]} {comma} {kwargs["summary"]}'
            return formatting

    return set_point


a = set_topic(name='zzone')
for_a = a(comma="/")
print(for_a)
print(set_topic(name='zzone')(comma="::::"))


b = set_topic(topic='zzoneddeock', summary="유투버 고양이 이름")
for_b = b(comma=":")
print(for_b)
print(set_topic(topic='zzoneddeock', summary="유투버 고양이 이름")(comma=':::::'))
print('\n')


# 상품 정보(상품명, 가격)를 여러 개 전달받은 뒤 번호를 1부터 순서대로 붙여준다.
# 함수1. 상품의 정보를 추가하는 함수
# 함수2. 상품의 정보를 수정하는 함수
# 함수3. 상품의 전체 정보를 조회하는 함수
# 함수1, 함수2, 함수3을 합쳐서 하나의 함수로 만든다.

def set_product1(*args):
    number = 0

    for product in args:
        number += 1
        product['number'] = number

    def insert(**kwargs):
        nonlocal number, args
        number += 1
        args += {'name': kwargs.get('name'), 'price': kwargs.get('price'), 'number': number},
        #튜플에 딕셔너리를 연결하려고 했기 때문에 오류 -> 마지막에 ,를 붙인다.

    def update(**kwargs):
        for product in args:
            if product['number'] == kwargs.get('number'):
                product['name'] = kwargs.get('name')
                product['price'] = kwargs.get('price')
                break
    def show():
        return args

    return {'insert': insert, 'update': update, 'show': show}

products = [
    {'name': '귤', 'price': 2000},
    {'name': '딸기', 'price': 3000},
    {'name': '사과', 'price': 4000},
]
product_service = set_product1(*products)
# print(product_service)
product_service.get('insert')(name='모니터', price=80000)
a = product_service['show']()
print(a)

