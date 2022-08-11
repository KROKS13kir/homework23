# функция, формирующая данные по необходимому файлу
def make_query(cmd, val, file):
    if cmd == 'filter':
        result = filter(lambda v: val in v, file)
        return result
    if cmd == 'map':
        try:
            result = [line.split()[int(val)] for line in file]
            return result
        except StopIteration:
            print("Выход за пределы")
    if cmd == 'unique':
        result = list(set(file))
        return result
    if cmd == 'sort':
        reverse_direction: bool = ('desc' == val.lower())
        return sorted(file, reverse=reverse_direction)
    if cmd == 'limit':
        try:
            return list(file)[:int(val)]
        except StopIteration:
            print("Выход за пределы")




