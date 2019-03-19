import logging
from typing import List

import pyautogui
from pywinauto import WindowSpecification
from pywinauto.element_info import ElementInfo

log = logging.getLogger(__name__)


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


def get_list_box_coordinate_center(list_box: WindowSpecification):
    list_box_coordinate = list_box.rectangle()

    x = list_box_coordinate.left + (list_box_coordinate.right - list_box_coordinate.left) / 2
    y = list_box_coordinate.top + (list_box_coordinate.bottom - list_box_coordinate.top) / 2
    return x, y


def get_all_items_info_string(list_box: WindowSpecification):
    x, y = get_list_box_coordinate_center(list_box)

    items = set(get_items_info_string(list_box))

    if len(items) == 0:
        return []

    last_item_string = ''
    while True:
        pyautogui.click(x, y)
        pyautogui.scroll(-1000)

        items_string = get_items_info_string(list_box)

        items = items.union(items_string)

        if items_string[-1] == last_item_string:
            break

        last_item_string = items_string[-1]

    first_item_string = ''
    while True:
        pyautogui.click(x, y)
        pyautogui.scroll(1000)

        items_string = get_items_info_string(list_box)

        if items_string[0] == first_item_string:
            break

        first_item_string = items_string[0]

    pyautogui.scroll(1000)
    pyautogui.scroll(1000)

    pyautogui.moveTo(50, 50, duration=0.1)

    return items


def get_items_info(list_box: WindowSpecification) -> List[ElementInfo]:
    return [item.element_info for item in list_box.children() if
            item.element_info.name.endswith('widget')]


def get_items_info_string(list_box: WindowSpecification):
    items = get_items_info(list_box)

    items = [item.name for item in items]

    items = list(map(lambda x: x.replace('_____widget', ''), items))

    return items


def clean_info_string(info_string: str) -> str:
    """
        В режиме "Валидации" появляются лишние символы
        Примеры:
        'dvalidating_1552732926_1552733226123'
        к
        'dvalidating123'

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
