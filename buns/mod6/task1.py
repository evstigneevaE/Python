
class Node:    # При создании объекта класса Node мы передаем значение узла и инициализируем атрибут next_node значением None.
    def __init__(self, value):
        self.value = value      # атрибут: value (значение узла)
        self.next_node = None   # атрибут: next_node (указатель на следующий узел)
        

class LinkedList:
    def __init__(self):
        self.head = None

    class LinkedListIterator:
 
        def __init__(self,head):
            self.current_node = head
   
        def __iter__(self):
            return self

        def __next__(self):
            if self.current_node is not None:
                value = self.current_node.value
                self.current_node = self.current_node.next_node
                return value
            else:
                raise StopIteration
    
    def __iter__(self):
        return LinkedList.LinkedListIterator(self.head)

    def push(self, val):               
        new_node = Node(val)           
        if self.head is None:           
            self.head = new_node        
        else:
            current_node = self.head    
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = new_node # ... и присваиваем его next_node новому узлу
        
    def get(self, index): # получение элемента по индексу (принимает индекс и возвращает значение элемента по этому индексу)
        if self.head is None:       # проверим: если список пустой
            print("Список пустой")  # выводим сообщение об этом
            return None             # возвращаем None
   
        current_node = self.head
        count = 0
        while current_node is not None:
            if count == index:
                return current_node.value
            current_node = current_node.next_node
            count += 1
        # Если индекс выходит за пределы списка, то выводим сообщение и возвращаем None.
        print("Некорректный индекс")
        return None


    def remove(self, index):         # удаление элемента по индексу (принимает индекс и удаляет элемент с этим индексом)
        if self.head is None:        # Проверяем, если список пустой
            print("Список пустой")   # выводим сообщение об этом и ничего не делаем
            return
        if index == 0:                       # Если индекс равен 0
            self.head = self.head.next_node  # то переопределяем голову как следующий узел и возвращаемся
            return
        # Иначе, мы проходим по списку до узла с индексом n-1
        current_node = self.head
        count = 0
        while current_node is not None:
            if count == index - 1:
                current_node.next_node = current_node.next_node.next_node # и переопределяем его next_node как следующий узел удаляемого узла.
                return
            current_node = current_node.next_node
            count += 1
        # Если индекс выходит за пределы списка, то выводим сообщение и возвращаем None.
        print("Некорректный индекс")
    
    
    def insert(self, index, val):        # вставить элемент val между элементами с номерами n-1 и n:
        if self.head is None:            # Проверяем, если список пустой
            print("Список пустой")       # то выводим сообщение об этом и ничего не делаем
            return
    
        # Создаем новый узел со значением val
        new_node = Node(val)
        if index == 0:                      # Если индекс равен 0
            new_node.next_node = self.head  # то переопределяем голову как новый узел, а его next_node как узел, который был первым
            self.head = new_node
            return
    
        # Иначе, мы проходим по списку до узла с индексом n-1
        current_node = self.head
        count = 0
        while current_node is not None:
            if count == index - 1:                              # и переопределяем его next_node как новый узел,
                new_node.next_node = current_node.next_node     # а next_node нового узла как следующий узел.
                current_node.next_node = new_node
                return
            current_node = current_node.next_node
            count += 1
        # Если индекс выходит за пределы списка, то выводим сообщение и возвращаем None.
        print("Некорректный индекс")
        

linkedList = LinkedList()
linkedList.push(1)
linkedList.push(2)
linkedList.push(3)

print(linkedList.get(0)) # Вывод:  1
print(linkedList.get(1)) # Вывод:  2
print(linkedList.get(2)) # Вывод:  3

linkedList.remove(2)
print(linkedList.get(2)) # Вывод:  "Некорректный индекс
#                                   None"

linkedList.push(4)
print(linkedList.get(2)) # Вывод:  4

linkedList.insert(2, 99)
print(linkedList.get(2)) # Вывод:  99
print(linkedList.get(3)) # Вывод:  4

# print(linkedList.size()) # 4

for item in linkedList:
    print(item, end=' ') # Вывод: 1 2 99 4 
