"""
Um função que desenha olhos. Exportação de PDF.
"""

add_library('pdf')  # Inclui biblioteca de PDF do Processing

def setup():
    size(500, 500)
    beginRecord(PDF, 'olho.pdf')
    cinza_escuro = color(100)  # cria um valor de cor
    cinza_claro = color(200)  # cria um valor de cor
    background(cinza_claro)  # fundo
    olho(width / 2, width / 4, width * .45, cinza_claro)
    olho(width / 2, width / 2, width * .37, cinza_escuro)
    olho(width / 2, width * .75, width * .3, cinza_claro)
    endRecord()  # finaliza salvamento do PDF

def olho(x, y, largura, cor):
    """
    Desenhe um olho na posição x, y com largura e cor.
    """
    pushStyle()  # preserva os atributos gráficos atuais
    noStroke()  # desliga o traço
    fill(255)  # preenchimento branco
    ellipse(x, y, largura, largura * .45)  # desenha branco
    fill(cor)  # cor de preenchimento do parâmetro
    circle(x, y, largura * .4)  # desenha iris
    fill(0)  # preenchimento preto
    circle(x, y, largura * .1)  # desenha pupila
    popStyle()  # retorna aos atributos gráficos anteriores
