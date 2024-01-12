# num1, num2 = map(int, input("두 정수를 입력하세요: ex)10 20\n").split(' '))

#unpacking / 값을 풀어서 적는 것

# def get_total(num1, num2, num3):
#     return num1 + num2 + num3


#packing / 값을 묶어서 적는 것
#외부에서 전달받은 값들이 numbers(튜플)에 저장된다.
#packing은 매개변수에서 가장 마지막에 적는다.

def get_total(*numbers):
    print(type(numbers))
    # print(numbers)
    total = 0
    for number in numbers:
        total += number
    return total


#여러 개의 값을 콤마로 구분해 전달한다.
total = get_total(1, 2, 3, 4, 5)
print(total)
print()

#여러 개의 값을 하나로 묶어서 전달하게 되면, packing으로 인해 첫 번째 방에 통채로 들어가게 된다.
#즉, 결과는 다음과 같다. ([1,2,3,4,5], )
#따라서 내부의 요소를 각각 전달하고 싶다면, 앞에 *을 작성해야 한다.
numbers = [1, 2, 3, 4, 5]
total = get_total(*numbers) # 여러개로 받기 때문에 *을 안 붙이면 하나로 인식한다. ([...],) -> 튜플
print(total)
print()

#국어, 영어, 수학 점수를 전달받은 뒤 총 점을 출력하는 함수
#packing으로 제작하기
def get_total(*subject):
    total = 0
    for number in subject:
        total += number
    print(total)
get_total(100, 45, 28)
print()

#문자열에서 'A'가 몇 개 있는 지 검사하는 함수
#packing으로 제작하기
def count_str(*strings):
    print(type(strings))
    print(strings)

    count = 0
    count_list = []
    for string in strings:
        str_list = [i for i in string]
        print(str_list)
        for i in range(len(str_list)):
            if str_list[i] == 'A':
                count += 1
        count_list.append(count)
        count = 0
    return print(count_list)

count_str("hoAhAhA", "A is one", "AA is two")


def get_count(*strs):
    a = [str.count("A") for str in strs]
    print(a)
get_count("hoAhAhA", "A is one", "AA is two")


"""
    count = 0
    counts = []
    for str in strs:
        for s in str:
            if s == "A":
                counts += 1
            counts.append(counts)
            count = 0
    return count
"""