

class DoubleElement:
    def __init__(self, *lst):
        self.lst = list(lst)
        self.index = 0

    # Метод __iter__ должен вернуть сам объект класса:
    def __iter__(self):
        return self
    
    # В методе __next__ нужно реализовать логику итерации по списку и возвращения пары элементов:
    def __next__(self):
        
        if len(self.lst) > 0:                        # проверяем, если список lst не пустой
            first_element = self.lst.pop(0)          # то извлекаем из него первый элемент и сохраняем его в переменную first_element. 
            if len(self.lst) > 0:                    # Далее, если список еще не пустой,
                second_element = self.lst.pop(0)     # извлекаем из него следующий элемент и сохраняем его в переменную second_element,
            else:
                second_element = None                #  иначе присваиваем None переменной second_element.
            return (first_element, second_element)   # Затем, возвращаем пару элементов (first_element, second_element)
        
        else:                                        # Если список lst становится пустым
            raise StopIteration                      # вызываем исключение StopIteration.

"
#

dL = DoubleElement(1,2,3,4)
for pair in dL:
    print(pair)

print()

dL = DoubleElement(1,2,3,4,5)
for pair in dL:
    print(pair)

