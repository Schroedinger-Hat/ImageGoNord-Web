# -*- coding: utf-8 -*-

import sys
import re
from os import path

from PIL import Image

from ImageGoNord.configs import arguments as confarg
from ImageGoNord.utility.quantize import quantize_to_palette
import ImageGoNord.utility.palette_loader as pl

class NordPaletteFile:
  AURORA      = "Aurora.txt"
  FROST       = "Frost.txt"
  POLAR_NIGHT = "PolarNight.txt"
  SNOW_STORM  = "SnowStorm.txt"

class GoNord(object):
  PALETTE_LOOKUP_PATH = "palettes/Nord/"
  USE_GAUSSIAN_BLUR = False

  AVAILABLE_PALETTE = []

  def __init__(self):
    '''Constructor: init variables & config'''
    self.set_default_nord_palette()

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
