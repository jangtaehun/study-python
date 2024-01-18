# 회원가입(SMS API) - 랜덤한 인증번호 6자리 발송 후 검사
# 아이디(이메일) 중복검사

# 로그인 후 마이페이지로 이동
# 회원 비밀번호 변경(EMAIL API) - 랜덤한 코드 10자리 발송 후 검사

# 사용자가 입력한 한국어를 영어로 번역
# 한국어와 번역된 문장을 DBMS에 저장
# 번역 내역 전체 조회

# 업로드한 이미지 파일의 이름과 이미지의 내용을 DBMS에 저장(OCR API)
# 이미지 경로: https://thumb.mt.co.kr/06/2012/02/2012021613230156226_1.jpg/dims/optimize/
# 경로와 추출한 텍스트 전체 조회


from crud_module import *
# from sms.send_sms import send_message
import hashlib
# import mail_module

import string
import random
letters_set = string.ascii_letters
random_list = random.sample(letters_set,6)
certification_number = ''.join(random_list)
print(certification_number)


def check_mail(email):
    find_by_id_query = "select email from task_member where email = %s"
    params = email
    member = find_by_id(find_by_id_query, params)
    if member is None:
        return None
    else:
        return member.get('email')

def check_pass(password):
    find_by_id_query = "select password from task_member where password = %s"
    params = password
    member = find_by_id(find_by_id_query, params)
    if member is None:
        return None
    else:
        return member.get('password')


class Use:
    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name

    @classmethod
    def make(cls, **kwargs):
        # print(kwargs)
        member = Member(**kwargs).__dict__

        insert_query = "insert into task_member(email, password, name) values (%s, %s, %s)"
        insert_params = (member['email'], member['password'], member['name'])
        save(insert_query, insert_params)

    @staticmethod
    def check_id(mail: str) -> dict:
        return check_mail(mail)

    @staticmethod
    def check_password(password: str) -> dict:
        return check_pass(password)


class Member(Use):
    #Overriding
    pass

# Use.make(email='jth', password='<PASSWORD>', name='jth')

choose_message = '번호 입력: '
secret_message = '인증번호 입력: '
email_message = '이메일을 입력해주세요: '
phone_message = "핸드폰 번호: "
name_message = '이름을 입력해주세요: '
password_message = '비밀번호를 입력해주세요: '

while True:
    check_login = False
    choose_num = input(choose_message)

    if choose_num == '1':
        input_email = input(email_message)
        if Use.check_id(input_email) is None:
            member_phone = input(phone_message)

            certification_number_input = input(secret_message)
            if certification_number_input == certification_number:
                input_name = input(name_message)

                input_password = input(password_message)
                encryption = hashlib.sha256()
                encryption.update(input_password.encode('utf-8'))
                Use.make(email=input_email, password=encryption.hexdigest(), name=input_name)
                print(f"{input_name}님 환영합니다~!")
        else:
            print("중복된 이메일입니다.")
            continue

    if choose_num == '2':
        check_password = input(password_message)
        encryption = hashlib.sha256()
        encryption.update(check_password.encode('utf-8'))
        if encryption.hexdigest() == Use.check_password(encryption.hexdigest()):
            message = "비밀번호 변경 [Y/n]: "
            check = input(message)
            if check == 'Y':
                letters_set = string.ascii_letters
                random_list = random.sample(letters_set, 6)
                certification_number = ''.join(random_list)
                print(certification_number)


                # Use.check_id(encryption.hexdigest())

                certification_number_input = input(secret_message)
                if certification_number_input == certification_number:
                    message = "새로운 비밀번호: "
                    member_password = input(message)
                    message = "재입력: "
                    member_password2 = input(message)

            print(f"{check_password}")
        else:
            print("틀림")