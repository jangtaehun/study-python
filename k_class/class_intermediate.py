
class Car:
    # 모든 객체가 공유하는 변수 => 정적 변수 = static variable
    wheel = 4
    def __init__(self, brand='', color='', price=0):
        self.brand = brand
        self.color = color
        self.price = price

    def engine_start(self):
        print(self.brand + '시동 켜짐')

    def engine_stop(self):
        print(self.brand + '시동 꺼짐')

mom_car = Car('Benz', 'Black', 15000)
daddy_car = Car('BMW', 'Blue', 8800 )

mom_car.engine_start()
daddy_car.engine_start()

mom_car.engine_stop()
daddy_car.engine_stop()

print(Car.wheel)

# Car.wheel = 6
# print(Car.wheel)

# new에서 먼저 받는다. new의 cls 매개변수
cars = [Car, Car]
mom_car = cars[0]()
daddy_car = cars[1]()
print(mom_car, daddy_car, sep='\n')