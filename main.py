import os
from colorama import Fore
from menu import Menu, MenuNoColor

try:
    while True:
        print("¿Que tipo de menú desea usar?")
        print("1.Menú con color")
        print("2.Menú sin color")
        type_menu = int(input("¿Que tipo de menú desea usar?"))
        if type_menu == 1:
            menu = Menu()
            end = menu.run()
            if end == 'ok':
                break
        elif type_menu == 2:
            menu = MenuNoColor()
            end = menu.run()
            if end == 'ok':
                break
        else:
            print("opcion incorrecta")

except Exception as e:
    print(f"{e}")
except KeyboardInterrupt:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.MAGENTA + '\nFIN DEL JUEGO\n')
