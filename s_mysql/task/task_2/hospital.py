from crud_module import *
import hashlib
from owner import Owner

# 보호자 추가
# 반려동물 추가
# 전체 목록
if __name__ == '__main__':

    # 보호자 추가
    save_many_query = "insert into tbl_owner(name, age, phone, address)\
                       values(%s, %s, %s, %s)"
    save_many_params = (
        ('장태훈', 20, '01012341234', '경기도 수원시'),
        ('이순신', 40, '01023456789', '경기도 화성'),
    )
    # save_many(save_many_query, save_many_params)


    # 반려동물 추가(1)
        #보호자 id
    find_by_id_query = "select id from tbl_owner where id = %s"
    find_by_id_params = 1,
    owner = find_by_id(find_by_id_query, find_by_id_params)
    owner_id = owner.get("id")

    save_many_query1 = "insert into tbl_pet(name, ill_name, age, weight, owner_id)\
                       values(%s, %s, %s, %s, %s)"
    save_many_params1 = (
        ('김쫀떡', '배탈', 7, 4, owner_id),
        ('소녀', '꾀병', 7, 3, owner_id),
    )
    # save_many(save_many_query1, save_many_params1)


    # 전체 목록
    find_all_query = "select u.*, p.* \
                      from tbl_owner u join tbl_pet p\
                      on u.id = p.owner_id\
                      order by u.id desc"
    posts = find_all(find_all_query)
    for post in posts:
        print(post)

    find_all_query = "select id, name, age, phone, address from tbl_owner"
    owners = find_all(find_all_query)
    owners_with_pets = []
    for owner in owners:
        find_all_by_query = "select id, name, ill_name, age, weight, owner_id from tbl_pet where owner_id = %s"
        find_all_by_params = owner.get("id"),
        pets = find_all_by(find_all_by_query, find_all_by_params)
        owners_with_pets.append(Owner(owner.get("id"), owner.get("name"), owner.get("age"), owner.get("phone"), owner.get("address"), pets))

    for owner in owners_with_pets:
        print(owner.__dict__)
