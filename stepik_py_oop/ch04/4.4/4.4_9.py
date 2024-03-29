def class_log(log_list):
    def log_methods(cls):
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, log_methods_decorated(v))
        return cls

    def log_methods_decorated(func):
        def wrapper(*args, **kwargs):
            log_list.append(func.__name__)
            return func(*args, **kwargs)
        return wrapper

    return log_methods


vector_log = []


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value


v = Vector(1, 2, 3)
v[0] = 10
r = v[1]
print(vector_log)
print('end')
