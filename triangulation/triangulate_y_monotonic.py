from triangulation.y_monotonic import is_y_monotonic
from triangulation.check_orientation import check_orientation
from triangulation.Line import Line
from triangulation.get_objects import get_left_right_chains


# BIG ASSUMPTION input polygons must be given in anticlockwise manner!!!!


def pop_chain(left_chain, right_chain, vertex):
    if left_chain[0] == vertex:
        left_chain.pop(0)
        return "left"
    right_chain.pop(0)
    return "right"


def diagonal_inside(a, b, c, current_chain):
    if current_chain == "left":
        tmp = 1
    else:
        tmp = -1
    return check_orientation(a, b, c) == tmp


def triangulate_y_monotonic(polygon):
    if not is_y_monotonic(polygon):
        print("not y monotonic")
        return

    left_chain, right_chain = get_left_right_chains(polygon)
    left_chain.sort(key=lambda tup: (tup[1], tup[0]), reverse=True)
    right_chain.sort(key=lambda tup: (tup[1], tup[0]), reverse=True)
    left_chain.pop(0)  # we don't need the top most point in our chains
    right_chain.pop(0)

    vertices = sorted(polygon.vertices, key=lambda tup: (tup[1], tup[0]), reverse=True)
    stack = [vertices[0], vertices[1]]
    triangulation = []

    # pop_chain pops a beginning from a chain that contains a vertex (in our case vertices[1])
    # and returns "left", "right" respectively
    # top_stack_chain refers to the chain on which the top of the stack is
    top_stack_chain = pop_chain(left_chain, right_chain, vertices[1])

    for vertex in vertices[2:-1]:
        current_vertex_chain = pop_chain(left_chain, right_chain, vertex)
        if current_vertex_chain != top_stack_chain:
            stack.pop(0)
            prev = stack[-1]
            while stack:
                triangulation.append(Line(vertex, stack.pop()))
            stack.append(prev)
            stack.append(vertex)
        else:
            prev = stack.pop()
            currently_processed = stack[-1]
            while stack and diagonal_inside(currently_processed, prev, vertex, top_stack_chain):
                prev = currently_processed
                currently_processed = stack.pop()
                triangulation.append(Line(vertex, currently_processed))

            stack.append(prev)
            stack.append(vertex)
        top_stack_chain = current_vertex_chain
    for vertex in stack[1:-1]:
        triangulation.append(Line(vertices[-1], vertex))
    return triangulation


def main():
    pass


if __name__ == "__main__":
    main()
