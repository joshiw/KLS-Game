import pygame
import sys
import os
import time
import math
import random
import logging

# Initialisiere Logging
logging.basicConfig(level=logging.DEBUG)

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

# Laden der Bilder für die Karte
fenster = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
floor = pygame.image.load('static/images/Texture/test5/tiles/2.png')
floor = pygame.transform.scale(floor, (64, 64))
floor2 = pygame.image.load('static/images/Texture/test5/tiles/3.png')
floor2 = pygame.transform.scale(floor2, (64, 64))

wall = pygame.image.load('static/images/Texture/test5/tiles/17.png')
wall = pygame.transform.scale(wall, (64, 64))
wall2 = pygame.image.load('static/images/Texture/test5/tiles/15.png')
wall2 = pygame.transform.scale(wall2, (64, 64))
wall3 = pygame.image.load('static/images/Texture/test5/tiles/14.png')
wall3 = pygame.transform.scale(wall3, (64, 64))
wall4 = pygame.image.load('static/images/Texture/test5/tiles/16.png')
wall4 = pygame.transform.scale(wall4, (64, 64))
wall5 = pygame.image.load('static/images/Texture/test5/tiles/17b.png')
wall5 = pygame.transform.scale(wall5, (64, 64))

corner1 = pygame.image.load('static/images/Texture/test5/tiles/11.png')
corner1 = pygame.transform.scale(corner1, (64, 64))
corner2 = pygame.image.load('static/images/Texture/test5/tiles/10.png')
corner2 = pygame.transform.scale(corner2, (64, 64))
corner3 = pygame.image.load('static/images/Texture/test5/tiles/12.png')
corner3 = pygame.transform.scale(corner3, (64, 64))
corner4 = pygame.image.load('static/images/Texture/test5/tiles/13.png')
corner4 = pygame.transform.scale(corner4, (64, 64))
corner5 = pygame.image.load('static/images/Texture/test5/tiles/21.png')
corner5 = pygame.transform.scale(corner5, (64, 64))
corner6 = pygame.image.load('static/images/Texture/test5/tiles/19.png')
corner6 = pygame.transform.scale(corner6, (64, 64))
corner7 = pygame.image.load('static/images/Texture/test5/tiles/22.png')
corner7 = pygame.transform.scale(corner7, (64, 64))

bookshelf = pygame.image.load('static/images/Texture/test5/tiles/bookshelf.png')
bookshelf = pygame.transform.scale(bookshelf, (65, 65))
table2 = pygame.image.load('static/images/Texture/test5/tiles/table2.png')
table2 = pygame.transform.scale(table2, (65, 65))
ChairS = pygame.image.load('static/images/Texture/test5/tiles/ChairS.png')
ChairS = pygame.transform.scale(ChairS, (50, 50))
door = pygame.image.load('static/images/Texture/test5/tiles/door.png')
door = pygame.transform.scale(door, (69, 69))
door2 = pygame.image.load('static/images/Texture/test5/tiles/door2.png')
door2 = pygame.transform.scale(door2, (69, 69))
rug = pygame.image.load('static/images/Texture/test5/tiles/rug.png')
rug = pygame.transform.scale(rug, (64, 64))
board = pygame.image.load('static/images/Texture/test5/tiles/board.png')
board = pygame.transform.scale(board, (64, 64))
board2 = pygame.image.load('static/images/Texture/test5/tiles/board2.png')
board2 = pygame.transform.scale(board2, (64, 64))
board3 = pygame.image.load('static/images/Texture/test5/tiles/board3.png')
board3 = pygame.transform.scale(board3, (64, 64))

