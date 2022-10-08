"""
Poster desenho() #1_outubro_2021 versão 191023a
https://desenho.lugaralgum.com (para licenças, créditos e agradecimentos!)
"""
import py5

from poster import poster

def setup():
    global frente, verso, semente, tiragem, f
    py5.size(1122, 1587)  #1122 1587
    py5.no_loop()
    
    frente = py5.load_shape('base_frente.svg')
    verso = py5.load_shape('base_poster.svg')
    """
    Aviso de erro quando tentei usar um VLW:
    Use createFont() instead of loadFont() when drawing text using the PDF library.
    """
    f = py5.create_font('Inconsolata Bold', 18)  # precisa ter Inconsolata Bold instalada
    # seed "master" da tiragem (não incluso para tiragem > 1)
    semente = set_seed(191220)  
    tiragem = 1
    print(semente)

def draw():
    """
    Gerar PDF de múltiplas páginas e sair.
    (desencane de olhar que fica feio na tela, abra o PDF!)
    """
    global semente
    pdf = py5.begin_record(py5.PDF, "desenho0-{}-{}.pdf".format(semente, tiragem))
    print(pdf)
    for i in range(tiragem):
        if tiragem > 1:
            semente = set_seed()
        py5.shape(frente)
        y_grade = py5.height - 31 - 321 / 2.
        x_grade = 25 + 321 / 2.
        py5.rect_mode(py5.CENTER)
        py5.no_stroke()
        py5.fill(200)
        py5.rect(x_grade, y_grade, 321, 321)
        py5.fill(0)
        grade(x_grade, y_grade, 6, 321, rnd_circ=True)
        pdf.next_page()
        py5.shape(verso)    
        largura_miolo = py5.width - 110
        poster(py5.width / 2, py5.height - 55 - largura_miolo / 2, 6, largura_miolo)
        py5.fill(255, 0, 0) # vermelho para debug da posição
        py5.text_font(f)
        py5.text_size(10.5)
        py5.fill(0)
        py5.text('s = '+str(semente), 47, 333)
        
        if i < tiragem - 1:
            pdf.next_page()
            
    py5.end_record()
    #py5.exit_sketch()  # fecha o sketch!
    
def set_seed(s=None):
    from random import seed
    if s is None:
        s = int(random(100000))
    py5.random_seed(s)  # Processing random seed setup
    seed(s)  # Python random seed setup
    return s

def grade(x_centro, y_centro, n, tam_total, rnd_circ=False):
    tam = tam_total / n
    desloc = (tam - tam_total) / 2.
    for i in range(n):
        x = x_centro + desloc + tam * i
        for j in range(n):
            y =  y_centro + desloc + tam * j
            if rnd_circ:
                # no Processing random(inicio, final_ni)
                py5.circle(x, y, py5.random(tam * .1, tam * .9))
            else: 
                py5.square(x, y, tam * .75)

py5.run_sketch()