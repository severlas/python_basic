def computation_square(a):
    perimeter = round(a * 4, 2)
    square = round(a**2, 2)
    diagonal = round(a * (2**0.5), 2)
    output = (perimeter, square, diagonal)
    return output


side = float(input('Введите сторону квадрата: '))
q = computation_square(side)
print(q)
