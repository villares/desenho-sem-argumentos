
def setup():
    size(800, 800)
    strokeWeight(15)
    bandeirinha(400, 400, 400)

def bandeirinha(x, y, tamanho):
    """ Bandeirinha na posição x, y com largura e altura 'tamanho' """
    metade = tamanho / 2
    pushMatrix()  # preserva o sistema de coordenadas atual
    translate(x, y)  # translada a origem do sistema de coordenadas
    beginShape()  # começa a desenhar a forma, inicia um polígono
    vertex(-metade, -metade)
    vertex(-metade, metade)
    vertex(0, 0)
    vertex(metade, metade)
    vertex(metade, -metade)
    endShape(CLOSE)  # encerra a forma a fechando no primeiro vértice
    popMatrix() # retorna o sistema de coordenadas anterior
