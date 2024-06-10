import pygame
import socketio
import sys
import os
import math

# Konstanten für das Spiel
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Verbindung zu SocketIO-Server
sio = socketio.Client()

class Player:
    def __init__(self, x, y, character, health=100):
        self.x = x
        self.y = y
        self.character = character
        self.health = health
        self.image = pygame.image.load(os.path.join(STATIC_DIR, f'Player {character}.png')).convert_alpha()
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.attacks = []

    def update(self, dx, dy):
        self.x += dx
        self.y += dy
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        for attack in self.attacks:
            attack.update()
            attack.draw(screen)

    def attack(self, direction):
        if self.character == 'Hannes':
            self.attacks.append(SoundWave(self.rect.centerx, self.rect.centery, direction))
        else:
            self.attacks.append(LeoGParticle(self.rect.centerx, self.rect.centery, direction))

class Attack:
    def __init__(self, x, y, direction):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.direction = direction

    def update(self):
        self.rect.x += self.direction[0]
        self.rect.y += self.direction[1]

    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)

class SoundWave(Attack):
    def __init__(self, x, y, direction):
        super().__init__(x, y, direction)
        self.radius = 10

    def update(self):
        self.radius += 5
        self.rect.inflate_ip(10, 10)

    def draw(self, screen):
        pygame.draw.circle(screen, GREEN, (self.rect.x, self.rect.y), self.radius, 2)

class LeoGParticle(Attack):
    pass

players = {}
local_player = None
STATIC_DIR = os.path.join(os.path.dirname(__file__), 'static', 'images')

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multiplayer Game")

@sio.event
def connect():
    print('Connected to server')

@sio.event
def disconnect():
    print('Disconnected from server')

@sio.event
def player_disconnected(sid):
    if sid in players:
        del players[sid]

@sio.event
def character_selected(data):
    global players
    sid = data['sid']
    character = data['character']
    if sid not in players:
        players[sid] = Player(200, 200, character)

@sio.event
def position_update(data):
    global players
    sid = data['sid']
    x = data['x']
    y = data['y']
    if sid in players:
        players[sid].x = x
        players[sid].y = y
        players[sid].rect.x = x
        players[sid].rect.y = y

@sio.event
def attack(data):
    sid = data['sid']
    x = data['x']
    y = data['y']
    character = data['character']
    if sid in players:
        direction = (math.cos(math.radians(0)), math.sin(math.radians(0)))
        players[sid].attack(direction)

sio.connect('http://localhost:5001')

def character_selection_screen():
    global local_player
    selected = False
    while not selected:
        screen.fill(WHITE)
        font = pygame.font.SysFont(None, 55)
        text = font.render("Wähle deinen Charakter", True, BLACK)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 4))
        characters = ['Hannes', 'LeoG', 'Arnold', 'Alessandro', 'Joshi', 'Kian']
        character_images = [pygame.image.load(os.path.join(STATIC_DIR, f'Player {char}.png')).convert_alpha() for char in characters]
        for i, img in enumerate(character_images):
            rect = img.get_rect(center=(WIDTH // 7 * (i + 1), HEIGHT // 2))
            screen.blit(img, rect)
            num_text = font.render(str(i + 1), True, BLACK)
            screen.blit(num_text, (rect.centerx - num_text.get_width() // 2, rect.bottom + 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, img in enumerate(character_images):
                    rect = img.get_rect(center=(WIDTH // 7 * (i + 1), HEIGHT // 2))
                    if rect.collidepoint(event.pos):
                        local_player = Player(200, 200, characters[i])
                        sio.emit('select_character', {'character': characters[i]})
                        selected = True
            elif event.type == pygame.KEYDOWN:
                if event.key in range(pygame.K_1, pygame.K_7):
                    char_index = event.key - pygame.K_1
                    local_player = Player(200, 200, characters[char_index])
                    sio.emit('select_character', {'character': characters[char_index]})
                    selected = True

def main():
    global local_player
    character_selection_screen()
    running = True
    clock = pygame.time.Clock()
    
    while running:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.constants.MOUSEBUTTONDOWN:
                if event.button == 1 and local_player:
                    direction = (math.cos(math.radians(0)), math.sin(math.radians(0)))
                    local_player.attack(direction)
                    sio.emit('attack', {'x': local_player.x, 'y': local_player.y, 'character': local_player.character})

        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_a]:
            dx = -5
        if keys[pygame.K_d]:
            dx = 5
        if keys[pygame.K_w]:
            dy = -5
        if keys[pygame.K_s]:
            dy = 5

        if local_player:
            local_player.update(dx, dy)
            sio.emit('update_position', {'x': local_player.x, 'y': local_player.y})

        for sid, player in players.items():
            player.draw(screen)

        if local_player:
            local_player.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    sio.disconnect()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
