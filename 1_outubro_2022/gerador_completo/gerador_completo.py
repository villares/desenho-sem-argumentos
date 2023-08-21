"""
Poster desenho() #1_outubro_2021 versão 191023a
https://desenho.lugaralgum.com (para licenças, créditos e agradecimentos!)
"""

from poster_com_py5 import draw_nodes, generate

variante = '_pt' # '_en' or '_pt'

def setup():
    global frente, verso, semente, tiragem, f
    size(112, 159)  #1122 1587
    no_loop()
    
    if variante == '_pt':
        frente = load_shape('data/base_frente.svg')
        verso = load_shape('data/base_poster.svg')
    else:
        frente = load_shape(f'data/base_frente{variante}.svg')
        verso = load_shape(f'data/base_poster{variante}.svg')
        
    """
    Aviso de erro quando tentei usar um VLW:
    Use createFont() instead of loadFont() when drawing text using the PDF library.
    """
    f = create_font('Inconsolata Bold', 18)  # precisa ter Inconsolata Bold instalada
    # seed "master" da tiragem (não incluso para tiragem > 1)
    semente = random_seed(20220000)  
    tiragem = 1
    print(semente)

def draw():
    """
    Gerar PDF de múltiplas páginas e sair.
    (desencane de olhar que fica feio na tela, abra o PDF!)
    """
    global semente
    pdf = begin_record(PDF, "desenho1{}-{}-{}.pdf".format(variante, semente, tiragem))
    print(pdf)
    for i in range(tiragem):
        if tiragem > 1:
            semente = random_seed()
        shape(frente) 
        pdf.next_page()
        #shape(verso)    
        largura_miolo = width - 110
        #poster(width / 2, height - 55 - largura_miolo / 2, 6, largura_miolo)
        generate(semente)
        draw_nodes()
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
