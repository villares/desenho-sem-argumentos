add_library('pdf')

def setup():
    size(500, 500)   # área de desenhp
    beginRecord(PDF, "estrela.pdf")
    noStroke()
    fill(200)
    rect(0, 0, width, height)
    stroke(0)
    strokeWeight(5)  # espessura do traço
    fill(255)
    estrela(125, 125, 12, 100, 75)  # estrela de 12 pontas
    estrela(375, 125, 5, 100, 50)  # estrela de 5 pontas
    estrela(125, 375, 7, 100, 50)  # estrela de 7 pontas
    estrela(375, 375, 9, 100, 30)  # estrela de 9 pontas
    endRecord()
    # saveFrame("estrela.png")

def estrela(x_centro, y_centro, num_pontas, raio_a, raio_b):
    """
    Desenhe uma estrela em x_centro, y_centro com num_pontas
    raio_a e raio_b são raios dos pontos internos e pontas
    """
    n = num_pontas * 2 # o dobro de pontos totais que pontas
    ang = radians(360. / n) # 360 graus / n em radianos
    beginShape() # começa a desenhar a forma
    for i in range(n):
        r = raio_a if i % 2 == 0 else raio_b 
        x = x_centro + sin(ang * i) * r
        y = y_centro + cos(ang * i) * r
        vertex(x, y)
    endShape(CLOSE) # encerra fechando no primeiro ponto
    

    
