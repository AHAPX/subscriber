def add_params(*args, **kwargs):
    def decorator(func):
        def wrapper(message):
            return func(message, *args, **kwargs)
        return wrapper
    return decorator
