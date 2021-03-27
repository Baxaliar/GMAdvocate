
# pip install simple_draw

import simple_draw as sd

length = 200

# Первый вариант дз


def triangle(point, angle=0):
    v1 = sd.get_vector(start_point=point, angle=0, length=100, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=100, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=100, width=3)
    v3.draw()


def square(point, angle=0):
    v1 = sd.get_vector(start_point=point, angle=0, length=100, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=100, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=100, width=3)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=100, width=3)
    v4.draw()


def pentagram(point, angle=0):
    v1 = sd.get_vector(start_point=point, angle=0, length=100, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=100, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=100, width=3)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=100, width=3)
    v4.draw()

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288, length=100, width=3)
    v5.draw()


def hexagon(point, angle=0):
    v1 = sd.get_vector(start_point=point, angle=0, length=100, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=100, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=100, width=3)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=100, width=3)
    v4.draw()

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=100, width=3)
    v5.draw()

    v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 300, length=100, width=3)
    v6.draw()


point_0 = sd.get_point(100, 100)
point_1 = sd.get_point(400, 100)
point_2 = sd.get_point(100, 300)
point_3 = sd.get_point(400, 300)
triangle(point=point_0)
square(point=point_1)
pentagram(point=point_2)
hexagon(point=point_3)
# for angle in range(0, 361, 30):
#     triangle(point=point_0, angle=angle)


sd.pause()
