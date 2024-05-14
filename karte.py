import pygame
import sys

# Initialisierung von  Pygame
pygame.init()

# Fenstergröße
WIDTH, HEIGHT = 800, 600

# Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Spielerposition und Geschwindigkeit
background_pos = [WIDTH // 2, HEIGHT // 2]
player_speed = 5

# Erstellen des Fensters
screen = pygame.display.set_mode((WIDTH, HEIGHT))
spielerfigur = pygame.image.load("static/images/walküre.jpg")
pygame.display.set_caption("Raumschiff Bewegung")

# Hauptspiel-Schleife
running = True
while running:
    # Ereignisüberwachung
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Spielerbewegung
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        background_pos[0] += player_speed
    if keys[pygame.K_RIGHT]:
        background_pos[0] -= player_speed
    if keys[pygame.K_UP]:
        background_pos[1] += player_speed
    if keys[pygame.K_DOWN]:
        background_pos[1] -= player_speed

    # Spielfeld zurücksetzen
    screen.fill((0,0,0))

    screen.blit(spielerfigur,background_pos)

    # Spieler zeichnen
    pygame.draw.circle(screen, WHITE, (400,300), 20)

    # Bildschirm aktualisieren
    pygame.display.flip()

    # Bildschirm aktualisieren
    pygame.display.update()

    # Framerate einstellen
    pygame.time.Clock().tick(60)

# Pygame beenden
pygame.quit()
sys.exit()
