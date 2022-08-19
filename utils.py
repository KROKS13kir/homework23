# функция, формирующая данные по необходимому файлу
import re
from typing import Iterable, Optional


def make_query(cmd: Optional[str], val: Optional[str], file: Iterable) -> Iterable:
    data_mapped = map(lambda x: x.strip, file)
    if cmd == 'unique':
        return set(data_mapped)
    if val:
        if cmd == 'filter':
            result = filter(lambda v: val in v, data_mapped)
            return result
        if cmd == 'map':
            return map(lambda x: x.split(" ")[int(val)], data_mapped)
        if cmd == 'sort':
            reverse_direction: bool = ('desc' == val.lower())
            return sorted(data_mapped, reverse=reverse_direction)
        if cmd == 'limit':
            return list(data_mapped)[:int(val)]
        if cmd == 'regex':
            regex = re.compile(val)
            result = filter(lambda x: regex.search(x), file)
            return result

    return data_mapped
