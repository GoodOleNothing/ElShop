import csv
from workshop.item import Item


class Phone(Item):

    def __init__(self, item_name, item_price, amount, number_of_sim):
        super().__init__(item_name, item_price, amount)
        self._number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        """Количество физических SIM-карт должно быть целым числом больше нуля."""
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value: int):
        if isinstance(value, int) and int(value) > 0:
            self._number_of_sim = value
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
