import pygame
import random

window_width = 800
window_height = 800

sphere_radius = 20
ball_diameter = sphere_radius * 2

class Ball:
    def __init__(self, x, y, infected):
        self.x = x
        self.y = y
        self.infected = infected
        self.vx = random.randint(-10, 10)
        self.vy = random.randint(-10, 10)

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x > window_width - sphere_radius or self.x < sphere_radius:
            self.vx = -self.vx
        if self.y > window_height - sphere_radius or self.y < sphere_radius:
            self.vy = - self.vy

n = int(input("Enter the number of balls: "))
t = float(input("Enter the time of epidemic transmission: "))

pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Simulation of the spread of the epidemic')


margin_from_the_wall = 10
crutches = []
for i in range(n):
    x = random.randint(sphere_radius + margin_from_the_wall, window_width - margin_from_the_wall)
    y = random.randint(sphere_radius + margin_from_the_wall, window_height - margin_from_the_wall)
    crutches.append(Ball(x, y, False))

bullet_carrier = random.randint(0,n-1)
crutches[bullet_carrier].infected = True

time = 0

immobile = []
how_many_immobile = int(input("enter the number of stationary balls: "))
for i in range(how_many_immobile):
    index_immobile = random.randint(0,n-1)
    immobile.append(index_immobile)

healthy = n - 1
contagious = 1
not_contagious = 0 

def wykres():
    pygame.draw.rect(screen, (255,255,255), (20, 20, 760, 70))
    pygame.draw.line(screen, (0,0,0), (20, 70), (780, 70))
    pygame.draw.line(screen, (0,0,0), (20, 20), (20, 70))
    pygame.draw.line(screen, (0,0,0), (780, 20), (780, 70))
    pygame.draw.rect(screen, (255,0,0), (20, 20, 760*contagious/n, 50))
    pygame.draw.rect(screen, (0,255,0), (20, 20, 760*healthy/n, 50))
    pygame.draw.rect(screen, (0,0,255), (20, 20, 760*not_contagious/n, 50))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))

    for i in range(len(crutches)):
        if i not in immobile:
            crutches[i].move()
        for j in range(len(crutches)):
            distance = ((crutches[i].x - crutches[j].x)**2 + (crutches[i].y - crutches[j].y)**2)**0.5
            if distance < ball_diameter:
                crutches[i].vx = -crutches[i].vx
                crutches[i].vy = -crutches[i].vy
                crutches[j].vx = -crutches[j].vx
                crutches[j].vy = -crutches[j].vy
                if crutches[i].infected == True and crutches[j].infected == False:
                    crutches[j].infected = True
                    contagious += 1
                    healthy -= 1
        if crutches[i].infected == True:
            pygame.draw.circle(screen, (255,0,0), (int(crutches[i].x), int(crutches[i].y)), sphere_radius)
        else:
            pygame.draw.circle(screen, (0,0,255), (int(crutches[i].x), int(crutches[i].y)), sphere_radius)
    
    wykres()
    time += 0.1
    pygame.display.flip()
    pygame.time.delay(10)

    for i in range(len(crutches)):
        if crutches[i].infected == True and time > t:
            crutches[i].infected = False
            not_contagious += 1
            contagious -= 1

pygame.quit()