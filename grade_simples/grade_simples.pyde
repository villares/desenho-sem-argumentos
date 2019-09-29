def setup():
    size(500, 500)
    strokeWeight(15)
    grade(250, 250, 3, 500.)

def grade(xo, yo, n, tw):
    cw = tw / n
    offset = (cw - tw) / 2.
    for i in range(n):
        x = xo + offset + cw * i
        for j in range(n):
            y =  yo + offset + cw * j
            circle(x, y, cw * .75)

def keyPressed():
    saveFrame("####.png")
    redraw()
