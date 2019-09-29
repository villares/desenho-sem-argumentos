def setup():
    size(500, 500)   # área de desenhp
    strokeWeight(15)  # espessura do traço
    estrela(250, 250, 7, 200, 100)  # estrela de 7 pontas

def estrela(x_centro, y_centro, num_pontas, raio_a, raio_b):
    """
    Desenha uma estrela com np pontas
    raio a e raio b são os raios internos e das pontas
    """
    n = num_pontas * 2 # o dobro de pontos que o número de pontas
    ang = radians(360. / n) # divide 360 graus por n e converte em radianos
    beginShape() # começa a desenhar a forma
    for i in range(n):
        r = raio_a if i % 2 == 0 else raio_b 
        x = x_centro + sin(ang * i) * r
        y = y_centro + cos(ang * i) * r
        vertex(x, y)
    endShape(CLOSE) # encerra uma forma fechada
