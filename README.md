# Juego de Personajes en Consola

## Descripción
Este proyecto es un juego de personajes desarrollado en Python para ejecutarse en la consola. Permite a los usuarios:
- Crear personajes con atributos personalizados.
- Listar personajes existentes.
- Fusionar dos personajes para generar uno nuevo con características combinadas.
- Eliminar personajes del listado.

El sistema incluye dos versiones del menú interactivo:
1. Con colores y estilos (usando la biblioteca `colorama`).
2. Sin colores ni estilos.

---

## Características
- **Menú interactivo**: Presenta opciones claras y permite al usuario navegar fácilmente por el juego.
- **Clases modulares**: Separación lógica del código en múltiples módulos.
- **Simulación visual**: Barras de progreso para acciones como creación y fusión de personajes (usando `tqdm`).
- **Compatibilidad multiplataforma**: Asegura la limpieza de la consola tanto en Windows como en Unix.

---

## Requisitos del Sistema

- Python 3.8 o superior.
- Las bibliotecas listadas en `requirements.txt`.

---

## Instalación
Sigue los pasos para configurar y ejecutar el proyecto en tu máquina local:

### 1. Clonar el Repositorio
```bash
git clone https://github.com/LASM24/juego-personajes-consola.git
cd juego-personajes-consola
```

### 2. Crear un Entorno Virtual
```bash
python -m venv venv
```
- En Windows:
  ```bash
  venv\Scripts\activate
  ```
- En Unix o MacOS:
  ```bash
  source venv/bin/activate
  ```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar el Juego
```bash
python main.py
```

---

## Archivos Principales

### `main.py`
Punto de entrada del programa. Permite alternar entre el menú con colores (`Menu`) y el menú sin colores (`MenuNoColor`).

### `menu.py`
Contiene las clases `Menu` y `MenuNoColor`, que gestionan el flujo principal del juego.

### `class_character.py`
Define la clase `Character`, que abstrae las propiedades y métodos relacionados con los personajes.

### `utils.py`
Funciones auxiliares para:
- Imprimir mensajes personalizados con colores y estilos.
- Simular progresos mediante barras visuales.

### `requirements.txt`
Lista las dependencias necesarias:
- `colorama`
- `tqdm`

---

## Uso
1. Al ejecutar `main.py`, el menú se mostrará en consola.
2. Selecciona una opción según las instrucciones.
3. Sigue las indicaciones para crear, listar, fusionar o eliminar personajes.
4. Para cambiar entre las versiones de menú, edita el archivo `main.py` comentando/descomentando las líneas de inicialización del menú.

---

## Ejemplo
```bash
¡¡BIENVENIDO AL MENÚ!!
1. Listar personajes
2. Crear personaje
3. Fusionar personajes
4. Eliminar personaje
0. Salir
Selecciona una opción:
```

---

## Contribuciones
Las contribuciones son bienvenidas. Si deseas colaborar:
1. Realiza un fork del repositorio.
2. Crea una rama con tu funcionalidad o corrección.
3. Envía un Pull Request.

---
