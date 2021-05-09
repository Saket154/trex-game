import pygame, sys

pygame.init()

from pygame.constants import KEYDOWN, K_DOWN, K_UP


clock = pygame.time.Clock()

#screen
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption('T-REX')

def tree_movement():
    screen.blit(tree, (tree_x, tree_y))
    screen.blit(tree1, (tree_x + 400, tree_y))
    screen.blit(tree2, (tree_x + 800, tree_y - 8))
    screen.blit(tree3, (tree_x + 1200, tree_y - 8))
    screen.blit(tree4, (tree_x + 1600, tree_y - 2)) 
    screen.blit(tree5, (tree_x + 2000, tree_y - 3))

def background_mov():
    screen.blit(background,(background_pos_x, 0))
    screen.blit(background,(background_pos_x + 600, 0))

background = pygame.image.load('background.png').convert()
tree = pygame.image.load('tree.PNG').convert()
tree = pygame.transform.scale(tree, (70, 50))
tree1 = pygame.image.load('tree1.PNG').convert()
tree1 = pygame.transform.scale(tree, (100, 60))
tree2 = pygame.image.load('tree2.PNG').convert()
tree2 = pygame.transform.scale(tree, (90, 60))
tree3 = pygame.image.load('tree3.PNG').convert()
tree3 = pygame.transform.scale(tree, (45, 60))
tree4 = pygame.image.load('tree4.PNG').convert()
tree4 = pygame.transform.scale(tree, (70, 60))
tree5 = pygame.image.load('tree5.PNG').convert()
tree5 = pygame.transform.scale(tree, (50, 50))

trex = pygame.image.load('dra1.png').convert()
trex = pygame.transform.scale(trex, (70, 60))
trex1 = pygame.image.load('dra2.png').convert()
trex1 = pygame.transform.scale(trex1, (70, 60))
trex2 = pygame.image.load('dra3.png').convert()
trex2 = pygame.transform.scale(trex2, (70, 60))
trex3 = pygame.image.load('dra4.png').convert()
trex3 = pygame.transform.scale(trex3, (70, 60))

trex_all = [trex, trex, trex, trex1, trex1, trex1, trex2, trex2, trex2, trex3, trex3, trex3,]
trex_walk = 0

trex_x = 100
trex_y = 268

white = (255,255,255)
background_velocity = 0
background_pos_x = 0

tree_x = 500
tree_y = 282

jump = True
gravity = 7


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                background_velocity = 5
                jump = True

    
    if background_pos_x < -600:
        background_pos_x = 0

    if tree_x < -2000:
        tree_x = 560

    if 276 > trex_y > 125:
        if jump == True:
            trex_y -= 7
    else: 
        jump = False

    if tree_x < trex_x + 50 < tree_x + 70 and tree_y < trex_y + 50 < tree_y + 50:
        background_velocity = 0
        trex_walk = 0
        jump = False

    if tree_x + 400 < trex_x + 50 < tree_x + 470 and tree_y < trex_y + 50 < tree_y + 50:
        background_velocity = 0
        trex_walk = 0
        jump = False

    if tree_x + 800 < trex_x + 50 < tree_x + 870 and tree_y < trex_y + 50 < tree_y + 50:
        background_velocity = 0
        trex_walk = 0
        jump = False

    if tree_x + 1200 < trex_x + 50 < tree_x + 1270 and tree_y < trex_y + 50 < tree_y + 50:
        background_velocity = 0
        trex_walk = 0
        jump = False

    if tree_x + 1600 < trex_x + 50 < tree_x + 1670 and tree_y < trex_y + 50 < tree_y + 50:
        background_velocity = 0
        trex_walk = 0
        jump = False

    if tree_x + 2000 < trex_x + 50 < tree_x + 2070 and tree_y < trex_y + 50 < tree_y + 50:
        background_velocity = 0
        trex_walk = 0
        jump = False

    

        


    if trex_y < 275:
        if jump == False:
            trex_y += gravity

    background_pos_x -= background_velocity
    tree_x -= background_velocity

    background_pos_x -= background_velocity
    trex_walk += 1

    if trex_walk > 11:
        trex_walk = 0

    screen.fill(white)
    background_mov()
    screen.blit(trex_all[trex_walk], (trex_x, trex_y))
    tree_movement()

    pygame.display.update()
    clock.tick(60)