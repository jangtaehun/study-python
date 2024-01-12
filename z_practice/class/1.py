
class Bank:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @classmethod
    def open_account(cls, **kwargs):
        # print(kwargs) # {'a': 'a', 'b': 'b'}
        user = [ShinHan, KookMin, KaKao][1](**kwargs)
        print(user)

class ShinHan(Bank):
    pass

class KookMin(Bank):
    pass

class KaKao(Bank):
     pass

a = ShinHan(a='a', b='b')
# print(a)
a.open_account(a='a', b='b')

#kwargs
#콤마로 구분하여, key=value 형태로 전달
class Bank:
    def __init__(self, a, b):
        self.a = a
        self.b = b

a = {'a': 1, 'b':2}
user = Bank(**a)
print(user)
# **kwargs는 함수 호출시에 사용되며, 이는 딕셔너리의 키를 인자명으로,
# 그에 대응하는 값을 인자값으로 사용
# Bank 클래스의 인스턴스를 생성할 때 a와 b라는 두 개의 인자를 필요
# kwargs 딕셔너리에 a와 b라는 키와 그 값들을 저장하고
# 이를 Bank의 __init__ 메소드에 전달
# **kwargs = Bank(a=1, b=2) = kwargs

#packing = 여러 개의 변수를 하나의 리스트나 튜플로 묶는 것
#unpacking = 리스트나 튜플의 각 원소를 개별 변수에 할당하는 것
#**kwargs는 함수에 전달될 때 딕셔너리의 각 키-값 쌍을 개별 키워드 인자로 'unpack'