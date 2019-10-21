"""
Poster desenho() #0_outubro_2019
https://desenho.lugaralgum.com (para licenças, créditos e agradecimentos!)
"""

from __future__ import division
from random import choice, seed
from elementos import casinha, estrela, olho, grade
add_library('pdf')

def setup():
    size(1122, 1122)  # size(1122, 1587)
    print(random_seed(191019)) # use random_seed() para sortear uma seed!
    noLoop()

def draw():
    background(255)
    beginRecord(PDF, 'poster#####.pdf')
    rectMode(CENTER)
    strokeJoin(ROUND)
    poster(width / 2., height / 2., 6, width - 70)
    endRecord()

def poster(xo, yo, divisoes, largura_total, elemento=None):
    """
    Faça desenho do poster usando subdivisão recursiva
    """
    dim = largura_total / divisoes
    offset = (dim - largura_total) / 2
    for i in range(divisoes):
        x = xo + offset + dim * i
        for j in range(divisoes):
            y = yo + offset + dim * j
            seletor_elemento = choice((0, 1, 2, 3))
            if elemento is not None:  # elementos da grade
                desenha_elemento(x, y, dim, elemento)
            elif dim > 20 and random(10) < 8:  # pede subdivisão
                poster(x, y, 3, dim)
            elif 20 > dim > 15 and random(10) < 6:  # pede grade
                poster(x, y, 3, dim * 2, seletor_elemento + 2)
            else:  # pede um elemento "sozinho"
                desenha_elemento(x, y, dim, seletor_elemento)
    if divisoes == 6:  # uma vez só, para a grade-poster grande apenas
        w_olho = largura_total / 18  # tamanho do olho
        x_olho = random(w_olho, largura_total / 2)
        y_olho = random(largura_total / 2, largura_total - w_olho)
        fill(0)
        square(x_olho, y_olho, w_olho)
        olho(x_olho, y_olho, w_olho * .9)

def desenha_elemento(x, y, w, seletor):
    stroke(0)
    strokeWeight(.5)
    if seletor == 0:
        fill(0)
        num_pontas = choice((5, 7, 9))
        ra, rb = w * .35, choice((w * .25, w * .15, w * .075))
        estrela(x, y, num_pontas, ra, rb)
    elif seletor == 1:
        fill(0)
        casinha(x, y, w)
    elif seletor == 2:
        fill(255)
        casinha(x, y, w)
    elif seletor == 3 or seletor == 4:
        noFill()
        casinha(x, y, w)
    else:
        grade(x, y, 2, w)
        noFill()

def keyPressed():
    redraw()
    print(random_seed())

def random_seed(s=None):
    if s is None:
        s = int(random(100000))
    randomSeed(s)  # Processing random seed setup
    seed(s)  # Python random seed setup
    return 's = {}'.format(s)
