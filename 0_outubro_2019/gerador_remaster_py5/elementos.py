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
    
    
"""
Uma função que desenha olhos. Exportação de PDF.
"""
"""
Uma função que desenha olhos. Exportação de PDF.
"""

def setup():  # função executada uma vez no começo
    size(500, 500)   # define área de desenho
    begin_record(PDF, 'olho.pdf')  # inicia gravação
    cinza_200 = color(200)   # cria um valor de cor
    cinza_100 = color(100)  # cria outro valor de cor
    olho(width / 2, height * 0.25, width * 0.45, cinza_200)
    olho(width / 2, height * 0.50, width * 0.37, cinza_100)
    olho(width / 2, height * 0.75, width * 0.30, cinza_200)
    end_record()  # encerra gravação
    
def olho(x, y, largura, cor=color(200, 200, 0)):
    """ Olho na posição x, y com largura e cor."""
    push_style() # preserva os atributos gráficos atuais
    no_stroke()  # desenha formas sem traço de contorno
    fill(255)    # preenchimnto branco
    ellipse(x, y, largura, largura * 0.45)  # branco do olho
    fill(cor)    # cor do parâmetro, preenchimento da iris
    circle(x, y, largura * 0.4)  # desenha a iris
    fill(0)      # preenchimento preto da pupila
    circle(x, y, largura * 0.1)   # desenha pupila
    pop_style() # retorna aos atributos gráficos anteriores
    
"""
Uma grade com laços encaixados e elementos variados.
"""

# def setup(): 
#     size(500, 500)
#     no_stroke()  # desenhar formas sem traço de contorno
#     fill(0)      # preenchimento preto
#     no_loop()    # faz o draw() parar depois de um frame
# 
# def draw():
#     background(200)  # fundo cinza (e limpa o frame)
#     grade(250, 250, 8, width, rnd_circ=True)
    
def grade(x_centro, y_centro, n, tam_total, rnd_circ=False):
    tam = tam_total / n
    desloc = (tam - tam_total) / 2
    for i in range(n):
        x = x_centro + desloc + tam * i
        for j in range(n):
            y =  y_centro + desloc + tam * j
            if rnd_circ:
                # no Processing random(inicio, final_ni)
                circle(x, y, random(tam * 0.1, tam * 0.9))
            else: 
                square(x, y, tam * 0.75)

def key_pressed():  # no evento de uma tecla ser pressionada
    save_frame('grade###.png')   # salva uma imagem PNG
    redraw()  # dispara uma nova execução do draw()