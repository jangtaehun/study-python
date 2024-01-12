# 상품
# 상품명, 가격
# 상품의 정보를 print()로 출력하는 함수

# stock = []
# class Product:
#     def __init__(self, product, price, stock):
#         self.product = product
#         self.price = price
#         self.stock = stock
#
#     def show(self):
#         stock.append({'product': self.product, 'price': self.price, 'stock': self.stock})
#         print(stock)
#
#
# # 마켓
# # 상품, 재고
# # 손님 한 명에게 한 개의 상품을 판매한다.
# # 판매 시 손님의 할인율을 적용하여 판매한다.
# class Market:
#     def __init__(self, product):
#         self.product = product
#         # self.stock = product.stock
#
#     def sell(self, customer):
#         self.customer = customer
#         discount_price = self.product.price * (1 - customer.sale * 0.01)
#         print(int(discount_price), product.stock)
#
#         for i in range(len(stock)):
#             if product.stock[i]['name'] == product.product.name:
#                 index = product.stock[i]
#
#
# # 손님
# # 이름, 나이, 할인율, 잔액
# class Customer:
#     def __init__(self, name, age, sale, money):
#         self.name = name
#         self.age = age
#         self.sale = sale
#         self.money = money
#
#
# product = Product('name', 1000, 3)
# product.show()
# customer = Customer('이름', 20, 20, 20000)
#
# market = Market(product)
# market.sell(customer)
#
# product.show()


# def market(self, obj, sale):
#     if obj in self.stock:
#         for i in range(len(self.stock)):
#             if self.stock[i]['name'] == obj:
#                 index = self.stock[i]
#                 del self.stock[self.stock.index(a)]
#         self.count -= 1
#         price = self.price * (1 - sale)



#상품
# 상품명, 가격
# 상품의 정보를 print()로 출력하는 함수
class Product:
    # 상품명, 가격
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def print_info(self):
        print(self.name, self.price)


#손님
# 이름, 나이, 할인율, 잔액
class Customer:
    # 이름, 나이, 할인율, 잔액
    def __init__(self, name, age, discount=0, money=0):
        self.name = name
        self.age = age
        self.discount = discount
        self.money = money


#마켓
# 상품, 재고
# 손님 한 명에게 한 개의 상품을 판매한다.
# 판매 시 손님의 할인율을 적용하여 판매한다.
class Market:
    def __init__(self, product):
        self.product = product
        # self.stock = stock

    def sell(self, customer):
        customer.money -= self.product.price * (1 - customer.discount * 0.01)
        product.stock -= 1

# 객체화
product = Product('사과', 3000, 40)
customer = Customer('한동석', 20, 30, money=10000)

market = Market(product)

market.sell(customer)

# print(market.stock)
print(product.stock)
print(customer.money)
