# 여러 개의 변수를 한 줄에 선언
a = 10; b = 20; c = 30
print(a,b,c, sep=', ')

a, b, c = 100, 200, 300 #(a,b,c) = (100, 200, 300)
print(a,b,c, sep=', ')

# 변수의 값을 서로 바꾸기
a = 11
b = 33
print(a, b)

temp = a
a = b
b = temp
print(a, b)

a, b = b, a
print(a, b)

# 동적 바인딩
a = 10
print(type(a))

a = 10.5
print(type(a))

a = 'A'
print(type(a))

a = 'abc'
print(type(a))

a = ['a', 'b', 'c']
print(type(a))

a = { "a": 1,
      'b': 2,
      'c': 3}
print(type(a))

a = True
print(type(a))

a = 5 > 2
print(a)
print(type(a))


# 변수명 주의사항
variable_int = 10
print(type(variable_int))

variable_float = 10.5
print(type(variable_float))

variable_char = 'A'
print(type(variable_char))

variable_string = "ABC"
print(type(variable_string))

variable_list = ['A', 'B', 'C']
print(type(variable_list))

variable_dict = {'A': 1, 'B': 2, 'C': 3}
print(type(variable_dict))

variable_bool = True
print(type(variable_bool))

# 서식문자
name = '장태훈'
print("이름: %s" %name)
print("이름: %s" %'abc')

age = 20
print("나이: %d" %age)

height = 15.55
print("키: %.1f" %height)
height = 15.45
print("키: %.1f" %height)
# 5의 경우에는 5의 앞자리가 홀수인 경우에 올림을 하고 짝수인 경우 버림을 하여 짝수로 만들어준다.
# 예를 들어 53.45는 53.4로, 32.75는 32.8로 반올림한다.
# 이를 오사오입(round-to-nearest_even) -> 평균값 오차가 가장 적다.
print("키: %.1f\n" %(round(height+0.0000000001, 1)))

print("이름: %s" %name)
print("나이: %d" %age)
print("키: %.1f\n" %height)

print("이름: %s\n나이: %d살\n키:%.1fcm" %(name, age, height))

print("%04d\n" %1)

print("="*20)
formatting = "이름: %s\n나이: %d살\n키:%.1fcm" %(name, age, height) #문자열로 담긴다.
print(formatting)
print("="*20)

# 실습
# 정수 2개를 변수에 담기
# 두 정수의 합을 아래 형식으로 출력하기
# 1 + 3 = 4
first_num = 1
second_num = 2
print("%d + %d = %d" %(first_num, second_num, first_num + second_num))

# format 함수
name = '장태훈'
age = 80
height = 156.26
print('이름: {}\n나이: {}\n키: {:.1f}\n'.format(name, age, height))
print('이름: {0}\n나이: {1}\n키: {2:.1f}\n'.format(name, age, height)) #list
print('이름: {1}\n나이: {0}\n키: {2:.1f}\n'.format(name, age, height))
print('이름: {name}\n나이: {age}\n키: {height}\n'.format(name=name, age=age, height=height)) #dictionary

formatting1 = '이름: {}\n나이: {}\n키: {:.1f}\n'.format(name, age, height)
formatting2 = '이름: {0}\n나이: {1}\n키: {2:.1f}\n'.format(name, age, height)
formatting3 = '이름: {name}\n나이: {age}\n키: {height}\n'.format(name=name, age=age, height=height)
print(formatting1)
print(formatting2)
print(formatting3)
print()

# format string
name = '장태훈'
age = 80
height = 156.26
#round(실수값, 반올림 자리수)
print(f'이름: {name}')
print(f'나이: {age}살')
print(f'키: {round(height, 1)}cm\n')

# 실습
# 아래 메세지를 format함수를 사용하여 출력한다.
# Hello 파이썬, python is fantastic !
# Hello 장고, Django is fantastic !
# Hello 리액트, React is fantastic !

lang_kr = '파이썬'
lang_en = 'python'
print(f'Hello {lang_kr}, {lang_en} is fantastic !')

lang_kr = '장고'
lang_en = 'Django'
print(f'Hello {lang_kr}, {lang_en} is fantastic !')

lang_kr = '리액트'
lang_en = 'react'
print(f'Hello {lang_kr}, {lang_en} is fantastic !\n')


# 실습
#값에 이름을 붙여서 해당 이름에 있는 값이 반영된다.
lang_kr = '파이썬'
lang_en = 'python'
print('Hello {lang_kr}, {lang_en} is fantastic !'.format(lang_kr=lang_kr, lang_en=lang_en))

#값에 할당된 번호를 작성하면 해당 값이 반영된다.
lang_kr = '장고'
lang_en = 'Django'
print('Hello {0}, {1} is fantastic !'.format(lang_kr, lang_en))

#자동으로 해당 순서에 값이 반영된다.
lang_kr = '리액트'
lang_en = 'react'
print('Hello {}, {} is fantastic !'.format(lang_kr, lang_en))

