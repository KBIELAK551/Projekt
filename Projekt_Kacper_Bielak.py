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