# -*- coding: utf-8 -*-
#! usr/bin/env python3
"""This is the example module.

This module does stuff.
"""

import sys
from os import path
from signal import signal, SIGINT
from utility.palette_loader import find_palette, load_palette_set
from PIL import Image, ImageFilter


def quantizetopalette(silf, palette):
    """<Short Description>

      <Description>

    Parameters
    ----------
    <argument name>: <type>
      <argument description>
    <argument>: <type>
      <argument description>

    Returns
    -------
    <type>
      <description>
    """
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
    """<Short Description>

      <Description>

    Parameters
    ----------
    <argument name>: <type>
      <argument description>
    <argument>: <type>
      <argument description>

    Returns
    -------
    <type>
      <description>
    """
    hex_triplets = [hex_color[i:i+2] for i in range(0, len(hex_color), 2)]
    triplets_integer = [int(hex_triplets[i], 16)
                        for i in range(len(hex_triplets))]
    return triplets_integer


def import_palette_from_file(filename):
    """<Short Description>

      <Description>

    Parameters
    ----------
    <argument name>: <type>
      <argument description>
    <argument>: <type>
      <argument description>

    Returns
    -------
    <type>
      <description>
    """
    f = open(filename, "r")
    palette = [line.replace('#', '').replace('\n', '')
               for line in f.readlines()]
    palette.remove('')
    return palette


def create_palette_data(palette):
    """<Short Description>

      <Description>

    Parameters
    ----------
    <argument name>: <type>
      <argument description>
    <argument>: <type>
      <argument description>

    Returns
    -------
    <type>
      <description>
    """
    data = []
    for color in palette:
        data.extend((export_tripletes_from_color(color)))
    return data


def signal_handler(self, sig, frame):
    """This method is used to define how the script handle the interruption.
    May use to stop some thread or destroy objects.
    Parameters
    ----------
    sig :
        The type of the signal
    frame :
        The frame argument is the stack frame, also known as execution frame. It point to the frame that was interrupted by the signal.
        The parameter is required because any thread might be interrupted by a signal, but the signal is only received in the main thread.
    Returns
    -------
    None
    """
    print("\nExit!")
    sys.exit(0)


if __name__ == '__main__':
    signal(SIGINT, signal_handler)
    args = sys.argv[1:]

    # Get absolute path of source
    path = path.dirname(path.realpath(__file__))

    # Get all palettes created
    palettes = find_palette(path + "/palettes")

    for arg in args:

        # list_palette = load_palette(path)

        key_value = arg.split("=")

        palettedata = []

        for palette in palettes:
            if "--{}".format(palette) in key_value[0].lower():
                if len(key_value) == 1:
                    print("Use all {} color set".format(palette.capitalize()))
                    palette_path = path + "/palettes/" + palette.capitalize() + "/"
                    palette_set = load_palette_set(palette_path)
                    for colors in palette_set:
                        palettedata.extend(create_palette_data(
                            import_palette_from_file(palette_path + colors + ".txt")))
                else:
                    print("TODO")

        print(palettedata)

        sys.exit(0)

        if not is_all:
            for palette in list_palette:
                if '--' + palette.lower() in key_value[0]:
                    print("Use {} color set".format(palette))
                    palettedata.extend(create_palette_data(
                        import_palette_from_file(path+palette)))

    sys.exit(0)

   # padding with black color | nordtheme palette is only 48
while len(palettedata) < 768:
    palettedata.extend(export_tripletes_from_color('2E3440'))

palimage = Image.new('P', (1, 1))
palimage.putpalette(palettedata)
oldimage = Image.open("images/lui.jpg")
quantizetopalette(oldimage, palimage)
