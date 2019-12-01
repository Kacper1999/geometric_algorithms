from bintrees import AVLTree
from voronoi_diagram.Structures import TaxiCabParabola


class StateStructure:
    def __init__(self, points):
        self.tree = AVLTree()
        for point in points:
            self.tree.insert(point.to_tuple(), point)

    def get_parabola_point_directly_above(self, point, sweep_line_position):
        tuple_point = point.to_tuple()
        next_point = None
        prev_point = None
        if self.tree.max_key() != tuple_point:
            next_point = self.tree.succ_item(tuple_point)
        if self.tree.min_key() != tuple_point:
            prev_point = self.tree.prev_item(tuple_point)
        parabola1 = None
        parabola2 = None
        if prev_point is not None:
            parabola1 = TaxiCabParabola(prev_point, sweep_line_position)
        if next_point is not None:
            parabola2 = TaxiCabParabola(next_point, sweep_line_position)
        if parabola1 is None:
            return parabola2.point
        if parabola2 is None:
            return parabola1.point
        cross_point = parabola1.proper_crossing_point(parabola2)
        if cross_point.x < point.x:
            return next_point
        return prev_point
