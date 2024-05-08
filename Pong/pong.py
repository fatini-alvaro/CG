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

# Define a velocidade de movimento das raquetes do jogador e do computador
raquete_player_1_dy = 5  # Velocidade de movimento da raquete do jogador para cima/baixo
raquete_pc_dy = 5  # Velocidade de movimento da raquete do computador para cima/baixo

#Define a velocidade da bola
velocidade_bola_x = 3 #Velocidade da bola para cima/baixo
velocidade_bola_y = 3 #Velocidade da bola para direita/esquerda

#Definir vencedor
vencedor = ""

#Definir controle
controle = False
rodando = True # Variável para controlar o loop principal do jogo

# Configuração da fonte
font_file = 'font/PressStart2P-Regular.ttf' #Passa o caminho do arquivo para uma variavel
font = pygame.font.Font(font_file, 20)

clock = pygame.time.Clock()  # Cria um objeto Clock para controlar a taxa de atualização da tela

# Metodo que inicializa o jogo, espera por comandos e mostra informações em tela
def menu_principal():
    global rodando, controle
    while True: # Loop infinito para aguardar comandos do usuario
        for event in pygame.event.get(): # Verifica se foi adcionado algum comando pelo usuario
            if event.type == pygame.QUIT: # Verifica se o comando foi de fechar a janela para fechar o jogo
                pygame.quit() 
                sys.exit()
            elif event.type == pygame.KEYDOWN: # Verifica se o comando é o pressionar de uma tecla
                if event.key == pygame.K_SPACE: # Verifica se a tecla pressionado é o espaço para retornar true e sair do looping do menu e iniciar o jogo
                    controle = True
                    return

        #Renderiza o texto do menu
        screen.fill(PRETO) # Preenche a tela com preta
        texto_menu = font.render("Pong", True, BRANCO)
        text_menu_rect = texto_menu.get_rect(center=(largura //2, altura // 2))
        screen.blit(texto_menu, text_menu_rect)

        tempo = pygame.time.get_ticks() #retorna o número de milissegundos desde que o Pygame foi inicializado.
        
        #Pressiona Space para jogar
        #Isso aqui gera um looping  infinito  por conta da logica impregada        
        # tempo % 2000 calcula o resto da divisão de tempo por 2000. Isso basicamente cria um ciclo de 2000 milissegundos (ou 2 segundos).
        # < 1000 verifica se o resto da divisão é menor que 1000. Isso significa que estamos no primeiro segundo do ciclo de 2000 milissegundos.
        #portanto, essa lógica está verificando se estamos no primeiro segundo de cada ciclo de 2 segundos. Isso pode ser útil em jogos para sincronizar eventos
        # que devem ocorrer a cada segundo, por exemplo.
        if tempo % 2000 < 1000: #calcula o resto da divisão de tempo por 2000. Isso basicamente cria um ciclo de 2000 milissegundos (ou 2 segundos).
            texto_iniciar = font.render("Pressione Espaço", True, BRANCO)
            texto_iniciar_rect = texto_iniciar.get_rect(center=(largura // 2, 450))
            screen.blit(texto_iniciar, texto_iniciar_rect)
            
        clock.tick(1)
        pygame.display.flip()

def posicao_inicial():
    global pc_x, pc_y, player_1_x, player_1_y, bola_x, bola_y, velocidade_bola_x, velocidade_bola_y, raquete_player_1_dy, raquete_pc_dy, score_player_1, score_pc;
    #Posição da Raquete do pc
    pc_x = 10 # Define a posição horizontal da raquete do computador. Neste caso, a raquete começa a 10 pixels da borda esquerda da tela
    pc_y = altura // 2 - raquete_altura // 2 # Define a posição vertical da raquete do computador. Esta posição é metade da altura da tela menos metade da altura da raquete para centralizar

    #Posição da Raquete do player
    player_1_x = largura - 20 # Define a posição horizontal da raquete do computador. Neste caso, a raquete começa a 20 pixels da borda direita da tela
    player_1_y = altura // 2 - raquete_altura // 2 # Define a posição vertical da raquete do computador. Esta posição é metade da altura da tela menos metade da altura da raquete para centralizar

    #Posição da bola
    bola_x = largura // 2 - tamanho_bola // 2 # Define a posição horizontal da bola no meio da tela menos metade da propria largura da bola pra centralizar bem
    bola_y = altura // 2 - tamanho_bola // 2 # Define a posição vertical da bola do computador. Esta posição é metade da altura da tela menos metade da altura da bola para centralizar

    # Define o Score 
    score_player_1 = 0 # Pontuacao do player 1 que sera mostrada em tela
    score_pc = 0 # Pontuacao do pc que sera mostrada em tela

def fim_jogo():
    global rodando, vencedor
    while True: # Loop infinito para aguardar comandos do usuario
        for event in pygame.event.get(): # Verifica se foi adcionado algum comando pelo usuario
            if event.type == pygame.QUIT: # Verifica se o comando foi de fechar a janela para fechar o jogo
                pygame.quit() 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    controle = True
                    posicao_inicial()
                    return
        #Renderiza o texto do menu
        screen.fill(PRETO)
        texto_fim = font.render(f"Vencedor: {vencedor}", True, BRANCO)
        text_film_rect = texto_fim.get_rect(center=(largura // 2, altura // 2))
        screen.blit(texto_fim, text_film_rect)

        pygame.display.flip()


menu_principal() #Chama o metodo menu_principal que vai verificar se o usuario startou o jogo (alem de mostrar informações em tela)
posicao_inicial()

while rodando:  # Loop principal do jogo que roda enquanto a variável "rodando" for True

    if not controle:
        fim_jogo()
    else:

        for event in pygame.event.get():  # Loop para verificar eventos do Pygame
            if event.type == pygame.QUIT:  # Verifica se o evento é o fechamento da janela
                rodando = False  # Define "rodando" como False para sair do loop principal

        screen.fill(PRETO)  # Preenche a tela com a cor preta

        bola_x += velocidade_bola_x #aplica mais velocidade para cima/baixo
        bola_y += velocidade_bola_y #aplica mais velocidade para direita/esquerda

        # Retangulos de Colisão
        bola_rect = pygame.Rect(bola_x, bola_y, tamanho_bola, tamanho_bola) #Gera o retangulo que fica envolta da bola
        raquete_pc_rect = pygame.Rect(pc_x, pc_y, raquete_largura, raquete_altura) #Gera o retangulo que fica envolta da raquete do pc
        raquete_player_1_rect = pygame.Rect(
            player_1_x, player_1_y, raquete_largura, raquete_altura
        ) #Gera o retangulo que fica envolta da raquete do player 1

        # Colisão da bola com a raquete do pc ou do player
        if bola_rect.colliderect(raquete_pc_rect) or bola_rect.colliderect(raquete_player_1_rect): #validacao quando a bolinha bate na raquete do pc ou do player 1
            velocidade_bola_x = -velocidade_bola_x #inverte o valor da velocidade em x para ela tomar o rumo oposto

        # Trata a colisão da bola com a borda de cima e de baixo da tela
        if bola_y <= 0 or bola_y >= altura - tamanho_bola: #se a bola bateu encima ou embaixo da tela
            velocidade_bola_y = -velocidade_bola_y #inverte o valor da velocidade em y para ela tomar o rumo oposto

        # Validacao para caso a bolinha saia da lateral da tela (no caso ponto de um jogador) a bola volta para o meio da tela para outra rodada e aumenta a pontuação do player
        if bola_x <= 0:
            bola_x = largura // 2 - tamanho_bola // 2 # Centraliza lateralmente
            bola_y =  altura // 2 - tamanho_bola // 2 # Centraliza verticalmente
            velocidade_bola_x = -velocidade_bola_x  #Inverte o lado da direção da bola para quando alguem fizer ponto a bola começar para o lado do perdedor
            score_player_1 += 1
            print(f"Score Player_1: {score_player_1}")
            if score_player_1 == 3:
                print("Player 1 ganhou!")
                vencedor = "Player 1"
                fim_jogo()

        # Validacao para caso a bolinha saia da lateral da tela (no caso ponto de um jogador) a bola volta para o meio da tela para outra rodada e aumenta a pontuação do pc
        if bola_x >= largura - tamanho_bola:
            bola_x = largura // 2 - tamanho_bola // 2 # Centraliza lateralmente
            bola_y =  altura // 2 - tamanho_bola // 2 # Centraliza verticalmente
            velocidade_bola_x = -velocidade_bola_x  #Inverte o lado da direção da bola para quando alguem fizer ponto a bola começar para o lado do perdedor
            score_pc += 1
            print(f"Score PC: {score_pc}")
            if score_pc == 3:
                print("PC ganhou!")
                vencedor = "PC"
                fim_jogo()

        # Movendo a raquete do pc para seguir a bola
        if pc_y + raquete_altura // 2 < bola_y:
            pc_y += raquete_pc_dy
        elif pc_y + raquete_altura // 2 > bola_y:
            pc_y -= raquete_pc_dy

        # Movendo a raquete do player para seguir a bola
        # if player_1_y + raquete_altura // 2 < bola_y:
        #     player_1_y += raquete_player_1_dy
        # elif player_1_y + raquete_altura // 2 > bola_y:
        #     player_1_y -= raquete_player_1_dy

        # Evitar que a raquete do pc saia da área da tela
        if pc_y < 0:
            pc_y = 0
        elif pc_y > altura - raquete_altura:
            pc_y = altura - raquete_altura

        # Evitar que a raquete do player saia da área da tela
        if pc_y < 0:
            pc_y = 0
        elif pc_y > altura - raquete_altura:
            pc_y = altura - raquete_altura

        # Mostrando Score no jogo
        fonte_score = pygame.font.Font(font_file, 24)
        score_texto = font.render(
            f"Score PC: {score_pc}       Score Player_1: {score_player_1}", True, BRANCO
        )
        score_rect = score_texto.get_rect(center=(largura //2, 30))
        screen.blit(score_texto, score_rect)

        # Desenha as raquetes do computador e do jogador, e a bola na tela
        pygame.draw.rect(screen, BRANCO, (pc_x, pc_y, raquete_largura, raquete_altura))  # Raquete do computador
        pygame.draw.rect(screen, BRANCO, (player_1_x, player_1_y, raquete_largura, raquete_altura))  # Raquete do jogador
        pygame.draw.ellipse(screen, BRANCO, (bola_x, bola_y, tamanho_bola, tamanho_bola))  # Bola
        pygame.draw.aaline(screen, BRANCO, (largura //2, 0), (largura //2, altura)) #Cria uma linha vertical no meio da tela

        # Controle Teclado do Player 1
        keys = pygame.key.get_pressed()  # Captura as teclas pressionadas

        # Movimentação da raquete do jogador para cima se a tecla de seta para cima estiver pressionada
        if keys[pygame.K_UP] and player_1_y > 0:  # Verifica se a tecla de seta para cima está pressionada e se a raquete não está na borda superior
            player_1_y -= raquete_player_1_dy  # Move a raquete do jogador para cima

        # Movimentação da raquete do jogador para baixo se a tecla de seta para baixo estiver pressionada
        if keys[pygame.K_DOWN] and player_1_y < altura - raquete_altura:  # Verifica se a tecla de seta para baixo está pressionada e se a raquete não está na borda inferior
            player_1_y += raquete_player_1_dy  # Move a raquete do jogador para baixo

        pygame.display.flip() # Atualiza a tela para exibir as alterações feitas nos desenhos

        clock.tick(60)  # Limita a taxa de atualização da tela a 120 frames por segundo

# fim_jogo()
pygame.quit()  # Encerra o Pygame
sys.exit()  # Encerra o programa