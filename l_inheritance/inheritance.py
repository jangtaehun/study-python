class A:
    def __init__(self, name):
        self.name = name
        print('부모 생성자')

    def print_intro(self):
        print('A')

#자식 생성자는 무조건 부모 생성자 먼저 호출한다.
class B(A):
    def __init__(self, name, age=0): #self = B
        super().__init__(name) #super = 부모 객체
        self.age = age #자식에서 만든 건 자식에서 새롭게 초기화
        print('자식 생성자')

    def add(self, number1, number2):
        return number1 + number2

    def print_intro(self):
        #부모의 메소드를 그대러 사용하고자 할 때 사용
        super().print_intro() #재정의를 하더라도 부모에게 있는 것을 사용하고자할 때 사용
        #자식의 메소드에서 추가할 내용 작성
        print('B')

b = B('장태훈') #b 객체 생성: 해당 필드(B)가 메모리에 할당이 되고, 주소값을 가지고와서 저장한다.
# print(b.name)
# b.print_intro()
print(b.add(1, 2))