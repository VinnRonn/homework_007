def test(*args, **kwargs):
    print(*args, **kwargs)


def decor_1(func):
    def inner(*args, **kwargs):
        print("decor_1")
        func(*args, **kwargs)
    return inner


def decor_2(func):
    def inner(*args, **kwargs):
        print("decor_2")
        func(*args, **kwargs)
    return inner


def decor_3(func):
    def inner(*args, **kwargs):
        print("decor_3")
        func(*args, **kwargs)
    return inner

@decor_1
@decor_2
@decor_3
def test(*args, **kwargs):
    print(*args, **kwargs)


test("TEST")