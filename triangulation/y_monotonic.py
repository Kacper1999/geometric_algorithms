from triangulation.check_orientation import below


def check_monotonic(start, stop, vertices, mode):
    length = len(vertices)
    while start != stop:
        a = vertices[start]
        b = vertices[(start + mode) % length]
        if below(a, b):  # a below b
            return False
        start = (start + mode) % length
    return True


def is_y_monotonic(polygon):
    top = max(polygon.vertices, key=lambda tup: (tup[1], tup[0]))
    bot = min(polygon.vertices, key=lambda tup: (tup[1], tup[0]))
    start = polygon.vertices.index(top)
    stop = polygon.vertices.index(bot)

    return check_monotonic(start, stop, polygon.vertices, -1) and check_monotonic(start, stop, polygon.vertices, 1)


def main():
    pass


if __name__ == "__main__":
    main()
