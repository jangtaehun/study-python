from crud_module import *
import hashlib

# 회원가입
# 회사 추가
# 회의실 추가
# 회의실마다 이용가능 시간 추가
# 예약 추가
# 회의실 전체 내용 조회(예약이 이미 완료된 회의실 시간은 보여지지 않는다).

def check_email(email):
    find_by_id_query = "select email from tbl_client where email = %s"
    params = email
    member = find_by_id(find_by_id_query, params)
    if member is None:
        return None
    else:
        return member.get('email')



email_message = "이메일을 입력해주세요: "
password_message = '비밀번호를 입력해주세요: '
name_message = '이름을 입력해주세요: '

if __name__ == '__main__':

    # 회원가입
    input_email = input(email_message)
    if check_email(input_email) is None:
        member_password = input(password_message)
        input_name = input(name_message)

        encryption = hashlib.sha256()
        encryption.update(member_password.encode('utf-8'))
        # Use.make(email=input_email, password=encryption.hexdigest(), name=input_name)
        insert_query = "insert into task_member(email, password, name) values (%s, %s, %s)"
        insert_params = (member['email'], member['password'], member['name'])
        save(insert_query, insert_params)

        print(f"{input_name}님 환영합니다~!")
    else:
        print("중복된 이메일입니다.")
        # continue
