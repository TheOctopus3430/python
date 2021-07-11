def log(prefix):
    def log_decorator(f):
        def wrapper(*args, **kw):
            print('[{}] {}()...'.format(prefix, f.__name__))
            return f(*args, **kw)
        return wrapper
    return log_decorator

@log('DEBr44UG')
def test():
    pass
test()