# '택시'에서 승객들에게 공통적으로 적용되는 자료
# - 기본 요금 : 5800원
# - 기본 주행 거리 : 2km
# - 택시 요금(기본 주행 거리 이후 거리 1km 당 요금)  : 1000원

# 택시 객체 생성시 승객별로 돈과, 거리를 받아서 생성

# 거리에 따른 요금 계산 메소드 정의
# 거리에 따른 잔돈 계산 메소드 정의

class Taxi:
    # 클래스 변수 -> 모든 인스턴스가 동일한 값을 사용하고자 할 때 사용 / 인스터스, 클래스 접근 O
    price = 5000
    de_distance = 2
    plus = 1000

    def __init__(self):
        self.income = 0

    def calculate(self, money, distance):
        # 인스턴스 변수 -> 클래스를 기반으로 만들어지느 모든 인스턴스들이 각각 따로 저장하는 변수 / 인스턴스마다 다른 값을 저장 / 클래스 접근 X
        # 인스턴스 메소드 -> 인스턴스 변수를 사용하는 메소드
        cost = Taxi.price
        if distance > self.de_distance:
            cost += (distance - self.de_distance) * self.plus

        self.income += cost

        #클로져
        def change():
            return money - cost

        return cost, change()

# Taxi 인스턴스 생성
taxi = Taxi()
print(taxi.calculate(100000, 10))
print(taxi.income)
