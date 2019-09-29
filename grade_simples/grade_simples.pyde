def grade(xo, yo, n, tam_total):
    tam_celula = tam_total / n
    desloc = (tam_celula - tam_total) / 2.
    for i in range(n):
        x = xo + desloc + tam_celula * i
        for j in range(n):
            y =  yo + desloc + tam_celula * j
            circle(x, y, tam_celula * .75)

def setup():
    size(500, 500)
    strokeWeight(15)
    grade(250, 250, 4, 500.)

def keyPressed():
    saveFrame("####.png")
    redraw()
