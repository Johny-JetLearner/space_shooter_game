import pygame
screen=pygame.display.set_mode((800,600))
space=pygame.image.load(r"C:\Users\pc\Desktop\SiderAddons\Python\pro game developer\space.png")
space_1=pygame.transform.scale(space,(800,600))
screen.blit(space_1,(0,0))
pygame.display.update()
red=pygame.image.load(r"C:\Users\pc\Desktop\SiderAddons\Python\pro game developer\red.png")
red=pygame.transform.scale(red,(44,77))
yellow=pygame.image.load(r"C:\Users\pc\Desktop\SiderAddons\Python\pro game developer\yellow.png")
yellow=pygame.transform.scale(yellow,(44,77))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()