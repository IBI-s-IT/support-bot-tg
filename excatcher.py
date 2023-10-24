def error_handler(exits: bool = True):
    def wrapper(func: callable):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f'An error occurred: {e}')
                if exits:
                    exit(1)
        return inner
    return wrapper
