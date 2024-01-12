def check(*, key: str, value: str) -> dict:
    for bank in Bank.banks:
        for user in bank:
            if user.get(key) == value:
                return user
    return None
# Bank 클래스에 선언된 클래스 변수로 선언된 bank 리스트를 불러와 bank에 각각 저장하고
# bank를 다시 user로 각각 저장해 리스트 안의 리스트에 접근해 key가 value와 같으면 해당 리스트를 반환한다.


class Bank:
    total_count = 3 #은행의 개수
    banks = [[] for count in range(total_count)] # 컴프리핸션을 이용해 banks라는 리스트에 세 개의 빈 리스트를 만든다.

    # 생성자를 이용해 인스턴스 변수를 만든다.n
    # __init__은 메모리를 할당하지 않는다. -> __new__가 메모리 할당
    def __init__(self, owner: str, account: str, phone: str, password: str, money: int):
        self.owner = owner
        self.account = account
        self.phone = phone
        self.password = password
        self.money = money


#어떤 은행에서 개설하는 지를 bank_choice로 전달받는다.
#개설에 필요한 모든 회원정보는  **kwargs로 받는다.
    @classmethod
    def open_account(cls, **kwargs):
        i = int(input('은행 선택: ')) - 1
        cls.banks[i].append({'owner': kwargs['owner'], 'account': kwargs['account'], 'phone': kwargs['phone'], 'password': kwargs['password'], 'money': kwargs['money']})


    @staticmethod
    def check_account_number(account_number: str) -> dict:
        return check(key='account_number', value=account_number)


    @staticmethod
    def check_phone(phone_number: str) -> dict:
        return check(key='phone', value=phone_number)


    def deposit(self, deposit): #입금
        self.money += deposit

    def withdraw(self, withdrow): #출금
        self.money -= withdrow
        # bank_number = int(input('은행 선택: ')) - 1
        # ask = int(input('계좌 번호: '))
        # for account in range(len(Bank.banks[bank_number])):
        #     if ask == Bank.banks[bank_number][account]['account_number_message']:
        #         Bank.banks[bank_number][account]['money_message'] -= withdrow
        #         return Bank.banks[bank_number][account]['money_message']

    def balance(self, bank): #확인
        return Bank.banks[bank-1]

    def __str__(self):
        pass



class ShinHan(Bank):
    def deposit(self, money: int):
        money //= 2
        super().deposit(money)


"""
class KookMin(Bank):
    # def open_account(self, owner_message, account_number_message, phone_message, password_message, money_message):
    #     super().open_account(owner_message, account_number_message, phone_message, password_message, money_message)
    pass


class KaKao(Bank):
    # def open_account(self, owner_message, account_number_message, phone_message, password_message, money_message):
    #     super().open_account(owner_message, account_number_message, phone_message, password_message, money_message)
    pass


shine = ShinHan()
shine.open_account('jang', 111, 109089, 1234, 0)
kook = KookMin()
kook.open_account('tae', 222, 100655, 1234, 2000)
kaka = KaKao()
kaka.open_account('jang', 111, 101233, 1234, 3000)


print(shine.balance(1))
print(shine.deposit(1000))
print(shine.withdraw(1000))
print(shine.balance(1))
"""



b = Bank.open_account(owner='jang', account="111", phone="109089", password="1234", money=1000)
c = Bank.open_account(owner='tae', account="222", phone="100655", password="1234", money=2000)
d = Bank.open_account(owner='hun', account="333", phone="10012", password="1234", money=3000)
print(Bank.banks)
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

        while True:
            # 서비스 메뉴
            pass
"""
