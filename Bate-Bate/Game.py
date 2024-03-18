import pygame
import sys
from MecMovimento import MovendoTexto

class Game:
  def __init__(self):
    pygame.init()
    self.largura = 800
    self.altura = 600
    self.tela = pygame.display.set_mode((self.largura, self.altura))  # Cria a janela do jogo com as dimensões especificadas
    pygame.display.set_caption("Bate-Bola")  # Define o título da janela do jogo
    self.clock = pygame.time.Clock()  # Cria um objeto Clock para controlar a taxa de quadros por segundo do jogo
    self.MovendoTexto = MovendoTexto("Alvaro", 50, self.largura, self.altura)  # Cria uma instância da classe MovendoTexto

  def run(self):
    rodando = True
    while rodando:
      for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
          rodando = False

      self.MovendoTexto.move()
      self.tela.fill((0, 0, 0))  # Preenche a tela com a cor preta
      self.tela.blit(self.MovendoTexto.texto_surf, self.MovendoTexto.rect)  # Desenha o texto na tela
      pygame.display.flip()  # Atualiza a tela
      self.clock.tick(60)  # Limita a taxa de quadros por segundo do jogo
        
    pygame.quit
    sys.exit()