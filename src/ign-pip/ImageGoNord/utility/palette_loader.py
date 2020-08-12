"""This is the example module.

This module does stuff.
"""
from os import listdir


def load_palette_set(path):
    """Create a list of every colors set on the path given.

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
    directories = listdir(path)

    palette_list = [palette_file.replace(
        ".txt", '') for palette_file in directories]

    return palette_list


def find_palettes(path):
    """Create a set with every palettes stored in the directory given.

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
    palettes = [palette.lower() for palette in listdir(path)]
    return palettes


def import_palette_from_file(filename):
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
    opened_file = open(filename, "r")
    palette = [line.replace('#', '').replace('\n', '')
               for line in opened_file.readlines()]
    palette.remove('')
    return palette


def create_data_colors(palette):
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
    data = []
    for color in palette:
        data.extend((export_tripletes_from_color(color)))
    return data


def export_tripletes_from_color(hex_color):
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
    hex_triplets = [hex_color[i:i+2] for i in range(0, len(hex_color), 2)]
    triplets_integer = [int(hex_triplets[i], 16)
                        for i in range(len(hex_triplets))]
    return triplets_integer
