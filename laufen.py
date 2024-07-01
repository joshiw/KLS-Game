import pygame
import sys
import osssssssad

# Pygame initialisieren
pygame.init()

# Bildschirmabmessungen
WIDTH, HEIGHT = 2000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Laufanimation")

# Pfad zum statischen Ordner
STATIC_DIR = os.path.join(os.path.dirname(__file__), 'static', 'images')
print(f"STATIC_DIR: {STATIC_DIR}")

# Bilder laden
try:
    images_right = [pygame.image.load(os.path.join(STATIC_DIR, f'arnold_walk{i}.png')) for i in range(3)]
    images_left = [pygame.image.load(os.path.join(STATIC_DIR, f'arnold_walk{i}.png')) for i in range(3, 6)]
    images_down = [pygame.image.load(os.path.join(STATIC_DIR, f'arnold_walk{i}.png')) for i in range(6, 8)]
    images_up = [pygame.image.load(os.path.join(STATIC_DIR, f'resized_arnold_walk{i}.png')) for i in range(9, 11)]
except pygame.error as e:
    print(f"Fehler beim Laden der Bilder: {e}")
    pygame.quit()
    sys.exit()
except FileNotFoundError as e:
    print(f"Fehler: Datei nicht gefunden. {e}")
    pygame.quit()
    sys.exit()

current_image_index = 0
current_images = images_right

# Position der Figur
x_pos = 0
y_pos = HEIGHT // 2 - current_images[0].get_height() // 2

# Animationseinstellungen
clock = pygame.time.Clock()
frame_rate = 15  # Bilder pro Sekunde
frame_rate2 = 10  # Bilder pro Sekunde
# Hauptschleife
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        current_images = images_right
        current_image_index = (current_image_index + 1) % len(current_images)
        x_pos += 5  # Bewegt sich 5 Pixel nach rechts
    elif keys[pygame.K_a]:
        current_images = images_left
        current_image_index = (current_image_index + 1) % len(current_images)
        x_pos -= 5  # Bewegt sich 5 Pixel nach links
    elif keys[pygame.K_s]:
        current_images = images_down
        current_image_index = (current_image_index + 1) % len(current_images)
        y_pos += 7.5  # Bewegt sich 5 Pixel nach unten
        clock.tick(frame_rate2)
    elif keys[pygame.K_w]:
        current_images = images_up
        current_image_index = (current_image_index + 1) % len(current_images)
        y_pos -= 7.5  # Bewegt sich 5 Pixel nach unten
        clock.tick(frame_rate2)
    # Bildschirm löschen
    screen.fill((0, 0, 0))

    # Figur zeichnen
    screen.blit(current_images[current_image_index], (x_pos, y_pos))

    # Anzeige aktualisieren
    pygame.display.flip()

    # Framerate begrenzen
    clock.tick(frame_rate)

pygame.quit()
sys.exit()
