import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))
space=pygame.image.load(r"C:\Users\pc\Desktop\SiderAddons\Python\pro game developer\space.png")
space_1=pygame.transform.scale(space,(800,600))
pygame.display.update()
Goku=pygame.image.load(r"C:\Users\pc\Desktop\SiderAddons\Python\pro game developer\goku.png")
Goku=pygame.transform.scale(Goku,(105,85))
Vegeta=pygame.image.load(r"C:\Users\pc\Desktop\SiderAddons\Python\pro game developer\Vegeta.png")
Vegeta=pygame.transform.scale(Vegeta,(80,80))
Vegeta=pygame.transform.rotate(Vegeta,360)
rectangle_Goku=pygame.Rect(0,300,80,60)
rectangle_Vegeta=pygame.Rect(700,300,80,60)
def display_images():
    screen.blit(Goku,(rectangle_Goku.x,rectangle_Goku.y))
    screen.blit(Vegeta,(rectangle_Vegeta.x,rectangle_Vegeta.y))
    pygame.display.update()
def Gokumove (keys_pressed):
    if keys_pressed[pygame.K_a]:
        rectangle_Goku.x=rectangle_Goku.x-3
    if keys_pressed[pygame.K_d]:
        if rectangle_Goku.x<320:
            rectangle_Goku.x=rectangle_Goku.x+3
    if keys_pressed[pygame.K_w]:
        if rectangle_Goku.y>0:
            rectangle_Goku.y-=3
    if keys_pressed[pygame.K_s]:
        if rectangle_Goku.y<540:
            rectangle_Goku.y+=3
while True:
    screen.blit(space_1,(0,0))
    keys_pressed=pygame.key.get_pressed()
    Gokumove(keys_pressed)
    display_images()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()