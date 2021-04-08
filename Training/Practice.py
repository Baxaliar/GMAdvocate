
import simple_draw as sd

sd.resolution = (1366, 768)

# sd.snowflake(center=point_0, length=200, factor_a=.5)

y = 500
x = 100

y_2 = 450
x_2 = 150
while True:
    sd.clear_screen()
    point = sd.get_point(x, y)
    sd.snowflake(center=point, length=50)
    y -= 10
    if y < 50:
        break
    x = x * 1.1

    point_2 = sd.get_point(x_2, y_2)
    sd.snowflake(center=point_2, length=50)
    y_2 -= 10
    if y_2 < 50:
        break
    x_2 = x_2 * 1.1

    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
