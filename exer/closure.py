def make_adder():
    x = 0

    def inc(x) -> int:
        x += 1
        return x

    return inc(x)
