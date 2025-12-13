
from clases import Tablero
from funciones import pedir_coordenadas, coordenada_aleatoria

print("=======================================")
print("        BIENVENIDO A HUNDIR LA FLOTA   ")
print("=======================================\n")
print("Tu objetivo es hundir los barcos enemigos antes de que hundan los tuyos.\n")

# Inicialización de tableros
jugador = Tablero(jugador_id="Jugador")
maquina = Tablero(jugador_id="Máquina")

turno_jugador = True  # Empieza el jugador

# Bucle principal del juego
while True:

    # Comprobar si alguien ganó
    if jugador.vidas == 0:
        print("\n=== HAS PERDIDO ===")
        print("La máquina ha hundido todos tus barcos.\n")
        break

    if maquina.vidas == 0:
        print("\n=== ¡HAS GANADO! ===")
        print("Hundiste todos los barcos enemigos.\n")
        break

    # ------------------------------------------------------------------
    # TURNO DEL JUGADOR
    # ------------------------------------------------------------------
    if turno_jugador:
        print("\nTU TABLERO:")
        print(jugador.tablero)

        print("\nTABLERO DEL ENEMIGO (Lo que has descubierto):")
        print(maquina.tablero_visto)

        print("\n--- TU TURNO DE DISPARO ---")
        x, y = pedir_coordenadas()

        impacto = maquina.disparo(x, y)
        if impacto:
            print(f"¡IMPACTO en ({x}, {y})! Puedes volver a disparar.\n")
            continue
        else:
            print(f"Agua en ({x}, {y}). Turno de la máquina.\n")
            turno_jugador = False

    # ------------------------------------------------------------------
    # TURNO DE LA MÁQUINA
    # ------------------------------------------------------------------
    else:
        print("Turno de la máquina...\n")

        x, y = coordenada_aleatoria()
        impacto = jugador.disparo(x, y)

        if impacto:
            print(f"La máquina ACERTÓ en ({x}, {y}) y repite turno.\n")
            continue
        else:
            print(f"La máquina falló en ({x}, {y}). Te toca a ti.\n")
            turno_jugador = True
    
























































































































































