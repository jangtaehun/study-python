"""
class Member:
    number = 0
    def __init__(self, id, password, name):
        self.id = id
        self.password = password
        self.name = name
        Member.number += 1

        print(self.id, self.password, self.name, Member.number)

    @classmethod
    def manager(cls, id, password, name, number=0):
        id = f'admin_' + id
        number += 1
        return cls(id, password, name)

member1 = Member('zzoneddeock', 12345, 'jth')
member2 = Member.manager('jangth', 12345, 'jang')
"""


#회원
# 번호, 아이디, 비밀번호, 이름
# 번호는 자동으로 1씩 증가한다.
# 관리자로 회원가입 시, 아이디 앞에 'admin_'을 자동으로 붙여준다.(class method)
class Member:
    # private: 자신의 클래스에서만 접근 가능 / 다른 언어에서도 접근 가능 -> 다른 언어는 메소드만 접근 가능 / 메소드로 접근해라
    # 1. 외부에서 접근하지 말자!
    # 2. 외부에서 접근할 때 꼭 메소드로 접근하자!
    __number = 0

    def __init__(self, id, password, name):
        self.id = id
        self.password = password
        self.name = name
        Member.__number += 1

        print(self.id, self.password, self.name, Member.__number)

    @classmethod
    def manager(cls, **kwargs):
        kwargs['id'] = 'admin_' + kwargs.get('id')
        return cls(**kwargs)

    @staticmethod
    def get_number():
        return Member.__number

    @staticmethod
    def set_number():
        return Member.__number + 1


user = Member('jth', 1234, 'jang')
print(user.id)
print()

user = Member.manager(id='admin1', password=1234, name='jang')
print(user.id)
print()

print(Member.get_number())
print(Member.set_number())