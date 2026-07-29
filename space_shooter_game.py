import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))
space=pygame.image.load(r"C:\Users\pc\Desktop\SiderAddons\Python\pro game developer\space.png")
space_1=pygame.transform.scale(space,(800,600))
screen.blit(space_1,(0,0))
pygame.display.update()
red=pygame.image.load(r"C:\Users\pc\Desktop\SiderAddons\Python\pro game developer\red.png")
red=pygame.transform.scale(red,(80,60))
yellow=pygame.image.load(r"C:\Users\pc\Desktop\SiderAddons\Python\pro game developer\yellow.png")
yellow=pygame.transform.scale(yellow,(80,60))
yellow=pygame.transform.rotate(yellow,90)
red=pygame.transform.rotate(red,270)
rectangle_yellow=pygame.Rect(0,300,80,60)
rectangle_red=pygame.Rect(700,300,80,60)
rectangle=pygame.Rect(375,0,25,2000)
def display_images():
  screen.blit(yellow,(rectangle_yellow.x,rectangle_yellow.y))
  screen.blit(red,(rectangle_red.x,rectangle_red.y))
  pygame.draw.rect(screen,"white",rectangle)
  pygame.display.update()
def yellowspaceshipmove(keys_pressed):
    if keys_pressed[pygame.K_a]:
        rectangle_yellow.x=rectangle_yellow.x-3
    if keys_pressed[pygame.K_d]:
            if rectangle_yellow.x<=320:
                rectangle_yellow.x=rectangle_yellow.x+3
def redspaceshipmove(keys_pressed):
    if keys_pressed[pygame.K_LEFT]:
        if rectangle_red.x>375:
            rectangle_red.x=rectangle_red.x-3
    if keys_pressed[pygame.K_RIGHT]:
            if rectangle_red.x<=750:
                rectangle_red.x=rectangle_red.x+3
while True:
    keys_pressed=pygame.key.get_pressed()
    yellowspaceshipmove(keys_pressed)
    redspaceshipmove(keys_pressed)
    display_images()
    screen.blit(space_1,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()