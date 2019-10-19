add_library('pdf')
"""Exemplo de desenho interativo com setup() e draw()."""

def setup(): # função executada uma vez no começo 
    size(500, 500) # define área de desenho
    beginRecord(PDF, "casinha.pdf")
    background(100) # limpa a área com fundo cinza escuro
    strokeWeight(2) # ajusta espessura do traço
        
def draw(): # função executada cerca de 60 vezes por segundo
    if mousePressed: # se o mouse estiver pressionado
        casinha(mouseX, mouseY, 40) # desenhe na ponta do 
            
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
    
    
def keyPressed():
    endRecord()
    exit()
    
