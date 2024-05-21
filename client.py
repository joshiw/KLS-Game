import socket, pygame

width = 500
height = 500
win = pygame.display.set_mode((width, height))

def player():
    def _init_(self, x, y, width, hight, color):
        self.x = x
        self.y = y
        self.width = width
        self.hight = hight
        self.color = color
        self.rect = (x, y, width, hight)

def draw(self, win):
    pygame.draw.rect(win, self.color, self.rect)

def move(self):
    

def window():
    win.fill((255,255,255))

def main():
    host = '127.0.0.1'
    port = 12345

    server_connection = socket.socket()
    server_connection.bind((host, port))

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()