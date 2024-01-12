class A:
    pass

class B(A):
    pass

a = A()
b = B()

print(isinstance(a, A))
print(isinstance(b, B))

print(isinstance(b, A))
# 모든 자식은 부모 타입이다. -> b는 B타입이며, A타입이다.
print(isinstance(a, B))
# 부모는 절대 자식 타입이 될 수 없다.