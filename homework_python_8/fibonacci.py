def fibonacci(n):
    list_fib = []
    f_1 = 0
    f_2 = 1
    for i in range(n):
        f_1, f_2 = f_2, f_1 + f_2
        list_fib.append(f_1)
    return list_fib


# Проверка
n_input = int(input('Введите число: '))
fib_result = fibonacci(n_input)
print(fib_result)
