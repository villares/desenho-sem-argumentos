def setup():
    size(800, 800)
    strokeWeight(15)
    olho(400, 400, 400, color(100))
    
def draw():
    strokeWeight(1)
    olho(mouseX, mouseY, 100, color(random(256)))

def olho(x, y, largura, cor):
    """ Olho na posição x, y com largura e cor """
    metade = largura / 2
    fill(255)
    ellipse(x, y, largura, metade)
    fill(cor)
    circle(x, y, metade)
    fill(0)
    circle(x, y, largura / 10)
