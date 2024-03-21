import random  # Importa o módulo random para gerar números aleatórios
import sys  # Importa o módulo sys para lidar com funcionalidades do sistema
import pygame  # Importa a biblioteca Pygame para desenvolvimento de jogos em Python


pygame.init() # Inicializa o Pygame

PRETO = (0,0,0)  # Define a cor preta em formato RGB
BRANCO = (255,255,255) # Define a cor branca em formato RGB

largura = 800 # Define a largura da tela do jogo
altura = 600 # Define a altura da tela do jogo

screen = pygame.display.set_mode((largura, altura)) # Cria a janela do jogo com as dimensões especificadas
pygame.display.set_caption("PONG") # Define o título da janela do jogo como "PONG"

#Definição da Raquete
raquete_largura = 10 # Largura da raquete
raquete_altura = 60 # Altura da raquete
tamanho_bola = 10 # Diâmetro da bola

#Posição da Raquete do pc
pc_x = 10 # Define a posição horizontal da raquete do computador. Neste caso, a raquete começa a 10 pixels da borda esquerda da tela
pc_y = altura // 2 - raquete_altura // 2 # Define a posição vertical da raquete do computador. Esta posição é metade da altura da tela menos metade da altura da raquete para centralizar

#Posição da Raquete do player
player_1_x = largura - 20 # Define a posição horizontal da raquete do computador. Neste caso, a raquete começa a 20 pixels da borda direita da tela
player_1_y = altura // 2 - raquete_altura // 2 # Define a posição vertical da raquete do computador. Esta posição é metade da altura da tela menos metade da altura da raquete para centralizar

#Posição da bola
bola_x = largura // 2 - tamanho_bola // 2 # Define a posição horizontal da bola no meio da tela menos metade da propria largura da bola pra centralizar bem
bola_y = altura // 2 - tamanho_bola // 2 # Define a posição vertical da bola do computador. Esta posição é metade da altura da tela menos metade da altura da bola para centralizar

# Define a velocidade de movimento das raquetes do jogador e do computador
raquete_player_1_dy = 5  # Velocidade de movimento da raquete do jogador para cima/baixo
raquete_pc_dy = 5  # Velocidade de movimento da raquete do computador para cima/baixo

clock = pygame.time.Clock()  # Cria um objeto Clock para controlar a taxa de atualização da tela

rodando = True # Variável para controlar o loop principal do jogo
while rodando:  # Loop principal do jogo que roda enquanto a variável "rodando" for True
    for event in pygame.event.get():  # Loop para verificar eventos do Pygame
        if event.type == pygame.QUIT:  # Verifica se o evento é o fechamento da janela
            rodando = False  # Define "rodando" como False para sair do loop principal

    screen.fill(PRETO)  # Preenche a tela com a cor preta

    # Desenha as raquetes do computador e do jogador, e a bola na tela
    pygame.draw.rect(screen, BRANCO, (pc_x, pc_y, raquete_largura, raquete_altura))  # Raquete do computador
    pygame.draw.rect(screen, BRANCO, (player_1_x, player_1_y, raquete_largura, raquete_altura))  # Raquete do jogador
    pygame.draw.ellipse(screen, BRANCO, (bola_x, bola_y, tamanho_bola, tamanho_bola))  # Bola

    keys = pygame.key.get_pressed()  # Captura as teclas pressionadas

    # Movimentação da raquete do jogador para cima se a tecla de seta para cima estiver pressionada
    if keys[pygame.K_UP] and player_1_y > 0:  # Verifica se a tecla de seta para cima está pressionada e se a raquete não está na borda superior
        player_1_y -= raquete_player_1_dy  # Move a raquete do jogador para cima

    # Movimentação da raquete do jogador para baixo se a tecla de seta para baixo estiver pressionada
    if keys[pygame.K_DOWN] and player_1_y < altura - raquete_altura:  # Verifica se a tecla de seta para baixo está pressionada e se a raquete não está na borda inferior
        player_1_y += raquete_player_1_dy  # Move a raquete do jogador para baixo

    pygame.display.flip() # Atualiza a tela para exibir as alterações feitas nos desenhos

    clock.tick(120)  # Limita a taxa de atualização da tela a 120 frames por segundo

pygame.quit()  # Encerra o Pygame
sys.exit()  # Encerra o programa