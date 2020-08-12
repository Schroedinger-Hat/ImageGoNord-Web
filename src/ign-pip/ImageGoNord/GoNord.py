# -*- coding: utf-8 -*-

import sys
import re
from os import path

from PIL import Image

from ImageGoNord.configs import arguments as confarg
from ImageGoNord.utility.quantize import quantize_to_palette
import ImageGoNord.utility.palette_loader as pl

class GoNord(object):
  def __init__(self):
    '''Constructor: init variables & config'''
    print('init imagegonord class')
    self.x = 'a'

def xd():
  print("ciao")