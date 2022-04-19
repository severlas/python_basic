class Cat:

    def __init__(self, weight, length):  # Инициализируем обьект и добавляем его атрибуты
        self.weight = weight
        self.length = length

    def __add__(self, other):  # Реализовываем метод сложения собаки и кота
        if isinstance(self, Cat) and isinstance(other, Dog):
            weight = ((self.weight + other.weight) / 2)
            length = ((self.length + other.length) / 2)
            return CatDog(weight, length)

    def __str__(self) -> str:  # Приводим обьект к строке
        return f'Длина кота: {self.length} см, \nВес кота: {self.weight} кг'


class Dog:

    def __init__(self, weight, length):  # Инициализируем обьект и добавляем его атрибуты
        self.weight = weight
        self.length = length

    def __add__(self, other):  # Реализовываем метод сложения собаки и кота
        if isinstance(self, Dog) and isinstance(other, Cat):
            weight = ((self.weight + other.weight) / 2)
            length = ((self.length + other.length) / 2)
            return CatDog(weight, length)

    def __str__(self) -> str:  # Приводим обьект к строке
        return f'Длина собаки: {self.length} см, \nВес собаки: {self.weight} кг'


class CatDog:

    def __init__(self, weight, length):  # Инициализируем обьект и добавляем его атрибуты
        self.weight = weight
        self.length = length

    def __str__(self) -> str:  # Приводим обьект к строке
        return f'Длина котопса: {self.length} см, \nВес котопса: {self.weight} кг'


#  Для проверки
cat = Cat(5, 45)
dog = Dog(8, 80)
cat_dog = cat + dog
print(type(cat+dog))
print(cat)
print(dog)
print(cat_dog)
