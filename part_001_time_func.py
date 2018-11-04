import time
start_time = time.time()


def time_activate(enabled=True):
    def time_count(func):
        def inner(*args, **kwargs):
            if enabled is True:
                result = func(*args, **kwargs)
                print("Result is", result)
                print("- %s seconds -" % (time.time() - start_time))
                return result
            else:
                return func(*args, **kwargs)
        return inner
    return time_count


@time_activate(enabled=False)
def sum(x, y):
    print(x, y)
    return x + y

sum(1, 4)


