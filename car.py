import pygame
WHITE = (255, 255, 255)
 
class Car(pygame.sprite.Sprite):
    #Deklaracja klasy na podstawie klasy Sprite z biblioteki Pygame.
    
    def __init__(self, color, width, height, speed):
        # Konstruktor tworzący samochód
        super().__init__()
        
        # Domyślne parametry samochodu
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        #Parametry samochodu podane przez programistę.
        self.width= width
        self.height= height
        self.color = color
        self.speed = speed
        
        # Narysowanie samochodu
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
        
        # później zastąpimy prostokąt grafiką
        # self.image = pygame.image.load("car.png").convert_alpha()
 
        # dopasowanie rozmiarów.
        self.rect = self.image.get_rect()

    def moveRight(self, pixels): #ruch w prawo
        self.rect.x += pixels
 
    def moveLeft(self, pixels): #ruch w lewo
        self.rect.x -= pixels
 
    def moveForward(self, speed): #ruch do przodu
        self.rect.y += self.speed * speed / 20
 
    def moveBackward(self, speed): #ruch do tyłu
        self.rect.y -= self.speed * speed / 20
 
    def changeSpeed(self, speed): #zmiana prędkości samochodu
        self.speed = speed
 
    def repaint(self, color): #ponowne narysowanie samochodu
        self.color = color
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
