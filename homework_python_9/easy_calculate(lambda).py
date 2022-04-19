def math_operation(operation):
    if operation == '+':
        return lambda a, b: a + b
    if operation == '-':
        return lambda a, b: a - b
    if operation == '*':
        return lambda a, b: a * b
    if operation == '**':
        return lambda a, b: a ** b
    if operation == '/':
        return lambda a, b: a / b





# Проверка ф-и
operation_func = input('Введите операцию над числами: \t')
input_a = int(input('Введите первое числа: \t'))
input_b = int(input('Введите второе числа: \t'))
result_operation = math_operation(operation_func)
result_func = result_operation(input_a, input_b)
print(f'Результат:\t {result_func}')
