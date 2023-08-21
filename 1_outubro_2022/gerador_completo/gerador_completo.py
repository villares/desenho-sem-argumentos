"""
Poster desenho() #1_outubro_2021 versão 191023a
https://desenho.lugaralgum.com (para licenças, créditos e agradecimentos!)
"""

import random  # sample, shuffle, seed
import py5
#from poster_com_py5 import draw_nodes, generate

nodes = {}
unvisited_nodes = []

EVN_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (1, -1))
ODD_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1,  1), (1,  1))

W = 25
H = W * py5.sqrt(3) / 2  # sin(radians(60))
OX, OY = W / 2, H / 2  # deslocamento (offset)

variante = '_pt'  # '_en' or '_pt'
rnd_seed = 20220000

def setup():
    global verso, tiragem, frente
    py5.size(1122, 1587)
    generate(rnd_seed)
    tiragem = 1
    # precisa ter Inconsolata Bold instalada
    f = py5.create_font('Inconsolata Bold', 10)
    py5.no_loop()
    if variante == '_pt':
        frente = py5.load_shape('data/base_frente.svg')
        verso = py5.load_shape('data/base_poster.svg')
    else:
        frente = py5.load_shape(f'data/base_frente{variante}.svg')
        verso = py5.load_shape(f'data/base_poster{variante}.svg')


def draw():
    global rnd_seed
    pdf = py5.create_graphics(int(py5.width * 0.75), int(py5.height * 0.75),
                              py5.PDF, "desenho1{}-{}-{}.pdf".
                              format(variante, rnd_seed, tiragem))
    py5.begin_record(pdf)
    py5.no_fill()
    for i in range(tiragem):
        pdf.scale(0.75)
        py5.background(255)
        py5.shape(frente)
        pdf.next_page()
        pdf.scale(0.75)
        py5.background(255)
        py5.shape(verso)
        py5.text_size(11)
        py5.text('generate({})'.format(rnd_seed), 52, 266)
        with py5.push_matrix():
            largura_miolo = py5.width - 110
            py5.translate(py5.width / 2, py5.height - 55 - largura_miolo / 2)
            # fill(255, 0, 0)
            # circle(0, 0, 100)
            # noFill()
            for n, v in nodes.items():
                ia, ja, ka = n
                ib, jb, gen = v
                w = py5.remap(gen, 0, 50, 0, W)
                xa, ya = ij_to_xy(ia, ja)
                xb, yb = ij_to_xy(ib, jb)
                py5.stroke_weight(min(abs(W / 30 + 3 - w / 5), 2))
                if gen < 50:
                    py5.line(xa, ya, xb, yb)
                hexagon(xa, ya, w)
        if i < tiragem - 1:
            pdf.next_page()
            rnd_seed += 1
            generate(rnd_seed)

    py5.end_record()
    py5.exit_sketch()


def generate(s):
    global rnd_seed
    rnd_seed = s
    random.seed(s)
    print('seed: {}'.format(s))
    nodes.clear()
    unvisited_nodes[:] = []
    add_starting_points()
    previous_len_nodes = -1
    while previous_len_nodes != len(nodes):
        previous_len_nodes = len(nodes)
        unvisited_nodes[:] = grow()


def add_starting_points():
    for k in range(4):
        limit = py5.width // W // 2 - 1
        i = random.randint(-limit, limit)
        j = random.randint(-limit, limit)
        nodes[(i, j, k % 2)] = (i, j, 0)
        unvisited_nodes.append((i, j, k % 2))


def grow():
    for i, j, k in unvisited_nodes:
        nbs = EVN_NBS if i % 2 == 0 else ODD_NBS
        _, _, gen = nodes[(i, j, k)]
        random.seed(k + gen // 10)
        xnbs = random.sample(nbs, 3)
        random.shuffle(xnbs)
        for ni, nj in xnbs:
            ini, jnj = i + ni, j + nj
            if (ini, jnj, k) not in nodes and visible(ini, jnj):
                nodes[(ini, jnj, k)] = (i, j, gen + 1)
                yield ini, jnj, k


def ij_to_xy(i, j):
    y = j * H + OY if i % 2 == 0 else j * H + H / 2 + OY
    x = i * W * 3 / 4 + OX
    return x, y


def visible(i, j):
    x, y = ij_to_xy(i, j)
    return (abs(x) < py5.width / 2 - W * 4 and
            abs(y) < py5.width / 2 - W * 4)  # square


def hexagon(xo, yo, r):
    ang = py5.TWO_PI / 6
    py5.begin_shape()  # começa a desenhar a forma
    for i in range(6):
        py5.vertex(xo + py5.cos(i * ang) * r,
                   yo + py5.sin(i * ang) * r)
    py5.end_shape(py5.CLOSE)


def key_pressed():
    if py5.key == ' ':
        generate(py5.frame_count)
        py5.redraw()
    elif py5.key == 'a':
        add_starting_points()
    elif py5.key == 's':
        py5.save_frame('{}.png'.format(rnd_seed))


py5.run_sketch()
