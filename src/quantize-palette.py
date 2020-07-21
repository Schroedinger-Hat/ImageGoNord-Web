from PIL import Image

def quantizetopalette(silf, palette, dither=False):

    silf.load()

    palette.load()
    if palette.mode != "P":
        raise ValueError("bad mode for palette image")
    if silf.mode != "RGB" and silf.mode != "L":
        raise ValueError(
            "only RGB or L mode images can be quantized to a palette"
            )
    im = silf.im.convert("P", 1 if dither else 0, palette.im)

    # Altro metodo
    silf.quantize(palette=palette)
    
    # retrocompatibilità per le 4.0 di pillow
    return silf._new(im)

# polar light palette
palettedata = [46, 52, 64, 59, 66, 82, 67, 76, 94, 76, 86, 106]
palimage = Image.new('P', (16, 16))
palimage.putpalette(palettedata * 64)
oldimage = Image.open("images/test.png")
newimage = quantizetopalette(oldimage, palimage, dither=False)
newimage.save('images/out.png')