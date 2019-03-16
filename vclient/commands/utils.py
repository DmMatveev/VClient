import logging
from typing import Callable, List

import pyautogui
from pywinauto import WindowSpecification
from pywinauto.element_info import ElementInfo

log = logging.getLogger(__name__)

__all__ = ['wait_before', 'wait_after', 'get_all_items_info_string', 'clean_info_string']


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


@wait_before(1)
def get_all_items_info_string(list_box: WindowSpecification):
    items_string = get_items_info_string(list_box)

    first_item = items_string[0]
    last_item = items_string[-1]

    items = set(items_string)

    x, y = get_list_box_coordinate_center(list_box)
    while True:
        pyautogui.click(x, y)
        pyautogui.scroll(-1000)
        pyautogui.move(0, 0)

        items_string = get_items_info_string(list_box)

        items = items.union(items_string)

        if items_string[-1] == last_item:
            break

        last_item = items_string[-1]

    count_scroll = 0
    while True:
        count_scroll += 1

        pyautogui.click(x, y)
        pyautogui.scroll(1000)
        pyautogui.move(0, 0)

        items_string = get_items_info_string(list_box)

        if items_string[0] == first_item:
            break

        '''
        Элементы могут менять свое имя при изменение состояния
        Из-за этого по максимум поднимаем вверх        
        '''
        if count_scroll >= 50:
            log.warning('Первый элемент поменялся')
            break

    pyautogui.scroll(1000)
    pyautogui.scroll(1000)

    return items


@wait_before(0.5)
def click_item_in_list_box(list_box, find_item_name: str,
                           function_click: Callable[[int, int, int, int], None] = None) -> bool:
    found_item = None

    items = get_items_info(list_box)

    first_item = items[0].name
    last_item = items[-1].name

    x, y = get_list_box_coordinate_center(list_box)
    while True:
        pyautogui.click(x, y)
        pyautogui.scroll(-1000)
        pyautogui.move(0, 0)

        items = get_items_info(list_box)

        for item in items:
            if find_item_name in item.name:
                found_item = True

                list_box_rectangle = list_box.rectangle
                list_box_top = list_box_rectangle.top
                list_box_bottom = list_box_rectangle.top

                found_item_rectangle = item.rectangle
                found_item_top = found_item_rectangle.top
                found_item_bottom = found_item_rectangle.bottom

                if found_item_top < list_box_top:
                    pyautogui.click(x, y)
                    pyautogui.scroll(-(list_box_top - found_item_top + (list_box_top - found_item_top) / 2))

                if found_item_bottom > list_box_bottom:
                    pyautogui.click(x, y)
                    pyautogui.scroll(found_item_bottom - list_box_bottom + (found_item_bottom - list_box_bottom) / 2)

                function_click(found_item_rectangle.left,
                               found_item_rectangle.top,
                               found_item_rectangle.right,
                               found_item_rectangle.bottom)
                break

        if found_item or items[-1] == last_item:
            break

        last_item = items[-1]

def get_items_info(list_box: WindowSpecification) -> List[ElementInfo]:
    items = list_box.children()
    return [item.element_info for item in items if item.element_info.name.endswith('widget')]


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
