import os
from PIL import Image
import argparse
from itertools import product

def generate(n_colors):
    if n_colors[0] == 1:
        colors = 255
    elif n_colors[0] == 256:
        colors = 1
    else:
        colors = (256 // n_colors[0]) - 1


    current_directory = os.path.dirname(os.path.realpath(__file__))

    # Create the 'images' directory if it doesn't exist
    images_directory = os.path.join(current_directory, "images")
    os.makedirs(images_directory, exist_ok=True)

    x = 2
    y = 2

    n = 0

    n_pixels = x * y

    image = Image.new("RGB", (x, y)) # Create a X x Y grid image
    pixels = image.load()
    
    color_combinations = product(range(0, 256, colors), repeat=3*n_pixels)

    for colors in color_combinations:
        for i in range(n_pixels):
            row = i // x
            col = i % y
            rgb = colors[i * 3:i * 3 + 3]
            pixels[row, col] = rgb

        image_filename = os.path.join(images_directory, f"image_{n}.png")
        n += 1
        image.save(image_filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="All Image Generator")
    parser.add_argument("-n", "--n_colors", type=int, nargs='*', help="Specify the number of colors")
    args = parser.parse_args()

    if args.n_colors:
        n_colors = args.n_colors
    else:
        # If no n_colors is specified, it will use 256
        n_colors = [256]

    generate(n_colors)