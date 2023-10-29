import math


def func(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def make_decart_point(x, y):
    return {"x": x, "y": y}


def get_x(point):
    return point["x"]


def get_y(point):
    return point["y"]


def make_segment(p1, p2):
    return {"start": p1, "end": p2}


def get_mid_point_of_segment(segment):
    start = segment["start"]
    end = segment["end"]
    return make_decart_point(
        (get_x(start) + get_x(end)) / 2,
        (get_y(start) + get_y(end)) / 2
    )


def get_begin_point(segment):
    start = segment["start"]
    return make_decart_point(get_x(start), get_y(start))


def get_end_point(segment):
    end = segment["end"]
    return make_decart_point(get_x(end), get_y(end))


def make_point(x, y):
    return {
        "angle": math.atan2(y, x),
        "radius": math.sqrt((x ** 2) + (y ** 2)),
    }


# radius * cos(angle)
# BEGIN (write your solution here)
def get_x(point):
    return abs(point["radius"]) * math.cos(point["angle"])


def get_y(point):
    return abs(point["radius"]) * math.sin(point["angle"])


# END


def make_decart_point(x, y):
    return {"x": x, "y": y}


def get_x(point):
    return point["x"]


def get_y(point):
    return point["y"]


def get_quadrant(point):
    x = get_x(point)
    y = get_y(point)

    if x > 0 and y > 0:
        return 1
    if x < 0 < y:
        return 2
    if x < 0 and y < 0:
        return 3
    if y < 0 < x:
        return 4

    return None


def make_rectangle(left_high_point, width, height):
    right_high_point = make_decart_point(get_x(left_high_point) + width, get_y(left_high_point))
    left_low_point = make_decart_point(get_x(left_high_point), get_y(left_high_point) - height)
    right_low_point = make_decart_point(get_x(right_high_point), get_y(right_high_point) - height)
    return {
        'left_high_point': left_high_point,
        'right_high_point': right_high_point,
        'left_low_point': left_low_point,
        'right_low_point': right_low_point,
    }


def contains_origin(rectangle):
    return True if len({get_quadrant(point) for point in rectangle.values()}) == 4 else False


p = make_decart_point(0, 1)
rectangle = make_rectangle(p, 4, 5)

print(contains_origin(rectangle)) # False

rectangle2 = make_rectangle(make_decart_point(-4, 3), 5, 4)
print(contains_origin(rectangle2)) # True
