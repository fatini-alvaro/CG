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

tamanho_fonte = 50
fonte = pygame.font.SysFont(None, tamanho_fonte)

texto = fonte.render("Alvaro", True, BRANCO)

texto_topo_esquerdo = texto.get_rect() #Topo esquerdo
texto_centro_esquerdo = texto.get_rect() #Topo esquerdo
texto_centro = texto.get_rect(center=(largura/2, altura/2)) #Centro
texto_topo = texto.get_rect(center=(largura/2, 25)) #Topo
texto_embaixo = texto.get_rect(center=(largura/2, altura-25)) #Embaixo
texto_topo_direito = texto.get_rect(center=(largura-60, 25)) #Topo direito
texto_embaixo_direito = texto.get_rect(center=(largura-60, altura-25)) #Embaixo direito
texto_embaixo_esquerdo = texto.get_rect(center=(60, altura-25)) #Embaixo esquerdo

texto_topo_esquerdo.left = 0
texto_topo_esquerdo.top = 0

#Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    tela.fill(PRETO)
    tela.blit(texto, texto_centro)
    tela.blit(texto, texto_topo)
    tela.blit(texto, texto_embaixo)
    tela.blit(texto, texto_topo_direito)
    tela.blit(texto, texto_topo_esquerdo)
    tela.blit(texto, texto_embaixo_direito)
    tela.blit(texto, texto_embaixo_esquerdo)
    pygame.display.flip()


# ----------------------
    
    