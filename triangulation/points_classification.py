import triangulation.check_orientation as check_o


def classify_points(polygon):
    start_p = []
    end_p = []
    merge_p = []
    split_p = []
    regular_p = []

    prev = polygon.vertices[-1]
    for i, point in enumerate(polygon.vertices):
        following = polygon.vertices[(i + 1) % len(polygon.vertices)]

        if check_o.above(point, prev) and check_o.above(point, following):
            if check_o.check_orientation(prev, point, following) == 1:
                start_p.append(point)
            else:
                split_p.append(point)
        elif check_o.below(point, prev) and check_o.below(point, following):
            if check_o.check_orientation(prev, point, following) == 1:
                end_p.append(point)
            else:
                merge_p.append(point)
        else:
            regular_p.append(point)
        prev = point
    return start_p, end_p, merge_p, split_p, regular_p


def main():
    pass


if __name__ == "__main__":
    main()
