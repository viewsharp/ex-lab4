# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False

        if kwargs.get('ignore_case') is True:
            items = map(lambda line: line.lower(), items)
        self.items = list(set(items))
        self.items.sort(reverse=True)

    def __next__(self):
        if not self.items:
            raise StopIteration
        return self.items.pop()

    def __iter__(self):
        return self
