# clases.py
import numpy as np
import random
from variables import TAM, BARCOS, AGUA, BARCO, IMPACTO, FALLO

class Tablero:
    def __init__(self, jugador_id, barcos=BARCOS):
        self.jugador_id = jugador_id
        self.barcos = barcos
        self.tam = TAM

        # Tablero real (barcos + impactos)
        self.tablero = np.full((TAM, TAM), AGUA, dtype=str)

        # Tablero visto por el adversario (sin barcos)
        self.tablero_visto = np.full((TAM, TAM), AGUA, dtype=str)

        # Vidas = número total de casillas con barco
        self.vidas = sum(self.barcos.values())

        # Coloca los barcos al iniciar
        self.colocar_barcos()

    # ------------------------------------------------------------------
    def colocar_barcos(self):
        """Coloca los barcos en posiciones aleatorias del tablero."""
        for nombre, eslora in self.barcos.items():
            colocado = False
            while not colocado:
                x = random.randint(0, self.tam - 1)
                y = random.randint(0, self.tam - 1)

                orient = random.choice(["N", "S", "E", "O"])

                coords = self._generar_posiciones(x, y, eslora, orient)

                if coords and self._posicion_libre(coords):
                    for (cx, cy) in coords:
                        self.tablero[cx, cy] = BARCO
                    colocado = True

    # ------------------------------------------------------------------
    def _generar_posiciones(self, x, y, eslora, orient):
        """Devuelve una lista de coordenadas si el barco cabe, si no None."""
        coords = []
        for i in range(eslora):
            if orient == "N":
                nx, ny = x - i, y
            elif orient == "S":
                nx, ny = x + i, y
            elif orient == "E":
                nx, ny = x, y + i
            else:  # O
                nx, ny = x, y - i

            if nx < 0 or nx >= self.tam or ny < 0 or ny >= self.tam:
                return None
            coords.append((nx, ny))
        return coords

    # ------------------------------------------------------------------
    def _posicion_libre(self, coords):
        """Comprueba que las coordenadas están libres."""
        return all(self.tablero[x, y] == AGUA for x, y in coords)

    # ------------------------------------------------------------------
    def disparo(self, x, y):
        """Procesa un disparo sobre este tablero."""
        casilla = self.tablero[x, y]

        if casilla == BARCO:
            self.tablero[x, y] = IMPACTO
            self.tablero_visto[x, y] = IMPACTO
            self.vidas -= 1
            return True  # impacto
        else:
            if self.tablero[x, y] == AGUA:
                self.tablero[x, y] = FALLO
            self.tablero_visto[x, y] = FALLO
            return False