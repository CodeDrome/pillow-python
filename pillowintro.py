import PIL
from PIL import Image
from PIL import ImageEnhance


def main():

    print("--------------------------")
    print("| codedrome.com          |")
    print("| Introduction to Pillow |")
    print("--------------------------\n")

    print("Pillow version {}\n".format(PIL.PILLOW_VERSION))

    openfilepath = "NationalGallery/nationalgallery.jpg"

    info_and_copy(openfilepath, "NationalGallery/nationalgallery_copy.jpg")

    #resize(openfilepath, "nationalgallery_resized.jpg")

    #thumbnail(openfilepath, "nationalgallery_thumbnail.jpg")

    #rotate(openfilepath, "nationalgallery_rotated.jpg")

    #crop(openfilepath, "nationalgallery_cropped.jpg")

    #set_pixels(openfilepath, "nationalgallery_pixels_set.jpg")

    #color(openfilepath, "nationalgallery_color_enhanced.jpg")
    #contrast(openfilepath, "nationalgallery_contrast_enhanced.jpg")
    #brightness(openfilepath, "nationalgallery_brightness_enhanced.jpg")
    #sharpness(openfilepath, "nationalgallery_sharpness_enhanced.jpg")

    #add_watermark(openfilepath, "watermark.png", "nationalgallery_watermark.jpg")


def info_and_copy(openfilepath, savefilepath):

    try:

        image = Image.open(openfilepath)

        print("filename:           {}".format(image.filename))
        print("size:               {}".format(image.size))
        print("width:              {}".format(image.width))
        print("height:             {}".format(image.height))
        print("format:             {}".format(image.format))
        print("format description: {}".format(image.format_description))
        print("mode:               {}".format(image.mode))

        image_copy = image.copy()

        image_copy.save(savefilepath)

    except IOError as ioe:

        print(ioe)

    except ValueError as ve:

        print(ve)


def resize(openfilepath, savefilepath):

    try:

        image = Image.open(openfilepath)

        image = image.resize( (100, int(100 * (image.height / image.width))) )

        image.save(savefilepath)

        print("Image resized")

    except IOError as ioe:

        print(ioe)

    except ValueError as ve:

        print(ve)


def thumbnail(openfilepath, savefilepath):

    try:

        image = Image.open(openfilepath)

        image.thumbnail((100, 100))

        image.save(savefilepath)

        print("Image resized")

    except IOError as ioe:

        print(ioe)

    except ValueError as ve:

        print(ve)


def rotate(openfilepath, savefilepath):

    try:

        image = Image.open(openfilepath)

        image = image.rotate(270, expand=1)

        image.save(savefilepath)

        print("Image rotated")

    except IOError as ioe:

        print(ioe)

    except ValueError as ve:

        print(ve)


def crop(openfilepath, savefilepath):

    try:

        image = Image.open(openfilepath)

        image = image.crop((85, 20, 500, 300))

        image.save(savefilepath)

        print("Image cropped")

    except IOError as ioe:

        print(ioe)

    except ValueError as ve:

        print(ve)


def set_pixels(openfilepath, savefilepath):

    try:

        image = Image.open(openfilepath)

        y = int(image.height / 2)

        for x in range(0, image.width):

            image.putpixel((x, y), (255,0,0))

        image.save(savefilepath)

        print("Image pixels set")

    except IOError as ioe:

        print(ioe)

    except ValueError as ve:

        print(ve)


def color(openfilepath, savefilepath):

    try:

        image = Image.open(openfilepath)

        enhancer = ImageEnhance.Color(image)

        image = enhancer.enhance(2.0)

        image.save(savefilepath)

        print("Image color enhanced")

    except IOError as ioe:

        print(ioe)

    except ValueError as ve:

        print(ve)


def contrast(openfilepath, savefilepath):

    try:

        image = Image.open(openfilepath)

        enhancer = ImageEnhance.Contrast(image)

        image = enhancer.enhance(2.0)

        image.save(savefilepath)

        print("Image contrast enhanced")

    except IOError as ioe:

        print(ioe)

    except ValueError as ve:

        print(ve)


def brightness(openfilepath, savefilepath):

    try:

        image = Image.open(openfilepath)

        enhancer = ImageEnhance.Brightness(image)

        image = enhancer.enhance(0.5)

        image.save(savefilepath)

        print("Image brightness enhanced")

    except IOError as ioe:

        print(ioe)

    except ValueError as ve:

        print(ve)


def sharpness(openfilepath, savefilepath):

    try:

        image = Image.open(openfilepath)

        enhancer = ImageEnhance.Sharpness(image)

        image = enhancer.enhance(2.0)

        image.save(savefilepath)

        print("Image sharpness enhanced")

    except IOError as ioe:

        print(ioe)

    except ValueError as ve:

        print(ve)


def add_watermark(openfilepath, watermarkfilepath, savefilepath):

    try:

        main_image = Image.open(openfilepath).copy()
        watermark_image = Image.open(watermarkfilepath).copy()

        x = main_image.size[0] - watermark_image.size[0] - 16
        y = main_image.size[1] - watermark_image.size[1] - 16

        main_image.paste(watermark_image, (x, y), watermark_image)

        main_image.save(savefilepath)

        print("Watermark added")

    except IOError as ioe:

        print(ioe)

    except ValueError as ve:

        print(ve)


main()
