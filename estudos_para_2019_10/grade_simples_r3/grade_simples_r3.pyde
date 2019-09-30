def setup():
    size(500, 500)
    strokeWeight(10)
    noLoop()

def draw():
    background(200)    
    grade(250, 250, 4, 500., randomize=True)

def grade(x_centro, y_centro, n, tam_total, randomize=False):
    tam = tam_total / n
    desloc = (tam - tam_total) / 2.
    for i in range(n):
        x = x_centro + desloc + tam * i
        for j in range(n):
            y =  y_centro + desloc + tam * j
            if randomize:
                circle(x, y, random(10, tam * .9))
            else: 
                square(x, y, tam * .75)

def keyPressed():
    saveFrame("grade.png")
    redraw()
