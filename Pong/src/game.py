import pygame
import sys
from menu import Menu
from events import Events

class Game:
  def __init__(self):
    pygame.init()
    self.larguraTela = 800 # Define a largura da tela do jogo
    self.alturaTela = 600 # Define a altura da tela do jogo
    self.corPreto = (0,0,0) # Define a cor preta em formato RGB
    self.corBranco = (255,255,255) # Define a cor branca em formato RGB
    
    # Configuração da fonte
    self.font_file = 'font/PressStart2P-Regular.ttf' #Passa o caminho do arquivo para uma variavel
    self.font = pygame.font.Font(self.font_file, 20)
    
    self.screen = pygame.display.set_mode((self.larguraTela, self.alturaTela))  # Cria a janela do jogo com as dimensões especificadas
    pygame.display.set_caption("PONG")  # Define o título da janela do jogo
    self.clock = pygame.time.Clock()  # Cria um objeto Clock para controlar a taxa de quadros por segundo do jogo
    self.rodando = True
    self.menu = Menu(self.clock, self.corBranco, self.corPreto, self.larguraTela, self.alturaTela)  # Cria uma instância da classe Menu
    

  def run(self):
    while self.rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.rodando = False
        self.screen.fill((0, 0, 0))  # Preenche a tela com preto

        dificuldade = self.menu.mostrar_menu(self.screen, pygame.font.Font(None, 32))
        if dificuldade is not None:
            self.events = Events(self.larguraTela, self.alturaTela, self.corBranco, self.corPreto, self.font_file, self.font, dificuldade)
            self.events.iniciar_jogo(self.screen, self.clock)

        pygame.display.flip()
        self.clock.tick(60)