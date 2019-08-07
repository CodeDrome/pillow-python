from PIL import Image, ImageDraw

import colors_histogram


def main():

    print("--------------------")
    print("| codedrome.com    |")
    print("| Pillow Histogram |")
    print("--------------------")

    filename = "central_st_giles_colour.jpg"

    try:

        image = Image.open(filename)

        histograms = colors_histogram.create_histograms(image)

        if image.mode == "RGB":

            histograms["red"].save(filename + "_histogram_red.png", "PNG")
            histograms["green"].save(filename + "_histogram_green.png", "PNG")
            histograms["blue"].save(filename + "_histogram_blue.png", "PNG")

        elif image.mode == "L":

            histograms["greyscale"].save(filename + "_histogram_greyscale.png", "PNG")

        image.close()

    except IOError as e:

        print(e)

    except ValueError as e:

        print(e)


main()
