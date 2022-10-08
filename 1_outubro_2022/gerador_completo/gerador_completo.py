"""
Poster desenho() #1_outubro_2021 versão 191023a
https://desenho.lugaralgum.com (para licenças, créditos e agradecimentos!)
"""

from poster import poster
from elementos import grade

def setup():
    global frente, verso, semente, tiragem, f
    size(112, 159)  #1122 1587
    no_loop()
    
    #frente = load_shape('base_frente.svg')
    #verso = load_shape('base_poster.svg')
    """
    Aviso de erro quando tentei usar um VLW:
    Use createFont() instead of loadFont() when drawing text using the PDF library.
    """
    f = create_font('Inconsolata Bold', 18)  # precisa ter Inconsolata Bold instalada
    # seed "master" da tiragem (não incluso para tiragem > 1)
    semente = random_seed(191220)  
    tiragem = 1
    print(semente)

def draw():
    """
    Gerar PDF de múltiplas páginas e sair.
    (desencane de olhar que fica feio na tela, abra o PDF!)
    """
    global semente
    pdf = begin_record(PDF, "desenho0-{}-{}.pdf".format(semente, tiragem))
    print(pdf)
    for i in range(tiragem):
        if tiragem > 1:
            semente = random_seed()
        #shape(frente)
        y_grade = height - 31 - 321 / 2.
        x_grade = 25 + 321 / 2.
        rect_mode(CENTER)
        no_stroke()
        fill(200)
        rect(x_grade, y_grade, 321, 321)
        fill(0)
        grade(x_grade, y_grade, 6, 321, rnd_circ=True)
        pdf.next_page()
        #shape(verso)    
        largura_miolo = width - 110
        poster(width / 2, height - 55 - largura_miolo / 2, 6, largura_miolo)
        # fill(255, 0, 0) # vermelho para debug da posição
        text_font(f)
        text_size(10.5)
        fill(0)
        text('s = '+str(semente), 47, 333)
        print(i)
        if i < tiragem - 1:
            pdf.next_page()
            
    end_record()
    exit_sketch()  # fecha o sketch!
    
def random_seed(s=None):
    from random import seed
    if s is None:
        s = int(random(100000))
    random_seed(s)  # Processing random seed setup
    seed(s)  # Python random seed setup
    return s
