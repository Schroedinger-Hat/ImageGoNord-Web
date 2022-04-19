#!usr/bin/env python3
"""
ImageGoNord, a converter for a rgb images to norththeme palette.
Usage: gonord [OPTION]...

Mandatory arguments to long options are mandatory for short options too.

Startup:
  -h, --help                       print this help and exit
  -v, --version                    display the version of Image Go Nord and exit

Logging:
  -q, --quiet                      quiet (no output)

I/O Images:
  -i=FILE, --img=FILE              specify input image name
  -o=FILE, --out=FILE              specify output image name

Theme options:
  --PALETTE[=LIST_COLOR_SET]        the palette can be found on the
                                    src/palettes/ directory by replace the palette
                                     with the name is possible to select the theme
                                     and if necessary you can specify the set of
                                     colors you want to use.
                                     Ex: python src/cli.py --nord=aur,p,s
                                     is possible to pass the name of the color
                                     or the first character of the name set.

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
import sys
from os import path, listdir
from pathlib import Path

from ImageGoNord import GoNord

from configs import arguments as confarg
from configs import messages

ABSOLUTE_PATH = path.dirname(path.realpath(__file__))

DEFAULT_EXTENSION = ".png"
DEFAULT_FILENAME = f'out.{DEFAULT_EXTENSION}'

QUIET_MODE = False
OUTPUT_IMAGE_PATH = "nord" + DEFAULT_EXTENSION
PALETTE_CHANGED = False
VERSION = Path(ABSOLUTE_PATH + "/VERSION").read_text()


class SplitCommaSeparatedArguments(argparse.Action):
    def __call__(self, parser, namespace, sizes, option_string=None):
        dimensions = [value.strip() for value in sizes.split(",")]
        dimensions = [*dimensions, *dimensions] if len(dimensions) == 1 else dimensions
        setattr(namespace, self.dest, dimensions)


class ParsePaletteArgument(argparse.Action):
    def __call__(self, parser, namespace, palette, option_string=None):
        palette = palette if palette else True
        setattr(namespace, self.dest, palette)


ap = argparse.ArgumentParser(prog='ImageGoNord', description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
ap.add_argument('-v', '--version', action='version', version=f'%(prog)s {VERSION}')
ap.add_argument('-q', '--quiet', action='store_true')
ap.add_argument('-i', '--img', type=str, metavar='<path>', required=True)
ap.add_argument('-o', '--out', type=str, metavar='<path>', default=DEFAULT_FILENAME)
ap.add_argument('-na', '--no-avg', action='store_true')
ap.add_argument('-pa', '--pixel-area', action=SplitCommaSeparatedArguments, default=[])
ap.add_argument('-b', '--blur', action='store_true')

# Add palette arguments
PALETTE_LIST = []
for palette in listdir(f"{ABSOLUTE_PATH}/palettes/"):
    PALETTE_LIST += [palette.lower()]
    ap.add_argument(f"--{palette.lower()}", nargs="*")


def console_log(*params):
    if not QUIET_MODE:
        print("\n".join(params))


def check_required_arguments(parsed_args):
    if not parsed_args.img:
        ap.error(messages.logs['img']['error'].format(parsed_args.img) + messages.logs['general_error'])

    if not parsed_args.out:
        ap.error(messages.logs['out']['error'].format(parsed_args.out) + messages.logs['general_error'])

    #TODO: scrivere il codice per avere una palette alla volta


if __name__ == '__main__':
    args = sys.argv[1:]
    parsed_args = ap.parse_args()
    # print(parsed_args)
    # print(vars(parsed_args))
    check_required_arguments(parsed_args)

    QUIET_MODE = parsed_args.quiet

    # If help given then print the docstring of the module and exit
    go_nord = GoNord()

    # Get absolute path of source project
    ABSOLUTE_PATH = path.dirname(path.realpath(__file__))

    # Reading input image
    image = go_nord.open_image(parsed_args.img)
    console_log(messages.logs["img"]['info'].format(ABSOLUTE_PATH + "/" + parsed_args.img))

    # Setting output
    output_path = Path(parsed_args.out)
    OUTPUT_IMAGE_PATH = str(output_path) + (DEFAULT_EXTENSION if not output_path.suffix else "")
    console_log(messages.logs["out"]['info'].format(ABSOLUTE_PATH + "/" + OUTPUT_IMAGE_PATH))

    # Enable/disable avg algoritm
    if parsed_args.no_avg:
        go_nord.disable_avg_algorithm()
        console_log(messages.logs["navg"]['info'])

    # Select pixel area
    if parsed_args.pixel_area:
        (w, h) = parsed_args.pixel_area
        go_nord.set_avg_box_data(w=w, h=h)

    if parsed_args.blur:
        go_nord.enable_gaussian_blur()

    # Get all palettes
    palettes = [palette.lower() for palette in listdir(ABSOLUTE_PATH + "/palettes")]

    for arg in args:
        key_value = [kv for kv in arg.split("=", 1) if kv != ""]
        key = key_value[0].lower()

        for palette in palettes:
            if "--{}".format(palette) in key:
                palette_path = ABSOLUTE_PATH + "/palettes/" + palette.capitalize() + "/"
                go_nord.set_palette_lookup_path(palette_path)
                go_nord.reset_palette()
                if len(key_value) > 1:
                    palette_set = [palette_file.replace(".txt", '') for palette_file in listdir(palette_path)]
                    selected_colors = [selected_color.lower() for selected_color in key_value[1].split(",")]
                    console_log(confarg.logs["pals"][1].format(palette.capitalize()))
                    for selected_color in selected_colors:
                        lowered_palette = list(map(str.lower, palette_set))
                        print(lowered_palette)
                        if selected_color in lowered_palette:
                            index_color = lowered_palette.index(selected_color)
                            go_nord.add_file_to_palette(palette_set[index_color] + ".txt")
                            console_log(confarg.logs["pals"][2].format(palette_set[index_color]))
                            PALETTE_CHANGED = True
                        else:
                            console_log(confarg.logs["pals"][-1].format(selected_color))
                    for palette_color in palette_set:
                        if palette_color.lower() not in selected_colors:
                            console_log(confarg.logs["pals"][3].format(palette_color))
                else:
                    PALETTE_CHANGED = True
                    console_log(confarg.logs["pals"][0].format(palette.capitalize()))
                    go_nord.set_palette_lookup_path(palette_path)
                    for ps in [palette_file for palette_file in listdir(palette_path)]:
                        go_nord.add_file_to_palette(ps)

    if not PALETTE_CHANGED:
        console_log(confarg.logs["pals"][4])
        palette_path = ABSOLUTE_PATH + "/palettes/Nord/"
        go_nord.reset_palette()
        palette_set = [palette_file.replace(".txt", '') for palette_file in listdir(palette_path)]
        go_nord.set_palette_lookup_path(palette_path)
        for ps in palette_set:
            go_nord.add_file_to_palette(ps + ".txt")

    quantize_image = go_nord.convert_image(image, save_path=OUTPUT_IMAGE_PATH)
    sys.exit(0)
