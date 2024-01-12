# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.
data_dict = {}

title = "zzangtae's store"
menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n"
search_menu = "1.상품명으로 검색\n2.가격으로 검색\n"
append_message = '추가하실 상품명과 가격을 입력하세요.\n예)상품명 가격'
search_name_message_for_update = '수정하실 상품명을 입력하세요.'
update_message = '새로운 상품명과 가격을 입력하세요.\n예)상품명 가격'
delete_message = '삭제하실 상품명을 입력하세요.'
search_name_message, search_price_message = '상품명: ', '가격: '

result_message = ""
append_error_message = "추가 실패(중복된 상품명)"
update_error_message1 = "수정 실패(존재하지 않는 상품명)"
update_error_message2 = "수정 실패(중복된 상품명)"
delete_error_message = "삭제 실패(존재하지 않는 상품명)"
search_name_error_message = "검색 실패(존재하지 않는 상품명)"
search_error_message = "검색 결과가 없습니다."
error_message = "다시 입력해주세요."
no_item_message = "목록이 없습니다."

while True:
    outside_message = int(input(title + '\n' + menu + "메뉴 선택: "))
    #사용자에게 menu를 보여주고 입력한 menu를 outside_message에 저장한다.

    choice1, choice2, choice3, choice4, choice5, choice6 = \
        outside_message==1, outside_message==2, outside_message==3, outside_message==4, outside_message==5, outside_message==6
    #outside_message==1, outside_message==2, ...를
    #choice1, choice2, choice3, choice4, choice5, choice6 각각에 저장한다.

    #추가 / choice가 1일 때 실행
    if choice1:
        new_name, new_price = input(append_message + ": ").split()
        #추가할 상품과 가격을 입력하면 new_name과 new_price에 나누어서 저장한다.
        if new_name not in data_dict.keys():
            #입력한 상품명이 없다면,
            data_dict[new_name] = int(new_price)
            continue
            #오류 메세지를 출력하지 않기 위해서 즉시 다음 반복으로 이동한다.
        else:
            result_message = append_error_message

    #수정 / choice가 2일 때
    elif choice2:
        choice2_message = input(search_name_message_for_update + ": ")
        #수정할 상품 이름을 입력하면 choice2_message에 저장한다.
        if choice2_message in data_dict.keys():
            new_name, new_price = input(update_message + ": ").split()
            if new_name not in data_dict:
                del data_dict[new_name]
                data_dict[new_name] = int(new_price)
                continue
                # 오류 메세지를 출력하지 않기 위해서 즉시 다음 반복으로 이동한다.
            else:
                data_dict[new_name] = int(new_price)
                #만약 수정할 이름이 기존 리스트인 name_list에 있다면, 오류 메시지를 출력한다.
        else:
            result_message = update_error_message1
            #choice2_message에 저장된 문자열이 name_list에 존재하면 에러 메시지를 result_message에 저장한다.

    #삭제 / choice가 3일 때
    elif choice3:
        choice3_message = input(delete_message + ": ")
        #사용자가 입력한 내용을 choice3_message에 삭제할 상품의 이름을 저장한다.
        if choice3_message in data_dict.keys():
            # delete_index = name_list.index(choice3_message)
            del data_dict[choice3_message]
            continue
        else:
            result_message = delete_error_message
            #choice3_message에 저장된 문자열이 name_list에 없으면 에러 메시지를 result_message에 저장한다.

    #검색
    elif choice4:
        choice4_message = int(input(search_menu + ": "))
        #검색할 방법을 입력받아 choice4_message에 저장한다.
        #상품명으로 검색
        if choice4_message == 1:
            keyword = input(search_name_message)
            if keyword in data_dict:
                for name, price in data_dict.items():
                    if keyword == name:
                        print(f'"{name}": {price}')
                continue
            else: result_message = search_name_error_message
            #a가 name_list에 없다면 에러 메시지를 result_message에 저장한다.
        #가격으로 검색
        elif choice4_message == 2:
            check = False
            price = int(input(search_price_message))
            min = price * 0.5
            max = price * 1.5
            for name, price in data_dict.items():
                if min <= price <= max:
                    check = True
                    print(f'"{name}": {price}')

            if check == True:
                continue

            if not check:
                result_message = search_error_message

    #목록
    elif choice5:
        #메뉴에서 5를 입력하면 choice5가 실행된다.
        # 오류 메세지를 출력하지 않기 위해서 즉시 다음 반복으로 이동한다.
        if len(data_dict) != 0:
            for name, price in data_dict.items():
                print(f'Name: {name}, Price: {price}')
                continue
        else:
            result_message = no_item_message
            #name_list가 0이라면 에러 메시지를 result_message에 저장한다.

    #종료
    elif choice6:
        break

    # 그 외
    else:
        result_message = error_message

    print(result_message)
    result_message = ""