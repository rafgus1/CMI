import pygame as pg
pg.init()
rozmiar=(400,320)
ekran = pg.display.set_mode(rozmiar)
pg.display.set_caption("Pierwsza gra")

zakoncz = True

zegar = pg.time.Clock()

while zakoncz:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            zakoncz = False
    ekran.fill((255,255,255))
    pg.draw.rect(ekran,(0,160,0),[0,0,75,320], 0)
    pg.draw.rect(ekran,(160,160,160),[77,0,60,320], 0)
    pg.draw.rect(ekran,(160,160,160),[139,0,60,320], 0)
    pg.draw.rect(ekran,(160,160,160),[201,0,60,320], 0)
    pg.draw.rect(ekran,(160,160,160),[263,0,60,320], 0)
    pg.draw.rect(ekran,(0,160,0),[325,0,75,320], 0)
    pg.display.flip()
    zegar.tick(60)

pg.quit()
