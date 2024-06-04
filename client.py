import pygame

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("client")

clientNumber = 0

class player():
    def _init_(self, x, y, width, hight, color):
        self.x = x
        self.y = y
        self.width = width
        self.hight = hight
        self.color = color
        self.rect = (x, y, width, hight)
        self.vel = 3

def draw(self, win):
    pygame.draw.rect(win, self.color, self.rect)

def move(self):
    keys = pygame.keys.get_pressed()
    if keys[pygame.K_LEFT]:
        self.x -= self.vel
    if keys[pygame.K_RIGHT]:
        self.x += self.vel
    if keys[pygame.K_UP]:
        self.y -= self.vel
    if keys[pygame.K_DOWN]:
        self.y += self.vel

def window():
    win.fill((255,255,255))

def readrawWindow(win, player):
    win.fill((255,255,255))
    player.draw(win)
    pygame.display.update()

def main():
    run = True
    p = player(50,50,100,100(0,255,0))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        readrawWindow(win, p)

main()