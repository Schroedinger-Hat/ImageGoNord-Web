"""This is the example module.

This module does stuff.
"""

from PIL import ImageFilter, Image


def quantize_to_palette(input_file, output_file, palette, blur):
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

    source_image = Image.open(input_file)
    source_image.load()
    new_image = Image.new('P', (1, 1))
    new_image.putpalette(palette)
    new_image.load()

    if new_image.mode != "P":
        raise ValueError("bad mode for palette image")
    if source_image.mode != "RGB" and source_image.mode != "L":
        raise ValueError(
            "only RGB or L mode images can be quantized to a palette"
        )

    # color quantize, mode P
    image_color_quantize = source_image.quantize(
        colors=256, method=0, kmeans=5, palette=new_image)
    # convert again from P mode to RGB
    image_convert_rgb = image_color_quantize.convert('RGB')

    # reduce rumor noise by applying a blur
    final_image = image_convert_rgb
    if blur:
        final_image = image_convert_rgb.filter(ImageFilter.GaussianBlur(1))

    # save
    final_image.save(output_file)


def color_difference(color1, color2):
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
    return sum([abs(component1-component2) for component1, component2 in zip(color1, color2)])


def get_avg_color(pixels, w=-2, h=3):
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
    average_sum = []
    for k in range(w, h):
        for l in range(w, h):
            try:
                average_sum.append(pixels[i+k, j+l])
                n += 1
            except:
                pass

    size = len(average_sum)
    r = 0
    g = 0
    b = 0
    for x in average_sum:
        r += x[0]
        g += x[1]
        b += x[2]

    return (r/size, g/size, b/size)


def replace_color(input_file, output_file, palette, blur):
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
    source_image = Image.open(input_file)
    source_image.load()
    new_image = Image.new('P', (1, 1))
    new_image.putpalette(palette)
    new_image.load()

    pixels = source_image.load()

    for i in range(source_image.size[0]):
        for j in range(source_image.size[1]):
            color_to_check = pixels[i, j]

            if False:
                color_to_check = get_avg_color(pixels)

            differences = [[color_difference(color_to_check, target_value), target_name]
                           for target_name, target_value in palette.items()]
            differences.sort()
            pixels[i, j] = tuple(palette[differences[0][1]])

    if blur:
        source_image = source_image.filter(ImageFilter.GaussianBlur(1))

    source_image.save(output_file)
