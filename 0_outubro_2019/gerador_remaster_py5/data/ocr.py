import pytesseract
import cairosvg
from PIL import Image

def extract_text(svg_file):
    with open(svg_file, 'r') as svg:
        svg_code = svg.read()

    png_file = svg_file.replace('.svg', '.png')
    cairosvg.svg2png(bytestring=svg_code, write_to=png_file)

    text = pytesseract.image_to_string(Image.open(png_file))
    return text

if __name__ == '__main__':
    text = extract_text('base_frente.svg')
    print(text)