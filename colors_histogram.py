from PIL import Image, ImageDraw


def create_histograms(image):

    """
    Takes a Pillow image.
    Returns a dictionary of Pillow images of colour
    histograms.
    For colour (mode "RGB") images there are 3 with
    keys "red", "green" and "blue".
    For greyscale (mode "L") images there is one with key "greyscale".
    Raises ValueError if mode is not "RGB" or "L"
    """

    if image.mode == "RGB":

        normalized_frequencies = _create_normalized_frequencies_rgb(image)

        return {"red": _create_histogram((0,), normalized_frequencies["red"]),
                "green": _create_histogram((1,), normalized_frequencies["green"]),
                "blue": _create_histogram((2,), normalized_frequencies["blue"])}

    elif image.mode == "L":

        normalized_frequencies = _create_normalized_frequencies_greyscale(image)

        return {"greyscale": _create_histogram((0,1,2), normalized_frequencies)}

    else:

        raise ValueError("Image must have mode of RGB or L")


def _create_normalized_frequencies_rgb(image):

    frequencies = image.histogram()

    max_freq = max(frequencies)

    normalized_frequencies = {"red": [f / max_freq for f in frequencies[0:256]],
                              "green": [f / max_freq for f in frequencies[256:512]],
                              "blue": [f / max_freq for f in frequencies[512:768]]}

    return normalized_frequencies


def _create_normalized_frequencies_greyscale(image):

    frequencies = image.histogram()
    max_freq = max(frequencies)

    normalized_frequencies = [f / max_freq for f in frequencies]

    return normalized_frequencies


def _create_histogram(channels, frequencies):

    width = 256
    height = 158
    column_width = 1

    im = Image.new("RGB", (width, height), (255,255,255))

    draw = ImageDraw.Draw(im)

    col = [0,0,0]

    for v in range(0, 256):

        for channel in channels:
            col[channel] = v

        draw.line(xy=[(v, height),(v, height - (height * frequencies[v]))],
                  fill=tuple(col),
                  width=column_width)

    return im
