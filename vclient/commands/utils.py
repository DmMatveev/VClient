import logging
from typing import List, Callable, Tuple, NamedTuple

import pyautogui
from pywinauto import WindowSpecification
from pywinauto.controls.uia_controls import ListViewWrapper
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


def get_all_items_info_string(list_box: WindowSpecification) -> List[str]:
    list_box = list_box.wrapper_object()

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

    pyautogui.click(x, y)
    pyautogui.scroll(1000)
    pyautogui.scroll(1000)

    pyautogui.moveTo(50, 50, duration=0.1)

    return items


def select_item_in_list_box(list_box: WindowSpecification, find_item: str,
                            converting_info_to_string: Callable[[str], NamedTuple], field: str) -> Tuple[
    int, int, int, int]:
    list_box = list_box.wrapper_object()

    x, y = get_list_box_coordinate_center(list_box)

    list_box_rectangle = list_box.rectangle()
    list_box_top = list_box_rectangle.top
    list_box_bottom = list_box_rectangle.bottom

    print(f'Найти ip {find_item}')


    found_item = False
    last_item = None
    while True:
        list_box.set_focus()  # проверить

        items = get_items_info(list_box)

        if len(items) == 0:
            raise RuntimeError('items != 0')

        for item in items:
            if item.name == '':
                raise RuntimeError('item.name == ""')

            if find_item == getattr(converting_info_to_string(item.name), field):
                found_item = True

                print(f'ip find {getattr(converting_info_to_string(item.name), field)}')

                found_item_rectangle = item.rectangle
                found_item_top = found_item_rectangle.top
                found_item_bottom = found_item_rectangle.bottom

                rectangle = item.rectangle

                if found_item_top < list_box_top:
                    pyautogui.click(x, y)
                    pyautogui.scroll(50)

                elif found_item_bottom > list_box_bottom:
                    pyautogui.click(x, y)
                    pyautogui.scroll(-50)

                else:
                    rectangle = item.rectangle
                    return (rectangle.left,
                            rectangle.top,
                            rectangle.right,
                            rectangle.bottom)

                items = get_items_info(list_box)
                for item in items:
                    if find_item == getattr(converting_info_to_string(item.name), field):
                        rectangle = item.rectangle
                        return (rectangle.left,
                                rectangle.top,
                                rectangle.right,
                                rectangle.bottom)

        if found_item or items[-1] == last_item:
            raise RuntimeError('error')

        last_item = items[-1]

        pyautogui.click(x, y)
        pyautogui.scroll(-50)
        pyautogui.scroll(-50)
        pyautogui.scroll(-50)
        pyautogui.click(x, y)


def get_items_info(list_box: ListViewWrapper) -> List[ElementInfo]:
    return [item.element_info for item in list_box.children() if
            item.element_info.name.endswith('widget')]


def get_items_info_string(list_box: ListViewWrapper) -> str:
    items = get_items_info(list_box)

    items = [item.name for item in items]

    items = list(map(lambda x: x.replace('_____widget', ''), items))

    return items


def get_list_box_coordinate_center(list_box: ListViewWrapper):
    list_box_coordinate = list_box.rectangle()

    x = list_box_coordinate.left + (list_box_coordinate.right - list_box_coordinate.left) / 2
    y = list_box_coordinate.top + (list_box_coordinate.bottom - list_box_coordinate.top) / 2
    return x, y


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