# Karte für die Mauersteine aus Spiel 1
# Karte für die Mauersteine
Karte = [
    [1, 25, 25, 19, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8],
    [1, 25, 25, 20, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 3],
    [1, 11, 12, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 10, 24, 0, 0, 0, 10, 24, 0, 0, 0, 10, 24, 0, 0, 0, 10, 24, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 10, 24, 0, 0, 0, 10, 24, 0, 0, 0, 10, 24, 0, 0, 0, 10, 24, 0, 0, 0, 0, 0, 0, 3],
    [1, 22, 0, 14, 14, 0, 10, 24, 0, 0, 0, 10, 24, 0, 0, 0, 10, 24, 0, 0, 0, 10, 24, 0, 0, 0, 0, 0, 0, 3],
    [1, 23, 0, 14, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 23, 0, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 0, 0, 0, 0, 0, 3],
    [1, 23, 0, 14, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 21, 0, 14, 14, 0, 10, 24, 0, 0, 0, 10, 24, 0, 0, 0, 10, 24, 0, 0, 0, 10, 24, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 10, 24, 0, 0, 0, 10, 24, 0, 0, 0, 10, 24, 0, 0, 0, 10, 24, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 10, 24, 0, 0, 0, 10, 24, 0, 0, 0, 10, 24, 0, 0, 0, 10, 24, 0, 0, 0, 0, 0, 0, 3],
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

def feldpruefung(x, y):
    if Karte[y + 1][x + 1] != 1 and Karte[y + 1][x + 1] != 2 and Karte[y + 1][x + 1] != 3 and Karte[y + 1][x + 1] != 4 and Karte[y + 1][x + 1] != 5 and Karte[y + 1][x + 1] != 6 and Karte[y + 1][x + 1] != 7 and Karte[y + 1][x + 1] != 8 and Karte[y + 1][x + 1] != 10 and Karte[y + 1][x + 1] != 18 and Karte[y + 1][x + 1] != 20 and Karte[y + 1][x + 1] != 21 and Karte[y + 1][x + 1] != 22 and Karte[y + 1][x + 1] != 23 and Karte[y + 1][x + 1] != 9:
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
            logging.error(f"Fehler beim Laden des Bildes {image_path}: {e}")
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
            logging.info("Spieler besiegt!")

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
        logging.debug(f"Lade Bilder für {self.__class__.__name__}")
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

# Charakter Juliana
class Juliana(Character):
    def __init__(self, x, y):
        super().__init__(x, y, os.path.join(STATIC_DIR, 'Player Juliana.png'), health=4, max_ammo=6)

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
            logging.error(f"Fehler beim Laden des Bildes {image_path}: {e}")
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
            logging.info("Boss besiegt!")

    def fire_particle(self, player):
        direction_x = player.rect.centerx - self.rect.centerx
        direction_y = player.rect.centery - self.rect.centery
        distance = math.sqrt(direction_x**2 + direction_y**2)
        direction = (direction_x / distance * 5, direction_y / distance * 5)  # Geschwindigkeit von 5 Pixel pro Frame
        damage = max(1, int(10 / (distance / 50)))  # Mehr Schaden bei kürzerer Distanz
        particle = Particle(self.rect.centerx, self.rect.centery, direction, damage)
        self.particles.append(particle)

# Hauptspielklasse
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("KLS Spiel")
        self.clock = pygame.time.Clock()
        self.character_selected = False
        self.player = None
        self.boss = Boss(WIDTH // 2, HEIGHT // 2, os.path.join(STATIC_DIR, 'Boss Hr. Van Helden.png'))
        self.show_settings = False
        self.settings_image = pygame.image.load(os.path.join(STATIC_DIR, 'SETTINGS.png')).convert_alpha()
        self.settings_image = pygame.transform.scale(self.settings_image, (50, 50))
        self.settings_button = self.settings_image.get_rect(topleft=(10, 10))  # Einstellungs-Knopf
        self.fullscreen = False
        self.show_shadows = True
        self.resolutions = [(1280, 720), (1920, 1080), (2560, 1440), (3840, 2160)]
        self.current_resolution_index = self.resolutions.index((WIDTH, HEIGHT))

    def show_loading_screen(self):
        self.screen.fill(WHITE)
        font = pygame.font.SysFont(None, 55)
        text = font.render("Lädt...", True, BLACK)
        self.screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
        pygame.display.flip()

    def load_game_assets(self):
        self.show_loading_screen()
        pygame.time.delay(200)

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
            juliana = pygame.image.load(os.path.join(STATIC_DIR, 'Player Juliana.png')).convert_alpha()
            # Positioniere die Charaktere auf dem Bildschirm
            characters = [
                (hannes_image, "1", Hannes, WIDTH // 8),
                (leog_image, "2", LeoG, 2 * WIDTH // 8),
                (arnold_image, "3", Arnold, 3 * WIDTH // 8),
                (alessandro_image, "4", Alessandro, 4 * WIDTH // 8),
                (joshi_image, "5", Joshi, 5 * WIDTH // 8),
                (kian_image, "6", Kian, 6 * WIDTH // 8),
                (juliana, "7", Juliana, 7 * WIDTH // 8)
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
                            logging.debug(f"Charakter {char_class.__name__} gewählt")
                            self.player = char_class(200, 200)
                            self.character_selected = True
                elif event.type == pygame.KEYDOWN:
                    for _, number, char_class, _ in characters:
                        if event.key == getattr(pygame, f'K_{number}'):
                            logging.debug(f"Charakter {char_class.__name__} mit Tastendruck gewählt")
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
        logging.debug("Karte wird gezeichnet")
        
        tile_mapping = {
            0: floor,
            1: wall,
            2: wall3,
            3: wall2,
            4: wall4,
            5: corner2,
            6: corner3,
            7: corner4,
            8: corner1,
            9: bookshelf,
            10: [floor, table2],
            11: [floor, door],
            12: [floor, door2],
            13: [floor, corner5],
            14: rug,
            15: corner6,
            16: [floor, wall5],
            17: [wall4, wall],
            18: corner7,
            19: [wall2, corner2],
            20: [wall, wall2],
            21: [floor, board],
            22: [floor, board2],
            23: [floor, board3],
            24: [floor, ChairS],
            25: floor2,
            26: [floor, door],
        }
        
        for y in range(17):
            for x in range(30):
                tile = Karte[y][x]
                elements = tile_mapping.get(tile)
                if elements:
                    if isinstance(elements, list):
                        for element in elements:
                            element_zeichnen(self.screen, x, y, element)
                    else:
                        element_zeichnen(self.screen, x, y, elements)



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
