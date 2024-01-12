student= {
    "name": "한동석",
    "email": "koreaacadety@gmail.com"
}

print(student["name"])
print(student.get('name'))

# get()을 사용하면 key를 찾지 못 했을 때 원하는 default 값으로 설정이 가능하며,
# default 값이 없을 때에는 None을 가져온다.
print(student.get('phone'))
print(student.get('phone', '01000002222'))

#오류
# print(student['phone'])

#수정
#   'name' key값이 이미 있기 때문에, 아래의 코드는 '수정'
student['name'] = '장태훈'
print(student)

#추가
#   'phone'이라는 key값이 없기 때문에 이래의 코드는 '추가'
student['phone'] = '01011112222'
print(student)

if 'email' in student:
    student['email'] = 'jangth@naver.com'
else:
    student['email'] = 'jangth0056@naver.com'
print(student)

my_dict = {
    1: '장태훈',
    "two": "20살",
    False: [10, 20, 30],
    "row": [
        {"name": "ted", "age":40},
        {"name": "jack", "age":30},
        {"name": "john", "age":20}
    ]
}

#row에 있는 회원 3명의 정보를 모두 출력
if 'row' in my_dict:
    print(type(my_dict["row"]))
    for data in my_dict["row"]:
        print(f'{data["name"]}, {data["age"]}')

#1~10까지 중 홀수와 짝수가 있다
#사용자가 짝수를 입력하면 짝수만 출력하고 홀수를 입력하면 홀수만 출력한다.
#dict를 사용한다.
num_dict = {
            "짝수": list(i+1 for i in range(1, 10, 2)), # [i * 2 + 1 for i in range(5)]
            "홀수": list(i for i in range(1, 10, 2)) # [(i + 1) * 2 for i in range(5)]
            }

# num = input("홀수 짝수: ")
# print(", ".join(map(str, num_dict[num])))

student = {
    "name": "장태훈",
    "email": "janajdjdj@skdskdsf.com"
}

# key 분리
print(student.keys())

# value 분리
print(list(student.values()))
print('\n\n')
# item 분리
#한 쌍씩 가져온다.
print(list(student.items()))
for ket, value in student.items():
    print(f'{ket}: {value}')


