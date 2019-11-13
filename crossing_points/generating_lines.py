import random


def is_vertical(line, error=10 ** (-8)):
    if abs(line[0][0] - line[1][0]) < error:
        return True
    return False


def remove_problematic(lines, error=10 ** (-8)):
    for line in lines:
        if is_vertical(line):
            lines.remove(line)


def generate_lines(how_many=20, lower_bound=-100, upper_bound=100, error=10 ** (-8)):
    lines = []
    while len(lines) != how_many:
        x1 = random.uniform(lower_bound, upper_bound)
        y1 = random.uniform(lower_bound, upper_bound)
        x2 = random.uniform(lower_bound, upper_bound)
        y2 = random.uniform(lower_bound, upper_bound)
        a = (x1, y1)
        b = (x2, y2)
        line = [a, b]
        if is_vertical(line, error):
            continue
        lines.append(line)
