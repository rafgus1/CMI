import pygame, random
#importowanie klasy Car
from car import Car
pygame.init()
 
GREEN = (20, 255, 140) #deklarowanie kolorów
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
        
SCREENWIDTH=400 #ustalenie rozmiarów okna gry
SCREENHEIGHT=500
 
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size) #włączenie okna z grą
pygame.display.set_caption("Car Racing") #nadanie tytułu dla okna
 
#Zadeklarowanie zbioru graczy
all_sprites_list = pygame.sprite.Group()
 
playerCar = Car(RED, 20, 30, 5) #zdefiniowanie gracza 1
playerCar.rect.x = 200
playerCar.rect.y = 300


computerCar = Car(PURPLE, 20, 30, 5) #zdefiniowanie gracza 2
computerCar.rect.x = 100
computerCar.rect.y = 300
# doda
all_sprites_list.add(playerCar)
all_sprites_list.add(computerCar)
#Ustalenie flagi zamknięcia aplikacji...
carryOn = True
clock=pygame.time.Clock()
 
while carryOn:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                carryOn=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #x wychodzi z gry
                     carryOn=False
 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerCar.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            playerCar.moveRight(5)
        if keys[pygame.K_DOWN]:
            playerCar.moveForward(5)
        if keys[pygame.K_UP]:
            playerCar.moveBackward(5)
        if keys[pygame.K_a]:
            computerCar.moveLeft(5)
        if keys[pygame.K_d]:
            computerCar.moveRight(5)
        if keys[pygame.K_s]:
            computerCar.moveForward(5)
        if keys[pygame.K_w]:
            computerCar.moveBackward(5)
            
        #Aktualizacja graczy
        all_sprites_list.update()
 
        #rysowanie tła
        screen.fill(GREEN)
        #rysowanie drogi
        pygame.draw.rect(screen, GREY, [40,0, 200,300])
        #rysowanie lini na drodze
        pygame.draw.line(screen, WHITE, [140,0],[140,300],5)
        
        #rysowanie wszystkich graczy
        all_sprites_list.draw(screen)
 
        #odświeżenie ekranu
        pygame.display.flip()
 
        #opźnienie gry 60
        clock.tick(60)
 
pygame.quit()
