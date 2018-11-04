def cach(func):
    cach = {}

    def inner(*args):
        tuple1 = args    #строки 6 и 7 реализованы для 2х аргументов
        tuple2 = (tuple1[1], tuple1[0])
        if args in cach:
            print(cach[args])
        else:
            result = func(*args)
            cach.update({tuple1: result})
            cach.update({tuple2: result})
        print(cach)
        return cach
    return inner


@cach
def sum(x, y):
    result = x + y
    print('Function called, result ', result)
    return result

sum(2, 4)
sum(2, 5)
sum(2, 4)
sum(1, 8)