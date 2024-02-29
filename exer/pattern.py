x = 1
y = 1


def modify(x) -> int:
    x = 8
    return x


def modify2():
    global y
    y = 8
    return y


x = modify(1)
modify2()
print(x, "\n", y)
