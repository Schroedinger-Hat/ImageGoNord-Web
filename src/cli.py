#!usr/bin/env python3
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

import argparse
import re
import sys
from os import path, listdir
from pathlib import Path

from ImageGoNord import GoNord

from configs import arguments as confarg
from configs import messages


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
    return Path(path.dirname(path.realpath(__file__)) + "/VERSION").read_text()


DEFAULT_EXTENSION = ".png"
DEFAULT_FILENAME = f'out.{DEFAULT_EXTENSION}'

QUIET_MODE = False
OUTPUT_IMAGE_NAME = "nord" + DEFAULT_EXTENSION
PALETTE_CHANGED = False
VERSION = get_version()


class SplitDimensions(argparse.Action):
    def __call__(self, parser, namespace, sizes, option_string=None):
        dimensions = [value.strip() for value in sizes.split(",")]
        dimensions = [*dimensions, *dimensions] if len(dimensions) == 1 else dimensions
        setattr(namespace, self.dest, dimensions)


ap = argparse.ArgumentParser(prog='ImageGoNord',
                             description="ImageGoNord, a converter for a rgb images to norththeme palette.")

ap.add_argument('-q', '--quiet', action='store_true')
ap.add_argument('-v', '--version', action='version', version=f'%(prog)s {get_version()}')

ap.add_argument('-i', '--img', type=str, metavar='<path>',
                help='specify input image path')

ap.add_argument('-o', '--out', type=str, metavar='<path>', default=DEFAULT_FILENAME,
                help='specify output image path')

ap.add_argument('-na', '--no-avg', action='store_true',
                help='disable average pixels optimization algorithm on conversion')

ap.add_argument('-pa', '--pixels-area', action=SplitDimensions,
                help='disable average pixels optimization algorithm on conversion')

ap.add_argument('-b', '--blur', action='store_true',
                help='use blur on the final result')


def to_console(*params):
    if QUIET_MODE:
        return

    for param in params:
        print(param)


if __name__ == '__main__':
    args = sys.argv[1:]
    parsed_args = ap.parse_args()

    print(parsed_args)
    QUIET_MODE = parsed_args.quiet

    if not parsed_args.img:
        ap.error(
            messages.logs['img']['error'].format(parsed_args.img)
            + messages.logs['general_error']
        )

    if not parsed_args.out:
        ap.error(
            messages.logs['out']['error'].format(parsed_args.out)
            + messages.logs['general_error']
        )

    # If help given then print the docstring of the module and exit
    go_nord = GoNord()

    # Get absolute path of source project
    absolute_path = path.dirname(path.realpath(__file__))

    # Get all palettes created
    palettes = [palette.lower() for palette in listdir(absolute_path + "/palettes")]

    # Reading input image
    image = go_nord.open_image(parsed_args.img)
    to_console(messages.logs["img"]['info'].format(absolute_path + "/" + parsed_args.img))

    # Setting output
    IMAGE_PATTERN = r'([A-z]|[\/|\.|\-|\_|\s])*\.([a-z]{3}|[a-z]{4})$'
    OUTPUT_IMAGE_NAME += "" if re.search(IMAGE_PATTERN, parsed_args.out) else DEFAULT_EXTENSION
    to_console(messages.logs["out"]['info'].format(absolute_path + "/" + OUTPUT_IMAGE_NAME))

    # Enable/disable avg algoritm
    if parsed_args.no_avg:
        go_nord.disable_avg_algorithm()
        to_console(messages.logs["navg"]['info'])

    # Select pixel area
    if parsed_args.dimensions:
        (w, h) = parsed_args.dimensions
        go_nord.set_avg_box_data(w=w, h=h)

    if parsed_args.blur:
        go_nord.disable_gaussian_blur()

    for arg in args:
        key_value = [kv for kv in arg.split("=", 1) if kv != ""]
        key = key_value[0].lower()

        for palette in palettes:
            if "--{}".format(palette) in key:
                palette_path = absolute_path + "/palettes/" + palette.capitalize() + "/"
                go_nord.set_palette_lookup_path(palette_path)
                if len(key_value) > 1:
                    go_nord.reset_palette()
                    palette_set = [palette_file.replace(".txt", '') for palette_file in listdir(palette_path)]
                    selected_colors = [selected_color.lower() for selected_color in key_value[1].split(",")]
                    to_console(confarg.logs["pals"][1].format(palette.capitalize()))
                    for selected_color in selected_colors:
                        lowered_palette = list(map(str.lower, palette_set))
                        if selected_color in lowered_palette:
                            index_color = lowered_palette.index(selected_color)
                            go_nord.add_file_to_palette(palette_set[index_color] + ".txt")
                            to_console(confarg.logs["pals"][2].format(palette_set[index_color]))
                            PALETTE_CHANGED = True
                        else:
                            to_console(confarg.logs["pals"][-1].format(selected_color))
                    for palette_color in palette_set:
                        if palette_color.lower() not in selected_colors:
                            to_console(confarg.logs["pals"][3].format(palette_color))
                else:
                    PALETTE_CHANGED = True
                    to_console(confarg.logs["pals"][0].format(palette.capitalize()))
                    palette_path = absolute_path + "/palettes/" + palette.capitalize() + "/"
                    go_nord.reset_palette()
                    palette_set = [palette_file.replace(".txt", '') for palette_file in listdir(palette_path)]
                    go_nord.set_palette_lookup_path(palette_path)
                    for palette_color in palette_set:
                        go_nord.add_file_to_palette(palette_color + ".txt")

    if not PALETTE_CHANGED:
        to_console(confarg.logs["pals"][4])
        palette_path = absolute_path + "/palettes/Nord/"
        go_nord.reset_palette()
        palette_set = [palette_file.replace(".txt", '') for palette_file in listdir(palette_path)]
        go_nord.set_palette_lookup_path(palette_path)
        for palette_color in palette_set:
            go_nord.add_file_to_palette(palette_color + ".txt")

    quantize_image = go_nord.convert_image(image, save_path=OUTPUT_IMAGE_NAME)
    sys.exit(0)
