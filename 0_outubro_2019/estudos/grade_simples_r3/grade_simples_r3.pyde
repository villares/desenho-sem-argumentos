"""
Exemplo de uso de uma função que desenha uma grade.
"""

def setup():
    size(500, 500)
    noStroke()
    fill(0)
    noLoop()

def draw():
    background(200)    
    grade(250, 250, 8, width, rnd_circ=True)

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
                
def keyPressed():
    saveFrame("grade.png")
    redraw()
