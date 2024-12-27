from typing import List
import os
from class_character import Character
from utils import fusion_progress, custom_print, creation_progress
from colorama import Fore, Style, init

init(autoreset=True)

def validations_new_character(name: str, strength: int, speed: int) -> bool:
    return len(name) >= 4 and 0 > strength <= 10 and 0 > speed <= 10

class Menu:
    def __init__(self) -> None:
        self.__characters: List[Character] = []
        self.options = {
            "1": self.list_characters,
            "2": self.create_character,
            "3": self.merge_characters,
            "4": self.delete_character,
        }

    def clear_console(func):
        def wrapper(self, *args, **kwargs):
            os.system('cls' if os.name == 'nt' else 'clear')
            return func(self, *args, **kwargs)
        return wrapper

    def find_character_by_name(self, name: str) -> Character | None:
        """Busca un personaje por su nombre."""
        for character in self.__characters:
            if name.lower() == character.name.lower():
                return character
        return None

    @clear_console
    def display_menu(self) -> None:
        custom_print("¡¡BIENVENIDO AL MENÚ!!", color=Fore.GREEN, style=Style.BRIGHT)
        custom_print("1. Listar personajes", color=Fore.CYAN)
        custom_print("2. Crear personaje", color=Fore.CYAN)
        custom_print("3. Fusionar personajes", color=Fore.CYAN)
        custom_print("4. Eliminar personaje", color=Fore.CYAN)
        custom_print("0. Salir", color=Fore.CYAN)

    @clear_console
    def list_characters(self) -> None:
        """Lista todos los personajes."""
        custom_print("Personajes:", color=Fore.CYAN)
        if not self.__characters:
            custom_print("No hay personajes creados.", color=Fore.YELLOW)
        for idx, character in enumerate(self.__characters, 1):
            custom_print(f"{idx}. {character.info}", color=Fore.MAGENTA)
        input(Fore.WHITE + "Presione Enter para continuar...")

    @clear_console
    def create_character(self) -> None:
        name = input(Fore.CYAN + "Inserte nombre: ")
        strength = int(input(Fore.CYAN + "Inserte fuerza (0-10): "))
        speed = int(input(Fore.CYAN + "Inserte velocidad (0-10): "))

        if validations_new_character(name, strength, speed):
            new_character = Character(name, strength, speed)
            self.__characters.append(new_character)
            creation_progress()
            custom_print(f"Nuevo personaje creado: {new_character.info}", color=Fore.GREEN, style=Style.BRIGHT)
        else:
            custom_print("Valores incorrectos. Intente nuevamente.", color=Fore.RED)
        input(Fore.WHITE + "Presione Enter para continuar...")

    @clear_console
    def merge_characters(self) -> None:
        name_1 = input(Fore.CYAN + "Inserte nombre de personaje 1: ")
        name_2 = input(Fore.CYAN + "Inserte nombre de personaje 2: ")

        char1 = self.find_character_by_name(name_1)
        char2 = self.find_character_by_name(name_2)

        if char1 and char2:
            new_character = char1 + char2
            self.__characters.append(new_character)
            custom_print(f"Resultado de la fusión: {new_character.info}", color=Fore.GREEN, style=Style.BRIGHT)
        else:
            custom_print("Uno o ambos personajes no existen.", color=Fore.RED)
        input(Fore.WHITE + "Presione Enter para continuar...")

    @clear_console
    def delete_character(self) -> None:
        name = input(Fore.CYAN + "Inserte nombre de personaje a eliminar: ")
        filtered_characters = [char for char in self.__characters if char.name.lower() != name.lower()]
        if len(filtered_characters) == len(self.__characters):
            custom_print(f"No se encontró ningún personaje con el nombre '{name}'.", color=Fore.RED)
        else:
            self.__characters = filtered_characters
            custom_print(f"Personaje '{name}' eliminado.", color=Fore.GREEN, style=Style.BRIGHT)
        input(Fore.WHITE + "Presione Enter para continuar...")

    @clear_console
    def run(self):
        while True:
            self.display_menu()
            choice = input(Fore.CYAN + "Selecciona una opción: ").strip()
            if choice == "0":
                os.system('cls' if os.name == 'nt' else 'clear')
                print(Fore.MAGENTA + '\nFIN DEL JUEGO\n')
                return 'ok'
            elif choice in self.options:
                self.options[choice]()
            else:
                custom_print("Opción no válida. Intente nuevamente.", color=Fore.RED)


class MenuNoColor:
    def __init__(self) -> None:
        self.__characters: List[Character] = []
        self.options = {
            "1": self.list_characters,
            "2": self.create_character,
            "3": self.merge_characters,
            "4": self.delete_character,
        }

    def clear_console(func):
        def wrapper(self, *args, **kwargs):
            os.system('cls' if os.name == 'nt' else 'clear')
            return func(self, *args, **kwargs)
        return wrapper

    def find_character_by_name(self, name: str) -> Character | None:
        """Busca un personaje por su nombre."""
        for character in self.__characters:
            if name.lower() == character.name.lower():
                return character
        return None

    @clear_console
    def display_menu(self) -> None:
        print("¡¡BIENVENIDO AL MENÚ!!")
        print("1. Listar personajes")
        print("2. Crear personaje")
        print("3. Fusionar personajes")
        print("4. Eliminar personajes")
        print("0. Salir")

    @clear_console
    def list_characters(self) -> None:
        """Lista todos los personajes."""
        print("Personajes:")
        if not self.__characters:
            print("No hay personajes creados.")
        for idx, character in enumerate(self.__characters, 1):
            print(f"{idx}. {character.info}")
        input("Presione Enter para continuar...")

    @clear_console
    def create_character(self) -> None:
        name = input("Inserte nombre: ")
        strength = self.input_int("Inserte fuerza (0-10): ", 0, 10)
        speed = self.input_int("Inserte velocidad (0-10): ", 0, 10)

        if validations_new_character(name, strength, speed):
            new_character = Character(name, strength, speed)
            self.__characters.append(new_character)
            fusion_progress()
            print(f"Nuevo personaje creado: {new_character.info}")
        else:
            print("Valores incorrectos. Intente nuevamente.")
        input("Presione Enter para continuar...")

    @clear_console
    def merge_characters(self) -> None:
        name_1 = input("Inserte nombre de personaje 1: ")
        name_2 = input("Inserte nombre de personaje 2: ")

        char1 = self.find_character_by_name(name_1)
        char2 = self.find_character_by_name(name_2)

        if char1 and char2:
            new_character = char1 + char2
            self.__characters.append(new_character)
            print(f"Resultado de la fusión: {new_character.info}")
        else:
            print("Uno o ambos personajes no existen.")
        input("Presione Enter para continuar...")

    @clear_console
    def delete_character(self) -> None:
        name = input("Inserte nombre de personaje a eliminar: ")
        filtered_characters = [char for char in self.__characters if char.name.lower() != name.lower()]
        if len(filtered_characters) == len(self.__characters):
            print(f"No se encontró ningún personaje con el nombre '{name}'.")
        else:
            self.__characters = filtered_characters
            print(f"Personaje '{name}' eliminado.")
        input("Presione Enter para continuar...")

    @clear_console
    def run(self):
        while True:
            self.display_menu()
            choice = input("Selecciona una opción: ").strip()
            if choice == "0":
                os.system('cls' if os.name == 'nt' else 'clear')
                print(Fore.MAGENTA + '\nFIN DEL JUEGO\n')
                return 'ok'
            elif choice in self.options:
                self.options[choice]()
            else:
                print("Opción no válida. Intente nuevamente.")