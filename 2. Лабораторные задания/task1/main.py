import doctest
from typing import Optional, Union


class Stapler:
    def __init__(self, width_staple: Union[int, float] = None, quanitity_staple: Optional[int] = None):
        """
        Создание и подготовка к работе объекта Степлер

        :param width_staple: ширина используемых скоб в Степлере
        :param quanitity_staple: количество скоб в касете Степлера

        Пример:
        >>> stapler = Stapler(24, 50)
        """
        self.width_staple = None
        self.init_width_staple(width_staple)
        self.quanitity_staple = None
        self.init_quanitity_staple(quanitity_staple)

    def init_width_staple(self, width_staple):
        """
        Метод инициализирующий атрибут width_staple

        :param width_staple: ширина используемых скоб в Степлере

        Пример:
        >>> stapler = Stapler(24,50)
        >>> stapler.init_width_staple(26)
        """
        if not isinstance(width_staple, (int, float)):
            raise TypeError("Ширина скобы должна быть целым или вещественным числом! ")
        if width_staple < 0:
            raise ValueError("Ширина скобы не может быть числом отрицательным!")
        self.width_staple = width_staple

    def init_quanitity_staple(self, quanitity_staple):
        """
        Метод инициализирующий атрибут quanitity_staple

        :param quanitity_staple: количество скоб в касете Степлера

         Пример:
        >>> stapler = Stapler(24,50)
        >>> stapler.init_quanitity_staple(60)
        """
        if not isinstance(quanitity_staple, int):
            raise TypeError("Количество скоб должно быть целым числом! ")
        if quanitity_staple < 0:
            raise ValueError("Количество скоб не может быть числом отрицательным!")
        self.quanitity_staple = quanitity_staple

    def get_quanitity_staple(self, count_staple: int):
        """
        Функция добовляющая определенное количество скоб

        :param count_staple: Количество добавленных скоб

        Пример:
        >>> stapler = Stapler(26, 60)
        >>> stapler.get_quanitity_staple(50)

        """
        if not isinstance(count_staple, int):
            raise TypeError("Количество добавляемы скоб должно быть целым числом!")
        self.quanitity_staple += count_staple
        return self.quanitity_staple

    def __repr__(self):
        return f'Stapler({self.width_staple}, {self.quanitity_staple})'


class Marker:
    def __init__(self, color: str, qanitity_ink: (int, float)):
        """
        Создание и подготовка к работе объекта Маркер

        :param color: цвет маркера
        :param qanitity_ink:Количество чернил в маркере
        """
        self.color = self.unit_color(color)
        self.qanitity_ink = 0
        self.qanitity_ink = qanitity_ink

    def unit_color(self, color_: str) -> str:
        """
        Метод инициализирующий цвет маркера

        :param color_: Обозначает цвет маркера
        """
        if not isinstance(color_, str):
            raise TypeError("Цвет маркера должен иметь тип str")
        self.color = color_
        return self.color

    def unit_qanitity_ink(self, qanitity_ink: (int, float)):
        """
        Метод инициализирующий количество чернил в маркере

        :param qanitity_ink: количество чернил в маркере
        """
        if not isinstance(qanitity_ink, (int, float)):
            raise TypeError("Количество чернил должно быть типа int или float")
        if qanitity_ink < 0:
            raise ValueError("Количество чернил не может быть меньше нуля")
        self.qanitity_ink = qanitity_ink

    def add_qanitity_ink(self, count_ink: (int, float)):
        """
        Метод добавляющий количество чернил в маркере

        :param count_ink: Количество добавленных чернил
        :return Общее колиество чернил в маркере
        """
        self.qanitity_ink += count_ink
        return self.qanitity_ink

    def spend_it_qanitity_ink(self, count_ink: (int, float)):
        """
        Метод  убавляющий количество чернил в маркере

        :param count_ink: Количество использованных чернил
        :return Общее количество чернил в маркере
        """
        self.qanitity_ink -= count_ink
        return self.qanitity_ink

    def __repr__(self):
        return f'Marker({self.color}, {self.qanitity_ink})'


class Flower:

    def __init__(self, color: str, count_bud: int, perennial: bool):
        """
        Создание и подготовка к работе объекта Цветок

        :param color: Цвет бутона
        :param count_bud: Количество бутонов на цветке
        :param perennial: Характеристика показывающая является ли цветок многолетним
        """
        self.color = self.init_color(color)
        self.count_bud = self.init_count_bud(count_bud)
        self.perennial = self.init_perennial(perennial)

    def init_color(self, color_: str):
        """
        Метод инициализирующий цвет цветка

        :param color_: цвет бутона
        """
        if not isinstance(color_, str):
            raise TypeError("Цвет цветка должен быть типом str")
        self.color = color_
        return self.color

    def init_count_bud(self, count: int):
        """
        Метод инициализирующий количество бутонов на цветке
        :param count: количество бутонов
        """
        if not isinstance(count, int):
            raise TypeError("Количество бутонов должно быть типом int")
        if count < 0:
            raise ValueError("Количество бутоов не может быть меньше ноля")
        self.count_bud = count
        return self.count_bud

    def init_perennial(self, perennial: bool):
        """
        Метод инициализирующий многолетие цветка

        :param perennial: принимает значение True если цветок многолетний
        """
        if not isinstance(perennial, bool):
            raise TypeError("Многолетие цветка должно быть типом bool")
        self.perennial = perennial
        return self.perennial

    def cut_off_bud(self, cut_off_bud: int) -> int:
        """
        Метод указывающий сколько бутонов срезано с цветка

        :param cut_off_bud: количество срезанных бутонов
        :return Общее количство бутонов после срезки
        """
        if not isinstance(cut_off_bud, int):
            raise TypeError("Количество срезанных бутонов должно быть типом int")
        if cut_off_bud < 0:
            raise ValueError("Количество срезанных бутонов должно быть больше ноля")
        if cut_off_bud > self.count_bud:
            raise ValueError("Количество срезанных бутонов не может быть больше общего количества бутонов")
        self.count_bud -= cut_off_bud
        return self.count_bud

    def __repr__(self):
        return f"Flower({self.color}, {self.count_bud}, {self.perennial})"

# TODO Написать 3 класса с документацией и аннотацией типов

if __name__ == "__main__":
    # stapler = Stapler(24, 50)
    # print(stapler)
    # stapler.get_quanitity_staple(-50)
    # print(stapler)
    doctest.testmod()
    marker = Marker()
    # print(marker)
    # marker.add_qanitity_ink(50)
    # print(marker)
    # marker.spend_it_qanitity_ink(100)
    # print(marker)
    # flower = Flower("Красный", 15, False)
    # print(flower)
    # flower.cut_off_bud(10)
    # print(flower)

    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
