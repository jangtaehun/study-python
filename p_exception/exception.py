
# try:
#     number = int(input("정수를 입력하세요: "))
#
# except ValueError as e:
#     print("정수만 입력해주세요")
#
# print('반드시 실행되어야 하는 문장')


# try:
#     print(10 / 0)
#
# except ZeroDivisionError as e:
#     print('분모가 0입니다.')

# datas = [1,2,3]
#
# try:
#     print(datas[3])
#     print('오류가 없어요') #오류가 발생하지 않는다면 실행된다.
# except ValueError:
#     pass
#
# except IndexError:
#     print('인덱스 확인!')
#
# else: #쓸 필요가 없다.
#     print('오류가 없어요') #try에 작성한 문장에서 오류가 발생하지 않는다면 실행
#
# finally:
#     print('반드시 실행되어야 하는 문장')


# nickname = input("닉네임: ")
# if nickname == "멍청이":
#     raise RuntimeError

class BadWordError(Exception):
    def __str__(self):
        return "비속어 금지!"

def check_bad_word(message):
    if '멍청이' in message:
        raise BadWordError()

chat = input('chat: ')
try:
    check_bad_word(chat)
    print(chat)
except BadWordError as e:
    print(e)