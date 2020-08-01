# -*- coding: utf-8 -*-
#! usr/bin/env python3
"""ImageGoNord, a converter for a rgb images to norththeme palette.
Usage: gonord [OPTION]...

Mandatory arguments to long options are mandatory for short options too.

Startup:
  -V,  --version                    display the version of Image Go Nord and exit [TODO]
  -h,  --help                       print this help and exit

Logging:
  -q,  --quiet                      quiet (no output)

  -l=FILE,  --log=FILE              create a log file [TODO]

I/O Images:
  -i,  --img=FILE                   specify input image name [TODO]
  -o,  --out=FILE                   specify output image name [TODO]

  -o=FILE,  --out=FILE              specify output image name

Theme options:
       --PALETTE[=LIST_COLOR_SET]   the palette can be found on the src/palettes/
                                    directory (actually there is only nord), by
                                    replace the palette with the name is possible
                                    to select the theme and if necessary you can
                                    specify the set of colors you want to use.
                                    Ex: python src/cli.py --nord=aur,p,s is
                                    possible to pass the name of the color or
                                    the first character of the name set.
       --img=<image_source>         simply put the local path of the image you
                                    want to convert
                                    

                                    Tra le altre cose sono da prevedere dei parametri extra per determinare alcune variabili di editing, come:

utilizzo SI | NO dell'algoritmo di conversione ottimizzato con la media pixel
area pixel da considerare per il calcolo del colore medio
utilizzo di blur nel risultato finale SI | NO

Email bug reports, questions, discussions to <schrodinger.hat.show@gmail.com>
and/or open issues at https://github.com/Schrodinger-Hat/ImageGoNord/issues/new.
"""

import sys
from signal import signal, SIGINT
from os import path

from utility.signaler import signal_handler
from utility.palette_loader import *

BLACK_REPLACE = "2E3440"
DEFAULT_EX = ".png"
QUIET_MODE = False


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


def log(string):
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
    if QUIET_MODE:
        return
    print(string)


if __name__ == '__main__':
    signal(SIGINT, signal_handler)
    args = sys.argv[1:]

    if len(args) == 0:
        print(__doc__)
        sys.exit(1)

    # If help given then print the docstring of the module and exit
    if "--help" in args:
        print(__doc__)
        sys.exit(0)

    QUIET_MODE = "-q" in args or "--quiet" in args

    # Get absolute path of source project
    src_path = path.dirname(path.realpath(__file__))

    # Get all palettes created
    palettes = find_palettes(src_path + "/palettes")

    for arg in args:

        key_value = [kv for kv in arg.split("=", 1) if kv != ""]
        key = key_value[0].lower()

        palettedata = []

        for palette in palettes:
            palette_path = src_path + "/palettes/" + palette.capitalize() + "/"
            if "--{}".format(palette) in key_value[0].lower():
                if len(key_value) == 1:
                    log("Use all {} color set".format(palette.capitalize()))
                    palette_set = load_palette_set(palette_path)
                    for colors_name in palette_set:
                        colors_palette = import_palette_from_file(
                            palette_path + colors_name + ".txt")
                        colors_set = create_data_colors(colors_palette)
                        palettedata.extend(colors_set)
                else:
                    log("Use {} palette".format(palette.capitalize()))
                    selected_colors = key_value[1].split(",")
                    palette_set = load_palette_set(palette_path)
                    for selected_color_set in selected_colors:
                        for colors_name in palette_set:
                            if is_colors_selected(selected_color_set, colors_name):
                                log("Selected {} as {}".format(
                                    selected_color_set, colors_name))
                                colors_palette = import_palette_from_file(
                                    palette_path + colors_name + ".txt")
                                colors_set = create_data_colors(colors_palette)
                                palettedata.extend(colors_set)
                    if len(palettedata) == 0:
                        log("No colors set correctly given!")
                        log("Exit!")

        is_image = key in ("--img" or "-i")
        IMAGE_PATTERN = r'([A-z]|[\/|\.|\-|\_|\s])*\.([a-z]{3}|[a-z]{4})$'
        if is_image:
            if len(key_value) > 1 and (re.search(IMAGE_PATTERN, key_value[1]) is not None):
                input_image = key_value[1]
                log("Load image {}".format(src_path + "/" + input_image))
            else:
                log("You need to pass the image path!")
                sys.exit(1)
            continue
        del is_image

        is_output_file_name = key in ("--out" or "-o")
        if is_output_file_name:
            if len(key_value) > 1:
                output_image_name = key_value[1]
                # If the image name have already an extension do not set the default one
                output_image_name += "" if re.search(
                    IMAGE_PATTERN, output_image_name) else DEFAULT_EX
                log("Output image {}".format(
                    src_path + "/" + output_image_name))
            else:
                log("No output filename specify within the arguments!")
            continue

    sys.exit(0)

    # padding with black color | nordtheme palette is only 48
    while len(palettedata) < 768:
        palettedata.extend(export_tripletes_from_color(BLACK_REPLACE))

    palimage = Image.new('P', (1, 1))
    palimage.putpalette(palettedata)
    oldimage = Image.open("images/lui.jpg")
    quantizetopalette(oldimage, palimage)
