import pygame
import random

class MovendoTexto:
  def __init__(self, texto, fonte_tamanho, largura, altura):
    self.font = pygame.font.SysFont(None, fonte_tamanho)
    self.texto = texto
    self.largura = largura
    self.altura = altura
    self.texto_surf = self.font.render(texto, True, (255, 255, 255))  # Renderiza o texto com a fonte e a cor especificadas
    self.rect = self.texto_surf.get_rect(center=(largura/2, altura/2))  # Obtém o retângulo que envolve o texto e o posiciona no centro da janela

    self.velocidade_x = self.gerrar_numero_nao_zero()
    self.velocidade_y = self.gerrar_numero_nao_zero()

  def gerrar_numero_nao_zero(self):
    numero = 0
    while numero == 0:
      numero = random.randint(-1, 1)
    return numero
  
  def move(self):
    self.rect.x += self.velocidade_x
    self.rect.y += self.velocidade_y

    # Verifica se o texto atingiu os limites da janela e ajusta as velocidades e a cor do texto
    if self.rect.left <= 0:
      self.velocidade_x = random.randint(0,1)
      self.velocidade_y = random.randint(-1, 1)
      self.change_color()

    if self.rect.right >= self.largura:
      self.velocidade_x = random.randint(-1,0)
      self.velocidade_y = random.randint(-1, 1)
      self.change_color()

    if self.rect.top <= 0:
      self.velocidade_x = random.randint(-1, 1)
      self.velocidade_y = random.randint(0, 1)
      self.change_color()

    if self.rect.bottom >= self.altura:
      self.velocidade_x = random.randint(-1, 1)
      self.velocidade_y = random.randint(-1, 0)
      self.change_color()

  def change_color(self):
    color_texto = (
      random.randint(0, 255),
      random.randint(0, 255),
      random.randint(0, 255)
    )
    self.texto_surf = self.font.render(self.texto, True, color_texto) # Renderiza o texto com a nova cor