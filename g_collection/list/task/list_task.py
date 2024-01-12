# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.
name_list = []
price_list = []

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
        if new_name not in name_list:
            #입력한 상품명이 없다면,
            #name_list와 price_list에 각각 추가한다.
            name_list.append(new_name)
            price_list.append(int(new_price))
            continue
            #오류 메세지를 출력하지 않기 위해서 즉시 다음 반복으로 이동한다.
        else:
            result_message = append_error_message

    #수정 / choice가 2일 때
    elif choice2:
        choice2_message = input(search_name_message_for_update + ": ")
        #수정할 상품 이름을 입력하면 choice2_message에 저장한다.
        if choice2_message in name_list:
            #입력한 상품이 name_list에 존재하면, 수정할 이름과 가격을 입력받아 각각 new_name과 new_price에 저장한다.
            #만약 수정할 이름이 기존 리스트인 name_list에 없다면,
            #입력한 상품을 index()를 이용해 name_list에서의 인덱스 번호를 index에 저장한다.
            #index에 저장된 값을 이용해 name_list / price_list에 저장된 값을 수정한 값으로 바꾼다.
            new_name, new_price = input(update_message + ": ").split()
            if new_name not in name_list:
                index = name_list.index(choice2_message)
                name_list[index], price_list[index] = new_name, int(new_price)
                continue
                # 오류 메세지를 출력하지 않기 위해서 즉시 다음 반복으로 이동한다.
            else:
                result_message = update_error_message2
                #만약 수정할 이름이 기존 리스트인 name_list에 있다면, 오류 메시지를 출력한다.
        else:
            result_message = update_error_message1
            #choice2_message에 저장된 문자열이 name_list에 존재하면 에러 메시지를 result_message에 저장한다.

    #삭제 / choice가 3일 때
    elif choice3:
        choice3_message = input(delete_message + ": ")
        #사용자가 입력한 내용을 choice3_message에 삭제할 상품의 이름을 저장한다.
        if choice3_message in name_list:
            #choice3_message가 name_list에 있다면,
            #index()를 사용해 name_list에서의 인덱스를 구해 delete_index에 저장한다.
            #delete_index에 저장된 인덱스를 이용해 name_list / price_list에 저장된 값을 del을 사용해 삭제한다.
            # 오류 메세지를 출력하지 않기 위해서 즉시 다음 반복으로 이동한다.
            delete_index = name_list.index(choice3_message)
            del name_list[delete_index]
            del price_list[delete_index]
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
            a = input(search_name_message)
            #choice4_message가 1이면 상품명을 통한 검색이며, 상품명을 입력받아 a에 저장한다.
            #a가 name_list에 존재하면 name_list에서 a의 인덱스를 search_index에 저장한다.
            #저장한 index값을 이용해 name_list에서 값을 찾아 출력한다.
            # 오류 메세지를 출력하지 않기 위해서 즉시 다음 반복으로 이동한다.
            if a in name_list:
                search_index = name_list.index(a)
                print(name_list[search_index], price_list[search_index])
                continue
            else: result_message = search_name_error_message
            #a가 name_list에 없다면 에러 메시지를 result_message에 저장한다.
        #가격으로 검색
        elif choice4_message == 2:
            #choice4_message가 2이면 가격을 통한 검색이며, 가격을 입력받아 price에 저장한다.
            #가격 검색 시 오차 범위는 ±50%로 설정하기 위해 각각의 값을 min, max에 저장한다.
            #omprehesion을 이용해 price_list에서 price가 min, max 사이에 있는 값으로 이루어진 리스트를 생성한다.
            #생생된 리스트의 값에 대한 인덱스를 구해서 result_index에 저장한다.
            price = int(input(search_price_message))
            min = price * 0.5
            max = price * 1.5
            result_index = [price_list.index(i) for i in [price for price in price_list if min <= price <= max]]
            if len(result_index) != 0:
                #만약 result_index 리스트가 0이 아니라면
                #for문을 통해 name_list / price_list에서 해당하는 상품을 출력한다.
                # 오류 메세지를 출력하지 않기 위해서 즉시 다음 반복으로 이동한다.
                for i in result_index:
                    print(name_list[i], price_list[i])
                    continue
            else:
                result_message = search_error_message
                # 만약 result_index 리스트가 0이면, 에러 메시지를 result_message에 저장한다.

    #목록
    elif choice5:
        #메뉴에서 5를 입력하면 choice5가 실행된다.
        #name_list가 0이 아니라면, name_list와 price_list를 출력한다.
        # 오류 메세지를 출력하지 않기 위해서 즉시 다음 반복으로 이동한다.
        if len(name_list) != 0:
            print(name_list)
            print(price_list)
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