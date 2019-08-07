import exif


def main():

    print("-----------------")
    print("| codedrome.com |")
    print("| Pillow EXIF   |")
    print("-----------------\n")

    try:

        filepath = "vaults_theatre.jpg"

        exif_dict = exif.generate_exif_dict(filepath)

        print_exif_dict(exif_dict)

    except IOError as ioe:

        print(ioe)


def print_exif_dict(exif_dict):

    for k, v in exif_dict.items():

        if v["raw"] is not None:
            print(k)
            print("-" * len(k))
            print("    tag:       {}".format(v["tag"]))
            print("    raw:       {}".format(v["raw"]))
            print("    processed: {}\n".format(v["processed"]))


main()
