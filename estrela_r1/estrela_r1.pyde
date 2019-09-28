def setup():
    size(500, 500)   # área de desenhp
    strokeWeight(15)  # espessura do traço
    estrela(250, 250, 7, 200, 100)  # estrela de 7 pontas

def estrela(x_centro, y_centro, num_pontas, raio_a, raio_b):
    """
    Desenha uma estrela com np pontas
    raio a e raio b são os raios internos e das pontas
    """
    n = num_pontas * 2 # a forma é um polígono o dobro de pontos que as pontas
    inc = radians(360. / n) # ângulo de eincremento entre os pontos
    beginShape() # começa a desenhar a forma
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
    endShape(CLOSE) # encerra uma forma fechada
    
    # pushMatrix() # reserva o sistema de coordenadas atual
    # translate(x_centro, y_centro) # altera a origem do desenho
    # n = num_pontas * 2 # a forma é um polígono o dobro de pontos que as pontas
    # inc = radians(360. / n) # ângulo de incremento
    # beginShape() # começa a desenhar a forma
    # for i in range(n):
    #     if i % 2 == 0:
    #         r = raio_a
    #     else:
    #         r = raio_b
    #     x = sin(inc * i) * r
    #     y = cos(inc * i) * r
    #     vertex(x, y)
    # endShape(CLOSE) # encerra uma forma fechada
    # popMatrix()
