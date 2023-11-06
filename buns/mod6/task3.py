

def is_armstrong_number(n):
    num_str = str(n) # преобразуем число в строку для удобства обращения к отдельным цифрам
    num_len = len(num_str) # получаем длину числа
    armstrong_sum = sum(int(digit)**num_len for digit in num_str) # сумма цифр числа, возведенных в степень
    return armstrong_sum == n # проверяем, является ли полученная сумма равной исходному числу

def get_armstrong_numbers():
    num = 10                           # начинаем с числа 10, для пропуска чисел от 0 до 9, так как они не являются числами Армстронга.
    while True:                        # Если число num является числом Армстронга
        if is_armstrong_number(num):   # то оно возвращается с помощью ключевого слова yield
            yield num                  # Это позволяет использовать функцию get_armstrong_numbers() как генератор.
        num += 1 # увеличиваем число для проверки следующего
        
armstrong_generator = get_armstrong_numbers() # Создаем экземпляр генератора

for i in range(8):                            # Получаем и выводим первые 8 чисел Армстронга
    print(next(armstrong_generator), end=' ') # Каждый элемент генератора получается с помощью функции next(armstrong_generator)


