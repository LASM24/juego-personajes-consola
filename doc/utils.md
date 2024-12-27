# utils.py

## Descripción General

El archivo `utils.py` contiene funciones auxiliares diseñadas para mejorar la experiencia del usuario en el juego. Estas funciones se centran en proporcionar una salida visual atractiva y en simular progresos para acciones clave como la creación y fusión de personajes.

---

## Funciones

### `custom_print`

#### Definición
```python
def custom_print(*args, color=Fore.WHITE, style=Style.NORMAL, **kwargs):
```

#### Descripción
Esta función imprime mensajes en consola con colores y estilos personalizados utilizando la librería `colorama`.

#### Parámetros
- **`*args`**: Lista de argumentos que se unirán y se imprimirán como un solo mensaje.
- **`color`**: Define el color del texto (por defecto, blanco). Valores comunes:
  - `Fore.RED`: Rojo.
  - `Fore.GREEN`: Verde.
  - `Fore.YELLOW`: Amarillo.
  - `Fore.CYAN`: Cian.
- **`style`**: Define el estilo del texto (por defecto, normal). Valores comunes:
  - `Style.BRIGHT`: Texto en negrita.
  - `Style.DIM`: Texto tenue.
- **`**kwargs`**: Argumentos adicionales para la función `print`, como `end` o `sep`.

#### Ejemplo de Uso
```python
custom_print("Este es un mensaje importante", color=Fore.RED, style=Style.BRIGHT)
```

---

### `fusion_progress`

#### Definición
```python
def fusion_progress():
```

#### Descripción
Simula el progreso de la fusión de personajes mediante una barra de progreso generada con la librería `tqdm`.

#### Detalles Técnicos
- Utiliza `tqdm` para mostrar una barra de progreso.
- Pausa el flujo de ejecución durante 0.01 segundos por cada paso para simular el tiempo transcurrido.

#### Ejemplo de Uso
```python
fusion_progress()
```

---

### `creation_progress`

#### Definición
```python
def creation_progress():
```

#### Descripción
Simula el progreso de la creación de un personaje con una barra de progreso generada por `tqdm`.

#### Detalles Técnicos
- Similar a `fusion_progress`, pero con un mensaje de descripción diferente.
- Pausa el flujo de ejecución durante 0.01 segundos por cada paso.

#### Ejemplo de Uso
```python
creation_progress()
```

---

## Dependencias

- **`colorama`**: Para manejar colores y estilos en consola.
  - **Instalación**: `pip install colorama`
- **`tqdm`**: Para generar barras de progreso.
  - **Instalación**: `pip install tqdm`
- **`time`**: Para simular pausas en la ejecución.

---

## Notas
- **Compatibilidad**: `colorama` requiere inicialización en sistemas Windows (ya está hecho en otros archivos del proyecto).

