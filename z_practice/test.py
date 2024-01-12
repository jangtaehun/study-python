def check(*, key: str, value: str) -> dict:
    for bank in Bank.banks:
        for user in bank:
            if user.get(key) == value:
                return user
    return None
# 중복 검사 / 핸드폰 번호와 계좌 번호를 이용해 검사한다. -> key, value 이용
# Bank 클래스에 선언된 클래스 변수로 선언된 bank 리스트(DB)를 불러와 bank에 각각 저장하고
# bank를 다시 user로 각각 저장해 리스트 안의 리스트에 접근해 key가 value와 같으면 해당 리스트를 반환한다.


class Bank:
    total_count = 3 # 은행의 개수
    banks = [[] for count in range(total_count)] # 컴프리핸션을 이용해 banks라는 리스트에 세 개의 빈 리스트를 만든다.

    # 생성자를 이용해 인스턴스 변수를 만든다.
    # __init__은 메모리를 할당하지 않는다. -> __new__가 메모리 할당
    def __init__(self, owner: str, account: str, phone: str, password: str, money: int):
        self.object = self  # 각 회원의 object 필드에는 필드의 주소값이 담긴다
        self.owner = owner
        self.account = account
        self.phone = phone
        self.password = password
        self.money = money


#어떤 은행에서 개설하는 지를 bank_choice로 전달받는다.
#개설에 필요한 모든 회원정보는  **kwargs로 받는다. / 임의의 키워드 인수들을 수용
    @classmethod
    def open_account(cls, bank_choice, **kwargs):
        print(kwargs)
        user = [ShinHan, KookMin, KaKao][bank_choice-1](**kwargs) #함수 호출시에 사용
        # ShinHan, KookMin, KaKao 세 개의 클래스를 원소로 가지는 리스트를 생성 = 모두 Bank 클래스를 상속
        # 리스트 인덱싱을 이용해 리스트의 원소를 선택

#kwargs = {'owner': 'jang', 'account': '111', 'phone': '109089', 'password': '1234', 'money': 1000}
        # -> KookMin(**kwargs)
        # KookMin 클래스를 이용해 클래스의 인스턴스를 생성 -> user에 할당
        # **kwargs는 키워드 인자를 사용한 함수 호출 방식으로, kwargs라는 딕셔너리의 각 키-값 쌍을 인자로 넘겨준다.
        # kwargs는 Bank 클래스의 __init__ 메소드에 필요한 인자를 담고 있다.

# self.object는 open_account 메서드를 호출할 때 전달되는 인자가 아니라, __init__ 메서드 내에서 객체가 생성되는 과정에서 자동으로 설정되는 인스턴스 변수
# KookMin이라는 클래스의 인스턴스를 생성할 때 __init__ 메서드가 호출되며, 이 메서드 내에서 self.object 값이 초기화됩니다.


        # 객체를 변수에 할당하면 해당 변수는 객체를 참조. 즉, 해당 객체가 메모리 상에 위치한 주소를 가리키게 됩니다.

        # -> KookMin 객체의 __str__ 또는 __repr__ 메소드를 호출
        # 메소드들이 정의되어 있지 않으므로, 파이썬은 기본 object 클래스의 __repr__ 메소드를 사용
        # => 메소드는 객체의 클래스 이름과 메모리 주소를 반환

        # **kwargs는 함수 호출에서 사용되는 것, 키워드 인수들을 함수에 전달하는 것을 의미
        # a = ShinHan(a='a', b='b') -> print(a) = 주소값

        # KookMin 클래스에는 인수를 처리할 수 있는 __init__ 메서드가 없다.
        # 따라서 부모 클래스인 Bank의 __init__ 메서드로 이동
        print(user)
        cls.banks[bank_choice-1].append(user.__dict__)
        print(cls.banks)
        #은행 리스트에 고객 정보를 dict 타입으로 변환해서 담는다.
        #check 함수에서 원하는 key로 회원의 정보를 찾기 위해서
        return user

#self에 접근하는 메소드가 아니여서 staticmethod 데코레이터를 붙여서 사용
    @staticmethod
    def check_account_number(account_number: str) -> dict:
        #check()에서 검사할 때 key와 value(계좌번호)를 전달
        return check(key='account_number', value=account_number)


    @staticmethod
    def check_phone(phone_number: str) -> dict:
        # check()에서 검사할 때 key와 value(핸드폰 번호)를 전달
        return check(key='phone', value=phone_number)


    def deposit(self, deposit): #입금
        self.money += deposit

    def withdraw(self, withdrow): #출금
        self.money -= withdrow

    def balance(self, bank): #확인
        return Bank.banks[bank-1]

    # def __str__(self):
    #     return f'{self.owner}, {self.account_number}, {self.phone}, {self.password}, {self.money}'
    # 객체를 출력하면 __str__()가 실행되기 때문에
    # 편하고 빠르게 회원 정보를 확인할 수가 있다. -> 재정의 안 하면 repr실행


class ShinHan(Bank):
    def deposit(self, money: int):
        money //= 2
        super().deposit(money)



class KookMin(Bank):
    def withdraw(self, money: int):
        money *= 1.5
        super().withdraw(int(money))


class KaKao(Bank):
    def balance(self):
        self.money //= 2
        return super().balance()


b = Bank.open_account(bank_choice=1, owner='jang', account="111", phone="109089", password="1234", money=1000)
# c = Bank.open_account(bank_choice=1, owner='tae', account="222", phone="100655", password="1234", money=2000)
# d = Bank.open_account(bank_choice=2, owner='hun', account="333", phone="10012", password="1234", money=3000)
# print(Bank.banks)
# print(b)
# ShinHan.deposit(1000)
# print(b.check_account_number('111'))


