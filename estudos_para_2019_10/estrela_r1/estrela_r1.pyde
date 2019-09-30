def setup():
    size(500, 500)   # área de desenhp
    strokeWeight(15)  # espessura do traço
    estrela(250, 250, 7, 200, 100)  # estrela de 7 pontas

def estrela(x_centro, y_centro, num_pontas, raio_a, raio_b):
    """
    Desenhe uma estrela em x_centro, y_centro com num_pontas
    raio_a e raio_b são os raios internos e das pontas
    """
    n = num_pontas * 2 # a forma tem o dobro de pontos que pontas
    inc = radians(360. / n) # ângulo (incremento) entre os pontos
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
    endShape(CLOSE) # encerra a forma fechando no primeiro ponto
