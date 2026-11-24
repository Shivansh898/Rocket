import pygame
pygame.init()
WIDTH = 600
HEIGHT = 600 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("blue")
rocket = pygame.image.load("Rocket/images/rocket.png")
bg = pygame.image.load("Rocket/images/bg.png")
bg1 = pygame.transform.scale(bg,(600,600))
planet = pygame.image.load("Rocket/images/planet.png")
font1 = pygame.font.SysFont("gigi",120)
text1 = font1.render("Game Over!",True,"green")
font2 = pygame.font.SysFont("gigi",120)
text2 = font2.render("YOU WON!!!!!",True,"green")
x = 400
y = 400
bool = False
boool = False
running = True
while running:
    y+= 0.01
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y -= 5
            elif event.key == pygame.K_DOWN:
                y+= 5
            elif event.key == pygame.K_LEFT:
                x-= 5
            elif event.key == pygame.K_RIGHT:
                x+=5
    pygame.display.update()
    screen.blit(bg1,(0,0))
    screen.blit(rocket,(x,y))
    screen.blit(planet,(300,20))
    pygame.display.update()
    if y >= 600:
        bool = True
    elif y <= 80:
        boool = True
    if bool:
        screen.blit(text1,(65,200))
    if boool:
        screen.blit(text2,(65,200))
        running = False






    