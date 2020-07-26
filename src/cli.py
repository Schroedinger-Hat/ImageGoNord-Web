# -*- coding: utf-8 -*-
#! usr/bin/env python3
"""This is the example module.

This module does stuff.
"""

import sys
from signal import signal, SIGINT
from os import path

from utility.signaler import signal_handler
from utility.palette_loader import *

BLACK_REPLACE = '2E3440'


def is_colors_selected(selection, color_name):
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
    for index in range(len(selection)):
        if selection[index] != color_name[index].lower():
            return False
    return True


if __name__ == '__main__':
    signal(SIGINT, signal_handler)
    args = sys.argv[1:]

    # Get absolute path of source project
    src_path = path.dirname(path.realpath(__file__))

    # Get all palettes created
    palettes = find_palettes(src_path + "/palettes")

    for arg in args:

        key_value = arg.split("=")

        palettedata = []

        for palette in palettes:
            palette_path = src_path + "/palettes/" + palette.capitalize() + "/"
            if "--{}".format(palette) in key_value[0].lower():
                if len(key_value) == 1:
                    print("Use all {} color set".format(palette.capitalize()))
                    palette_set = load_palette_set(palette_path)
                    for colors_name in palette_set:
                        colors_palette = import_palette_from_file(
                            palette_path + colors_name + ".txt")
                        colors_set = create_data_colors(colors_palette)
                        palettedata.extend(colors_set)
                else:
                    print("Use {} palette".format(palette.capitalize()))
                    selected_colors = key_value[1].split(",")
                    palette_set = load_palette_set(palette_path)
                    for selected_color_set in selected_colors:
                        for colors_name in palette_set:
                            if is_colors_selected(selected_color_set, colors_name):
                                print("Selected {} as {}".format(
                                    selected_color_set, colors_name))
                                colors_palette = import_palette_from_file(
                                    palette_path + colors_name + ".txt")
                                colors_set = create_data_colors(colors_palette)
                                palettedata.extend(colors_set)
                    if len(palettedata) == 0:
                        print("No colors set correctly given!")
                        print("Exit!")

        if key_value[0].lower() == "--img" and len(key_value) > 1:
            input_image = key_value[1]
            print("Load image {}".format(src_path + "/" + input_image))

    sys.exit(0)

    # padding with black color | nordtheme palette is only 48
    while len(palettedata) < 768:
        palettedata.extend(export_tripletes_from_color(BLACK_REPLACE))
    
    palimage = Image.new('P', (1, 1))
    palimage.putpalette(palettedata)
    oldimage = Image.open("images/lui.jpg")
    quantizetopalette(oldimage, palimage)
