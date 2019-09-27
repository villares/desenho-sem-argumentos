def setup():
    size(500, 500)   # área de desenhp
    strokeWeight(15)  # espessura do traço
    estrela(250, 250, 7, 200, 100)  # estrela de 7 pontas

def estrela(x, y, np, ra, rb):
    """
    Desenha uma estrela com np pontas
    raio a e raio b são os raios internos e das pontas
    """
    pushMatrix() # reserva o sistema de coordenadas atual
    translate(x, y) # altera a origem do desenho
    n = np * 2 # a forma é um polígono o dobro de pontos que as pontas
    ang = radians(360. / n) 
    beginShape() # começa a desenhar a forma
    for i in range(n):
        if i % 2 == 0:
            r = ra
        else:
            r = rb
        x = sin(ang * i) * r
        y = cos(ang * i) * r
        vertex(x, y)
    endShape(CLOSE) # encerra uma forma fechada
    popMatrix()
