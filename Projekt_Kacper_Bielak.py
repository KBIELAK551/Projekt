import pygame
import random

szerokosc_okna = 800
wysokosc_okna = 800

promien_kuli = 20
srednica_kuli = promien_kuli * 2

class Kula:
    def __init__(self, x, y, infected):
        self.x = x
        self.y = y
        self.infected = infected
        self.vx = random.randint(-10, 10)
        self.vy = random.randint(-10, 10)

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x > szerokosc_okna - promien_kuli or self.x < promien_kuli:
            self.vx = -self.vx
        if self.y > wysokosc_okna - promien_kuli or self.y < promien_kuli:
            self.vy = - self.vy

n = int(input("Podaj liczbę kul: "))
t = float(input("Podaj czas transmisji choroby: "))

pygame.init()
screen = pygame.display.set_mode((szerokosc_okna, wysokosc_okna))
pygame.display.set_caption('Symulacja rozprzestrzeniania się choroby')


margines_od_sciany = 10
kule = []
for i in range(n):
    x = random.randint(promien_kuli + margines_od_sciany, szerokosc_okna - margines_od_sciany)
    y = random.randint(promien_kuli + margines_od_sciany, wysokosc_okna - margines_od_sciany)
    kule.append(Kula(x, y, False))

index_zaraz = random.randint(0,n-1)
kule[index_zaraz].infected = True

czas = 0

nieruchome = []
ile_nieruchomych = int(input("Podaj liczbę kul nieruchomych: "))
for i in range(ile_nieruchomych):
    index_nieruchomy = random.randint(0,n-1)
    nieruchome.append(index_nieruchomy)

zdrowi = n - 1
zarazliwi = 1
niezarazliwi = 0 

def wykres():
    pygame.draw.rect(screen, (255,255,255), (20, 20, 760, 70))
    pygame.draw.line(screen, (0,0,0), (20, 70), (780, 70))
    pygame.draw.line(screen, (0,0,0), (20, 20), (20, 70))
    pygame.draw.line(screen, (0,0,0), (780, 20), (780, 70))
    pygame.draw.rect(screen, (255,0,0), (20, 20, 760*zarazliwi/n, 50))
    pygame.draw.rect(screen, (0,255,0), (20, 20, 760*zdrowi/n, 50))
    pygame.draw.rect(screen, (0,0,255), (20, 20, 760*niezarazliwi/n, 50))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))

    for i in range(len(kule)):
        if i not in nieruchome:
            kule[i].move()
        for j in range(len(kule)):
            odleglosc = ((kule[i].x - kule[j].x)**2 + (kule[i].y - kule[j].y)**2)**0.5
            if odleglosc < srednica_kuli:
                kule[i].vx = -kule[i].vx
                kule[i].vy = -kule[i].vy
                kule[j].vx = -kule[j].vx
                kule[j].vy = -kule[j].vy
                if kule[i].infected == True and kule[j].infected == False:
                    kule[j].infected = True
                    zarazliwi += 1
                    zdrowi -= 1
        if kule[i].infected == True:
            pygame.draw.circle(screen, (255,0,0), (int(kule[i].x), int(kule[i].y)), promien_kuli)
        else:
            pygame.draw.circle(screen, (0,0,255), (int(kule[i].x), int(kule[i].y)), promien_kuli)
    
    wykres()
    czas += 0.1
    pygame.display.flip()
    pygame.time.delay(10)

    for i in range(len(kule)):
        if kule[i].infected == True and czas > t:
            kule[i].infected = False
            niezarazliwi += 1
            zarazliwi -= 1

pygame.quit()