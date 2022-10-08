# -*- encoding: utf-8 -*-

import py5
from py5 import *

def setup():
    py5.size(400, 400)
    
    poligono_regular(100, 100, 100, 6)
    
    

def casinha(x, y, tamanho):
    """ Casinha na po_sição x, y com largura e altura 'tamanho' """
    metade = tamanho / 2
    push_matrix()  # preserva o sistema de coordenadas atual
    translate(x, y)  # translada a origem do sistema de coordenadas
    begin_shape()  # começa a desenhar a forma, inicia um polígono
    vertex(0, -metade)
    vertex(-metade, 0)
    vertex(-metade, metade)
    vertex(metade, metade)
    vertex(metade, 0)
    end_shape(CLOSE)  # encerra a forma a fechando no primeiro vértice
    pop_matrix() # retorna o sistema de coordenadas anterior
    
def poligono_regular(x_centro, y_centro, r, lados):
    """
    Desenha um polígono regular cujos vértices estariam em um
    círculo com centro em x_centro, y_centro e raio `r`
    """
    begin_shape() # começa a desenhar a forma
    for i in range(lados):
        ang = i * TWO_PI / lados
        x = x_centro + sin(ang) * r
        y = y_centro + cos(ang) * r
        vertex(x, y)
    end_shape(CLOSE) # encerra uma forma fechada
    
py5.run_sketch()

    
def grade(xo, yo, n, tam_total):
    tam_celula = tam_total / n
    desloc = (tam_celula - tam_total) / 2.
    for i in range(n):
        x = xo + desloc + tam_celula * i
        for j in range(n):
            y =  yo + desloc + tam_celula * j
            rect_mode(CENTER)
            square(x, y, tam_celula * .6)
