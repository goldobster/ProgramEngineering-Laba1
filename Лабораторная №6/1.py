def f1(n):
    def f2(x):
        return x + n
    return f2


a = f1(5)
print(a(8))  # 13 (8 + 5)