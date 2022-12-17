# This imports the use of the python image library.
from PIL import Image

# This tells the program to open the images to be used.
image_desert = Image.open('desert.jpg')
image_cactus = Image.open('cactus.jpg')

# This tells the program to load the images onto different variables.
pixels_desert = image_desert.load()
pixels_cactus = image_cactus.load()

# This removes the green screen and applies the background image to replace the pixels.
for x in range(0, 800):
    for y in range(0, 600):
        (r, g, b) = pixels_cactus[x, y]
        if r <= 150 and g >= 210 and b <= 60:
            pixels_cactus[x, y] = pixels_desert[x, y]

# This will save the new image.
image_cactus.save('cactus_desert.jpg')

# This will show the image with changes made.
image_cactus.show()