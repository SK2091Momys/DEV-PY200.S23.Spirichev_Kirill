from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        #  TODO заменить на метод

          # объем стакана
        self.capacity_volume = None
        self.init_capacity_volume(capacity_volume)
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError
        self.occupied_volume = occupied_volume  # объем жидкости в стакане

#  TODO создать метод, который будет инициализировать атрибут capacity_volume
    def init_capacity_volume (self, volume):
        if not isinstance(volume, (int, float)):
            raise TypeError
        if not volume > 0:
            raise ValueError
        self.capacity_volume = volume


if __name__ == "__main__":
    glass1 = Glass(200, 100)
    ...  # TODO инициализировать экземпляр класса Glass
    print(glass1.capacity_volume)  # TODO распечатать атрибут capacity_volume
    print(glass1.occupied_volume)  # TODO распечатать атрибут occupied_volume
