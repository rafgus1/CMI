import pygame, random
pygame.init() # inicjalizacja gry
width = 800 # szerokość okna
height = 600 #wysokość okna

screen = pygame.display.set_mode((width, height)) #włączenie okna z grą

white = (255,255,255) #definicja kolorów
red = (255,0,0)
black = (0,0,0)

x = 200 #pozycja x gracza
y = 200 #pozycja y gracza
r = 25   #promień koła

kropki = []

for i in range(0,10):
   x2 = random.randint(0, width)
   y2 = random.randint(0, height)
   r2 = random.randint(r-10, r+10)
   dx = random.random()-0.5
   dy = random.random()-0.5
   kolor = [random.randint(100,220),random.randint(100,220),random.randint(100,220)]
   rect2 = pygame.Rect(x2-r2, y2-r2, 2*r2, 2*r2)
   kropki.append([rect2,kolor,float(x2),dx,float(y2),dy])

rect = pygame.Rect(x-r, y-r, 2*r, 2*r) #zdefiniowanie obszaru gracza

while True:

   rect.x = x-r 
   rect.y = y-r
   rect.width = 2*r
   rect.height = 2*r
      
   screen.fill(white) #wypełnienia

   for kropka in kropki:
      rect2 = kropka[0]
      kolor = kropka[1]
      x2 = kropka[2]#####
      dx = kropka[3]#####
      x2 += dx#####
      y2 = kropka[4]#####
      dy = kropka[5]#####
      y2 += dy#####
      r2 = rect2.width/2#####
      if x2>width+r2: #####
         x2=-r2 #####
      if x2<-r2: #####
         x2=width+r2 #####
      if y2>height+r2: #####
         y2=-r2#####
      if y2<-r2:       #####
         y2=height+r2#####
      rect2.x = int(x2-r2)#####
      rect2.y = int(y2-r2)#####
      pygame.draw.circle(screen, kolor, rect2.center, int(r2*1.2))
      kropka[2] = x2#####
      kropka[4] = y2#####
      
   pygame.draw.circle(screen, red, rect.center, int(r*1.2)) #narysowanie gracz

   for event in pygame.event.get(): #zakończenie gray
      if event.type == pygame.QUIT: #po kliknięciu w x na oknie z grą
         pygame.quit()

   keys = pygame.key.get_pressed() #odczyt klawisza z klawiatury
   if keys[pygame.K_LEFT]: #ruch w lewo
      x -= 1
   if keys[pygame.K_RIGHT]: #ruch w prawo
      x += 1
   if keys[pygame.K_UP]: #ruch do góry
      y -= 1
   if keys[pygame.K_DOWN]: #ruch do dołu
      y += 1
   
   if x>width+r: #przechodzenie przez prawą krawędź
      x=-r
   if x<-r:
      x=width+r #przechodzenie przez lewą krawędź
      
   if y>height+r: #przechodzenie przez dolną krawędź
      y=-r
   if y<-r:       #przechodzenie przez górną krawędź
      y=height+r
      
   for kropka in kropki:
      rect2 = kropka[0]
      if rect.colliderect(rect2):
         if r>int(rect2.width/2): #############
            kolor = [random.randint(100,220),random.randint(100,220),random.randint(100,220)]
            kropka[1] = kolor
            rect2.x = random.randint(0, width)
            rect2.y = random.randint(0, height)
            kropka[2]=float(rect2.x)
            kropka[4]=float(rect2.y)
            r2 = random.randint(r-20, r+5)
            rect2.width = 2*r2
            rect2.height = 2*r2
            r += int(100/r)
            if r>100:
               r=100
         else:################
            r-=20##############
            if r<20:##########
               r=20##############
      
   pygame.display.update() #aktualizacja ekranu




