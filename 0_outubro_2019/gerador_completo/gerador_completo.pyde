"""
Poster desenho() #0_outubro_2019 versão 191023a
https://desenho.lugaralgum.com (para licenças, créditos e agradecimentos!)
"""

from poster import poster
from elementos import grade
add_library('pdf')

def setup():
    global frente, verso, semente, tiragem, f
    size(1122, 1587)
    noLoop()
    
    frente = loadShape('base_frente.svg')
    verso = loadShape('base_poster.svg')
    """
    Aviso de erro quando tentei usar um VLW:
    Use createFont() instead of loadFont() when drawing text using the PDF library.
    """
    f = createFont('Inconsolata-Bold', 18)  # precisa ter Inconsolata Bold instalada

    # 10 com 191020; 100 com 191021; 100 com 191022;
    # 01 com 191929 (amostra); 1 com 191110;
    # 10 com 191111.
    # seed "master" da tiragem (não incluso para tiragem > 1)
    semente = random_seed(191020)  
    tiragem = 1

def draw():
    """
    Gerar PDF de múltiplas páginas e sair.
    (desencane de olhar que fica feio na tela, abra o PDF!)
    """
    global semente
    pdf = beginRecord(PDF, "desenho0-{}-{}.pdf".format(semente, tiragem))
    
    for i in range(tiragem):
        if tiragem > 1:
            semente = random_seed()
        shape(frente)
        y_grade = height - 31 - 321 / 2.
        x_grade = 25 + 321 / 2.
        rectMode(CENTER)
        noStroke()
        fill(200)
        rect(x_grade, y_grade, 321, 321)
        fill(0)
        grade(x_grade, y_grade, 6, 321, rnd_circ=True)
        pdf.nextPage()
        shape(verso)    
        largura_miolo = width - 110
        poster(width / 2, height - 55 - largura_miolo / 2, 6, largura_miolo)
        # fill(255, 0, 0) # vermelho para debug da posição
        textFont(f)
        textSize(10.5)
        fill(0)
        text('s = '+str(semente), 47, 333)
        if i < tiragem - 1:
            pdf.nextPage()
            
    endRecord()
    exit()  # fecha o sketch!
    
def random_seed(s=None):
    from random import seed
    if s is None:
        s = int(random(100000))
    randomSeed(s)  # Processing random seed setup
    seed(s)  # Python random seed setup
    return s
