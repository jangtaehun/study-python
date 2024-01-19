from crud_module import *
from datetime import datetime
import hashlib
from search import ConferenceRoom

# 회원가입
# 회사 추가
# 회의실 추가
# 회의실마다 이용가능 시간 추가
# 예약 추가
# 회의실 전체 내용 조회(예약이 이미 완료된 회의실 시간은 보여지지 않는다).

not_reserve = []

find_all_query = ("select * from tbl_office o \
                  join tbl_conference_room c on o.id = c.office_id \
                  join tbl_part_time p on p.conference_room_id = c.id \
                  ")

owners = find_all(find_all_query)
print(owners)

# for owner in owners:
#     formatted_time = owner["time"].total_seconds()
#     iso_formatted_time = datetime.utcfromtimestamp(formatted_time).isoformat()
#     time_part = iso_formatted_time[11:]
#     not_reserve.append(ConferenceRoom(time_part, owner.get("conference_room_id")))

# for owner in not_reserve:
#     print(owner.__dict__)


# find_all_query = "select p.time, p.conference_room_id from tbl_part_time p join tbl_reservation r on p.conference_room_id = r.conference_room_id \
#                                                   where r.conference_room_id =''"
# owners = find_all(find_all_query)
# print(owners)
#
# find_all_by_query = "select time from tbl_part_time where conference_room_id = %s"
# find_all_by_params = 2
# owners = find_all_by(find_all_by_query, find_all_by_params)
# time_table = []
# for owner in owners:
#     formatted_time = owner["time"].total_seconds()
#     iso_formatted_time = datetime.utcfromtimestamp(formatted_time).isoformat()
#     time_part = iso_formatted_time[11:]
#     print(f'{2}회의실에 추가된 시간: {time_part}')
#     time_table.append(time_part)
# print(time_table)


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
office_message = '회사 이름을 입력해주세요: '
location_message = '회사 위치를 입력해주세요: '
conference_message = '회의실을 추가하시겠습니까?: y/n '
conference_room_message = '어떤 회의실을 이용하시겠습니까: '

# """
if __name__ == '__main__':

    # 회원가입
    while True:
        input_email = input(email_message)
        if check_email(input_email) is None:
            member_password = input(password_message)
            input_name = input(name_message)


            encryption = hashlib.sha256()
            encryption.update(member_password.encode('utf-8'))
            # Use.make(email=input_email, password=encryption.hexdigest(), name=input_name)
            insert_query = "insert into tbl_client(email, password, name) values (%s, %s, %s)"
            insert_params = (input_email, encryption.hexdigest(), input_name)
            save(insert_query, insert_params)


            print(f"{input_name}님 환영합니다~!")

            # 회사 추가
            input_email = input(email_message)
            if check_email(input_email):
                office_name = input(office_message)
                office_location = input(location_message)
                insert_query = "insert into tbl_office(name, location) values(%s, %s)"
                insert_params = [office_name, office_location]
                save(insert_query, insert_params)
                print(f'{office_location}에 있는 {office_name}에 다니시는 {input_name}님 반갑습니다.')

                conference = input(conference_message)

                if conference == 'y':
                        # 회의실 추가
                            # 회사 id 조회
                    # find_by_id_query = "select id from tbl_office where name = %s"
                    # find_by_id_params = office_name,
                    # office_ids = find_by_id(find_by_id_query, find_by_id_params)
                    # office_id = office_ids.get("id")
                    # print(office_id)
                    insert_room = input('회의실 번호: ')
                    insert_query = "insert into tbl_conference_room(office_id) values (%s)"
                    insert_params = insert_room
                    save(insert_query, insert_params)

                else:
                    break
                # continue
            else:
                print("회원가입을 해주세요.")

            # 회의실마다 이용가능 시간 추가
                # 회의실 id 조회 -> 회사 이름, 회사id
            find_all_query = "select name from tbl_office"
            office_info = find_all(find_all_query)
            for office_info in office_info:
                print(office_info)

            office_name = input("회사 이름을 입력해주세요: ")

            find_all_by_query = "select id from tbl_office where name = %s"
            find_all_by_params = office_name,
            office_id = find_by_id(find_all_by_query, find_all_by_params)

            find_by_id_query = "select id from tbl_conference_room where office_id = %s"
            find_by_id_params = office_id['id'],
            conference_ids = find_all_by(find_by_id_query, find_by_id_params)

            if conference_ids is None:
                print('예약 가능한 회의실이 없습니다.')
            else:
                for conference_id in conference_ids:
                    print(f'시간 추가 가능한 회사: {conference_id["id"]}')

            conference_room = input(conference_room_message)

            find_all_by_query = "select time from tbl_part_time where conference_room_id = %s"
            find_all_by_params = conference_room
            owners = find_all_by(find_all_by_query, find_all_by_params)
            time_table = []
            for owner in owners:
                formatted_time = owner["time"].total_seconds()
                iso_formatted_time = datetime.utcfromtimestamp(formatted_time).isoformat()
                time_part = iso_formatted_time[11:]
                print(f'{conference_room}회의실에 추가된 시간: {time_part}')
                time_table.append(time_part)

            time = input('이용 가능 시간 추가: ex)HH:MM ')
            if time not in time_table:
                insert_query = "insert into tbl_part_time(time, conference_room_id) values (%s, %s)"
                insert_params = (time, conference_room)
                save(insert_query, insert_params)
                print(f"{office_name} 회사의 {conference_room}번 회의실 이용 가능 시간이 추가되었습니다.")
            else:
                print('이미 추가된 시간입니다.')

            # 회의실 예약
            reserve = input('예약하시겠습니까?: y/n')
            if reserve == 'y':
                input_email = input(email_message)
                if check_email(input_email):

                    
                    time_table = []
                    find_all_query = "select p.time from tbl_part_time p join tbl_reservation r on p.conference_room_id = r.conference_room_id \
                                      where r.conference_room_id = 0"
                    times = find_all(find_all_query)

                    for time in times:
                        formatted_time = time["time"].total_seconds()
                        iso_formatted_time = datetime.utcfromtimestamp(formatted_time).isoformat()
                        time_part = iso_formatted_time[11:]
                        print(f'{conference_room}회의실 이용 가능 시간: {time_part}')
                        time_table.append(time_part)


                    if len(time_table) != 0:
                        insert_query = "insert into tbl_reservation(time, client_email, conference_room_id) values (%s, %s, %s)"
                        insert_params = (time, input_email, conference_room)
                        save(insert_query, insert_params)
                        print(f"{office_name} 회사의 {conference_room}번 회의실 {time}에 예약되었습니다.")
                    else:
                        print("이용 가능 시간이 없습니다.")

            else:
                # 회의실 전체 내용 조회(예약이 이미 완료된 회의실 시간은 보여지지 않는다).
                not_reserve = []

                find_all_query = "select p.time, p.conference_room_id from tbl_part_time p join tbl_reservation r on p.conference_room_id = r.conference_room_id \
                                                      where r.conference_room_id =''"
                owners = find_all(find_all_query)

                for owner in owners:
                    not_reserve.append(ConferenceRoom(owner.get("time"), owner.get("conference_room_id")))

                for owner in not_reserve:
                    print(owner.__dict__)

        else:
            print("중복된 이메일입니다.")
            continue
# """
# 1. datetime.datetime.isoformat()
# 2. datetime.date.isoformat()