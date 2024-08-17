import pygame
from random import randint

pygame.init()#pygame atends evrything together to make it work

width, height = 1000, 1200
fps = 80
tile = 32

window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)
direction = [[0,-1], [1, 0], [0, 1], [-1, 0]]

objects = []

class MainBattleTank:
    def __init__(self, color, px, py, direct, keyList):
        objects.append(self)
        self.type='tank'
        self.color=color
        self.rect=pygame.Rect(px, py, tile, tile)
        self.direct=direct
        self.moveSpeed=5
        self.hp = 10000
        self.shottime=0
        self.dmg=500
        self.bs=1000
        self.dlelaay=15
        self.keyLeft=keyList[0]
        self.keyRight=keyList[1]
        self.keyUp=keyList[2]
        self.keyDown=keyList[3]
        self.keyShot=keyList[4]

    def update(self):
        if keys[self.keyLeft]:
            self.rect.x -= self.moveSpeed
            self.direct = 3
        elif keys[self.keyRight]:
            self.rect.x += self.moveSpeed
            self.direct = 1
        elif keys[self.keyUp]:
            self.rect.y -= self.moveSpeed
            self.direct = 0
        elif keys[self.keyDown]:
            self.rect.y += self.moveSpeed
            self.direct = 2
        if self.rect.left < 0:
            self.rect.right = width
        elif self.rect.right > width:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.bottom = height
        elif self.rect.bottom > height:
            self.rect.top = 0

        if keys[self.keyShot] and self.shottime == 0:
            dx = direction[self.direct][0]*self.bs
            dy = direction[self.direct][1]*self.bs
            shell(self,self.rect.centerx,self.rect.centery,dx,dy,self.dmg)
            self.shottime=self.dlelaay
        if self.shottime>0:
            self.shottime-=1
    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)
        x = self.rect.centerx + direction[self.direct][0] * 30
        y = self.rect.centery + direction[self.direct][1] * 30
        pygame.draw.line(window, 'gray', self.rect.center, (x, y), 4)

    def dooy(self,valuey):
        self.hp-=valuey
        if self.hp<=0:

MainBattleTank('green', 100, 275, 0, (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_SPACE))
MainBattleTank('yellow', 650, 275, 0, (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_KP_ENTER))

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    keys = pygame.key.get_pressed()

    for obj in objects:
        obj.update()

    window.fill('black')
    for obj in objects:
        obj.draw()

    pygame.display.update()
    clock.tick(fps)

pygame.quit()


