# if
# for
# while

"""
1. 커피 가격은 2500원이고 음료수 가격은 2000원이다.
2. 입력한 인원만큼 반복하는 시스템이다.
3. 1을 입력하면 커피, 2를 입력하면 음료수, 3을 입력하면 종료된다.
4. 주문을 마치면 총 금액과 어떤 음료를 몇 개 주문했는지 출력되는 코드를 작성하시오.
ex)
몇 잔을 주문하겠습니까? ex) 3
 입력: 2

어떤 것을 선택하시겠습니까? 1. 커피, 2. 탄산, 3. 종료
 입력: 1
커피 1잔

어떤 것을 선택하시겠습니까? 1. 커피, 2. 탄산, 3. 종료
 입력: 2
탄산음료 1캔

총 주문 금액: 4500, 주문 상품: 커피 1잔, 탄산음료 1캔입니다.
"""
coffee = 2500
coffee_choice = 0

drink = 2000
drink_choice = 0

cost = 0

people = int(input("몇 잔을 주문하겠습니까? ex) 3\n 입력: "))
while people:
     choice = int(input("어떤 것을 선택하시겠습니까? 1. 커피, 2. 탄산, 3. 종료\n 입력: "))
     choice1, choice2, choice3= choice == 1, choice == 2, choice == 3

     if choice1:
         cost += coffee
         coffee_choice += 1
         people -= 1
         print(f'커피 {coffee_choice}잔\n')
     elif choice2:
         cost += drink
         drink_choice += 1
         people -= 1
         print(f'탄산음료 {drink_choice}캔\n')
     elif choice3:
         people = 0
     else:
        print("다시 선택해주세요.\n")
print(f'총 주문 금액: {cost}, 주문 상품: 커피 {drink_choice}잔, 탄산음료 {drink_choice}캔입니다.\n')


"""
1. 상품 가격은 1000원이다.
2. 두 개를 사면 한 개를 무료로 준다. 2+1
3. 구매 상품 수에 따라 가격을 계산하는 코드 작성
"""
price = 1000
goods = int(input("몇 개 주문: ex)3\n입력: "))
cost = 0

for i in range(1, goods+1):
    if i % 2 == 0:
        print("2+1 상품입니다.")
        continue
    cost += price

print(f'총 가격은 {cost}원입니다.')
