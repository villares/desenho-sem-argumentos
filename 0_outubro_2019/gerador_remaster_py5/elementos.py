# py5 imported mode code

"""
Exemplo de desenho interativo com setup() e draw()
"""

def setup():  # função executada uma vez no começo
    size(500, 500)   # define área de desenho
    background(200)  # limpa o desenho com fundo cinza
    stroke_weight(2) # ajusta espessura do traço
    
def draw():  # função executada cerca de 60 vezes por segundo
    if is_mouse_pressed:  # se o mouse estiver pressionado
        casinha(mouse_x, mouse_y, 40)  # desenho em x, y do mouse

def casinha(x, y, tamanho):
    """
    Desenha casinha na posição x, y com largura e altura 'tamanho'
    """
    metade = tamanho / 2
    push_matrix()  # preserva o sistema de coordenadas atual
    translate(x, y)  # translada a origem do sistema de coordenadas
    begin_shape()  # começa a desenhar a forma, inicia um polígono
    vertex(0, -metade)
    vertex(-metade, 0)
    vertex(-metade, metade)
    vertex(metade, metade)
    vertex(metade, 0)
    end_shape(CLOSE)  # encerra a forma a fechando no 1o vértice
    pop_matrix() # retorna o sistema de coordenadas anterior
    
"""
Desenhando quatro estrelas diferentes.
"""
    
def setup():
    size(500, 500)
    stroke_weight(5)
    estrela(125, 125, 12, 100, 75)
    estrela(375, 125, 5, 100, 50)
    estrela(125, 375, 7, 100, 50)
    estrela(375, 375, 9, 100, 50)

def estrela(x_centro, y_centro, num_pontas, raio_a, raio_b):
    """
    Desenha uma estrela em x_centro, y_centro com num_pontas
    raio_a e raio_b são o raio interno e raio das pontas.
    """
    # Calcula ângulo de incremento entre os vértices
    inc = radians(360 / num_pontas) / 2 
    begin_shape() # começa a desenhar a forma
    ang = 0 # começando com o ângulo 0
    while ang < TWO_PI:
        x = x_centro + sin(ang) * raio_a
        y = y_centro + cos(ang) * raio_a
        vertex(x, y)
        ang += inc
        x = x_centro + sin(ang) * raio_b
        y = y_centro + cos(ang) * raio_b
        vertex(x, y)
        ang += inc
    end_shape(CLOSE) # encerra uma forma fechada
    
    
def olho(x, y, largura, cor=color(100)):
    """ Olho na posição x, y com largura e cor """
    push_style() # preserva os atributos gráficos atuais
    no_stroke()
    fill(255)
    ellipse(x, y, largura, largura * .45)
    fill(cor)
    circle(x, y, largura * .4)
    fill(0)
    circle(x, y, largura * .1)
    pop_style() # retorna os atributos gráficos anteriores
    
    
def grade(x_centro, y_centro, n, tam_total, rnd_circ=False):
    tam = tam_total / n
    desloc = (tam - tam_total) / 2.
    for i in range(n):
        x = x_centro + desloc + tam * i
        for j in range(n):
            y =  y_centro + desloc + tam * j
            if rnd_circ:
                # no Processing random(inicio, final_ni)
                circle(x, y, random(tam * .1, tam * .9))
            else: 
                square(x, y, tam * .75)
