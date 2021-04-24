# -*- coding: utf-8 -*-
#! usr/bin/env python3
"""ImageGoNord, a converter for a rgb images to norththeme palette.
Usage: gonord [OPTION]...

Mandatory arguments to long options are mandatory for short options too.

Startup:
  -h,  --help                       print this help and exit

  -v,  --version                    display the version of Image Go Nord and
                                    exit

Logging:
  -q,  --quiet                      quiet (no output)

I/O Images:
  -i=FILE,  --img=FILE              specify input image name

  -o=FILE,  --out=FILE              specify output image name

Theme options:
  --PALETTE[=LIST_COLOR_SET]        the palette can be found on the
                                    src/palettes/ directory (actually there is
                                    only nord), by replace the palette with the
                                    name is possible to select the theme and if
                                    necessary you can specify the set of colors
                                    you want to use.
                                    Ex: python src/cli.py --nord=aur,p,s is
                                    possible to pass the name of the color or
                                    the first character of the name set.

Conversion:

  -na, --no-avg                     do not use the average pixels optimization
                                    algorithm on conversion

  -pa=INT,INT, --pixel-area=INT,INT specify pixels of the area for average
                                    color calculation

  -b, --blur                        use blur on the final result


Email bug reports, questions, discussions to <schrodinger.hat.show@gmail.com>
and/or open issues at https://github.com/Schrodinger-Hat/ImageGoNord/issues/new
"""

import sys
import re
from os import path, listdir
from ImageGoNord import GoNord

import configs.arguments as confarg

VERSION = open(path.dirname(path.realpath(__file__)) +
               "/VERSION", 'r').readline()
DEFAULT_EXTENSION = ".png"
QUIET_MODE = False
OUTPUT_IMAGE_NAME = "nord" + DEFAULT_EXTENSION
PALETTE_CHANGED = False


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

    go_nord = GoNord()

    IMAGE_ARGUMENT_PATTERN = r'-(-img|i)=*'
    IS_IMAGE_PASSED = False
    for arg in args:
        searched_arg = re.search(IMAGE_ARGUMENT_PATTERN, arg)
        if searched_arg is not None:
            IS_IMAGE_PASSED = True
            break
    if not IS_IMAGE_PASSED:
        to_console(confarg.logs["img"][1].format(arg))
        to_console(confarg.logs["img"][-1])
        to_console(confarg.logs["err"][0])
        sys.exit(1)

    QUIET_MODE = "-q" in args or "--quiet" in args

    # Get absolute path of source project
    src_path = path.dirname(path.realpath(__file__))

    # Get all palettes created
    palettes = [palette.lower() for palette in listdir(src_path + "/palettes")]

    for arg in args:

        key_value = [kv for kv in arg.split("=", 1) if kv != ""]
        key = key_value[0].lower()

        condition_argument = key in ["--img", "-i"]
        IMAGE_PATTERN = r'([A-z]|[\/|\.|\-|\_|\s])*\.([a-z]{3}|[a-z]{4})$'
        if condition_argument:
            if (len(key_value) > 1 and
                    re.search(IMAGE_PATTERN, key_value[1]) is not None):
                image = go_nord.open_image(key_value[1])
                to_console(confarg.logs["img"][0].format(
                    src_path + "/" + key_value[1]))
            else:
                to_console(confarg.logs["img"][1].format(arg))
                to_console(confarg.logs["img"][-1])
                to_console(confarg.logs["err"][0])
                sys.exit(1)
            continue

        condition_argument = key in ["--out", "-o"]
        if condition_argument:
            if len(key_value) > 1:
                OUTPUT_IMAGE_NAME = key_value[1]
                # If the image name have already an extension do not set the
                # default one
                OUTPUT_IMAGE_NAME += "" if re.search(
                    IMAGE_PATTERN, OUTPUT_IMAGE_NAME) else DEFAULT_EXTENSION
                to_console(confarg.logs["out"][0].format(
                    src_path + "/" + OUTPUT_IMAGE_NAME))
            else:
                to_console(confarg.logs["out"][1].format(arg))
                to_console(confarg.logs["out"][-1])
                to_console(confarg.logs["err"][0])
                sys.exit(1)
            continue

        condition_argument = key in ["--no-avg", "-na"]
        if condition_argument:
            if len(key_value) > 1:
                to_console(confarg.logs["navg"][1].format(arg))
                to_console(confarg.logs["navg"][-1])
                to_console(confarg.logs["err"][0])
                sys.exit(1)
            else:
                go_nord.disable_avg_algorithm()
                to_console(confarg.logs["navg"][0])
            continue

        condition_argument = key in ["-pa", "--pixels-area"]
        if condition_argument:
            try:
                area_value = key_value[1].split(",")
                try:
                    go_nord.set_avg_box_data(w=area_value[0], h=area_value[1])
                    to_console(confarg.logs["pxls"][0].format(area_value[0]))
                    to_console(confarg.logs["pxls"][1].format(area_value[1]))
                except IndexError:
                    go_nord.set_avg_box_data(w=area_value[0], h=area_value[0])
                    to_console(confarg.logs["pxls"][0].format(area_value[0]))
                    to_console(confarg.logs["pxls"][1].format(area_value[0]))
            except IndexError:
                to_console(confarg.logs["pxls"][-2].format(arg))
                to_console(confarg.logs["pxls"][-1])
                to_console(confarg.logs["err"][0])
                sys.exit(1)

        condition_argument = key in ["--blur", "-b"]
        if condition_argument:
            if len(key_value) > 1:
                to_console(confarg.logs["blur"][-2].format(arg))
                to_console(confarg.logs["blur"][-1])
                to_console(confarg.logs["err"][0])
                sys.exit(1)
            else:
                go_nord.enable_gaussian_blur()
                to_console(confarg.logs["blur"][0])
            continue
        del condition_argument

        for palette in palettes:
            if "--{}".format(palette) in key:
                PALETTE_CHANGED = True
                palette_path = src_path + "/palettes/" + palette.capitalize() + "/"
                go_nord.set_palette_lookup_path(palette_path)
                if len(key_value) > 1:
                    go_nord.reset_palette()
                    palette_set = [palette_file.replace(".txt", '')
                                   for palette_file in listdir(palette_path)]
                    selected_colors = key_value[1].split(",")
                    to_console(confarg.logs["pals"][1]
                               .format(palette.capitalize()))
                    for selected_color in selected_colors:
                        if selected_color in palette_set:
                            go_nord.add_file_to_palette(
                                selected_color + ".txt")
                            to_console(confarg.logs["pals"][2]
                                       .format(selected_color))
                        else:
                            to_console(confarg.logs["pals"][-1]
                                       .format(selected_color))
                    for palette_color in palette_set:
                        if palette_color not in selected_colors:
                            to_console(confarg.logs["pals"][3]
                                       .format(palette_color))
                else:
                    to_console(confarg.logs["pals"][0]
                               .format(palette.capitalize()))

    if not PALETTE_CHANGED:
        to_console(confarg.logs["pals"][4])
        palette_path = src_path + "/palettes/Nord/"
        go_nord.reset_palette()
        palette_set = [palette_file.replace(".txt", '')
                       for palette_file in listdir(palette_path)]
        go_nord.set_palette_lookup_path(palette_path)
        for palette_color in palette_set:
            go_nord.add_file_to_palette(
                palette_color + ".txt")

    quantize_image = go_nord.convert_image(
        image,
        save_path=OUTPUT_IMAGE_NAME)
    sys.exit(0)
