def f2(x):
    return x**2


def f1(f2):
    for i in range(5):
        yield f2(i)

a = f1(f2)
print(next(a))  # 0
print(next(a))  # 1
print(next(a))  # 4
print(next(a))  # 9
print(next(a))  # 16
print(next(a))  # StopIteration