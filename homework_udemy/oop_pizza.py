class Pizza:
    order = 0

    def __init__(self, ingredients: list):
        self.ingredients = ingredients
        # Pizza.order += 1
        # self.order_number = Pizza.order    # 1-й вариант решения

    @property
    def order_number(self):
        Pizza.order += 1
        return Pizza.order                   # 2-й вариант решения

    @classmethod
    def garden_feast(cls):
        result_g_f = ['spinach', 'olives', 'mushroom']
        return cls(result_g_f)

    @classmethod
    def meat_festival(cls):
        result_m_f = ['beef', 'meatball', 'bacon']
        return cls(result_m_f)

    @classmethod
    def hawaiian(cls):
        result_h = ['ham', 'pineapple']
        return cls(result_h)


p0 = Pizza(['bacon', 'parmesan', 'ham'])
p1 = Pizza(['bacon', 'ham'])
p2 = Pizza.garden_feast()
p3 = Pizza.meat_festival()
p4 = Pizza.meat_festival()
p5 = Pizza.hawaiian()
print(p1.ingredients)
print(p2.ingredients)
print(p3.ingredients)
print(p4.ingredients)
print(p0.order_number)
print(p1.order_number)
print(p2.order_number)
print(p3.order_number)
print(p4.order_number)
print(p5.order_number)
