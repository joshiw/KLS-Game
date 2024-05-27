import pygame
import sys
import os
import time
import math

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
        self.health = 5
        self.max_health = self.health
        self.alive = True
        self.attacks = []

    def update(self, dx, dy):
        if self.alive:
            self.rect.x += dx
            self.rect.y += dy
            for attack in self.attacks:
                attack.update()

    def draw(self, screen):
        if self.alive:
            screen.blit(self.image, self.rect)
            self.draw_health_bar(screen)
            for attack in self.attacks:
                attack.draw(screen)

    def draw_health_bar(self, screen):
        health_bar_width = 50
        health_bar_height = 5
        fill_width = int(health_bar_width * (self.health / self.max_health))
        border_rect = pygame.Rect(self.rect.centerx - health_bar_width // 2, self.rect.top - 10, health_bar_width, health_bar_height)
        fill_rect = pygame.Rect(self.rect.centerx - health_bar_width // 2, self.rect.top - 10, fill_width, health_bar_height)
        pygame.draw.rect(screen, RED, fill_rect)
        pygame.draw.rect(screen, WHITE, border_rect, 1)

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.alive = False
            print("Spieler besiegt!")

    def attack(self):
        if self.alive:
            new_attack = SoundWave(self.rect.centerx, self.rect.centery)
            self.attacks.append(new_attack)

# Schallwellenklasse
class SoundWave:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.max_radius = 100
        self.speed = 5
        self.damage = 1
        self.active = True

    def update(self):
        if self.active:
            self.radius += self.speed
            if self.radius > self.max_radius:
                self.active = False

    def draw(self, screen):
        if self.active:
            pygame.draw.circle(screen, GREEN, (self.x, self.y), self.radius, 2)

    def collide(self, rect):
        if self.active:
            distance = math.sqrt((self.x - rect.centerx) ** 2 + (self.y - rect.centery) ** 2)
            return distance < self.radius + rect.width / 2
        return False

# Partikelklasse für die Angriffe des Bosses
class Particle:
    def __init__(self, x, y, direction, damage):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.direction = direction
        self.damage = damage

    def update(self):
        self.rect.x += self.direction[0]
        self.rect.y += self.direction[1]

    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)

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
        self.alive = True
        self.particles = []
        self.last_attack_time = time.time()
        self.speed = 1  # Geschwindigkeit des Bosses

    def update(self, players):
        current_time = time.time()
        if current_time - self.last_attack_time >= 2:
            for player in players:
                if player.alive:
                    self.fire_particle(player)
            self.last_attack_time = current_time

        for particle in self.particles:
            particle.update()
        
        # Entferne Partikel, die außerhalb des Bildschirms sind
        self.particles = [p for p in self.particles if p.rect.x > 0 and p.rect.x < WIDTH and p.rect.y > 0 and p.rect.y < HEIGHT]

        if self.alive:
            self.move_towards_nearest_player(players)

    def draw(self, screen):
        if self.alive:
            screen.blit(self.image, self.rect)
            self.draw_health_bar(screen)
        for particle in self.particles:
            particle.draw(screen)

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
            self.alive = False
            print("Boss besiegt!")

    def fire_particle(self, player):
        direction_x = player.rect.centerx - self.rect.centerx
        direction_y = player.rect.centery - self.rect.centery
        distance = math.sqrt(direction_x**2 + direction_y**2)
        direction = (direction_x / distance * 5, direction_y / distance * 5)  # Geschwindigkeit von 5 Pixel pro Frame
        damage = max(1, int(10 / (distance / 50)))  # Mehr Schaden bei kürzerer Distanz
        particle = Particle(self.rect.centerx, self.rect.centery, direction, damage)
        self.particles.append(particle)

    def move_towards_nearest_player(self, players):
        nearest_player = None
        min_distance = float('inf')

        for player in players:
            if player.alive:
                distance_x = player.rect.centerx - self.rect.centerx
                distance_y = player.rect.centery - self.rect.centery
                distance = math.sqrt(distance_x**2 + distance_y**2)
                if distance < min_distance:
                    min_distance = distance
                    nearest_player = player

        if nearest_player:
            direction_x = nearest_player.rect.centerx - self.rect.centerx
            direction_y = nearest_player.rect.centery - self.rect.centery
            distance = math.sqrt(direction_x**2 + direction_y**2)
            if distance > 0:
                move_x = (direction_x / distance) * self.speed
                move_y = (direction_y / distance) * self.speed
                self.rect.x += move_x
                self.rect.y += move_y

# Hauptspielklasse
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Among Us 2D")
        self.clock = pygame.time.Clock()
        self.player1 = Player(200, 200, os.path.join(STATIC_DIR, 'Player Hannes.png'))
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
            if self.player1.alive:
                if keys[pygame.K_a]:
                    player1_dx = -5
                if keys[pygame.K_d]:
                    player1_dx = 5
                if keys[pygame.K_w]:
                    player1_dy = -5
                if keys[pygame.K_s]:
                    player1_dy = 5
                if keys[pygame.K_SPACE]:
                    self.player1.attack()

            # Spieler 2 Steuerung (Pfeiltasten)
            if self.player2.alive:
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
            self.boss.update([self.player1, self.player2])

            # Kollisionserkennung und Schaden
            if self.boss.alive:
                if self.player1.alive and self.player1.rect.colliderect(self.boss.rect):
                    self.boss.take_damage(1)
                if self.player2.alive and self.player2.rect.colliderect(self.boss.rect):
                    self.boss.take_damage(1)

            # Partikelkollisionen überprüfen und Partikel entfernen
            for particle in self.boss.particles[:]:
                if self.player1.alive and self.player1.rect.colliderect(particle.rect):
                    self.player1.take_damage(particle.damage)
                    self.boss.particles.remove(particle)
                elif self.player2.alive and self.player2.rect.colliderect(particle.rect):
                    self.player2.take_damage(particle.damage)
                    self.boss.particles.remove(particle)

            # Schallwellen-Kollisionen überprüfen und Boss Schaden zufügen
            for attack in self.player1.attacks[:]:
                if attack.collide(self.boss.rect):
                    self.boss.take_damage(1)
                    attack.active = False  # Deaktiviere die Schallwelle nach dem Treffer

            self.boss.draw(self.screen)
            self.player1.draw(self.screen)
            self.player2.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
