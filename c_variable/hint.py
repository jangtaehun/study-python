from typing import List, Dict, Set, Tuple, Union, Final

data: Final[int] = 10 #변경 금지
print(data)

class A:
    pass

#매개변수: 자료형, union: 둘 중 상관 없다.
class B:
    def test(data:Union[int, str], number:int|float, data1: A, datas: List[int], data_dict: Dict[str, int])->int:
        pass



