prices = {"Strawberries": 1.5, "Banana": 0.5, "Mango": 2.5,
              "Blueberries": 1, "Raspberries": 1, "Apple": 1.75,
              "Pineapple": 3.5}


class Beverage:

    def __init__(self, ingredients: list):
        self.ingredients = ingredients

    def get_cost(self):
        result_l = []
        for i in self.ingredients:
            if i in prices:
                result_l.append(prices.get(i))
        r = round(sum(result_l), 2)
        return f'${r:.2f}'

    def get_price(self):
        cost = float(Beverage.get_cost(self)[1:])
        r = round(cost * 2.5, 2)
        return f'${r:.2f}'

    def get_name(self):
        self.ingredients.sort()
        result_get_name = ' '.join(self.ingredients)
        result = result_get_name.replace('berries', 'berry')
        if len(self.ingredients) == 1:
            return f'{result} Smoothie'
        elif len(self.ingredients) > 1:
            return f'{result} Fusion'


# Проверка
s1 = Beverage(['Banana'])
s2 = Beverage(["Strawberries", "Banana", "Mango",
              "Blueberries", "Raspberries", "Apple",
              "Pineapple"])

s3 = Beverage(["Strawberries", "Blueberries", "Raspberries"])

print(s1.ingredients)
print(s1.get_cost())
print(s1.get_price())
print(s1.get_name())
print(s2.ingredients)
print(s2.get_cost())
print(s2.get_price())
print(s2.get_name())
print(s3.ingredients)
print(s3.get_cost())
print(s3.get_price())
print(s3.get_name())
