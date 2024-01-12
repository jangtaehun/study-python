#인간(부모)
# 이름, 나이
    #걷기(walk)
    # '두 발로 걷습니다' 출력

#원숭이(자식)
# 이름, 나이, 동물원 이름
    #걷기(walk)
    # '두 발로 걷습니다', '네 발로 걷습니다' 출력


class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def walk(self):
        print("두 발로 걷습니다.")

class Monkey(Human):
    def __init__(self, name, age, location):
        super().__init__(name, age)
        # self.name = name
        # self.age = age
        self.location = location

    def walk(self):
        super().walk()
        print('네 발로 걷습니다.')

human = Human('jang', 22)
monkey = Monkey('monkey', 2, 'zoo')

human.walk()
print()
monkey.walk()