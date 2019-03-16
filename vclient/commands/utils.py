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


def clean_info_string(info_string: str) -> str:
    """
        В режиме "Валидации" появляются лишние символы
        Примеры:
        '1552732926_1552733226123'
        к
        '123'

        'dvalidating_1552733285_155273358511https11'
        к
        'dvalidating11https11'

    """
    if '_' in info_string:
        number_size = info_string.rindex('_') - info_string.index('_') - 1
        part1, _, part2 = info_string.split('_')
        part2 = part2[number_size:]

        info_string = part1 + part2

    return info_string
