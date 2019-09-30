"""
Exemplo de uso de uma função que desenha um olho.
"""

def setup():
    size(500, 500)
    background(0) # fundo preto
    cinza_escuro =  color(100) # cria um valor de cor
    olho(width / 2, width / 2, width * .8, cinza_escuro)

def olho(x, y, largura, cor):
    """Denhenhe um olho na posição x, y com largura e cor da iris."""
    pushStyle() # preserva os atributos gráficos atuais
    noStroke() # desliga o traço
    fill(255) # preenchimento branco
    ellipse(x, y, largura, largura * .45) # desenha elipse branca 
    fill(cor) # cor de preenchimento do parâmetro
    circle(x, y, largura * .4) # desenha a iris
    fill(0) # preenchimento preto
    circle(x, y, largura * .1) # desenha a pupila
    popStyle() # retorna aos atributos gráficos anteriores
    
    saveFrame("olho.png")



    
