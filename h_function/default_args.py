# 만약 값을 매개변수로 전달하지 않았을 경우
# 기본 값을 설정할 수 있고, arg=value로 작성한다.
# default 값은 마지막에 사용한다.
def sub(num1, num2, num3, num4=0):
    return num1 - num2 - num3 - num4

result = sub(1,2,3)
print(result)


#실습
#이름을 전달받지 못하면 '익명'으로 대체하고
#나이를 전달받지 못하면 0으로 대체하자
def get_info(name='익명', age=0):
    return {'name': name, 'age': age}

result = get_info(name='장태훈', age=22)
print(result)

result = get_info()
print(result)