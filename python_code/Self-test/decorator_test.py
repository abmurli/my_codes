def star(func):
    print(func.__name__)
    def inner(*args, **kwargs):
        print("A" * 30)
        # this will call percent
        func(*args, **kwargs)
        print("A" * 30)
    return inner


def percent(func):
    print(func.__name__)
    def outer(*args, **kwargs):
        print("B" * 30)
        func(*args, **kwargs)
        print("B" * 30)
    return outer


@percent
@star
def printer(msg):
    print(msg)


printer("Hello")


