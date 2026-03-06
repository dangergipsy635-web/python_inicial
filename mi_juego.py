import pygame
import random
import sys

# Inicializar pygame
pygame.init()

# Configuración de pantalla
ANCHO = 600
ALTO = 400
TAM_CELDA = 20

VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Viborita - Snake Game")

# Colores
NEGRO = (0, 0, 0)
VERDE = (0, 200, 0)
ROJO = (200, 0, 0)
BLANCO = (255, 255, 255)

# Reloj
clock = pygame.time.Clock()
FPS = 10

# Fuente
fuente = pygame.font.SysFont("Arial", 25)


def dibujar_serpiente(serpiente):
    for bloque in serpiente:
        pygame.draw.rect(VENTANA, VERDE, (bloque[0], bloque[1], TAM_CELDA, TAM_CELDA))


def mostrar_puntaje(puntaje):
    texto = fuente.render(f"Puntaje: {puntaje}", True, BLANCO) 
    VENTANA.blit(texto, (10, 10))


def generar_comida():
    x = random.randrange(0, ANCHO, TAM_CELDA)
    y = random.randrange(0, ALTO, TAM_CELDA)
    return [x, y]


def juego():
    serpiente = [[100, 100]]
    direccion = "RIGHT"
    comida = generar_comida()
    puntaje = 0

    while True:
        VENTANA.fill(NEGRO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and direccion != "DOWN":
                    direccion = "UP"
                if evento.key == pygame.K_DOWN and direccion != "UP":
                    direccion = "DOWN"
                if evento.key == pygame.K_LEFT and direccion != "RIGHT":
                    direccion = "LEFT"
                if evento.key == pygame.K_RIGHT and direccion != "LEFT":
                    direccion = "RIGHT"

        cabeza = serpiente[0].copy()

        if direccion == "UP":
            cabeza[1] -= TAM_CELDA
        if direccion == "DOWN":
            cabeza[1] += TAM_CELDA
        if direccion == "LEFT":
            cabeza[0] -= TAM_CELDA
        if direccion == "RIGHT":
            cabeza[0] += TAM_CELDA

        # Colisiones con bordes
        if (
            cabeza[0] < 0 or
            cabeza[0] >= ANCHO or
            cabeza[1] < 0 or
            cabeza[1] >= ALTO or
            cabeza in serpiente
        ):
            return puntaje

        serpiente.insert(0, cabeza)

        # Comer comida
        if cabeza == comida:
            puntaje += 1
            comida = generar_comida()
        else:
            serpiente.pop()

        pygame.draw.rect(VENTANA, ROJO, (comida[0], comida[1], TAM_CELDA, TAM_CELDA))
        dibujar_serpiente(serpiente)
        mostrar_puntaje(puntaje)

        pygame.display.update()
        clock.tick(FPS)


def game_over(puntaje):
    VENTANA.fill(NEGRO)
    texto = fuente.render(f"Game Over! Puntaje final: {puntaje}", True, BLANCO)
    VENTANA.blit(texto, (ANCHO // 2 - 150, ALTO // 2))
    pygame.display.update()
    pygame.time.wait(3000)


if __name__ == "__main__":
    puntaje_final = juego()
    game_over(puntaje_final)