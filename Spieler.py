import pygame
import sys
import os

# Konstanten für das Spiel
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Pfad zum statischen Ordner
STATIC_DIR = os.path.join(os.path.dirname(__file__), 'static', 'images')

# Spielerklasse
class Player:
    def __init__(self, x, y, image_path):
        try:
            self.image = pygame.image.load(image_path).convert_alpha()
            self.rect = self.image.get_rect(center=(x, y))
        except pygame.error as e:
            print(f"Fehler beim Laden des Bildes {image_path}: {e}")
            self.image = pygame.Surface((50, 50))
            self.image.fill((255, 0, 0))
            self.rect = self.image.get_rect(center=(x, y))
        self.health = 100

    def update(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Boss-Klasse
class Boss:
    def __init__(self, x, y, image_path):
        try:
            self.original_image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.original_image, (100, 100))  # Bild skalieren
            self.rect = self.image.get_rect(center=(x, y))
        except pygame.error as e:
            print(f"Fehler beim Laden des Bildes {image_path}: {e}")
            self.image = pygame.Surface((10, 10))
            self.image.fill((255, 0, 0))
            self.rect = self.image.get_rect(center=(x, y))
        self.health = 300
        self.max_health = self.health

    def update(self):
        # Hier könnte die Logik für die Bewegung des Bosses implementiert werden
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.draw_health_bar(screen)

    def draw_health_bar(self, screen):
        health_bar_width = 100
        health_bar_height = 10
        fill_width = int(health_bar_width * (self.health / self.max_health))
        border_rect = pygame.Rect(self.rect.centerx - health_bar_width // 2, self.rect.top - 20, health_bar_width, health_bar_height)
        fill_rect = pygame.Rect(self.rect.centerx - health_bar_width // 2, self.rect.top - 20, fill_width, health_bar_height)
        pygame.draw.rect(screen, RED, fill_rect)
        pygame.draw.rect(screen, WHITE, border_rect, 2)

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0  # Verhindert, dass die Gesundheit negativ wird
            print("Boss besiegt!")

# Hauptspielklasse
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Among Us 2D")
        self.clock = pygame.time.Clock()
        self.player1 = Player(200, 200, os.path.join(STATIC_DIR, 'knight.png'))
        self.player2 = Player(600, 400, os.path.join(STATIC_DIR, 'knight.png'))
        self.boss = Boss(WIDTH // 2, HEIGHT // 2, os.path.join(STATIC_DIR, 'lehrer1.png'))

    def run(self):
        running = True
        while running:
            self.screen.fill(BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            player1_dx, player1_dy = 0, 0
            player2_dx, player2_dy = 0, 0

            # Spieler 1 Steuerung (WASD)
            if keys[pygame.K_a]:
                player1_dx = -5
            if keys[pygame.K_d]:
                player1_dx = 5
            if keys[pygame.K_w]:
                player1_dy = -5
            if keys[pygame.K_s]:
                player1_dy = 5

            # Spieler 2 Steuerung (Pfeiltasten)
            if keys[pygame.K_LEFT]:
                player2_dx = -5
            if keys[pygame.K_RIGHT]:
                player2_dx = 5
            if keys[pygame.K_UP]:
                player2_dy = -5
            if keys[pygame.K_DOWN]:
                player2_dy = 5

            self.player1.update(player1_dx, player1_dy)
            self.player2.update(player2_dx, player2_dy)
            self.boss.update()

            # Kollisionserkennung und Schaden
            if self.player1.rect.colliderect(self.boss.rect):
                self.boss.take_damage(1) 
            if self.player2.rect.colliderect(self.boss.rect):
                self.boss.take_damage(1) 

            self.player1.draw(self.screen)
            self.player2.draw(self.screen)
            self.boss.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
