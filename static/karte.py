import pygame
import sys

# Initialisierung von Pygame
pygame.init()

# Fenstergröße
WIDTH, HEIGHT = 800, 600

# Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Spielerposition und Geschwindigkeit
player_pos = [WIDTH // 2, HEIGHT // 2]
player_speed = 5

# Erstellen des Fensters
screen = pygame.display.set_mode((WIDTH, HEIGHT))
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
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed

    # Spielfeld zurücksetzen
    screen.fill(BLACK)

    # Zentrierung des Spielers im sichtbaren Bereich
    player_draw_pos = [WIDTH // 2 - player_pos[0], HEIGHT // 2 - player_pos[1]]

    # Spieler zeichnen
    pygame.draw.circle(screen, WHITE, (WIDTH // 2, HEIGHT // 2), 20)  # Spielerposition bleibt immer in der Mitte des Bildschirms

    # Bildschirm aktualisieren
    pygame.display.flip()

    # Framerate einstellen
    pygame.time.Clock().tick(60)

# Pygame beenden
pygame.quit()
sys.exit()