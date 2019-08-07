import PIL
from PIL import Image
from PIL import ImageEnhance


def main():

    print("-----------------")
    print("| codedrome.com |")
    print("| More Pillow   |")
    print("-----------------\n")

    openfilepath = "central_st_giles.jpg"
    show_image_info(openfilepath)

    # The desaturate function is the wrong way to change an image
    # to black and white and is included here with show_image_info
    # to demonstrate that it leaves the image with a mode of RGB
    # desaturate(openfilepath, "central_st_giles_desaturated.jpg")
    # show_image_info("central_st_giles_desaturated.jpg")

    # This is the correct way to convert an image to B&W.
    # Calling show_image_info will show a mode of L
    # mode_L(openfilepath, "central_st_giles_mode_L.jpg")
    # show_image_info("central_st_giles_mode_L.jpg")

    # mode_L("central_st_giles_bw.jpg", "central_st_giles_bw.jpg")
    # show_image_info("central_st_giles_mode_L.jpg")

    #contrast("central_st_giles_mode_L.jpg", "central_st_giles_mode_L_increased_contrast.jpg", 2.0)

    #bands_brightness(openfilepath, "central_st_giles_bands_brightness.jpg", 1.0, 1.0, 2.0)

    #quality_demo("central_st_giles.jpg")


def show_image_info(openfilepath):

    """
    Open an image and show a few attributes
    """

    try:

        image = Image.open(openfilepath)

        print("filename:           {}".format(image.filename))
        print("size:               {}".format(image.size))
        print("width:              {}".format(image.width))
        print("height:             {}".format(image.height))
        print("format:             {}".format(image.format))
        print("format description: {}".format(image.format_description))
        print("mode:               {}\n".format(image.mode))

    except IOError as ioe:

        print(ioe)


def desaturate(openfilepath, savefilepath):

    """
    Convert an image to black and white the wrong way.
    This method still leaves the image with a colour
    depth of 24 bit RGB.
    The correct method is to use convert("L")
    """

    try:

        image = Image.open(openfilepath)

        enhancer = ImageEnhance.Color(image)

        image = enhancer.enhance(0.0)

        image.save(savefilepath)

        print("Image desaturated")

    except IOError as ioe:

        print(ioe)

    except ValueError as ve:

        print(ve)


def mode_L(openfilepath, savefilepath):

    """
    The correct way to convert an image to black and white.
    Do not use ImageEnhance.Color to reduce saturation to 0
    as that leaves the colour depth at 24 bit.
    """

    try:

        image = Image.open(openfilepath)

        image = image.convert("L")

        image.save(savefilepath)

        print("Mode changed to L")

    except IOError as ioe:

        print(ioe)

    except ValueError as ve:

        print(ve)


def contrast(openfilepath, savefilepath, amount):

    """
    A general-purpose function to change the contrast
    by the specified amount and save the image.
    """

    try:

        image = Image.open(openfilepath)

        enhancer = ImageEnhance.Contrast(image)

        image = enhancer.enhance(amount)

        image.save(savefilepath)

        print("Contrast changed")

    except IOError as ioe:

        print(ioe)

    except ValueError as ve:

        print(ve)


def bands_brightness(openfilepath, savefilepath, r, g, b):

    """
    Split the image into colour channels (bands),
    change the brightness of each by the specified amount,
    merge the channels and save the image.
    """

    try:

        image = Image.open(openfilepath)

        # image.split() returns a tuple so we need to convert
        # it to a list so we can overwrite the bands.
        bands = list(image.split())

        enhancer = ImageEnhance.Brightness(bands[0])
        bands[0] = enhancer.enhance(r)

        enhancer = ImageEnhance.Brightness(bands[1])
        bands[1] = enhancer.enhance(g)

        enhancer = ImageEnhance.Brightness(bands[2])
        bands[2] = enhancer.enhance(b)

        image = PIL.Image.merge("RGB", bands)

        image.save(savefilepath)

        print("Band brightnesses changed")

    except IOError as ioe:

        print(ioe)

    except ValueError as ve:

        print(ve)


def quality_demo(openfilepath):

    """
    Save the specified image at several different quality levels
    for demonstration purposes.
    Quality can be any value between 1 (awful) to 100 (best).
    Anything < 50 is unlikely to be acceptable.
    """

    try:

        image = Image.open(openfilepath)

        for q in range(25, 101, 25):

            filename = str(q) + ".jpg"

            image.save(filename, quality=q)

        print("Image saved at various qualities")

    except IOError as ioe:

        print(ioe)

    except ValueError as ve:

        print(ve)


main()
