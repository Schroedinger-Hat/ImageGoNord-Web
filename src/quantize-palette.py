# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter
import os


def quantizetopalette(silf, palette):
    global palettedata

    silf.load()

    palette.load()
    if palette.mode != "P":
        raise ValueError("bad mode for palette image")
    if silf.mode != "RGB" and silf.mode != "L":
        raise ValueError(
            "only RGB or L mode images can be quantized to a palette"
        )

    # color quantize, mode P
    im = silf.quantize(colors=256, method=0, kmeans=5, palette=palette)
    # convert again from P mode to RGB
    im = im.convert('RGB')
    # reduce rumor noise by applying a blur
    im = im.filter(ImageFilter.GaussianBlur(1))
    # save
    im.save("images/quantize.jpg")

    return im


def export_tripletes_from_color(hex_color):
    hex_triplets = [hex_color[i:i+2] for i in range(0, len(hex_color), 2)]
    triplets_integer = [int(hex_triplets[i], 16)
                        for i in range(len(hex_triplets))]
    return triplets_integer


def import_palette_from_file(filename):
    f = open(filename, "r")
    palette = [line.replace('#', '').replace('\n', '')
               for line in f.readlines()]
    palette.remove('')
    return palette


def create_palette_data(palette):
    data = []
    for color in palette:
        data.extend((export_tripletes_from_color(color)))
    return data

def color_difference (color1, color2):
    return sum([abs(component1-component2) for component1, component2 in zip(color1, color2)])

path = "palettes/Nord/"
directories = os.listdir(path)

palettedata = {}
for palette in directories:
  hex_colors = import_palette_from_file(path+palette)
  for hex_color in hex_colors:
    palettedata[hex_color] = export_tripletes_from_color(hex_color)

# padding with black color | nordtheme palette is only 48
# while len(palettedata) < 768:
#   palettedata.extend(export_tripletes_from_color('2E3440'))

# palimage = Image.new('P', (1, 1))
# palimage.putpalette(palettedata)
oldimage = Image.open("images/crazy.jpeg")
pixels = oldimage.load()

for i in range(oldimage.size[0]):    # for every col:
  for j in range(oldimage.size[1]):    # For every row
    differences = [[color_difference(pixels[i, j], target_value), target_name] for target_name, target_value in palettedata.items()]
    differences.sort()  # sorted by the first element of inner lists
    my_color_name = differences[0][1]
    pixels[i, j] = tuple(palettedata[my_color_name])

oldimage.save('images/quantize.jpg')
# quantizetopalette(oldimage, palimage)

