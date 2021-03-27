
import simple_draw as sd


def draw_figure(sides_number, point, angle):
    p_next = point
    for i in range(sides_number-1):
        v_next = sd.get_vector(start_point=p_next, angle=angle + (360 / sides_number)*i, length=100, width=3)
        v_next.draw()
        p_next = sd.get_point(v_next.end_point.x, v_next.end_point.y)
    else:
        p_last = p_next
        sd.line(start_point=p_last, end_point=point, width=3)


def triangle(point):
    draw_figure(3, point=point, angle=0)


def square(point):
    draw_figure(4, point=point, angle=0)


def pentagram(point):
    draw_figure(5, point=point, angle=0)


def hexagon(point):
    draw_figure(6, point=point, angle=0)


point_0 = sd.get_point(100, 100)
point_1 = sd.get_point(400, 100)
point_2 = sd.get_point(100, 300)
point_3 = sd.get_point(400, 300)
triangle(point=point_0)
square(point=point_1)
pentagram(point=point_2)
hexagon(point=point_3)

sd.pause()
