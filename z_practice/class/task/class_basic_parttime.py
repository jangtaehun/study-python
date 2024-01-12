# '모든 직원'에 공통적으로 적용되는 내용
# - 시급
# - 직원수

# '각 직원'별로 적용되는 내용
# - 별명
# - 근무지(기본값: '청담동')
# - 급여 총액(초기값: 0, 생성자로 초기화 불가능)

# 직원 급여 계산
#   '근무 시간 + 상여금'에 따른 직원 급여 계산
#   '상여금'은 지정 하지 않으면 0 으로 처리

class PartTimer:
    pay_of_hour = 10000
    total_of_part_timers = 0

    def __init__(self, name, location='청담동'):
        self.name = name
        self.location = location
        self.total_pay = 0
        PartTimer.total_of_part_timers += 1

    def calculate(self, work, bonus=0):
        total_money = PartTimer.pay_of_hour * work + bonus
        self.total_pay += total_money
        return total_money


a = PartTimer('jang', 'aaa')
b = PartTimer('tae')

print(a.name, a.location, a.total_pay)
print(a.calculate(8, 8000))
print(a.total_pay)
print()

ryan = PartTimer('라이언')
neo = PartTimer('네오', '역삼동')

print(ryan.name, ryan.location, ryan.total_pay)
result = ryan.calculate(8, 10000)
print(ryan.name, ryan.location, ryan.total_pay)