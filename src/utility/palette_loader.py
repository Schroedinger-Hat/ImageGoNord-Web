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
