import pygame
import sys
import time
import random


# Initialisierung von Pygame
pygame.init()

# unser Multiplikator
MULTIPLIKATOR = 64

# Fenstergröße
WIDTH, HEIGHT = 30 * MULTIPLIKATOR, 17 * MULTIPLIKATOR

# Spielfeld erzeugen über Berechnung
fenster = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
floor = pygame.image.load('static/images/Texture/test5/tiles/2.png')
floor = pygame.transform.scale(floor, (64, 64))

wall = pygame.image.load('static/images/Texture/test5/tiles/17.png')
wall = pygame.transform.scale(wall, (64, 64))
wall2 = pygame.image.load('static/images/Texture/test5/tiles/15.png')
wall2 = pygame.transform.scale(wall2, (64, 64))
wall3 = pygame.image.load('static/images/Texture/test5/tiles/14.png')
wall3 = pygame.transform.scale(wall3, (64, 64))
wall4 = pygame.image.load('static/images/Texture/test5/tiles/16.png')
wall4 = pygame.transform.scale(wall4, (64, 64))

corner1 = pygame.image.load('static/images/Texture/test5/tiles/11.png')
corner1 = pygame.transform.scale(corner1, (64, 64))
corner2 = pygame.image.load('static/images/Texture/test5/tiles/10.png')
corner2 = pygame.transform.scale(corner2, (64, 64))
corner3 = pygame.image.load('static/images/Texture/test5/tiles/12.png')
corner3 = pygame.transform.scale(corner3, (64, 64))
corner4 = pygame.image.load('static/images/Texture/test5/tiles/13.png')
corner4 = pygame.transform.scale(corner4, (64, 64))

bookshelf = pygame.image.load('static/images/Texture/test5/tiles/bookshelf.png')
barrel = pygame.image.load('static/images/Texture/test5/tiles/barrel.png')
barrel = pygame.transform.scale(barrel, (32, 32))
door = pygame.image.load('static/images/Texture/test5/tiles/door.png')
door = pygame.transform.scale(door, (64, 64))


# Titel für Fensterkopf
pygame.display.set_caption("Breakout in Python")
spielaktiv = True

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()

# Karte für die Mauersteine
Karte1 = [
    [5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 0, 0, 0, 0, 0, 0, 3],
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

Karte2 = [
    [5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 7],
]

#Startkarte festlegen
Karte = Karte1

# Korrekturfaktor berechnen
def kor(zahl):
    return zahl * MULTIPLIKATOR

# Spielelement zeichnen
def element_zeichnen(spalte, reihe, art):
    #pygame.draw.rect(fenster, farbe, [kor(spalte) + 1, kor(reihe) + 1, kor(1) - 1, kor(1) - 1])
    fenster.blit(art, [kor(spalte) + 1, kor(reihe) + 1, kor(1) - 1, kor(1) - 1])

def feldpruefung(x,y):
    if Karte [y+1][x+1]!=1 and Karte [y+1][x+1]!=2 and Karte [y+1][x+1]!=3 and Karte [y+1][x+1]!=4 and Karte [y+1][x+1]!=5 and Karte [y+1][x+1]!=6 and Karte [y+1][x+1]!=7 and Karte [y+1][x+1]!=8:
        return True
    else:
        return False
    
# Spielerposition und Geschwindigkeit
player_pos = [WIDTH // 2, HEIGHT // 2]
player_speed = 10

# Laden des Spielerbildes
spielerfigur = pygame.image.load("static/images/TopG.png")

# Schleife Hauptprogramm
while spielaktiv:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            spielaktiv = False
            print("Game over")

    # Spielerbewegung
    keys = pygame.key.get_pressed()
    x = int(player_pos[0]/MULTIPLIKATOR)
    y = int(player_pos[1]/MULTIPLIKATOR)
    if keys[pygame.K_LEFT]:
        if feldpruefung(x-1, y):
            player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        if feldpruefung(x+1, y):
            player_pos[0] += player_speed
    if keys[pygame.K_UP]:
        if feldpruefung(x, y-1):
            player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        if feldpruefung(x, y+1):
            player_pos[1] += player_speed

    #Karte wechseln
    if Karte[y][x] == 11:
        Karte = Karte2
        print("Tür erreicht")
    if Karte[y][x] == 12:
        Karte = Karte1
        print("Tür erreicht")     

    # Mauersteine zeichnen
    for x in range(30):
        for y in range(17):
            if Karte[y][x] == 0:
                element_zeichnen(x, y, floor)
            if Karte[y][x] == 1:
                element_zeichnen(x, y, wall)
            if Karte[y][x] == 2:
                element_zeichnen(x, y, wall3)
            if Karte[y][x] == 3:
                element_zeichnen(x, y, wall2)
            if Karte[y][x] == 4:
                element_zeichnen(x, y, wall4)    
            if Karte[y][x] == 5:
                element_zeichnen(x, y, corner2)
            if Karte[y][x] == 6:
                element_zeichnen(x, y, corner3)   
            if Karte[y][x] == 7:
                element_zeichnen(x, y, corner4)  
            if Karte[y][x] == 8:
                element_zeichnen(x, y, corner1)
            if Karte[y][x] == 9:
                element_zeichnen(x, y, bookshelf)  
            if Karte[y][x] == 10:
                element_zeichnen(x, y, floor)
                element_zeichnen(x, y, barrel)  
            if Karte[y][x] == 11:
                element_zeichnen(x, y, floor)
                element_zeichnen(x, y, door)
            if Karte[y][x] == 12:
                element_zeichnen(x, y, floor)
                element_zeichnen(x, y, door)  
           



    def handle_collisions():
        global player_speed
        x = player_pos[0]
        y = player_pos[1]
        if Karte [int(y/MULTIPLIKATOR)][int(x/MULTIPLIKATOR)] == 1:
            player_pos = y-1

    
    # Spieler zeichnen
    fenster.blit(spielerfigur, player_pos)

    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(60)

# Pygame beenden
pygame.quit()
sys.exit()