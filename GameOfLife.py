# Game of Life following DotCSV and varying (https://www.youtube.com/watch?v=qPtKv9fSHZY&t=634s)

# Librerías
import pygame
import numpy as np
import time

pygame.init()

# Ancho y alto de la pantalla.
width, height = 1000, 1000

# Creación de la pantalla.
screen = pygame.display.set_mode((height, width))

# Color del fondo = Casi negro, casi oscuro.
bg = 25, 25, 25

# Pintamos el fondo con el color elegido.
screen.fill(bg)

nxC, nyC = 50, 50

dimCW = width / nxC
dimCH = height / nyC

# Estado de las celdas. Vivas = 1; Muertas = 0.
gameState = np.zeros((nxC, nyC))

# Autómata palo.
gameState[7, 3] = 1
gameState[5, 4] = 1
gameState[5, 4] = 1
#
# Autómata móvil.
gameState[21, 21] = 1
gameState[22, 21] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1

gameState[10, 21] = 1
gameState[11, 21] = 1
gameState[12, 23] = 1
gameState[13, 23] = 1
gameState[14, 23] = 1
gameState[15, 21] = 1
gameState[16, 21] = 1
gameState[17, 23] = 1
gameState[18, 23] = 1
gameState[19, 23] = 1
gameState[20, 21] = 1
gameState[21, 23] = 1
gameState[23, 23] = 1

gameState[1, 1] = 1
gameState[1, 2] = 1
gameState[1, 3] = 1
gameState[2, 3] = 1
gameState[20, 23] = 1
pauseExect = False

# Bucle de ejecución.
while True:

    newGameState = np.copy(gameState)

    screen.fill(bg)

    time.sleep(0.1)

    # Registramos enventos de teclado y ratón.
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect

        mouseClick = pygame.mouse.get_pressed()

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[celX, celY] = 1

    for y in range (0, nxC):
        for x in range (0, nyC):

            if not pauseExect:

                # Calculamos el número de vecinos cercanos.
                n_neigh =   gameState[(x - 1)   % nxC, (y - 1)      % nyC] + \
                            gameState[(x)       % nxC, (y - 1)      % nyC] + \
                            gameState[(x + 1)   % nxC, (y - 1)      % nyC] + \
                            gameState[(x - 1)   % nxC, (y)          % nyC] + \
                            gameState[(x + 1)   % nxC, (y)          % nyC] + \
                            gameState[(x - 1)   % nxC, (y + 1)      % nyC] + \
                            gameState[(x)       % nxC, (y + 1)      % nyC] + \
                            gameState[(x + 1)   % nxC, (y + 1)      % nyC]

                # Rule #1: Una célula muerta con exactamente 3 vecinas vivas, "revive".
                if gameState[x, y] == 0 and n_neigh == 3:
                   newGameState[x, y] = 1

                # Rule #2: Una célula viva con menos de 2 o más de 3 vecinas vivas, "muere".
                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0

                # Creamos el polígono de cada celda a dibujar.
                poly = [((x)    * dimCW, y      * dimCH),
                        ((x+1)  * dimCW, y      * dimCH),
                        ((x+1)  * dimCW, (y+1)  * dimCH),
                        ((x)    * dimCW, (y+1)  * dimCH)]
                # Y dibujamos la celda para cada par de x e y.
                if newGameState[x, y] == 0:
                    pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
                else:
                    pygame.draw.polygon(screen, (128, 128, 128), poly, 0)

    # Actualizamos el estado del juego
    gameState = np.copy(newGameState)

    #Actualizamos la pantalla.
    pygame.display.flip()
