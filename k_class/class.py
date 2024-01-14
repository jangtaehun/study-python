class A:
    @classmethod
    def __new__(cls, *args, **kwargs): #메모리에 할당, 생성자 -> 리턴한 값을 init한테 준다. / 할당자, 메모리에 올린다.
        obj = super().__new__(cls)
        return obj

    # 처리 -> 생성자라고 한다. / new, init은 한 쌍
    def __init__(self,  data1, data2, name=''): # 초기화, 생성자
        # 생성자는 외부에서 전달받은 값으로
        # 해당 필드의 객체에 전달받은 값들을 각각 초기화한다.
        print(self)
        self.name = name
        self.data1 = data1
        self.data2 = data2

    # def print_name(self, name):
    #     print(name)

    def print_name(self, name):
        print(self.name)
        print(name)
        # print(self.data1, self.data2)

#객체화 / 필드가 객체화 될 때마다 새로 생성된다. a필드, b필드, ... => a, b는 다른 주소를 가지고 있다.
#a = 객체
a = A(10, 20, name='ddeock') # new -> 메모리 할당, 주소 -> init의 self에 주소가 담긴다. -> 객체에 담긴다.
# 객체를 변수에 할당하면 해당 변수는 객체를 참조. 즉, 해당 객체가 메모리 상에 위치한 주소를 가리키게 됩니다.
# print(a) #주소값이 나온다. A의 객체다.
# print(a.data1, a.data2)

a.print_name('zzone')
# a.data1 = 10
# a.data2 = 20
print()

b = A(100, 200, 'jangth') #A의 객체 생성 = 인스턴스 생성 -> b 객체 생성: 해당 필드(A)가 메모리에 할당이 되고, 주소값을 가지고와서 저장한다.
print(b) #주소값이 나온다. A의 객체다. => 주소가 self로 전달되었다.
b.print_name('zzoneddeock') #b를 self로 전달: 접근한 객체의 주소값이 전달된다(오브젝트). / 인수를 전달 / 객체가 접근할 때는 주소값이 간다. -> self
print(b.data1, b.data2)
b.print_name('ddeock')
b.data1 = 1
b.data2 = 2
b.print_name('ddeock')