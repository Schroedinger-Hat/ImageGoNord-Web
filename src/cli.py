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
from copy import copy
from os import path, listdir
from pathlib import Path

from ImageGoNord import GoNord

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
        palette = palette.strip().split(',') if palette else []
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
    ap.add_argument(f"--{palette.lower()}", action=ParsePaletteArgument, default=None, nargs='?')


def console_log(*params):
    if not QUIET_MODE:
        print("\n".join(params))


def check_required_arguments(parsed_args):
    if not parsed_args.img:
        ap.error(messages.logs['img']['error'].format(parsed_args.img) + messages.logs['general_error'])

    if not parsed_args.out:
        ap.error(messages.logs['out']['error'].format(parsed_args.out) + messages.logs['general_error'])

    palette_list = [p for p, v in vars(parsed_args).items() if p in PALETTE_LIST and v is not None]
    if len(palette_list) > 1:
        ap.error(
            messages.logs['palette']['too_many_palettes_error'].format(", ".join(palette_list))
            + messages.logs['general_error']
        )


if __name__ == '__main__':
    args = sys.argv[1:]
    parsed_args = ap.parse_args()
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
    parsed_args_dictionary = vars(parsed_args)
    selected_palette = next(p for p, v in parsed_args_dictionary.items() if p in PALETTE_LIST and v is not None)
    if not selected_palette:
        selected_palette = "north"
        console_log(messages.logs["pals"][4])

    palette_path = ABSOLUTE_PATH + "/palettes/" + selected_palette.capitalize() + "/"
    parsed_colors = parsed_args_dictionary.get(selected_palette)

    # Loading selected palette
    palette_colors_files = [f.capitalize() + '.txt' for f in parsed_colors]
    for pf in copy(palette_colors_files):
        if not Path(palette_path + pf).is_file():
            console_log(messages.logs["pals"][-1].format(pf.replace('.txt', '')))
            palette_colors_files.remove(pf)

    # If no palette is valid or non is chosed, use all colors palettes
    if not palette_colors_files:
        console_log(messages.logs["pals"][0].format(selected_palette.capitalize()))
        palette_colors_files = listdir(palette_path)

    # Apply selected colors
    console_log(messages.logs["pals"][1].format(selected_palette.capitalize()))
    go_nord.set_palette_lookup_path(palette_path)
    go_nord.reset_palette()
    for pf in palette_colors_files:
        go_nord.add_file_to_palette(pf)
        console_log(messages.logs["pals"][2].format(pf))

    # Convert the image
    quantize_image = go_nord.convert_image(image, save_path=OUTPUT_IMAGE_PATH)
    sys.exit(0)

