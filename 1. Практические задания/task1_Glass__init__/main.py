from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        #  TODO инициализировать объект "Стакан"
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError('Объем стакана должен быть целым или вещественным числом')
        if capacity_volume < 0:
            raise ValueError('Объем стакана должен быть больше или равен нулю')
        self.capacity_volume = capacity_volume
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError('Заполняемый объем стакана должен быть целым или вещественным числом')
        if occupied_volume < 0:
            raise ValueError('Объем заполняемой жидкости должен быть больше либо равен нулю')
        if occupied_volume > capacity_volume:
            raise ValueError('Объем заполняемой жидкости не может быть больше объема стакана')
        self.occupied_volume = occupied_volume


if __name__ == "__main__":
    ...  # TODO инициализировать два объекта типа Glass
    glass_1 = Glass(500, 300)
    print(glass_1.capacity_volume, glass_1.occupied_volume)
    # TODO попробовать инициализировать не корректные объекты
    glass_2 = Glass(250, 100)
    print(glass_2.capacity_volume, glass_2.occupied_volume)