# -*- coding: utf-8 -*-

import sys
import re
from os import path

from PIL import Image, ImageFilter

from ImageGoNord.configs import arguments as confarg
from ImageGoNord.utility.quantize import quantize_to_palette
import ImageGoNord.utility.palette_loader as pl
from ImageGoNord.utility.ConvertUtility import ConvertUtility

class NordPaletteFile:
  AURORA      = "Aurora.txt"
  FROST       = "Frost.txt"
  POLAR_NIGHT = "PolarNight.txt"
  SNOW_STORM  = "SnowStorm.txt"

class GoNord(object):
  PALETTE_LOOKUP_PATH   = "palettes/Nord/"
  USE_GAUSSIAN_BLUR     = False
  USE_AVG_COLOR         = False
  AVG_BOX_DATA          = {"w": -2, "h": 3}

  AVAILABLE_PALETTE = []

  def __init__(self):
    '''Constructor: init variables & config'''
    self.set_default_nord_palette()
    self.set_avg_box_data()

  def set_palette_lookup_path(self, path):
    '''Set the base_path for the palette folder'''
    self.PALETTE_LOOKUP_PATH = path

  def set_default_nord_palette(self):
    '''Set available palette as the default palette'''
    self.AVAILABLE_PALETTE = [
      NordPaletteFile.POLAR_NIGHT,
      NordPaletteFile.SNOW_STORM,
      NordPaletteFile.FROST,
      NordPaletteFile.AURORA,
    ]

  def get_palette_data(self):
    palettedata = {}
    for palette_file in self.AVAILABLE_PALETTE:
      hex_colors = pl.import_palette_from_file(self.PALETTE_LOOKUP_PATH + palette_file)
      for hex_color in hex_colors:
        palettedata[hex_color] = pl.export_tripletes_from_color(hex_color)

    return palettedata

  def reset_palette(self):
    '''Reset available palette array'''
    self.AVAILABLE_PALETTE = []

  def add_file_to_palette(self, file):
    '''Method for adding file to the available palette'''
    self.AVAILABLE_PALETTE.append(file)

  def enable_gaussian_blur(self):
    '''Enable gaussian blur on the output img'''
    self.USE_GAUSSIAN_BLUR = True

  def disable_gaussian_blur(self):
    '''Disable gaussian blur on the output img'''
    self.USE_GAUSSIAN_BLUR = False

  def open_image(self, path):
    return Image.open(path)

  def load_pixel_image(self, opened_image):
    return opened_image.load()

  def enable_avg_algorithm(self):
    self.USE_AVG_COLOR = True

  def disable_avg_algorithm(self):
    self.USE_AVG_COLOR = False

  def set_avg_box_data(self, w=-2, h=3):
    self.AVG_BOX_DATA['w'] = w
    self.AVG_BOX_DATA['h'] = h

  def quantize_image(self, image, palettedata, save='', save_path=False):
    while len(palettedata) < 768:
      palettedata.extend(pl.export_tripletes_from_color('2E3440'))

    palimage = Image.new('P', (1, 1))
    palimage.putpalette(palettedata)
    quantize_img = quantize_to_palette(image, palimage)

    if (save == True and save_path != ''):
      quantize_img.save(save_path)

    return quantize_img

  def convert_image(self, image, palettedata, save_path='', save=True):
    pixels = self.load_pixel_image(image)
    for i in range(image.size[0]):
      for j in range(image.size[1]):
        color_to_check = pixels[i, j]
        if self.USE_AVG_COLOR == True:
            color_to_check = ConvertUtility.get_avg_color(pixels=pixels, w=self.AVG_BOX_DATA['w'], h=self.AVG_BOX_DATA['h'])

        differences = [[ConvertUtility.color_difference(color1=color_to_check, color2=target_value), target_name]
                       for target_name, target_value in palettedata.items()]
        differences.sort()
        pixels[i, j] = tuple(palettedata[differences[0][1]])

    if (self.USE_GAUSSIAN_BLUR == True):
      image = image.filter(ImageFilter.GaussianBlur(1))

    if (save == True and save_path != ''):
      image.save(save_path)
    return image