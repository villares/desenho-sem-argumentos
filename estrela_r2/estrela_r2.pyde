def estrela(x_centro, y_centro, num_pontas, raio_a, raio_b):
    """
    Desenha uma estrela em x_centro, y_centro com num_pontas
    raio_a e raio_b são raios dos pontos internos e das pontas
    """
    n = num_pontas * 2 # número de pontos, dobro das pontas
    ang = radians(360. / n) # 360 graus / n em radianos
    beginShape() # começa a desenhar a forma
    for i in range(n):
        r = raio_a if i % 2 == 0 else raio_b 
        x = x_centro + sin(ang * i) * r
        y = y_centro + cos(ang * i) * r
        vertex(x, y)
    endShape(CLOSE) # encerra uma forma fechada
    
def setup():
    size(500, 500)   # área de desenhp
    strokeWeight(15)  # espessura do traço
    estrela(250, 250, 7, 200, 100)  # estrela de 7 pontas
