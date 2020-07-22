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


path = "palettes/Nord/"
directories = os.listdir(path)

palettedata = []
for palette in directories:
  palettedata.extend(create_palette_data(import_palette_from_file(path+palette)))

# padding with black color | nordtheme palette is only 48
while len(palettedata) < 768:
  palettedata.extend(export_tripletes_from_color('2E3440'))

palimage = Image.new('P', (1, 1))
palimage.putpalette(palettedata)
oldimage = Image.open("images/ig.jpg")
quantizetopalette(oldimage, palimage)

