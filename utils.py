from colorama import Fore, Style
from tqdm import tqdm
import time

def custom_print(*args, color=Fore.WHITE, style=Style.NORMAL, **kwargs):
    print(style + color + " ".join(map(str, args)), **kwargs)

def fusion_progress():
    for _ in tqdm(range(100), desc="Fusionando personajes"):
        time.sleep(0.01)

def creation_progress():
    for _ in tqdm(range(100), desc="Creando personaje"):
        time.sleep(0.01)
