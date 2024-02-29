import random
import sys 
import pygame

pygame.init()

#Configuração da tela
largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pygame")

PRETO = (0,0,0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
AMARELO = (255, 255, 0)

raio = 25
cor_circulo = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
circulo_pos = [largura // 2, altura // 2]

clock = pygame.time.Clock()

# velocidade_x = 1
# velocidade_y = 1

velocidade_x = random.randint(-1, 1)
velocidade_y = random.randint(-1, 1)

while velocidade_x == 0:
    velocidade_x = random.randint(-1,1)

while velocidade_y == 0:
    velocidade_y = random.randint(-1,1)

#Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    circulo_pos[0] += velocidade_x
    circulo_pos[1] += velocidade_y

    if circulo_pos[0] + raio >= largura:
        velocidade_x = -velocidade_x
        velocidade_y = random.randint(-1, 1)
        cor_circulo = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))       

    if circulo_pos[0] - raio <= 0:
        velocidade_x = -velocidade_x
        velocidade_y = random.randint(-1, 1)
        cor_circulo = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    if circulo_pos[1] + raio >= altura:
        velocidade_y = -velocidade_y
        velocidade_x = random.randint(-1, 1)
        cor_circulo = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    if circulo_pos[1] - raio <= 0:
        velocidade_y = -velocidade_y
        velocidade_x = random.randint(-1, 1)
        cor_circulo = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    clock.tick(300)
    tela.fill(PRETO)
    pygame.draw.circle(tela, cor_circulo, circulo_pos, raio)
    pygame.display.flip()