#캐릭터 닉네임을 정할 때 비속어를 사용하지 못하게 막아주기
#바보 멍게 해삼 운영자
#직접 Error를 제작하여, 발생 시 안내 메세지까지 출력하기

class NickNameError(Exception):
    def __str__(self):
        return "비속어 금지!"

def check_nickname(nickname):
    not_allowed_names = ['바보', '멍게', '해삼', '운영자']
    for name in not_allowed_names:
        if name in nickname:
            raise NickNameError


nickname = input('닉네임: ')
try:
    check_nickname(nickname)

except NickNameError as e:
    print(e)