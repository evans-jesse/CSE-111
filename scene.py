import tkinter as tk


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    left = scene_left
    top = scene_top
    right = scene_right
    bottom = scene_bottom

    draw_sky(canvas, left, top, right, bottom)
    draw_cloud(canvas, left, top, right, bottom)
    draw_hill(canvas, left, top, right, bottom)
    draw_sun(canvas, left, top, right, bottom)
    
    tree_center = scene_left + 650
    tree_top = scene_top + 200
    tree_height = 150
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)
    
    
def draw_sky(canvas, left, top, right, bottom):
    canvas.create_rectangle(0, 0, 799, 499, fill="#8cf5ff")
    
def draw_cloud(canvas, left, top, right, bottom):
    canvas.create_oval(100, 25, 250, 175, fill="#FFFFFF", width=False)
    canvas.create_oval(50, 75, 150, 175, fill="#FFFFFF", width=False)
    canvas.create_oval(200, 75, 300, 175, fill="#FFFFFF", width=False)
    
def draw_hill(canvas, left, top, right, bottom):
    # canvas.create_arc(500, 450, 700, 450, extent=50, fill="#20de16", style=tk.CHORD)
    canvas.create_oval(450, 345, 850, 950, fill="#20de16")

def draw_sun(canvas, left, top, right, bottom):
    canvas.create_oval(675, -75, 875, 125, fill="#f7e32a")

# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.


def draw_pine_tree(canvas, peak_x, peak_y, height):
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="dark green")


# Call the main function so that
# this program will start executing.
main()