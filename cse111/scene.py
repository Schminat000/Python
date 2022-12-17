# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas, scene_width, scene_height)
    draw_cloud(canvas, 150, 350, 200, 30)
    draw_cloud(canvas, 450, 450, 500, 20)
    for x in range(100, 700, 100):
        draw_pine(canvas, x, 150, 80)
    draw_pine(canvas, 550, 150, 250)
    draw_pine(canvas, 750, 150, 150)
    draw_ground(canvas, scene_width)
    draw_grid(canvas, scene_width, scene_height, 50)


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

def draw_pine(canvas, center_x, bottom, height):
    # Draw the trunk of the tree.
    trunk_width = height / 10
    trunk_height = height / 2
    left_trunk = center_x - trunk_width / 2
    bottom_trunk = bottom
    right_trunk = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height
    draw_rectangle(canvas, left_trunk, bottom_trunk, right_trunk,\
        trunk_top, fill="tan4")

    # Draw the skirt of the tree.
    skirt_width = height / 2
    skirt_left = center_x - skirt_width / 2
    skirt_bottom = trunk_top
    peak_x = center_x
    peak_y = bottom + height
    skirt_right = center_x + skirt_width / 2
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y,\
        skirt_right, skirt_bottom, fill="darkGreen")

def draw_sky(canvas, width, height):
    # Draw the sky.
    sky_width = 0
    sky_height = 0
    sky_width_1 = width
    sky_height_1 = height
    draw_rectangle(canvas, sky_width, sky_height, sky_width_1,\
        sky_height_1, fill="lightSkyBlue1")

def draw_ground(canvas, width):
    # Draw the ground.
    ground_width = 0
    ground_height = 0
    ground_width_1 = width
    ground_height_1 = 150
    draw_rectangle(canvas, ground_width, ground_height,\
        ground_width_1, ground_height_1, fill="springGreen4")

def draw_cloud(canvas, left, bottom, right, top):
    # Draw the clouds.
    cloud_left = left
    cloud_bottom = bottom
    cloud_right = right + 170
    cloud_top  = top + 270
    draw_oval(canvas, cloud_left, cloud_bottom, cloud_right,\
        cloud_top, fill="snow1")

def draw_grid(canvas, width, height, interval):
    # Draw vertical lines.
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x, label_y, f"{x}")

    # Draw horizontal lines.
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, label_x, y, f"{y}")

# Call the main function so that
# this program will start executing.
main()