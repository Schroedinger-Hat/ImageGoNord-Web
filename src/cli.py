# -*- coding: utf-8 -*-
#! usr/bin/env python3
"""ImageGoNord, a converter for a rgb images to norththeme palette.
Usage: gonord [OPTION]...

Mandatory arguments to long options are mandatory for short options too.

Startup:
  -v,  --version                    display the version of Image Go Nord and exit

  -h,  --help                       print this help and exit

Logging:
  -q,  --quiet                      quiet (no output)

I/O Images:
  -i=FILE,  --img=FILE              specify input image name

  -o=FILE,  --out=FILE              specify output image name

Theme options:
  --PALETTE[=LIST_COLOR_SET]        the palette can be found on the src/palettes/
                                    directory (actually there is only nord), by
                                    replace the palette with the name is possible
                                    to select the theme and if necessary you can
                                    specify the set of colors you want to use.
                                    Ex: python src/cli.py --nord=aur,p,s is
                                    possible to pass the name of the color or
                                    the first character of the name set.

Conversion:

  -n, --no_average                  do not use the average pixels optimization
                                    algorithm on conversion 

  -p=INT, --pixel_area=INT          specify pixels of the area for average color
                                    calculation

  -b, --blur                        use blur on the final result [TODO]


Email bug reports, questions, discussions to <schrodinger.hat.show@gmail.com>
and/or open issues at https://github.com/Schrodinger-Hat/ImageGoNord/issues/new.
"""

import sys
import re
from os import path
from datetime import date

from utility.palette_loader import *

VERSION = open(path.dirname(path.realpath(__file__)) +
               "/VERSION", 'r').readline()
BLACK_REPLACE = "2E3440"
DEAFAULT_EXTENSION = ".png"
QUIET_MODE = False
OPT_ = False


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


def to_console(string):
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


def get_version():
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
    file_version = open(path.dirname(path.realpath(__file__)) + "/VERSION")
    return file_version.readline()


if __name__ == '__main__':
    args = sys.argv[1:]

    if len(args) == 0:
        print(__doc__)
        sys.exit(1)

    # If help given then print the docstring of the module and exit
    if "--help" in args or "-h" in args:
        print(__doc__)
        sys.exit(0)

    if "--version" in args or "-v" in args:
        print(VERSION)
        sys.exit(0)

    IMAGE_ARGUMENT_PATTERN = r'-[-img|i]=*'
    IS_IMAGE_PASSED = False
    for arg in args:
        searched_arg = re.search(IMAGE_ARGUMENT_PATTERN, arg)
        if searched_arg is not None:
            IS_IMAGE_PASSED = True
            break
    if not IS_IMAGE_PASSED:
        print("The image path must be given!")
        sys.exit(1)

    QUIET_MODE = "-q" in args or "--quiet" in args

    # Get absolute path of source project
    src_path = path.dirname(path.realpath(__file__))

    # Get all palettes created
    palettes = find_palettes(src_path + "/palettes")

    for arg in args:

        key_value = [kv for kv in arg.split("=", 1) if kv != ""]
        key = key_value[0].lower()

        condition_argument = key in ("--img" or "-i")
        IMAGE_PATTERN = r'([A-z]|[\/|\.|\-|\_|\s])*\.([a-z]{3}|[a-z]{4})$'
        if condition_argument:
            if len(key_value) > 1 and (re.search(IMAGE_PATTERN, key_value[1]) is not None):
                input_image = key_value[1]
                to_console("Load image {}".format(
                    src_path + "/" + input_image))
            else:
                to_console("You need to pass the image path!")
                sys.exit(1)
            continue

        condition_argument = key in ("--out" or "-o")
        if condition_argument:
            if len(key_value) > 1:
                output_image_name = key_value[1]
                # If the image name have already an extension do not set the default one
                output_image_name += "" if re.search(
                    IMAGE_PATTERN, output_image_name) else DEAFAULT_EXTENSION
                to_console("Output image {}".format(
                    src_path + "/" + output_image_name))
            else:
                to_console("No output filename specify within the arguments!")
            continue

        condition_argument = key in ("--no_average" or "-n")
        if condition_argument:
            if not len(key_value) > 1:
                no_average = True
                to_console("No average pixels selected!")
            else:
                to_console("No average pixels do not want any values!")
            continue

        condition_argument = key in ("--pixels_area" or "-p")
        if condition_argument:
            if len(key_value) > 1:
                try:
                    pixels = int(key_value[1])
                    to_console("The area in pixels is {}".format(pixels))
                except ValueError as value_error:
                    to_console("The area pixels must be a number value!")
                    sys.exit(1)
            else:
                to_console("To set the area pixels you must pass a number!")
            continue

        del condition_argument

        palettedata = []

        for palette in palettes:
            palette_path = src_path + "/palettes/" + palette.capitalize() + "/"

            if "--{}".format(palette) in key:

                if len(key_value) == 1:
                    to_console("Use all {} color set".format(
                        palette.capitalize()))
                    palette_set = load_palette_set(palette_path)
                    for colors_name in palette_set:
                        colors_palette = import_palette_from_file(
                            palette_path + colors_name + ".txt")
                        colors_set = create_data_colors(colors_palette)
                        palettedata.extend(colors_set)
                else:
                    to_console("Use {} palette".format(palette.capitalize()))
                    selected_colors = key_value[1].split(",")
                    palette_set = load_palette_set(palette_path)
                    for selected_color_set in selected_colors:
                        for colors_name in palette_set:
                            if is_colors_selected(selected_color_set, colors_name):
                                to_console("Selected {} as {}".format(
                                    selected_color_set, colors_name))
                                colors_palette = import_palette_from_file(
                                    palette_path + colors_name + ".txt")
                                colors_set = create_data_colors(colors_palette)
                                palettedata.extend(colors_set)
                    if len(palettedata) == 0:
                        to_console("No colors set correctly given!")
                        to_console("Exit!")

    sys.exit(0)

    # padding with black color | nordtheme palette is only 48
    # while len(palettedata) < 768:
    #    palettedata.extend(export_tripletes_from_color(BLACK_REPLACE))

    #palimage = Image.new('P', (1, 1))
    # palimage.putpalette(palettedata)
    #oldimage = Image.open("images/lui.jpg")
    #quantizetopalette(oldimage, palimage)
