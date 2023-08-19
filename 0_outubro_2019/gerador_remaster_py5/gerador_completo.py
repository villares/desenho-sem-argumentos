"""
Poster desenho() #0_outubro_2019 versão 20230813
https://desenho.lugaralgum.com (para licenças, créditos e agradecimentos!)
"""

from poster import poster
from elementos import grade

def setup():
    global frente, verso, semente, tiragem, f
    size(1122, 1587)
    no_loop()
    
    
    frente = load_shape('base_frente.svg')
    verso = load_shape('base_poster_en.svg')
    """
    Aviso de erro quando tentei usar um VLW:
    Use createFont() instead of loadFont() when drawing text using the PDF library.
    """
    f = create_font('Inconsolata Bold', 18)  # precisa ter Inconsolata Bold instalada
    # 20 com 191220
    # 10 com 191020; 100 com 191021; 100 com 191022;
    # 01 com 191929 (amostra); 1 com 191110;
    # 10 com 191111.
    # seed "master" da tiragem (não incluso para tiragem > 1)
    semente = random_seeds(191220)  
    tiragem = 1

def draw():
    """
    Gerar PDF de múltiplas páginas e sair.
    (desencane de olhar que fica feio na tela, abra o PDF!)
    """
    global semente
    pdf = begin_record(PDF, "desenho0-{}-{}.pdf".format(semente, tiragem))
    
    for i in range(tiragem):
        if tiragem > 1:
            semente = random_seeds()
        shape(frente)
        y_grade = height - 31 - 321 / 2.
        x_grade = 25 + 321 / 2.
        rect_mode(CENTER)
        no_stroke()
        fill(200)
        rect(x_grade, y_grade, 321, 321)
        fill(0)
        grade(x_grade, y_grade, 6, 321, rnd_circ=True)
        pdf.next_page()
        shape(verso)    
        largura_miolo = width - 110
        poster(width / 2, height - 55 - largura_miolo / 2, 6, largura_miolo)
        text_font(f)
        text_size(11)
        # fill(255, 0, 0)  # vermelho para debug da posição
        text('s = '+str(semente), 48, 333)
        if i < tiragem - 1:
            pdf.next_page()
            
    end_record()
    exit_sketch()  # fecha o sketch!
    
def random_seeds(s=None):
    from random import seed
    if s is None:
        s = int(random(100000))
    random_seed(s)  # Processing random seed setup
    seed(s)  # Python random seed setup
    return s
