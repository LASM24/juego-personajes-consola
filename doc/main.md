# main.md

## Descripción General

El archivo `main.py` es el punto de entrada del juego en consola. Su principal función es inicializar el menú deseado (`Menu` o `MenuNoColor`) y gestionar el flujo de ejecución del programa, incluyendo el manejo de excepciones comunes como errores inesperados o interrupciones por teclado.

---

## Estructura del Código

### Importaciones

```python
import os
from colorama import Fore
from menu import Menu, MenuNoColor
```

#### Descripción
1. **`os`**: Permite limpiar la consola en función del sistema operativo (Windows o Unix).
2. **`colorama.Fore`**: Se utiliza para aplicar colores a los mensajes en consola.
3. **`Menu`, `MenuNoColor`**: Clases importadas desde `menu.py`, que definen las versiones con y sin colores del menú interactivo.

---

### Flujo Principal

#### Definición
```python
try:
    # menu = MenuNoColor()
    menu = Menu()
    menu.run()

except Exception as e:
    print(f"{e}")
except KeyboardInterrupt:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.MAGENTA + '\nFIN DEL JUEGO\n')
```

#### Detalles
1. **Selección del Menú**
   - **`menu = MenuNoColor()`**: Línea comentada. Permite inicializar la versión del menú sin colores.
   - **`menu = Menu()`**: Línea activa por defecto, inicializa el menú con colores.
   - Cambiar entre estas dos líneas facilita probar o utilizar distintas versiones del menú sin modificar demasiado el código.

2. **Ejecución del Menú**
   - **`menu.run()`**: Llama al método principal de la clase seleccionada, iniciando el flujo interactivo del juego.

3. **Manejo de Excepciones**
   - **`Exception`**: Captura errores inesperados y los muestra en consola.
   - **`KeyboardInterrupt`**: Permite al usuario salir del programa usando `Ctrl+C`. Limpia la consola antes de mostrar un mensaje de despedida.

---

## Notas

- **Cambio entre Menús**
  - Para cambiar entre `Menu` y `MenuNoColor`, basta con comentar/descomentar las líneas correspondientes.
  - Este enfoque permite una mayor flexibilidad sin necesidad de modificaciones adicionales al código.

- **Limpieza de Consola**
  - Utiliza `os.system('cls' if os.name == 'nt' else 'clear')` para asegurar que funcione tanto en Windows como en Unix.
