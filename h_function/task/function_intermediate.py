"""
user_info = [
    {'number':1, 'name': "john"},
    {'number':2, 'name': "mike"},
    {'number':3, 'name': "ted"},
    {'number':4, 'name': "lindy"},
    {'number':5, 'name': "adam"}
]

error_message = ""

#추가
def insert(*, number, name):

    :param number: 회원 번호
    :param name: 회원 이름
    user_info.append({'number': number, 'name': name})
insert(number=6, name="zzone")

#추가
#회원 번호는 자동 증가
number = 5
def auto_insert(*, name):
    global number
    number += 1
    user_info.append({'number': number, 'name': name})
auto_insert(name='zzone')


#목록
def user_list():
    return user_info
print(user_list())


#조회(번호로 조회)
def select(number):
    for user in user_info:
        if user['number'] == number:
            return user
    return {}

input_num = int(input("번호: "))
select(number=input_num)


#수정(번호로 이름 수정)
def update_list(*, number):
    for i in range(len(user_info)):
        if user_info[i]['number'] == number:
            input_name = input('이름: ')
            user_info[i]['name'] = input_name

def update(**kwargs):
    select(kwargs.get('number'))['name'] = kwargs.get('name')
update(number=1, name='ddeock')


input_num = int(input("번호: "))
update_list(number=input_num)
print(user_list())


#삭제(번호로 삭제)
def delete_list(*, number):
    for i in range(len(user_info)):
        if user_info[i]['number'] == number:
            del user_info[i]['number']
            del user_info[i]['name']

    # del user_info[user_info.index(select(number))]

input_num = int(input("번호: "))
delete_list(number=input_num)
print(user_list())





# 수정(번호로 이름 수정)
def update(**kwargs):
    '''

    :param kwargs: {'number': 기존 회원번호, 'name': '새로운 회원이름'}
    '''
    select(kwargs.get('number'))['name'] = kwargs.get('name')


# 삭제(번호로 삭제)
def delete(number):
    del user_info[user_info.index(select(number))]
"""


post_info = [
    {'number': 1, 'title': '테스트 제목1', 'content': '테스트 내용1', 'file': '/usr/post/file/img001.png', 'read_count': 0},
    {'number': 2, 'title': '테스트 제목2', 'content': '테스트 내용2', 'file': '/usr/post/file/img002.png', 'read_count': 0},
    {'number': 3, 'title': '테스트 제목3', 'content': '테스트 내용3', 'file': '/usr/post/file/img003.png', 'read_count': 0},
    {'number': 4, 'title': '테스트 제목4', 'content': '테스트 내용4', 'file': '/usr/post/file/img004.png', 'read_count': 0},
    {'number': 5, 'title': '테스트 제목5', 'content': '테스트 내용5', 'file': '/usr/post/file/img005.png', 'read_count': 0}
]


# 추가(조회수는 전달받지 않고 기본값 0으로 설정)
number = 5
def post_insert(file=None, read_count=0, **kwargs):
    """

    :param title: title을 받아와 저장한다.
    :param content: content를 받아와 저장한다.
    :param file: file을 받아와 저장하지만 값이 없으면 None으로 한다.
    :param read_count: read_count를 받아와 저장하지만 값이 없으면 0으로 한다.
    """
    global number
    number += 1
    post_info.append({'number': number, 'title': kwargs.get('title'), 'content': kwargs.get('content'), 'file': file, 'read_count': read_count})
post_insert(title="고양이", content="강아지")


# 목록(최신순으로 조회)
def post_list():
    # latest = []
    # for i in range(len(post_info), 0, -1):
    #     latest.append(post_info[-i])
    # return latest
    return post_info[::-1]  # [::-1] 역으로 슬라이싱
print(post_list())


# 조회(번호로 조회, 조회수 1 증가)
def post_search(number):
    for i in range(len(post_info)):
        if post_info[i]['number'] == number:
            return post_info[i]
        # print(post_info[number-1]['read_count'] )
    return {}

input_num = int(input("번호: "))
post_search(number=input_num)
print(post_list())

def read(number):
    post = post_search(number)
    post['read_count'] += 1
    return post
read(5)

print(post_list())

# 수정(번호로 정보 수정)
def update(number, file=None, read_count=0,**kwargs):
    post = post_search(number)
    post['title'] = kwargs.get('title')
    post['content'] = kwargs.get('content')
    post['file'] = kwargs.get('file')

update(number=1, title="고양이", content="강아지")
print(post_list())


# 삭제(번호로 삭제)
def post_delete(number):
    a = post_search(number)
    del post_info[post_info.index(a)]

post_delete(6)
print(post_list())


"""
# 전역변수
number = 5

# 추가(조회수는 전달받지 않고 기본값 0으로 설정)
def insert(**kwargs):
    '''
    
    :param kwargs: {'title': '게시글 제목', 'content': '게시글 내용', 'file': '파일의 경로'},
    :return: 
    '''
    global number
    number += 1
    post = {
        'number': number,
        'title': kwargs.get('title'),
        'content': kwargs.get('content'),
        'file': kwargs.get('file'),
        'read_count': 0
    }
    post_info.append(post)

# 목록(최신순으로 조회)
def select_all():
    return post_info[::-1]

# 조회(번호로 조회, 조회수 1 증가)
def read(number):
    post = select(number)
    post['read_count'] += 1
    return post

def select(number):
    for post in post_info:
        if post['number'] == number:
            return post

    return {}


# 수정(번호로 정보 수정)
def update(**kwargs):
    post = select(kwargs.get('number'))
    post['title'] = kwargs.get('title')
    post['content'] = kwargs['content']
    post['file'] = kwargs.get('file')


# 삭제(번호로 삭제)
def delete(number):
    del post_info[post_info.index(select(number))]


insert(title='테스트 제목6', content='테스트 내용6', file='')
print(select_all())
print(read(5))
print(read(5))
print(read(5))
post = read(5)
post['title'] = '수정된 제목'
update(**post)
print(read(5))
delete(5)
print(select_all())

"""