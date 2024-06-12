# menu.py
import pygame
import sys

class Menu:
    def __init__(self, clock, corBranco, corPreto, larguraTela, alturaTela):
        self.clock = clock
        self.corBranco = corBranco
        self.corPreto = corPreto
        self.larguraTela = larguraTela
        self.alturaTela = alturaTela

    def mostrar_menu(self, screen, font):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        return 'facil'
                    elif event.key == pygame.K_2:
                        return 'medio'
                    elif event.key == pygame.K_3:
                        return 'dificil'

			#Renderiza o texto do menu
            screen.fill(self.corPreto)  # Preenche a tela com preto
            texto_menu = font.render("Pong", True, self.corBranco)
            text_menu_rect = texto_menu.get_rect(center=(self.larguraTela //2, self.alturaTela // 2))
            screen.blit(texto_menu, text_menu_rect)

            texto_dificuldade = font.render("Pressione a tecla para definir a dificuldade 1: Fácil  2: Médio  3: Difícil", True, self.corBranco)
            texto_dificuldade_rect = texto_dificuldade.get_rect(center=(self.larguraTela // 2, self.alturaTela // 2 + 50))
            screen.blit(texto_dificuldade, texto_dificuldade_rect)

            self.clock.tick(1)
            pygame.display.flip()
