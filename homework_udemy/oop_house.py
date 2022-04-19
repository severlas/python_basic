class Human:
    default_name = 'No name'
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'Имя: {self.name} \n'
              f'Возраст: {self.age} \n'
              f'Деньги: {self.__money} \n'
              f'Дом: {self.__house}')

    @staticmethod
    def default_info():
        return f'{Human.default_name}, {Human.default_name}'

    def earn_money(self, amount):
        self.__money += amount
        print(f'Заработано {amount} денег, сейчас у вас {self.__money}')

    def buy_house(self, house, sale):
        price = house.final_price(sale)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print(f'Дом {house}, его цена - {price}, у вас недостаточно средств - {self.__money}')

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house


class House:

    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, sale):
        final_price = self._price * (100 - sale) / 100
        return final_price


class SmallHouse(House):
    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)


if __name__ == '__main__':

    Human.default_info()

    alexander = Human('Sergey', 24)
    alexander.info()

    small_house = SmallHouse(8_500)

    alexander.buy_house(small_house, 5)

    alexander.earn_money(5_000)
    alexander.buy_house(small_house, 5)

    alexander.earn_money(20_000)
    alexander.buy_house(small_house, 5)
    alexander.info()