"""
if __name__ == '__main__':
    bank_menu = "1. 신한 은행\n" \
                "2. 국민 은행\n" \
                "3. 카카오 뱅크\n" \
                "4. 나가기\n"

    menu = "1. 개설\n" \
           "2. 입금\n" \
           "3. 출금\n" \
           "4. 잔액\n" \
           "5. 은행 선택 메뉴로 돌아가기\n"

    owner_message = "예금주: "
    account_number_message = "계좌번호: "
    phone_message = "핸드폰 번호: "
    password_message = "비밀번호(4자리): "
    money_message = "예치금: "
    deposit_message = "입금액: "
    withdraw_message = "출금액: "
    error_message = "다시 시도해주세요"


    while True:
        #은행 선택
        bank_choice = int(input(bank_menu))

        #종료
        if bank_choice == 4:
            break

        # 메뉴의 번호 이외의 번호를 입력 시 밑으로 내려가지 못하게 막는다
        if bank_choice >1 or bank_choice > len(bank_menu):
            continue


        while True:
            # 서비스 메뉴
            menu_choice = int(input(menu))

            #은행 메뉴로 돌아간다
            if menu_choice == 6:
                break


            #계좌 만들기
            if menu_choice == 1:
                owner = input(owner_message)

                while True:
                    account_number = input(account_number_message)
                    # None은 False 값이지만 가독성과 직관성을 높이기 위해 is 연산자로 검사한다.
                    if Bank.check_account_number(account_number) is None:  # 직관성 -> None
                        break
                    # 만약 계좌번호가 없다면 탈출
                    
                while True:
                    phone = input(phone_message)
                    if Bank.check_phone(phone) is None:
                        break
                    # 만약 핸드폰 번호가 없다면(중복되지 않는다면) 탈출
                    
                while True:
                    password = input(password_message)
                    if len(password) == 4:
                        break
                    # 만약 비밀번호가 4자리면 탈출

                money = int(input(money_message))
                # 계좌가 개설된다.
                
                # 어떤 은행에서 개설했는 지를 bank_choice에 담아서 전달한다.
                # open_account()는 회원의 정보를 **kwargs로 받기 때문에 모두 풀어서 전달한다.
                user = Bank.open_account(bank_choice, owner=owner, account_number=account_number, phone=phone,
                                         password=password, money=money)
                # 재정의한 __str__()이 사용되고, 회원의 전체 정보를 확인한다.
                print(user)

            # 입금
            # 개설한 은행에서만 입금 가능(신한은행)
            elif menu_choice == 2:
                account_number = input(account_number_message)
                # 계좌번호 검색 결과가 user에 담긴다.
                user = Bank.check_account_number(account_number)
                # 해당 회원을 찾았다면
                if user is not None:
                    #비밀 번호를 검사한다.
                    if user['password'] == input(password_message):
                        #신한은행 회원인지 검사한다.
                        if isinstance(user.get('object'), ShinHan):
                            #현재 선택된 은행이 신한은행이 아니라면
                            if bank_choice != 1:
                                #신한은행 회원은 신한은행에서만 입금이 가능하다고 안내한다.
                                print('개설한 은행에서만 입금 서비스를 사용하실 수 있습니다.')
                                #입금 서비스를 이용하지 못 하도록 막아준다.
                                continue

                        #입금 서비스
                        deposit_money = int(input(deposit_message))
                        #계좌 개설 시 담아놓은 self(객체)를 통해 매소드를 접근한다.
                        user['object'].deposit(deposit_money)
                        continue

                else:
                    print(error_message)

            # 출금
            elif menu_choice == 3:
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)
                if user is not None:
                    if user['password'] == input(password_message):
                        #출금액을 입력받는다.
                        withdraw_money = int(input(withdraw_message))
                        #로그인한 회원의 은행이 국민은행이라면
                        #출금 수수료가 50%이기 때문에 잔액 검사시 1.5를 곱해준다.
                        if withdraw_money * (1.5 if isinstance(user['object'], KookMin) else 1) <= user['money']:
                            user['object'].withdraw(withdraw_money)
                        else:
                            print(error_message)

                else:
                    print(error_message)

            # 잔액 조회
            elif menu_choice == 4:
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)
                if user is not None:
                    if user['password'] == input(password_message):
                        print(f'현재 잔액: {user["object"].balance()}')
                        continue

                else:
                    print(error_message)

            # 계좌 번호 재설정
            # 핸드폰 번호, 비밀번호 입력 후
            # 정확하면, 해당 회원의 계좌번호 재설정(다시 입력받기)
            elif menu_choice == 5:
                phone = input(phone_message)
                user = Bank.check_phone(phone)
                if user is not None:
                    if user['password'] == input(password_message):
                        while True:
                            account_number = input(account_number_message)
                            if Bank.check_account_number(account_number) is None:
                                break
                        #새롭게 설정한 계좌번호로 등록한다.
                        #계좌를 개설할 때 __dict__로 저장했다.
                        #이 떄 __dict__를 수정하는 것 보다, 객체로 직접 접근해서 바꾸는 것이 안전하다.
                        #결국, __dict__도 self를 받아서 만들어진 객체이므로, 뿌리인 self로 접근하는 것이 좋다.
                        user.get('object').account_number = account_number
                        continue

                print('핸드폰 번호 혹은 비밀번호를 다시 확인해주세요.')

            else:
                print(error_message)
                
"""