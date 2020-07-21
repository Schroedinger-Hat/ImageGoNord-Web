from PIL import Image

class NordPalette():
    POLAR_NIGHT = [46, 52, 64, 59, 66, 82, 67, 76, 94, 76, 86, 106]
    SNOW_STORM = [216, 222, 233, 229, 233, 240, 236, 239, 244]
    FROST = [143, 188, 187, 136, 192, 208, 129, 161, 193, 94, 129, 172]
    AURORA = [191, 97, 106, 208, 135, 112, 235, 203, 139, 163, 190, 140, 180, 142, 173]

palettedata = NordPalette.FROST + NordPalette.POLAR_NIGHT + NordPalette.SNOW_STORM + NordPalette.AURORA

def quantizetopalette(silf, palette, dither=False):
    global palettedata

    silf.load()

    palette.load()
    if palette.mode != "P":
        raise ValueError("bad mode for palette image")
    if silf.mode != "RGB" and silf.mode != "L":
        raise ValueError(
            "only RGB or L mode images can be quantized to a palette"
            )

    #im = silf.im.convert("P", 1 if dither else 0, palette.im)
    im2 = silf.convert("P", None, None, palette.im, 4)

    # Altro metodo
    im = silf.quantize(colors=int(len(palettedata) / 3), method=None, kmeans=0, palette=palette)
    im.save("images/quantize.png")
    # retrocompatibilità per le 4.0 di pillow
    return im2

# polar light palette
palimage = Image.new('P', (16, 16))
palimage.putpalette(palettedata * 16)
oldimage = Image.open("images/mountain.jpg")
newimage = quantizetopalette(oldimage, palimage, dither=False)
newimage.save('images/out.png')