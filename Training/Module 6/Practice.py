
import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# x, y = 50, 50
# for color in rainbow_colors:
#     start_point = sd.get_point(x, y)
#     end_point = sd.get_point(x + 500, y + 500)
#     sd.line(start_point=start_point, end_point=end_point, color=color, width=4)
#     x += 5

# width = 4
# step = 5 + width
# for item, x in enumerate(range(50, 50 + step * 7, step)):
#     color = rainbow_colors[item]
#     sd.line(start_point=sd.get_point(x, 50), end_point=sd.get_point(x + 500, 550), width=width, color=color)

brick_x, brick_y = 100, 50

row = 0
for y in range(0, sd.resolution[1], brick_y):
    row += 1
    for x in range(0, sd.resolution[0], brick_x):
        x0 = x if row % 2 else x + brick_x // 2
        left_bottom = sd.get_point(x0, y)
        right_top = sd.get_point(x0 + brick_x, y + brick_y)
        sd.rectangle(left_bottom=left_bottom, right_top=right_top, width=1)
sd.pause()
