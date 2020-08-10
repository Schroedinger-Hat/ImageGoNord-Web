# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter
# import os


class Palette:
    AURORA = "Aurora.txt"
    FROST = "Frost.txt"
    POLAR_NIGHT = "PolarNight.txt"
    SNOW_STORM = "SnowStorm.txt"


LOOKUP_PATH = "palettes/Nord/"
# directories = os.listdir(path)

USE_AVG_COLOR = True
USE_GAUSSIAN_BLUR = False
AVAILABLE_PALETTE = [
    Palette.POLAR_NIGHT,
    Palette.SNOW_STORM,
    Palette.FROST,
    Palette.AURORA
]


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


def color_difference(color1, color2):
    return sum([abs(component1-component2) for component1, component2 in zip(color1, color2)])


def get_avg_color(pixels, w=-2, h=3):
    average_sum = []
    for k in range(w, h):
        for l in range(w, h):
            try:
                average_sum.append(pixels[i+k, j+l])
                n += 1
            except:
                pass

    size = len(average_sum)
    r = 0
    g = 0
    b = 0
    for x in average_sum:
        r += x[0]
        g += x[1]
        b += x[2]

    return (r/size, g/size, b/size)


palettedata = {}
for palette in AVAILABLE_PALETTE:
    hex_colors = import_palette_from_file(LOOKUP_PATH + palette)
    for hex_color in hex_colors:
        palettedata[hex_color] = export_tripletes_from_color(hex_color)

oldimage = Image.open("images/valley.jpg")
pixels = oldimage.load()

for i in range(oldimage.size[0]):
    for j in range(oldimage.size[1]):
        color_to_check = pixels[i, j]
        if USE_AVG_COLOR == True:
            color_to_check = get_avg_color(pixels)

        differences = [[color_difference(color_to_check, target_value), target_name]
                       for target_name, target_value in palettedata.items()]
        differences.sort()
        pixels[i, j] = tuple(palettedata[differences[0][1]])

if USE_GAUSSIAN_BLUR == True:
    oldimage = oldimage.filter(ImageFilter.GaussianBlur(1))

oldimage.save('images/quantize.jpg')
