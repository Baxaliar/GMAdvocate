
import simple_draw as sd

length = 200
n = 0


def draw_figure(sides_number, point, angle):
    v1 = sd.get_vector(start_point=point, angle=0, length=100, width=3)
    v1.draw()

    for i in range(0, sides_number):
        v_prev = sd.get_vector(start_point=v1.end_point, angle=angle + (360 / sides_number), length=100, width=3)
        v_prev.draw()

        v_next = sd.get_vector(start_point=v_prev.end_point, angle=angle + (360 / sides_number)*i, length=100, width=3)
        v_next.draw()


point_0 = sd.get_point(300, 300)
draw_figure(sides_number=3, point=point_0, angle=0)

sd.pause()
