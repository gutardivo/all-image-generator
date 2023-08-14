from PIL import Image
n = 5**2
n_colors = 2

r = int(n**(1/2))

# Generate and save images for all possible truth table outputs
for i in range(2**n):
    binary = bin(i)[2:].zfill(n)  # Convert the index to binary with leading zeros

    # Create image based on binary values
    image = Image.new("RGB", (r, r), "black")
    pixels = image.load()

    for k in range(int(n_colors-1)):
        for j in range(n):
            x = j % r   # X-coordinate of the pixel
            y = j // r  # Y-coordinate of the pixel


            if binary[j] == "1":
                if k == 0:
                    pixels[x, y] = (128, 128, 128)  # Set pixel to grey if k value is 0
                else:
                    pixels[x, y] = (255, 255, 255)  # Set pixel to white if k value is 1
                # pixels[x, y] = (255, 255, 255)  # Set pixel to white if k value is 1


        image.save(f"./images/{binary}_{k}.png")