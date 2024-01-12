# email을 입력받고 아이디와 도메인을 각각 분리하여 출력한다. 아이디@도메인
ID, Domain = input("이메일을 입력해주세요: ").split('@')
result = f'ID: {ID}\nDomain: {Domain}'
print(result + '\n')

'''
첫 번째 값으로 야드를 입력받고, 두 번째 값으로 인치를 입력받아서
    각각 cm로 변환하여 다음 형식에 맞추어 소수점 둘 째 자리까지 출력한다.

    1yd: 91.44cm
    1in: 2.54cm

    예)
        yard 입력: 10
        inch 입력: 10

        10 yard는 914.4cm
        10 inch는 25.4cm
'''

message = "yard와 inch를 입력해주세요."
exampl_message = 'ex) 10 10'
yard, inch = map(float, input(message + '\n' + exampl_message + '\n').split(" "))

yard = yard * 91.44
inch = inch * 2.54
result = f'yard: {round(yard, 2)}cm\ninch: {round(inch, 2)}cm'
print(result)
