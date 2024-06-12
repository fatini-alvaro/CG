# menu.py
import pygame  # Importa a biblioteca Pygame para desenvolvimento de jogos em Pythone
from pygame import mixer
import sys
import random  # Importa o módulo random para gerar números aleatórios

mixer.init()

# #Definir Sons
mixer.music.load("audios/music_game.mp3")
mixer.music.play(-1)
som = mixer.Sound("audios/Sound_A.wav")

class Events:
    def __init__(self, larguraTela, alturaTela, corBranco, corPreto, font_file, font, dificuldade):
        pygame.init()
        self.velocidade_bola_x = 3 #Velocidade da bola para cima/baixo
        self.velocidade_bola_y = 3 #Velocidade da bola para direita/esquerda
        self.tamanho_bola = 10 # Diâmetro da bola
        self.raquete_largura = 10 # Largura da raquete
        self.raquete_altura = 60 # Altura da raquete
        self.larguraTela = larguraTela # Define a largura da tela do jogo
        self.alturaTela = alturaTela # Define a altura da tela do jogo
        self.corBranco = corBranco
        self.corPreto = corPreto
        self.pc_x = 10 # Define a posição horizontal da raquete do computador. Neste caso, a raquete começa a 10 pixels da borda esquerda da tela
        self.pc_y = self.alturaTela // 2 - self.raquete_altura // 2 # Define a posição vertical da raquete do computador. Esta posição é metade da altura da tela menos metade da altura da raquete para centralizar
        self.player_1_x = self.larguraTela - 20 #  Define a posição horizontal da raquete do computador. Neste caso, a raquete começa a 20 pixels da borda direita da tela
        self.player_1_y = self.alturaTela // 2 - self.raquete_altura // 2 # posição vertical da raquete do computador. Esta posição é metade da altura da tela menos metade da altura da raquete para centralizar
        self.bola_x = self.larguraTela // 2 - self.tamanho_bola // 2 # posição horizontal da bola no meio da tela menos metade da propria largura da bola pra centralizar bem
        self.bola_y = self.alturaTela // 2 - self.tamanho_bola // 2 # posição vertical da bola do computador. Esta posição é metade da altura da tela menos metade da altura da bola para centralizar
        self.raquete_player_1_dy = 5 # Velocidade de movimento da raquete do jogador para cima/baixo
        self.raquete_pc_dy = 5 # Velocidade de movimento da raquete do computador para cima/baixo
        self.score_player_1 = 0 # Pontuacao do player 1 que sera mostrada em tela
        self.score_pc = 0 # Pontuacao do pc que sera mostrada em tela
        self.font_file = font_file
        self.font = font
        self.rodando = True
        self.vencedor = ""
        self.bola_invisivel = False
        self.bola_falsa = False
        self.bola_falsa_x = 0
        self.bola_falsa_y = 0
        self.velocidade_bola_falsa_x = 3
        self.velocidade_bola_falsa_y = 5

        if dificuldade == 'facil':
            self.velocidade_bola_x = 3
            self.velocidade_bola_y = 3
        elif dificuldade == 'medio':
            self.velocidade_bola_x = 5
            self.velocidade_bola_y = 5
        elif dificuldade == 'dificil':
            self.velocidade_bola_x = 7
            self.velocidade_bola_y = 7

        self.cores = [
            (255, 0, 0),    # Vermelho
            (0, 255, 0),    # Verde
            (0, 0, 255),    # Azul
            (255, 255, 0),  # Amarelo
            (255, 0, 255),  # Magenta
            (0, 255, 255)   # Ciano
        ]
        
        self.cor_bola = corBranco
        self.tempo_decorrido = 0
        self.incremento_velocidade = 0.1

    def iniciar_jogo(self, screen, clock):
        while self.rodando:

            # Processamento de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            screen.fill(self.corPreto)

            self.bola_x += self.velocidade_bola_x #aplica mais velocidade para cima/baixo
            self.bola_y += self.velocidade_bola_y #aplica mais velocidade para direita/esquerda            

            # Retangulos de Colisão
            bola_rect = pygame.Rect(self.bola_x, self.bola_y, self.tamanho_bola, self.tamanho_bola) #Gera o retangulo que fica envolta da bola
            raquete_pc_rect = pygame.Rect(self.pc_x, self.pc_y, self.raquete_largura, self.raquete_altura) #Gera o retangulo que fica envolta da raquete do pc
            raquete_player_1_rect = pygame.Rect(
                self.player_1_x, self.player_1_y, self.raquete_largura, self.raquete_altura
            ) #Gera o retangulo que fica envolta da raquete do player 1

            if self.bola_falsa:
                self.logica_bola_falsa(raquete_pc_rect, raquete_player_1_rect)

            # Colisão da bola com a raquete do pc ou do player
            if bola_rect.colliderect(raquete_pc_rect) or bola_rect.colliderect(raquete_player_1_rect): #validacao quando a bolinha bate na raquete do pc ou do player 1
                self.logica_colisao_com_raquete()


            # Trata a colisão da bola com a borda de cima e de baixo da tela
            if self.bola_y <= 0 or self.bola_y >= self.alturaTela - self.tamanho_bola: #se a bola bateu encima ou embaixo da tela
                self.velocidade_bola_y = -self.velocidade_bola_y #inverte o valor da velocidade em y para ela tomar o rumo oposto
                self.cor_bola = random.choice(self.cores)  # Muda a cor da bola

            self.valida_se_pontuou(screen)   

            self.movimenta_raquete_pc()         

            # Mostrando Score no jogo
            score_texto = self.font.render(
                f"Score PC: {self.score_pc}       Score Player_1: {self.score_player_1}", True, self.corBranco
            )
            score_rect = score_texto.get_rect(center=(self.larguraTela //2, 30))
            screen.blit(score_texto, score_rect)

            self.incrementa_tempo(clock)

            self.desenha_objetos_na_tela(screen)

            self.controle_movimentos()

            pygame.display.flip() # Atualiza a tela para exibir as alterações feitas nos desenhos

            clock.tick(60)  # Limita a taxa de atualização da tela a 120 frames por segundo

    def fim_jogo(self, screen):
        while True: # Loop infinito para aguardar comandos do usuario
            for event in pygame.event.get(): # Verifica se foi adcionado algum comando pelo usuario
                if event.type == pygame.QUIT: # Verifica se o comando foi de fechar a janela para fechar o jogo
                    pygame.quit() 
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        controle = True
                        return
            #Renderiza o texto do menu
            screen.fill(self.corPreto)
            texto_fim = self.font.render(f"Vencedor: {self.vencedor}", True, self.corBranco )
            text_film_rect = texto_fim.get_rect(center=(self.larguraTela // 2, self.alturaTela // 2))
            screen.blit(texto_fim, text_film_rect)

            pygame.display.flip()

    def logica_bola_falsa(self, raquete_pc_rect, raquete_player_1_rect):        
        self.bola_falsa_x += self.velocidade_bola_falsa_x #aplica mais velocidade para cima/baixo
        self.bola_falsa_y += self.velocidade_bola_falsa_y #aplica mais velocidade para direita/esquerda

        bola_rect_falsa = pygame.Rect(self.bola_falsa_x, self.bola_falsa_y, self.tamanho_bola, self.tamanho_bola) #Gera o retangulo que fica envolta da bola

        # Colisão com as raquetes
        if bola_rect_falsa.colliderect(raquete_pc_rect) or bola_rect_falsa.colliderect(raquete_player_1_rect):
            self.velocidade_bola_falsa_x = -self.velocidade_bola_falsa_x #inverte o valor da velocidade em x para ela tomar o rumo oposto
            self.cor_bola = random.choice(self.cores)  # Muda a cor da bola

        # Colisão com as paredes superior e inferior
        if self.bola_falsa_y<= 0 or self.bola_falsa_y >= self.alturaTela:
            self.velocidade_bola_falsa_y = -self.velocidade_bola_falsa_y #inverte o valor da velocidade em y para ela tomar o rumo oposto
            self.cor_bola = random.choice(self.cores)  # Muda a cor da bola

        if self.bola_falsa_x <= 0:
            self.bola_falsa = False

        if self.bola_falsa_x >= self.larguraTela - self.tamanho_bola:
            self.bola_falsa = False

    def logica_colisao_com_raquete(self):
        som.play()
        self.velocidade_bola_x = -self.velocidade_bola_x #inverte o valor da velocidade em x para ela tomar o rumo oposto
        self.cor_bola = random.choice(self.cores)  # Muda a cor da bola
        # 20% de chance da bola ficar invisível
        if random.random() < 0.2:
            self.bola_invisivel = True
        else:
            self.bola_invisivel = False

        # 10% de chance de criar uma bola falsa
        if random.random() < 0.1 and self.bola_falsa is False:
            self.bola_falsa_x = self.bola_x #aplica mais velocidade para cima/baixo
            self.bola_falsa_y = self.bola_y
            self.velocidade_bola_falsa_x = self.velocidade_bola_x
            self.velocidade_bola_falsa_y = -self.velocidade_bola_y
            self.bola_falsa = True

    def valida_se_pontuou(self, screen):
        # Validacao para caso a bolinha saia da lateral da tela (no caso ponto de um jogador) a bola volta para o meio da tela para outra rodada e aumenta a pontuação do player
        if self.bola_x <= 0:
            self.bola_x = self.larguraTela // 2 - self.tamanho_bola // 2 # Centraliza lateralmente
            self.bola_y =  self.alturaTela // 2 - self.tamanho_bola // 2 # Centraliza verticalmente
            self.velocidade_bola_x = -self.velocidade_bola_x  #Inverte o lado da direção da bola para quando alguem fizer ponto a bola começar para o lado do perdedor
            self.score_player_1 += 1
            self.bola_falsa = False
            print(f"Score Player_1: {self.score_player_1}")
            if self.score_player_1 == 3:
                print("Player 1 ganhou!")
                self.vencedor = "Player 1"
                self.fim_jogo(screen)
                return

        # Validacao para caso a bolinha saia da lateral da tela (no caso ponto de um jogador) a bola volta para o meio da tela para outra rodada e aumenta a pontuação do pc
        if self.bola_x >= self.larguraTela - self.tamanho_bola:
            self.bola_x = self.larguraTela // 2 - self.tamanho_bola // 2 # Centraliza lateralmente
            self.bola_y = self.alturaTela // 2 - self.tamanho_bola // 2 # Centraliza verticalmente
            self.velocidade_bola_x = -self.velocidade_bola_x  #Inverte o lado da direção da bola para quando alguem fizer ponto a bola começar para o lado do perdedor
            self.score_pc += 1
            self.bola_falsa = False
            print(f"Score PC: {self.score_pc}")
            if self.score_pc == 3:
                print("PC ganhou!")
                self.vencedor = "PC"
                self.fim_jogo(screen)
                return
            
    def movimenta_raquete_pc(self):
        # Movendo a raquete do pc para seguir a bola
        if self.pc_y + self.raquete_altura // 2 < self.bola_y:
            self.pc_y += self.raquete_pc_dy
        elif self.pc_y + self.raquete_altura // 2 > self.bola_y:
            self.pc_y -= self.raquete_pc_dy

        # Evitar que a raquete do pc saia da área da tela
        if self.pc_y < 0:
            self.pc_y = 0
        elif self.pc_y > self.alturaTela - self.raquete_altura:
            self.pc_y = self.alturaTela - self.raquete_altura

        # Evitar que a raquete do player saia da área da tela
        if self.pc_y < 0:
            self.pc_y = 0
        elif self.pc_y > self.alturaTela - self.raquete_altura:
            self.pc_y = self.alturaTela - self.raquete_altura

    def incrementa_tempo(self, clock):
        # Incrementa o tempo decorrido
        self.tempo_decorrido += clock.get_time()

        # Aumenta a velocidade da bola a cada 5 segundos
        if self.tempo_decorrido > 5000:  # 5000 milissegundos = 5 segundos
            self.velocidade_bola_x *= (1 + self.incremento_velocidade)
            self.velocidade_bola_y *= (1 + self.incremento_velocidade)
            self.tempo_decorrido = 0  # Reinicia o tempo decorrido

    def desenha_objetos_na_tela(self, screen):
        # Desenha as raquetes do computador e do jogador, e a bola na tela
        pygame.draw.rect(screen, self.corBranco, (self.pc_x, self.pc_y, self.raquete_largura, self.raquete_altura))  # Raquete do computador
        pygame.draw.rect(screen, self.corBranco, (self.player_1_x, self.player_1_y, self.raquete_largura, self.raquete_altura))  # Raquete do jogador

        if not self.bola_invisivel:
            pygame.draw.ellipse(screen, self.cor_bola, (self.bola_x, self.bola_y, self.tamanho_bola, self.tamanho_bola))  # Bola            
            if self.bola_falsa:
                pygame.draw.ellipse(screen, self.cor_bola, (self.bola_falsa_x, self.bola_falsa_y, self.tamanho_bola, self.tamanho_bola))

        pygame.draw.aaline(screen, self.corBranco, (self.larguraTela //2, 0), (self.larguraTela //2, self.alturaTela)) #Cria uma linha vertical no meio da tela

    def controle_movimentos(self):
        # Controle Teclado do Player 1
        keys = pygame.key.get_pressed()  # Captura as teclas pressionadas

        # Movimentação da raquete do jogador para cima se a tecla de seta para cima estiver pressionada
        if keys[pygame.K_UP] and self.player_1_y > 0:  # Verifica se a tecla de seta para cima está pressionada e se a raquete não está na borda superior
            self.player_1_y -= self.raquete_player_1_dy  # Move a raquete do jogador para cima

        # Movimentação da raquete do jogador para baixo se a tecla de seta para baixo estiver pressionada
        if keys[pygame.K_DOWN] and self.player_1_y < self.alturaTela - self.raquete_altura:  # Verifica se a tecla de seta para baixo está pressionada e se a raquete não está na borda inferior
            self.player_1_y += self.raquete_player_1_dy  # Move a raquete do jogador para baixo