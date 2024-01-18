from s_mysql.connection_module import *


@execute
def save(cursor: Cursor, query: str, params: list):
    print(cursor)
    print()
    print(query)
    print()
    print(params)
    cursor.execute(query, params)


@execute
def find_all(cursor: Cursor, query: str) -> list:
    cursor.execute(query)
    print(cursor) # 주소
    print()
    print(query) #쿼리문
    print()
    return cursor.fetchall()


@execute
def find_by_id(cursor: Cursor, query: str, params: list) -> dict:
    cursor.execute(query, params)
    return cursor.fetchone()


@execute
def update(cursor: Cursor, query: str, params: list):
    cursor.execute(query, params)


@execute
def delete(cursor: Cursor, query: str, params: list):
    cursor.execute(query, params)

# @execute
# def show_tabe(cursor: Cursor, query: str, params: list):