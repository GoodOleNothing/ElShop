from workshop.item import Item


class Mixing:
    """класс-миксер для смены языка"""
    def __init__(self, *args):
        super().__init__(*args)
        self._language = 'EN'

    @property
    def language(self):
        return self._language

    def change_lang(self):
        """Метод меняет язык"""
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'


class Keyboard(Mixing, Item):
    """Класc с сочетанием класса-миксера и основного класса"""
    pass



