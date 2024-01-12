class Magic:
    def __init__(self, name):
        self.name = name

    #초기화된 필드를 확인하고자 할 때 사용된다.
    def __str__(self):
        # return f'{self.__repr__()}, __repr__(self)로 사용됨'
        return f'name: {self.name}'

#객체를 출력하면 항상 __repr__()가 자동으로 뒤에 붙는다.
#print(Magic()) -> 문자열로 나온다. __repr__(self)가 생략된 것이다. -> 자동으로 쓰이며, 재정의하면 안 된다. 하고싶으면 __str__(self) 사용
# print(Magic().__repr__())

#만약 해당 클래스에서 __str__()을 재정의했다면 __repr__가 아니라 __str__()이 사용된다.
#따라서 생략해서 작성하면 __str__()이 붙게 된다.
#print(Magic()__str__())

magic = Magic('jang')
print(magic)


class Student:
    def __init__(self, number, score):
        self.number = number
        self.score = score

    def __add__(self, other):
        return self.score + other.score #객체.score -> 객체를 전달받았다.

    def __eq__(self, other): # 비교: 주소 -> 타입 -> 값
        # 주소 비교
        if self.__repr__() == other.__repr__():
            print('들어옴')
            return True

        # 타입 비교
        # isinstance(객체, 타입): 전달한 객체가 전달한 타입일 경우 True, 아니면 False
        if isinstance(other, Student):
            # 값 비교
            return self.number == other.number

std1 = Student(10, 30)
std2 = Student(10, 50)
total = std1.__add__(std2) #total = std1 + std2
print(total)

print(std1.__dict__)
print(std1.__dict__.__getitem__('score'))
print([1, 2, 3].__getitem__(2))
print([1, 2, 3].__contains__(1))
print()

print(std1 == std2) #주소를 비교하기 때문에 False
print()

std3 = Student(10, 20)
std4 = std3
print(std4==std3)