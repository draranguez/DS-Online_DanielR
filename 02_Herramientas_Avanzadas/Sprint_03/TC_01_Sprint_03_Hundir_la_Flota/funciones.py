import random
from variables import TAM

def pedir_coordenadas():
    """Pide coordenadas correctas al usuario (0-9)."""
    while True:
        try:
            x = int(input("Introduce X (0-9): "))
            y = int(input("Introduce Y (0-9): "))
            if 0 <= x < TAM and 0 <= y < TAM:
                return x, y
        except ValueError:
            pass
        print("Coordenadas inválidas, inténtalo de nuevo.\n")

def coordenada_aleatoria():
    """Genera una coordenada aleatoria para la máquina."""
    return random.randint(0, TAM - 1), random.randint(0, TAM - 1)

