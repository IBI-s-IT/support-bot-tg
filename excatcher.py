def error_handler(func: callable):
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(f'An error occurred: {e}')
            exit(1)
    return inner
