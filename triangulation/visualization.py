from configuration_for_visualization import *
from triangulation.triangulate_y_monotonic import get_left_right_chains, pop_chain, diagonal_inside
from triangulation.get_objects import lines_collection_to_lines, lines_to_lines_collection
from triangulation.points_classification import classify_points
from triangulation.y_monotonic import is_y_monotonic
from triangulation.Polygon import Polygon
from triangulation.Line import Line


def visualize_point_classification(scene=None):
    if scene is None:
        lines_collection = get_scene().lines[0]
    else:
        lines_collection = scene.lines[0]
    lines = lines_collection_to_lines(lines_collection)
    polygon = Polygon(lines)

    start_p, end_p, merge_p, split_p, regular_p = classify_points(polygon)

    scenes = [Scene([PointsCollection(start_p, color='lime'),
                     PointsCollection(end_p, color='red'),
                     PointsCollection(merge_p, color='darkblue'),
                     PointsCollection(split_p, color='cyan'),
                     PointsCollection(regular_p, color='peru')],
                    [lines_collection])]
    plot = Plot(scenes)
    plot.draw()


def visualize_left_right_chain():
    lines_collection = get_scene().lines[0]
    lines = lines_collection_to_lines(lines_collection)
    polygon = Polygon(lines)
    left_chain, right_chain = get_left_right_chains(polygon)
    scenes = [Scene([PointsCollection(left_chain, color='lime'),
                     PointsCollection(right_chain, color='red')],
                    [lines_collection])]
    plot = Plot(scenes)
    plot.draw()


def add_triangulation_scene(scenes, polygon, triangulation, stack, vertex, to=None):
    if to is not None:
        diagonal = [[vertex, to]]
    else:
        diagonal = []
    tmp = stack.copy()
    scene = Scene([PointsCollection(polygon.vertices, color="blue"),
                   PointsCollection(tmp, color="gold"),
                   PointsCollection([vertex], color="crimson")],
                  [lines_to_lines_collection(polygon.lines, "blue"),
                   lines_to_lines_collection(triangulation, "lime"),
                   LinesCollection(diagonal, color="gold")])
    scenes.append(scene)


def visualize_triangulation(polygon):
    if not is_y_monotonic(polygon):
        print("not y monotonic")
        return

    scenes = []

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
        add_triangulation_scene(scenes, polygon, triangulation, stack, vertex)
        current_vertex_chain = pop_chain(left_chain, right_chain, vertex)

        if current_vertex_chain != top_stack_chain:
            stack.pop(0)
            prev = stack[-1]
            while stack:
                triangulation.append(Line(vertex, stack.pop()))
                add_triangulation_scene(scenes, polygon, triangulation, stack, vertex)
            stack.append(prev)
            stack.append(vertex)
        else:
            prev = stack.pop()
            while stack:
                currently_processed = stack[-1]
                add_triangulation_scene(scenes, polygon, triangulation, stack, vertex, currently_processed)
                if diagonal_inside(currently_processed, prev, vertex, top_stack_chain):
                    prev = currently_processed
                    stack.pop()
                    triangulation.append(Line(vertex, currently_processed))
                    add_triangulation_scene(scenes, polygon, triangulation, stack, vertex)
                else:
                    break

            stack.append(prev)
            stack.append(vertex)
        top_stack_chain = current_vertex_chain

    if stack[1:-1]:
        add_triangulation_scene(scenes, polygon, triangulation, stack, vertices[-1])

    for vertex in stack[1:-1]:
        triangulation.append(Line(vertices[-1], vertex))
        add_triangulation_scene(scenes, polygon, triangulation, stack, vertices[-1])

    plot = Plot(scenes)
    plot.draw()


def main():
    visualize_point_classification()



if __name__ == "__main__":
    main()
