"""This is the example module.

This module does stuff.
"""
import os


def load_palette_set(path):
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
    directories = os.listdir(path)

    palette_list = [palette_file.replace(
        ".txt", '') for palette_file in directories]

    return palette_list


def find_palette(path):
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
    palettes = [palette.lower() for palette in os.listdir(path)]
    return palettes
