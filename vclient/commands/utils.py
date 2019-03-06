def wait_before(time_sleep):
    def decorator(method):
        def wrapper(*args, **kwargs):
            from time import sleep
            sleep(time_sleep)
            return method(*args, **kwargs)
        return wrapper
    return decorator


def wait_after(time_sleep):
    def decorator(method):
        def wrapper(*args, **kwargs):
            from time import sleep
            result = method(*args, **kwargs)
            sleep(time_sleep)
            return result
        return wrapper
    return decorator
