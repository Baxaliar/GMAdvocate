
import simple_draw as sd

sd.resolution = (1366, 768)


def branch(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    return v1.end_point


# Цикл
angle_0 = 90
length_0 = 200
point_0 = sd.get_point(100, 5)

next_angle = angle_0
next_length = length_0
next_point = point_0

while next_length > 1:
    next_point = branch(point=next_point, angle=next_angle, length=next_length)
    next_angle = next_angle - 30
    next_length = next_length * .75

# сделать функцию branch рекурсивной


sd.pause()
