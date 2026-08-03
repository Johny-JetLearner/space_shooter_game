import pgzrun
import random
WIDTH = 500
HEIGHT = 500
spaceship = Actor("spaceship")
spaceship.x = 300
spaceship.y = 200
score = 0
star = Actor("star")
star.x = random.randint(0,500)
star.y = random.randint(0,500)
def draw():
    screen.blit("space",(0,0))
    spaceship.draw()
    star.draw()
    screen.draw.text(str(score),center=(50,50))
def update():
    global score    
    if keyboard.up:
        spaceship.y = spaceship.y - 5
    if keyboard.down:
        spaceship.y = spaceship.y + 5
    if keyboard.right:
        spaceship.x = spaceship.x + 5
    if keyboard.left:
        spaceship.x = spaceship.x - 5       
    if spaceship.colliderect(star):
        star.x = random.randint(0,500)
        star.y = random.randint(0,500)
        score = score + 10
pgzrun.go()