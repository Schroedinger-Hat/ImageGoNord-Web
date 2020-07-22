# -*- coding: utf-8 -*-

from PIL import Image
import os


def quantizetopalette(silf, palette, dither=False):
    global palettedata

    silf.load()

    palette.load()
    if palette.mode != "P":
        raise ValueError("bad mode for palette image")
    if silf.mode != "RGB" and silf.mode != "L":
        raise ValueError(
            "only RGB or L mode images can be quantized to a palette"
        )

    #im = silf.im.convert("P", 1 if dither else 0, palette.im)
    im2 = silf.convert("P", None, None, palette.im, 4)

    # Altro metodo
    im = silf.quantize(colors=int(len(palettedata) / 3),
                       method=None, kmeans=0, palette=palette)
    im.save("images/quantize.png")
    # retrocompatibilità per le 4.0 di pillow
    return im2


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

palimage = Image.new('P', (16, 16))
palimage.putpalette(palettedata * 16)
oldimage = Image.open("images/mountain.jpg")
newimage = quantizetopalette(oldimage, palimage, dither=False)
newimage.save('images/out.png')

