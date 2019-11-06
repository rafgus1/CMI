import pygame, random
pygame.init()
width = 800
height = 600

screen = pygame.display.set_mode((width, height))

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

x = 200
y = 200
r = 25

xs = -10 #współrzędne strzału x
ys = -10 #współrzędne strzału y
dxs = 0 #przesuniecie strzału w poziomie
dys = 0 #przesuniecie strzału w pionie
rs = 10 
czyStrzelilem = False #nie ma strzału

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

rect = pygame.Rect(x-r, y-r, 2*r, 2*r) #obszar detekcji gracza
pocisk = pygame.Rect(xs-rs, ys-rs, 2*rs, 2*rs) #obszar detekcji pocisku 

while True:

   rect.x = x-r 
   rect.y = y-r
   rect.width = 2*r
   rect.height = 2*r
      
   screen.fill(white)

   for kropka in kropki:
      rect2 = kropka[0]
      kolor = kropka[1]
      x2 = kropka[2]
      dx = kropka[3]
      x2 += dx
      y2 = kropka[4]
      dy = kropka[5]
      y2 += dy
      r2 = rect2.width/2
      if x2>width+r2:
         x2=-r2
      if x2<-r2:
         x2=width+r2
      if y2>height+r2:
         y2=-r2
      if y2<-r2:       
         y2=height+r2
      rect2.x = int(x2-r2)
      rect2.y = int(y2-r2)
      pygame.draw.circle(screen, kolor, rect2.center, int(r2*1.2))
      kropka[2] = x2
      kropka[4] = y2
      
   pygame.draw.circle(screen, red, rect.center, int(r*1.2)) #narysowanie gracz

   if czyStrzelilem:
      xs+=dxs #ruch strzału w poziomie
      ys+=dys #ruch strzału w pionie
      pocisk.x = xs - rs
      pocisk.y = ys - rs
      if xs > width+rs:     ### czy strzał opuścił pole gry
         czyStrzelilem = False
      if xs < 0-rs:
         czyStrzelilem = False
      if ys > height+rs:
         czyStrzelilem = False
      if ys < 0-rs:
         czyStrzelilem = False
      pygame.draw.circle(screen, (0, 0, 255), (xs, ys), rs)
   
   for event in pygame.event.get(): #zakończenie gray
      if event.type == pygame.QUIT: #po kliknięciu w x na oknie z grą
         pygame.quit()

   keys = pygame.key.get_pressed() #odczyt klawisza z klawiatury
   if keys[pygame.K_LEFT]: #ruch w lewo
      x -= 1
      if not czyStrzelilem:
         dxs = -2
         dys = 0
   if keys[pygame.K_RIGHT]: #ruch w prawo
      x += 1
      if not czyStrzelilem:
         dxs = 2
         dys = 0
   if keys[pygame.K_UP]: #ruch do góry
      y -= 1
      if not czyStrzelilem:
         dxs = 0
         dys = -2
   if keys[pygame.K_DOWN]: #ruch do dołu
      y += 1
      if not czyStrzelilem:
         dxs = 0
         dys = 2
         
   if keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
      if not czyStrzelilem:
         dxs = 2
         dys = 2
         
   if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
      if not czyStrzelilem:
         dxs = 2
         dys = -2

   if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
      if not czyStrzelilem:
         dxs = -2
         dys = -2
         
   if keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
      if not czyStrzelilem:
         dxs = -2
         dys = 2

   if keys[pygame.K_s]:
      xs = x
      ys = y
      czyStrzelilem = True
      
   
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
         if r>int(rect2.width/2): 
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
            kropka[3] = random.random()-0.5 #dx losowanie nowego kierunku przeciwnika
            kropka[5] = random.random()-0.5 #dy losowanie nowego kierunku przeciwnika
         else:
            r-=20
            if r<20:
               r=20
      if pocisk.colliderect(rect2):
         czyStrzelilem = False
         kolor = [random.randint(100,220),random.randint(100,220),random.randint(100,220)]
         kropka[1] = kolor
         rect2.x = random.randint(0, width)
         rect2.y = random.randint(0, height)
         kropka[2]=float(rect2.x)
         kropka[4]=float(rect2.y)
         r2 = random.randint(r-20, r+5)
         rect2.width = 2*r2
         rect2.height = 2*r2         
      
   pygame.display.update() #aktualizacja ekranu
