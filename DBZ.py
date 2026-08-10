import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))
space=pygame.image.load(r"C:\Users\pc\Desktop\SiderAddons\Python\pro game developer\space.png")
space_1=pygame.transform.scale(space,(800,600))
screen.blit(space_1,(0,0))
pygame.display.update()
Goku=pygame.image.load(r"C:\Users\pc\Desktop\SiderAddons\Python\pro game developer\goku.png")
Goku=pygame.transform.scale(Goku,(80,60))
Vegeta=pygame.image.load(r"C:\Users\pc\Desktop\SiderAddons\Python\pro game developer\Vegeta.png")
Vegeta=pygame.transform.scale(Vegeta,(80,60))
Vegeta=pygame.transform.rotate(Vegeta,90)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()