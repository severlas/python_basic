class Tomato:
    states = {0: 'Отсутствует', 1: 'Цветет', 2: 'Зеленый', 3: 'Красный'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Помидор №{self._index} - {Tomato.states[self._state]}')


class TomatoBush:

    def __init__(self, num_tomato):
        self.tomatoes = [Tomato(index) for index in range(0, num_tomato)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []


class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Садовник работает...')
        self._plant.grow_all()
        print('Садовник закончил работу')

    def harvest(self):
        print('Садовник собирает урожай...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Садовник закончил сбор урожая')
        else:
            print('Слишком рано, ваши плоды еще не поспели!')

    @staticmethod
    def knowledge_base():
        print('''Здесь должна быть справка по садоводству ...''')


if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(7)
    gardener = Gardener('Karina', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()


