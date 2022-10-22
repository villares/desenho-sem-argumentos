add_library('pdf')
import random  # sample, shuffle, seed

nodes = {}
unvisited_nodes = []

EVN_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (1, -1))
ODD_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1,  1), (1,  1))

W = 25
H = W * sqrt(3) / 2  # sin(radians(60))
OX, OY = W / 2, H / 2  # deslocamento (offset)

def setup():
    global verso, tiragem, frente
    size(1122, 1587)
    generate(20220000)
    tiragem = 50
    f = createFont('Inconsolata Bold', 10)  # precisa ter Inconsolata Bold instalada
    noLoop()
    verso = loadShape('base_poster.svg')
    frente = loadShape('base_frente.svg')

def draw():
    pdf = createGraphics(int(width * 0.75), int(height * 0.75), PDF, "desenho0-{}-{}.pdf".format(rnd_seed, tiragem))
    beginRecord(pdf)
    noFill()
    for i in range(tiragem):
        pdf.scale(0.75)
        background(255)
        shape(frente)
        pdf.nextPage()
        pdf.scale(0.75)
        background(255)
        shape(verso)
        textSize(11)        
        text('generate({})'.format(rnd_seed), 52, 266)
        with pushMatrix():
            largura_miolo = width - 110
            translate(width / 2, height - 55 - largura_miolo / 2) 
            # fill(255, 0, 0)
            # circle(0, 0, 100)
            # noFill()
            for n, v in nodes.items():
                ia, ja, ka = n
                ib, jb, gen = v
                w = map(gen, 0, 50, 0, W)
                xa, ya = ij_to_xy(ia, ja)
                xb, yb = ij_to_xy(ib, jb)
                strokeWeight(min(abs(W / 30 + 3 - w / 5), 2))
                if gen < 50:
                    line(xa, ya, xb, yb)
                hexagon(xa, ya, w)
        if i < tiragem - 1:
            pdf.nextPage()
            global rnd_seed
            rnd_seed += 1
            generate(rnd_seed)

    
    endRecord()
    exit()

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
        limit = width / W / 2 - 1
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
    return (abs(x) < width / 2 - W * 4 and
            abs(y) < width / 2 - W * 4) # square

def hexagon(xo, yo, r):
    ang = TWO_PI / 6
    beginShape()  # começa a desenhar a forma
    for i in range(6):
            vertex(xo + cos(i * ang) * r,
                       yo + sin(i * ang) * r)
    endShape(CLOSE)

def keyPressed():
    if key == ' ':
        generate(frameCount)
        redraw()
    elif key == 'a':
        add_starting_points()
    elif key == 's':
        save_frame('{}.png'.format(rnd_seed))
