def setup():
    size(500, 500)
    strokeWeight(15)
    background(0)
    olho(250, 250, 400, color(100))
    
def olho(x, y, largura, cor):
    """ Olho na posição x, y com largura e cor """
    pushStyle() # preserva os atributos gráficos atuais
    noStroke()
    fill(255)
    ellipse(x, y, largura, largura * .5)
    fill(cor)
    circle(x, y, largura * .4)
    fill(0)
    circle(x, y, largura * .1)
    popStyle() # retorna os atributos gráficos anteriores
