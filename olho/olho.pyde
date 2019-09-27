def setup():
    size(800, 800)
    strokeWeight(15)
    background(0)
    olho(400, 400, 400, color(100))
    
def olho(x, y, largura, cor):
    """ Olho na posição x, y com largura e cor """
    noStroke()
    fill(255)
    ellipse(x, y, largura, largura * .5)
    fill(cor)
    circle(x, y, largura * .4)
    fill(0)
    circle(x, y, largura * .1)
