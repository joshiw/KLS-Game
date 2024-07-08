import pygame
import sys
import os
import time
import math
import random

# Konstanten für das Spiel
WIDTH, HEIGHT = 1920, 1080
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (175, 175, 175)

# Pfad zum statischen Ordner
STATIC_DIR = os.path.join(os.path.dirname(__file__), 'static', 'images')

# Initialisierung von Pygame
pygame.init()

# unser Multiplikator
MULTIPLIKATOR = 64

# Karte für die Mauersteine aus Spiel 1
Karte = [
    [5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 14, 14, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 12, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 7],
]

# Korrekturfaktor berechnen
def kor(zahl):
    return zahl * MULTIPLIKATOR

# Spielelement zeichnen
def element_zeichnen(screen, spalte, reihe, art):
    screen.blit(art, [kor(spalte) + 1, kor(reihe) + 1, kor(1) - 1, kor(1) - 1])

# Spielfeldprüfung
def feldpruefung(x, y):
    if Karte[y + 1][x + 1] not in {1, 2, 3, 4, 5, 6, 7, 8}:
        return True
    else:
        return False

# Schadensanzeige-Klasse
class DamageText:
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text
        self.start_time = time.time()
        self.duration = 1  # Dauer in Sekunden
        self.speed = 0.7  # Geschwindigkeit, mit der sich der Text nach oben bewegt

    def update(self):
        if time.time() - self.start_time < self.duration:
            self.y -= self.speed

    def draw(self, screen):
        if time.time() - self.start_time < self.duration:
            font = pygame.font.SysFont(None, 24)
            img = font.render(self.text, True, RED)
            screen.blit(img, (self.x - img.get_width() // 2, self.y))

    def is_expired(self):
        return time.time() - self.start_time >= self.duration

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

    def draw_shadow(self, screen):
        shadow_rect = self.rect.copy()
        shadow_rect.x += 5
        shadow_rect.y += 5
        pygame.draw.rect(screen, GRAY, shadow_rect)

# Partikelklasse für LeoG's Angriffe
class LeoGParticle:
    def __init__(self, x, y, direction):
        self.rect = pygame.Rect(x, y, 20, 20)  # Größere Partikel
        self.direction = direction
        self.damage = 2  # Mehr Schaden

    def update(self):
        self.rect.x += self.direction[0]
        self.rect.y += self.direction[1]

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, self.rect)

    def draw_shadow(self, screen):
        shadow_rect = self.rect.copy()
        shadow_rect.x += 5
        shadow_rect.y += 5
        pygame.draw.rect(screen, GRAY, shadow_rect)

# Basisklasse für Charaktere
class Character:
    def __init__(self, x, y, image_path, health, max_ammo):
        try:
            self.image = pygame.image.load(image_path).convert_alpha()
            self.rect = self.image.get_rect(center=(x, y))
        except pygame.error as e:
            print(f"Fehler beim Laden des Bildes {image_path}: {e}")
            self.image = pygame.Surface((50, 50))
            self.image.fill((255, 0, 0))
            self.rect = self.image.get_rect(center=(x, y))
        self.health = health
        self.max_health = health
        self.alive = True
        self.attacks = []
        self.damage_texts = []
        self.ammo = max_ammo
        self.max_ammo = max_ammo
        self.last_shot_time = time.time()
        self.last_ammo_time = time.time()

    def update(self, dx, dy):
        if self.alive:
            self.rect.x += dx
            self.rect.y += dy
            for attack in self.attacks:
                attack.update()
            for damage_text in self.damage_texts:
                damage_text.update()
            self.damage_texts = [dt for dt in self.damage_texts if not dt.is_expired()]
            self.replenish_ammo()

    def draw(self, screen):
        if self.alive:
            screen.blit(self.image, self.rect)
            self.draw_health_bar(screen)
            self.draw_ammo_bar(screen)
            for attack in self.attacks:
                attack.draw(screen)
            for damage_text in self.damage_texts:
                damage_text.draw(screen)

    def draw_shadow(self, screen):
        shadow_rect = self.rect.copy()
        shadow_rect.x += 5
        shadow_rect.y += 5
        shadow_image = self.image.copy()
        shadow_image.fill(GRAY, special_flags=pygame.BLEND_RGBA_MULT)
        screen.blit(shadow_image, shadow_rect)

    def draw_health_bar(self, screen):
        health_bar_width = 50
        health_bar_height = 5
        fill_width = int(health_bar_width * (self.health / self.max_health))
        border_rect = pygame.Rect(self.rect.centerx - health_bar_width // 2, self.rect.top - 10, health_bar_width, health_bar_height)
        fill_rect = pygame.Rect(self.rect.centerx - health_bar_width // 2, self.rect.top - 10, fill_width, health_bar_height)
        pygame.draw.rect(screen, RED, fill_rect)
        pygame.draw.rect(screen, WHITE, border_rect, 1)

    def draw_ammo_bar(self, screen):
        ammo_bar_width = 50
        ammo_bar_height = 5
        fill_width = int(ammo_bar_width * (self.ammo / self.max_ammo))
        border_rect = pygame.Rect(self.rect.centerx - ammo_bar_width // 2, self.rect.top - 20, ammo_bar_width, ammo_bar_height)
        fill_rect = pygame.Rect(self.rect.centerx - ammo_bar_width // 2, self.rect.top - 20, fill_width, ammo_bar_height)
        pygame.draw.rect(screen, GREEN, fill_rect)
        pygame.draw.rect(screen, WHITE, border_rect, 1)

    def take_damage(self, amount):
        self.health -= amount
        self.damage_texts.append(DamageText(self.rect.centerx, self.rect.top - 20, str(amount)))
        if self.health <= 0:
            self.health = 0
            self.alive = False
            print("Spieler besiegt!")

    def attack(self):
        pass  # Wird in den Unterklassen definiert

    def replenish_ammo(self):
        current_time = time.time()
        if current_time - self.last_ammo_time >= 2:
            if self.ammo < self.max_ammo:
                self.ammo += 1
            self.last_ammo_time = current_time

# Schallwellenatacke Hannes
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

    def draw_shadow(self, screen):
        if self.active:
            pygame.draw.circle(screen, GRAY, (self.x + 5, self.y + 5), self.radius, 2)

    def collide(self, rect):
        if self.active:
            distance = math.sqrt((self.x - rect.centerx) ** 2 + (self.y - rect.centery) ** 2)
            return distance < self.radius + rect.width / 2
        return False

# Charakter Hannes
class Hannes(Character):
    def __init__(self, x, y):
        super().__init__(x, y, os.path.join(STATIC_DIR, 'Player Hannes.png'), health=5, max_ammo=3)
        self.load_images()
        self.animation_index = 0
        self.animation_speed = 0.1
        self.animation_counter = 0
        self.current_direction = 'down'

    def load_images(self):
        self.walk_right_images = [pygame.image.load(os.path.join(STATIC_DIR, f'hannes_walk{i}.png')).convert_alpha() for i in range(3)]
        self.walk_left_images = [pygame.image.load(os.path.join(STATIC_DIR, f'hannes_walk{i}.png')).convert_alpha() for i in range(3, 6)]
        self.walk_down_images = [pygame.image.load(os.path.join(STATIC_DIR, f'hannes_walk{i}.png')).convert_alpha() for i in range(6, 9)]
        self.walk_up_images = [pygame.transform.scale(pygame.image.load(os.path.join(STATIC_DIR, f'hannes_walk{i}.png')).convert_alpha(), (64, 64)) for i in range(9, 12)]
    
    def update(self, dx, dy):
        super().update(dx, dy)
        if dx > 0:
            self.current_direction = 'right'
        elif dx < 0:
            self.current_direction = 'left'
        elif dy > 0:
            self.current_direction = 'down'
        elif dy < 0:
            self.current_direction = 'up'

        if dx != 0 or dy != 0:
            self.animate()

    def animate(self):
        self.animation_counter += self.animation_speed
        if self.animation_counter >= len(self.walk_right_images):
            self.animation_counter = 0
        self.animation_index = int(self.animation_counter)

        if self.current_direction == 'right':
            self.image = self.walk_right_images[self.animation_index]
        elif self.current_direction == 'left':
            self.image = self.walk_left_images[self.animation_index]
        elif self.current_direction == 'down':
            self.image = self.walk_down_images[self.animation_index]
        elif self.current_direction == 'up':
            self.image = self.walk_up_images[self.animation_index]

    def attack(self):
        current_time = time.time()
        if self.alive and self.ammo > 0 and current_time - self.last_shot_time >= 0.5:  # Mindestabstand zwischen Schüssen
            self.ammo -= 1
            self.last_shot_time = current_time
            new_attack = SoundWave(self.rect.centerx, self.rect.centery)
            self.attacks.append(new_attack)

# Charakter LeoG
class LeoG(Character):
    def __init__(self, x, y):
        super().__init__(x, y, os.path.join(STATIC_DIR, 'Player LeoG.png'), health=7, max_ammo=3)

    def attack(self):
        current_time = time.time()
        if self.alive and self.ammo > 0 and current_time - self.last_shot_time >= 0.5:  # Mindestabstand zwischen Schüssen
            self.ammo -= 1
            self.last_shot_time = current_time
            direction = (math.cos(math.radians(0)), math.sin(math.radians(0)))  # Beispielrichtung, kann angepasst werden
            new_attack = LeoGParticle(self.rect.centerx, self.rect.centery, direction)
            self.attacks.append(new_attack)
            

# Charakter Arnold
class Arnold(Character):
    def __init__(self, x, y):
        super().__init__(x, y, os.path.join(STATIC_DIR, 'Player Arnold.png'), health=6, max_ammo=4)
        self.load_images()
        self.animation_index = 0
        self.animation_speed = 0.1
        self.animation_counter = 0
        self.current_direction = 'down'

    def load_images(self):
        self.walk_right_images = [pygame.image.load(os.path.join(STATIC_DIR, f'arnold_walk{i}.png')).convert_alpha() for i in range(3)]
        self.walk_left_images = [pygame.image.load(os.path.join(STATIC_DIR, f'arnold_walk{i}.png')).convert_alpha() for i in range(3, 6)]
        self.walk_down_images = [pygame.image.load(os.path.join(STATIC_DIR, f'arnold_walk{i}.png')).convert_alpha() for i in range(6, 9)]
        self.walk_up_images = [pygame.transform.scale(pygame.image.load(os.path.join(STATIC_DIR, f'arnold_walk{i}.png')).convert_alpha(), (64, 64)) for i in range(9, 12)]

    
    def update(self, dx, dy):
        super().update(dx, dy)
        if dx > 0:
            self.current_direction = 'right'
        elif dx < 0:
            self.current_direction = 'left'
        elif dy > 0:
            self.current_direction = 'down'
        elif dy < 0:
            self.current_direction = 'up'

        if dx != 0 or dy != 0:
            self.animate()

    def animate(self):
        self.animation_counter += self.animation_speed
        if self.animation_counter >= len(self.walk_right_images):
            self.animation_counter = 0
        self.animation_index = int(self.animation_counter)

        if self.current_direction == 'right':
            self.image = self.walk_right_images[self.animation_index]
        elif self.current_direction == 'left':
            self.image = self.walk_left_images[self.animation_index]
        elif self.current_direction == 'down':
            self.image = self.walk_down_images[self.animation_index]
        elif self.current_direction == 'up':
            self.image = self.walk_up_images[self.animation_index]

    def attack(self):
        current_time = time.time()
        if self.alive and self.ammo > 0 and current_time - self.last_shot_time >= 0.5:  # Mindestabstand zwischen Schüssen
            self.ammo -= 1
            self.last_shot_time = current_time
            direction = (math.cos(math.radians(45)), math.sin(math.radians(45)))  # Beispielrichtung, kann angepasst werden
            new_attack = LeoGParticle(self.rect.centerx, self.rect.centery, direction)
            self.attacks.append(new_attack)

# Charakter Alessandro
class Alessandro(Character):
    def __init__(self, x, y):
        super().__init__(x, y, os.path.join(STATIC_DIR, 'Player Alessandro.png'), health=8, max_ammo=2)

    def attack(self):
        current_time = time.time()
        if self.alive and self.ammo > 0 and current_time - self.last_shot_time >= 0.5:  # Mindestabstand zwischen Schüssen
            self.ammo -= 1
            self.last_shot_time = current_time
            direction = (math.cos(math.radians(90)), math.sin(math.radians(90)))  # Beispielrichtung, kann angepasst werden
            new_attack = LeoGParticle(self.rect.centerx, self.rect.centery, direction)
            self.attacks.append(new_attack)

# Charakter Joshi
class Joshi(Character):
    def __init__(self, x, y):
        super().__init__(x, y, os.path.join(STATIC_DIR, 'Player Joshi.png'), health=5, max_ammo=5)

    def attack(self):
        current_time = time.time()
        if self.alive and self.ammo > 0 and current_time - self.last_shot_time >= 0.5:  # Mindestabstand zwischen Schüssen
            self.ammo -= 1
            self.last_shot_time = current_time
            direction = (math.cos(math.radians(135)), math.sin(math.radians(135)))  # Beispielrichtung, kann angepasst werden
            new_attack = LeoGParticle(self.rect.centerx, self.rect.centery, direction)
            self.attacks.append(new_attack)

# Charakter Kian
class Kian(Character):
    def __init__(self, x, y):
        super().__init__(x, y, os.path.join(STATIC_DIR, 'Player Kian.png'), health=4, max_ammo=6)

    def attack(self):
        current_time = time.time()
        if self.alive and self.ammo > 0 and current_time - self.last_shot_time >= 0.5:  # Mindestabstand zwischen Schüssen
            self.ammo -= 1
            self.last_shot_time = current_time
            direction = (math.cos(math.radians(180)), math.sin(math.radians(180)))  # Beispielrichtung, kann angepasst werden
            new_attack = LeoGParticle(self.rect.centerx, self.rect.centery, direction)
            self.attacks.append(new_attack)

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
        self.damage_texts = []

    def update(self, players):
        current_time = time.time()
        if self.alive:
            if current_time - self.last_attack_time >= 2:
                for player in players:
                    if player.alive:
                        self.fire_particle(player)
                self.last_attack_time = current_time
            for particle in self.particles:
                particle.update()
            # Entferne Partikel, die außerhalb des Bildschirms sind
            self.particles = [p for p in self.particles if p.rect.x > 0 and p.rect.x < WIDTH and p.rect.y > 0 and p.rect.y < HEIGHT]
            self.move_towards_nearest_player(players)
        for damage_text in self.damage_texts:
            damage_text.update()
        self.damage_texts = [dt for dt in self.damage_texts if not dt.is_expired()]

    def draw(self, screen):
        if self.alive:
            screen.blit(self.image, self.rect)
            self.draw_health_bar(screen)
        for particle in self.particles:
            particle.draw(screen)
        for damage_text in self.damage_texts:
            damage_text.draw(screen)

    def draw_shadow(self, screen):
        shadow_rect = self.rect.copy()
        shadow_rect.x += 5
        shadow_rect.y += 5
        shadow_image = self.image.copy()
        shadow_image.fill(GRAY, special_flags=pygame.BLEND_RGBA_MULT)
        screen.blit(shadow_image, shadow_rect)

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
        self.damage_texts.append(DamageText(self.rect.centerx, self.rect.top - 30, str(amount)))
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
        pygame.display.set_caption("KLS Spiel")
        self.clock = pygame.time.Clock()
        self.character_selected = False
        self.player = None
        self.boss = Boss(WIDTH // 2, HEIGHT // 2, os.path.join(STATIC_DIR, 'lehrer1.png'))
        self.show_settings = False
        self.settings_image = pygame.image.load(os.path.join(STATIC_DIR, 'SETTINGS.png')).convert_alpha()
        self.settings_image = pygame.transform.scale(self.settings_image, (50, 50))
        self.settings_button = self.settings_image.get_rect(topleft=(10, 10))  # Einstellungs-Knopf
        self.fullscreen = False
        self.show_shadows = True
        self.resolutions = [(1280, 720), (1920, 1080), (2560, 1440), (3840, 2160)]
        self.current_resolution_index = self.resolutions.index((WIDTH, HEIGHT))

        # Laden der Bilder für die Karte
        self.floor = pygame.image.load('static/images/Texture/test5/tiles/2.png').convert()
        self.floor = pygame.transform.scale(self.floor, (64, 64))
        self.wall = pygame.image.load('static/images/Texture/test5/tiles/17.png').convert()
        self.wall = pygame.transform.scale(self.wall, (64, 64))
        self.wall2 = pygame.image.load('static/images/Texture/test5/tiles/15.png').convert()
        self.wall2 = pygame.transform.scale(self.wall2, (64, 64))
        self.wall3 = pygame.image.load('static/images/Texture/test5/tiles/14.png').convert()
        self.wall3 = pygame.transform.scale(self.wall3, (64, 64))
        self.wall4 = pygame.image.load('static/images/Texture/test5/tiles/16.png').convert()
        self.wall4 = pygame.transform.scale(self.wall4, (64, 64))
        self.corner1 = pygame.image.load('static/images/Texture/test5/tiles/11.png').convert()
        self.corner1 = pygame.transform.scale(self.corner1, (64, 64))
        self.corner2 = pygame.image.load('static/images/Texture/test5/tiles/10.png').convert()
        self.corner2 = pygame.transform.scale(self.corner2, (64, 64))
        self.corner3 = pygame.image.load('static/images/Texture/test5/tiles/12.png').convert()
        self.corner3 = pygame.transform.scale(self.corner3, (64, 64))
        self.corner4 = pygame.image.load('static/images/Texture/test5/tiles/13.png').convert()
        self.corner4 = pygame.transform.scale(self.corner4, (64, 64))
        self.corner5 = pygame.image.load('static/images/Texture/test5/tiles/21.png').convert()
        self.corner5 = pygame.transform.scale(self.corner5, (64, 64))
        self.bookshelf = pygame.image.load('static/images/Texture/test5/tiles/bookshelf.png').convert()
        self.barrel = pygame.image.load('static/images/Texture/test5/tiles/barrel.png').convert()
        self.barrel = pygame.transform.scale(self.barrel, (32, 32))
        self.door = pygame.image.load('static/images/Texture/test5/tiles/door.png').convert()
        self.door = pygame.transform.scale(self.door, (69, 69))
        self.door2 = pygame.image.load('static/images/Texture/test5/tiles/door2.png').convert()
        self.door2 = pygame.transform.scale(self.door2, (69, 69))

    def show_loading_screen(self):
        self.screen.fill(WHITE)
        font = pygame.font.SysFont(None, 55)
        text = font.render("Lädt...", True, BLACK)
        self.screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
        pygame.display.flip()

    def load_game_assets(self):
        self.show_loading_screen()
        pygame.time.delay(2000)  # Simuliere das Laden von Assets

    def character_selection_screen(self):
        while not self.character_selected:
            self.screen.fill(WHITE)
            font = pygame.font.SysFont(None, 55)
            text = font.render("Wähle deinen Charakter", True, BLACK)
            self.screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 4))
            # Lade Bilder für die Charaktere
            hannes_image = pygame.image.load(os.path.join(STATIC_DIR, 'Player Hannes.png')).convert_alpha()
            leog_image = pygame.image.load(os.path.join(STATIC_DIR, 'Player LeoG.png')).convert_alpha()
            arnold_image = pygame.image.load(os.path.join(STATIC_DIR, 'Player Arnold.png')).convert_alpha()
            alessandro_image = pygame.image.load(os.path.join(STATIC_DIR, 'Player Alessandro.png')).convert_alpha()
            joshi_image = pygame.image.load(os.path.join(STATIC_DIR, 'Player Joshi.png')).convert_alpha()
            kian_image = pygame.image.load(os.path.join(STATIC_DIR, 'Player Kian.png')).convert_alpha()

            # Positioniere die Charaktere auf dem Bildschirm
            characters = [
                (hannes_image, "1", Hannes, WIDTH // 7),
                (leog_image, "2", LeoG, 2 * WIDTH // 7),
                (arnold_image, "3", Arnold, 3 * WIDTH // 7),
                (alessandro_image, "4", Alessandro, 4 * WIDTH // 7),
                (joshi_image, "5", Joshi, 5 * WIDTH // 7),
                (kian_image, "6", Kian, 6 * WIDTH // 7),
            ]

            for img, number, _, x_pos in characters:
                rect = img.get_rect(center=(x_pos, HEIGHT // 2))
                self.screen.blit(img, rect)
                num_text = font.render(number, True, BLACK)
                self.screen.blit(num_text, (rect.centerx - num_text.get_width() // 2, rect.bottom + 10))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for img, _, char_class, x_pos in characters:
                        rect = img.get_rect(center=(x_pos, HEIGHT // 2))
                        if rect.collidepoint(event.pos):
                            self.player = char_class(200, 200)
                            self.character_selected = True
                elif event.type == pygame.KEYDOWN:
                    for _, number, char_class, _ in characters:
                        if event.key == getattr(pygame, f'K_{number}'):
                            self.player = char_class(200, 200)
                            self.character_selected = True

    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        if self.fullscreen:
            self.screen = pygame.display.set_mode(self.resolutions[self.current_resolution_index], pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(self.resolutions[self.current_resolution_index])

    def change_resolution(self):
        self.current_resolution_index = (self.current_resolution_index + 1) % len(self.resolutions)
        pygame.display.set_mode(self.resolutions[self.current_resolution_index])

    def toggle_shadows(self):
        self.show_shadows = not self.show_shadows

    def draw_settings_menu(self):
        font = pygame.font.SysFont(None, 45)
        resolution_text = font.render(f"Resolution: {self.resolutions[self.current_resolution_index][0]}x{self.resolutions[self.current_resolution_index][1]}", True, BLACK)
        fullscreen_text = font.render(f"Fullscreen: {'On' if self.fullscreen else 'Off'}", True, BLACK)
        shadows_text = font.render(f"Shadows: {'On' if self.show_shadows else 'Off'}", True, BLACK)
        self.screen.blit(resolution_text, (WIDTH // 2 - resolution_text.get_width() // 2, HEIGHT // 2 - 60))
        self.screen.blit(fullscreen_text, (WIDTH // 2 - fullscreen_text.get_width() // 2, HEIGHT // 2 + 10))
        self.screen.blit(shadows_text, (WIDTH // 2 - shadows_text.get_width() // 2, HEIGHT // 2 + 80))

    def draw_map(self):
        for x in range(30):
            for y in range(17):
                if Karte[y][x] == 0:
                    element_zeichnen(self.screen, x, y, self.floor)
                elif Karte[y][x] == 1:
                    element_zeichnen(self.screen, x, y, self.wall)
                elif Karte[y][x] == 2:
                    element_zeichnen(self.screen, x, y, self.wall3)
                elif Karte[y][x] == 3:
                    element_zeichnen(self.screen, x, y, self.wall2)
                elif Karte[y][x] == 4:
                    element_zeichnen(self.screen, x, y, self.wall4)
                elif Karte[y][x] == 5:
                    element_zeichnen(self.screen, x, y, self.corner2)
                elif Karte[y][x] == 6:
                    element_zeichnen(self.screen, x, y, self.corner3)
                elif Karte[y][x] == 7:
                    element_zeichnen(self.screen, x, y, self.corner4)
                elif Karte[y][x] == 8:
                    element_zeichnen(self.screen, x, y, self.corner1)
                elif Karte[y][x] == 9:
                    element_zeichnen(self.screen, x, y, self.bookshelf)
                elif Karte[y][x] == 10:
                    element_zeichnen(self.screen, x, y, self.floor)
                    element_zeichnen(self.screen, x, y, self.barrel)
                elif Karte[y][x] == 11:
                    element_zeichnen(self.screen, x, y, self.floor)
                    element_zeichnen(self.screen, x, y, self.door)
                elif Karte[y][x] == 12:
                    element_zeichnen(self.screen, x, y, self.floor)
                    element_zeichnen(self.screen, x, y, self.door2)
                elif Karte[y][x] == 13:
                    element_zeichnen(self.screen, x, y, self.floor)
                    element_zeichnen(self.screen, x, y, self.corner5)
                elif Karte[y][x] == 14:
                    element_zeichnen(self.screen, x, y, self.floor)

    def run(self):
        self.load_game_assets()
        self.character_selection_screen()
        running = True
        while running:
            player_dx, player_dy = 0, 0  # Initialisiere die Variablen hier
            self.screen.fill(WHITE)
            self.draw_map()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.constants.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.settings_button.collidepoint(event.pos):
                            self.show_settings = not self.show_settings
                        else:
                            self.player.attack()
                if event.type == pygame.KEYDOWN:
                    if self.show_settings:
                        if event.key == pygame.K_f:
                            self.toggle_fullscreen()
                        elif event.key == pygame.K_r:
                            self.change_resolution()
                        elif event.key == pygame.K_s:
                            self.toggle_shadows()

            keys = pygame.key.get_pressed()
            # Spieler Steuerung (WASD)
            if self.player.alive:
                x = int(self.player.rect.centerx / MULTIPLIKATOR)
                y = int(self.player.rect.centery / MULTIPLIKATOR)
                if keys[pygame.K_a] and feldpruefung(x - 1, y):
                    player_dx = -3
                if keys[pygame.K_d] and feldpruefung(x + 1, y):
                    player_dx = 3
                if keys[pygame.K_w] and feldpruefung(x, y - 1):
                    player_dy = -3
                if keys[pygame.K_s] and feldpruefung(x, y + 1):
                    player_dy = 3

            self.player.update(player_dx, player_dy)
            self.boss.update([self.player])

            # Partikelkollisionen überprüfen und Partikel entfernen
            for particle in self.boss.particles[:]:
                if self.player.alive and self.player.rect.colliderect(particle.rect):
                    self.player.take_damage(particle.damage)
                    self.boss.particles.remove(particle)

            # Schallwellen-Kollisionen überprüfen und Boss Schaden zufügen
            for attack in self.player.attacks[:]:
                if isinstance(attack, SoundWave) and attack.collide(self.boss.rect):
                    self.boss.take_damage(1)
                    attack.active = False  # Deaktiviere die Schallwelle nach dem Treffer
                elif isinstance(attack, LeoGParticle) and attack.rect.colliderect(self.boss.rect):
                    self.boss.take_damage(2)  # Mehr Schaden durch LeoG's Partikel
                    self.player.attacks.remove(attack)

            # Zeichne Schatten, wenn aktiviert
            if self.show_shadows:
                self.boss.draw_shadow(self.screen)
                self.player.draw_shadow(self.screen)
                for attack in self.player.attacks:
                    attack.draw_shadow(self.screen)
                for particle in self.boss.particles:
                    particle.draw_shadow(self.screen)

            # Zeichne Charaktere und Partikel
            self.boss.draw(self.screen)
            self.player.draw(self.screen)
            for attack in self.player.attacks:
                attack.draw(self.screen)
            for particle in self.boss.particles:
                particle.draw(self.screen)

            # Zeichne den Einstellungs-Knopf
            self.screen.blit(self.settings_image, self.settings_button)

            if self.show_settings:
                self.draw_settings_menu()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
