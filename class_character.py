from __future__ import annotations

class Character:
    """Clase que abstrae las propiedades de un personaje y posee métodos para su autogestión."""
    def __init__(self, name: str, strength: int, speed: int) -> None:
        self.__name: str = name
        self.__strength: int = strength
        self.__speed: int = speed

    @property
    def name(self):
        return self.__name

    @property
    def info(self) -> str:
        """Devuelve información sobre el personaje."""
        return f'{self.__name}, fuerza: {self.__strength}, velocidad: {self.__speed}'

    def __add__(self, second_character: Character) -> Character:
        """Combina dos personajes en uno nuevo."""
        new_name = self.__name[:4] + second_character.__name[-4:]
        new_strength = round(((self.__strength + second_character.__strength) / 2) ** 1.2)
        new_speed = round(((self.__speed + second_character.__speed) / 2) ** 1.2)
        return Character(new_name, new_strength, new_speed)
