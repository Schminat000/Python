# This imports the use of the python image library.
from PIL import Image

# For creativity, this will randomize the colors on the given coordinates. Just for fun! It also tells us what the random numbers are going to be for the rgb colors down below.
import random
rgb_number_1 = random.randint(0, 255)
rgb_number_2 = random.randint(0, 255)
rgb_number_3 = random.randint(0, 255)
print(f'({rgb_number_1}, {rgb_number_2}, {rgb_number_3})')

# This tells the program to open the chosen image and also tells us, the size of the image, and the formatting.
image_original = Image.open('desert.jpg')
print(image_original.size)
print(image_original.format)

# This tells us what colors are used for the specific pixel.
pixels_desert = image_original.load()
print(pixels_desert[200,100])

# This takes the coordinate display colors and changes their colors randomly based on the random numbers above.
pixels_desert[200, 100] = (rgb_number_1, rgb_number_2, rgb_number_3)
pixels_desert[201, 100] = (rgb_number_3, rgb_number_2, rgb_number_1)
pixels_desert[202, 100] = (rgb_number_2, rgb_number_1, rgb_number_3)
pixels_desert[203, 100] = (rgb_number_3, rgb_number_1, rgb_number_2)
pixels_desert[204, 100] = (rgb_number_2, rgb_number_3, rgb_number_1)

# This will display and show the changes made to the image.
image_original.show()

# This saves the new and changed image.
image_original.save('the_file_goes_here.jpg')