# class_character.py

## Descripción General

Este archivo contiene la definición de la clase `Character`, que abstrae las propiedades y métodos asociados a un personaje en el contexto de un mini juego. Esta clase permite la creación de personajes, el acceso a su información y la combinación de dos personajes en uno nuevo.

## Importaciones y Contexto

### from __future__ import annotations
Esta importación permite el uso de anotaciones de tipo (type hints) para clases que aún no han sido definidas completamente o que se definen en el mismo archivo. Es especialmente útil para evitar problemas de referencia circular.

## Clase `Character`

### Definición
```python
class Character:
    """Clase que abstrae las propiedades de un personaje y posee métodos para su autogestión."""
```
La clase encapsula las características principales de un personaje, como nombre, fuerza y velocidad, junto con métodos para su gestión y manipulación.

### Constructor
```python
    def __init__(self, name: str, strength: int, speed: int) -> None:
        self.__name: str = name
        self.__strength: int = strength
        self.__speed: int = speed
```
#### Parámetros:
- `name` (str): Nombre del personaje.
- `strength` (int): Fuerza del personaje.
- `speed` (int): Velocidad del personaje.

#### Notas:
- Los atributos están encapsulados (prefijo `__`) para evitar acceso directo desde fuera de la clase.
- Se utiliza tipado explícito para garantizar claridad en los tipos esperados de los atributos.

### Propiedades

#### `name`
```python
    @property
    def name(self):
        return self.__name
```
Devuelve el nombre del personaje. Se implementa como una propiedad para garantizar acceso de solo lectura.

#### `info`
```python
    @property
    def info(self) -> str:
        """Devuelve información sobre el personaje."""
        return f'{self.__name}, fuerza: {self.__strength}, velocidad: {self.__speed}'
```
Devuelve una descripción detallada del personaje como un string, incluyendo su nombre, fuerza y velocidad.

#### Notas sobre las propiedades:
- Las propiedades en Python permiten abstraer el acceso a los atributos, haciendo que estos parezcan accesibles directamente pero en realidad pasando por un método.

### Método Especial `__add__`
```python
    def __add__(self, second_character: Character) -> Character:
        """Combina dos personajes en uno nuevo."""
        new_name = self.__name[:4] + second_character.__name[-4:]
        new_strength = round(((self.__strength + second_character.__strength) / 2) ** 1.2)
        new_speed = round(((self.__speed + second_character.__speed) / 2) ** 1.2)
        return Character(new_name, new_strength, new_speed)
```
#### Función:
Permite combinar dos objetos de tipo `Character` usando el operador `+`.

#### Parámetros:
- `second_character` (Character): El personaje con el que se combinará el actual.

#### Retorno:
Un nuevo objeto `Character`.

#### Detalles de Implementación:
1. El nuevo nombre combina las primeras 4 letras del primer personaje con las últimas 4 letras del segundo.
2. La nueva fuerza y velocidad se calculan como el promedio de las correspondientes en ambos personajes, elevado a la potencia de 1.2 para dar más peso a valores altos.
3. La función utiliza `round()` para garantizar que los valores sean enteros.

#### Uso de Métodos Especiales en Python:
Este es un ejemplo de sobrecarga de operadores. El método `__add__` redefine el comportamiento del operador `+` para objetos de la clase `Character`.

## Ejemplo de Uso
```python
# Creación de personajes
character1 = Character("Héroe", 50, 30)
character2 = Character("Villano", 40, 60)

# Acceso a información
print(character1.info)  # Output: Héroe, fuerza: 50, velocidad: 30

# Combinar personajes
new_character = character1 + character2
print(new_character.info)  # Output: algo como "Héroano, fuerza: 57, velocidad: 49"
```

## Conceptos Avanzados Utilizados

### Encapsulación
Los atributos `__name`, `__strength` y `__speed` están encapsulados, lo que significa que no son accesibles directamente desde fuera de la clase. Esto protege los datos internos y asegura que solo se acceda o modifique mediante métodos controlados.

### Propiedades (`@property`)
Se utilizan para exponer atributos de manera controlada, permitiendo lecturas pero no escrituras directas. Esto mejora la seguridad y flexibilidad.

### Sobrecarga de Operadores
El método `__add__` redefine cómo funciona el operador `+` para objetos de tipo `Character`. Esto permite crear una sintaxis más intuitiva y orientada al dominio (en este caso, la combinación de personajes).

### Tipado
Se utiliza tipado explícito (`str`, `int`, `Character`) para mejorar la claridad y detectar errores en tiempo de desarrollo.
