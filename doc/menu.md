# menu.py

## Descripción General

Este archivo define el menú principal del juego, permitiendo a los usuarios interactuar con la lista de personajes a través de diversas acciones como listar, crear, fusionar y eliminar personajes. 

Se proporcionan dos clases principales:

1. **`Menu`**: Implementación con decoraciones y colores para mejorar la experiencia visual del usuario.
2. **`MenuNoColor`**: Implementación simplificada sin decoraciones para contextos donde no se soporten librerías como `colorama` o se prefiera un diseño minimalista.

Ambas clases comparten la misma lógica funcional, con diferencias únicamente en la presentación visual.

---

## Clases

### Clase `Menu`

#### Definición
```python
class Menu:
```
Esta clase gestiona un menú interactivo que utiliza colores y estilos decorativos mediante la librería `colorama` para mejorar la experiencia visual.

#### Constructor
```python
    def __init__(self) -> None:
        self.__characters: List[Character] = []
        self.options = {
            "1": self.list_characters,
            "2": self.create_character,
            "3": self.merge_characters,
            "4": self.delete_character,
        }
```

- **`self.__characters`**: Una lista de objetos `Character` que representa los personajes disponibles.
- **`self.options`**: Diccionario que mapea las opciones del menú con los métodos correspondientes.

#### Métodos Importantes

1. **`clear_console(func)`**: Decorador que limpia la consola antes de ejecutar el método decorado. 
2. **`display_menu()`**: Muestra el menú interactivo con colores y estilos decorativos.
3. **`list_characters()`**: Lista todos los personajes disponibles, mostrando un mensaje decorado si la lista está vacía.
4. **`create_character()`**: Permite al usuario crear un nuevo personaje verificando entradas válidas.
5. **`merge_characters()`**: Fusiona dos personajes existentes en uno nuevo.
6. **`delete_character()`**: Elimina un personaje por su nombre.
7. **`find_character_by_name(name)`**: Busca un personaje en la lista por nombre y devuelve el objeto correspondiente o `None` si no se encuentra.
8. **`run()`**: Método principal que ejecuta el menú en un bucle infinito hasta que el usuario decida salir.

---

### Clase `MenuNoColor`

#### Definición
```python
class MenuNoColor:
```
Una alternativa simplificada de la clase `Menu` que no utiliza decoraciones ni colores. Es útil para entornos donde no se soporten librerías externas como `colorama` o se prefiera un diseño más básico.

#### Estructura General
La lógica funcional es idéntica a la clase `Menu`, lo que facilita su comparación y uso intercambiable según las necesidades del entorno.

---

## Uso Recomendado

### Cuándo usar `Menu`
- Si se busca una experiencia visual más atractiva.
- Cuando el entorno soporta colores y estilos decorativos, por ejemplo, en consolas modernas.

### Cuándo usar `MenuNoColor`
- En contextos donde se prefiera un diseño minimalista.
- Si se ejecuta el programa en un entorno que no soporta `colorama` o decoraciones (por ejemplo, terminales básicas).

---

## Ejemplo de Uso
```python
# Inicializar el menú decorado
menu = Menu()
menu.run()

# Inicializar el menú sin decoraciones
menu_no_color = MenuNoColor()
menu_no_color.run()
```

---

## Consideraciones Técnicas

1. **Decorador `clear_console`**: Implementado en ambas clases para garantizar que cada acción del menú comience con una consola limpia.
2. **Modularidad**: Las clases están diseñadas para ser altamente modulares, permitiendo la reutilización de métodos en diferentes contextos.
3. **Validaciones**: Las entradas del usuario para fuerza y velocidad deben ser números entre 0 y 10, como se define en el método `validations_new_character`.

---

## Dependencias
- **`os`**: Para limpiar la consola según el sistema operativo.
- **`colorama`**: Proporciona colores y estilos para los mensajes en consola.
- **`class_character`**: Importa la clase `Character` para manejar la lógica de los personajes.
- **`utils`**: Importa funciones auxiliares como `fusion_progress`, `custom_print` y `creation_progress`. 

---