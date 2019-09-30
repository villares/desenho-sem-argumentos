def setup():
    size(500, 500) # área de desenho
    strokeWeight(10)
    background(128)
    casinha(250, 250, 400)
    
    saveFrame("casinha.png")

def casinha(x, y, tamanho):
    """
    Desenhe casinha em x, y com largura e altura 'tamanho'.
    """
    metade = tamanho / 2
    pushMatrix()  # preserva o sistema de coordenadas atual
    translate(x, y)  # translada a origem das coordenadas
    beginShape()  # começa a desenhar a forma/polígono
    vertex(0, -metade)
    vertex(-metade, 0)
    vertex(-metade, metade)
    vertex(metade, metade)
    vertex(metade, 0)
    endShape(CLOSE)  # encerra fechando no 1o vértice
    popMatrix() # retorna o sistema de coordenadas anterior
    
    
