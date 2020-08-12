"""This is the example module.

This module does stuff.
"""

from PIL import ImageFilter

def quantize_to_palette(silf, palette):
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
    silf.load()
    palette.load()

    if palette.mode != "P":
        raise ValueError("bad mode for palette image")
    if silf.mode != "RGB" and silf.mode != "L":
        raise ValueError(
            "only RGB or L mode images can be quantized to a palette"
        )

    # color quantize, mode P
    im = silf.quantize(colors=256, method=0, kmeans=5, palette=palette)
    # convert again from P mode to RGB
    im = im.convert('RGB')
    # reduce rumor noise by applying a blur
    im = im.filter(ImageFilter.GaussianBlur(1))

    return im
