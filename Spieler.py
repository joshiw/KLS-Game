import pygame
import sys
import os

# Konstanten für das Spiel
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Pfad zum statischen Ordner
STATIC_DIR = os.path.join(os.path.dirname(__file__), 'static')

# Spielerklasse
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        try:
            self.image = pygame.image.load(image_path).convert_alpha()
            self.rect = self.image.get_rect(center=(x, y))
        except pygame.error as e:
            print(f"Fehler beim Laden des Bildes {image_path}: {e}")
            self.image = pygame.Surface((50, 50))
            self.image.fill((255, 0, 0))
            self.rect = self.image.get_rect(center=(x, y))

    def update(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

# Hauptspielklasse
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Among Us 2D")
        self.clock = pygame.time.Clock()
        self.players = pygame.sprite.Group()
        self.player1 = Player(200, 200, os.path.join(STATIC_DIR, 'static/images/knight.png'))
        self.player2 = Player(600, 400, os.path.join(STATIC_DIR, 'static/images/knight.png'))
        self.players.add(self.player1, self.player2)

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

            self.players.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
