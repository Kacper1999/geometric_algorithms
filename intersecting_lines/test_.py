import unittest
from intersecting_lines import intersecting_lines_algorithm as cla
from intersecting_lines.Line import Line
from intersecting_lines.state_structure import StateStructure


class Test(unittest.TestCase):
    test_lines1 = [Line((0, 0), (2, 2)),
                   Line((0, 2), (2, 0))]
    test_lines2 = [Line((2, 2), (0, 0)),
                   Line((2, 0), (0, 2))]

    points = [(0, 0), (2, 2), (0, 2), (2, 0), (1, 1.5), (1.5, 2.5), (-1, 1), (-2, 3)]
    lines = []
    i = 0
    while i < len(points):
        lines.append(Line(points[i], points[i + 1]))
        i += 2

    def test_cross_point(self):
        self.assertEqual((1, 1), self.test_lines1[0].cross_point(self.test_lines1[1]))
        self.assertEqual((1, 1), self.test_lines2[0].cross_point(self.test_lines2[1]))

    def test_initialize_event_point(self):
        result = [(-2, 3), (-1, 1), (0, 0), (0, 2), (1, 1.5), (1.5, 2.5), (2, 0), (2, 2)]
        event_points = cla.initialize_event_points(self.lines)
        for i in range(len(result)):
            self.assertEqual(result[i], event_points[i])

    def test_associate_lines_and_points(self):
        lines_and_points = cla.associate_lines_and_points(self.lines)
        self.assertEqual(self.lines[0], lines_and_points[(2, 2)])
        self.assertEqual(self.lines[1], lines_and_points[(0, 2)])
        self.assertEqual(self.lines[2], lines_and_points[(1.5, 2.5)])
        self.assertEqual(self.lines[3], lines_and_points[(-2, 3)])

    def test_determine_event_type(self):
        self.assertEqual("left endpoint", cla.determine_event_type(self.lines[0], self.lines[0].a))
        self.assertEqual("right endpoint", cla.determine_event_type(self.lines[1], self.lines[1].b))
        self.assertEqual("left endpoint", cla.determine_event_type(self.lines[2], self.lines[2].a))
        self.assertEqual("right endpoint", cla.determine_event_type(self.lines[3], self.lines[3].b))
        self.assertEqual("crossing", cla.determine_event_type(self.lines[3], (4, 5)))

    def test_get_index(self):
        state_structure = StateStructure()
        for point in self.points:
            state_structure.add(point)
        sorted_points = [(0, 0), (2, 0), (-1, 1), (1, 1.5), (0, 2), (2, 2), (1.5, 2.5), (-2, 3)]
        for i, point in enumerate(sorted_points):
            self.assertEqual(i, state_structure.get_index(point))

    def test_are_crossing(self):
        self.assertTrue(self.lines[0].crosses(self.lines[1]))

        i = 1
        while i < len(self.lines) - 1:
            self.assertFalse(self.lines[i].crosses(self.lines[i + 1]))
            i += 1

    def test_initialize_state_structure(self):
        state_structure = StateStructure(self.points)
        sorted_points = [(0, 0), (2, 0), (-1, 1), (1, 1.5), (0, 2), (2, 2), (1.5, 2.5), (-2, 3)]

        for i, point in enumerate(state_structure.points):
            self.assertEqual(sorted_points[i], point)

    def test_add_point(self):
        state_structure = StateStructure(self.points)
        state_structure.add((0, -2))
        state_structure.add((3, 0))
        state_structure.add((1, 4))
        state_structure.add((-2, 1))

        sorted_points = [(0, -2), (0, 0), (2, 0), (3, 0), (-2, 1), (-1, 1),
                         (1, 1.5), (0, 2), (2, 2), (1.5, 2.5), (-2, 3), (1, 4)]

        for i, point in enumerate(state_structure.points):
            self.assertEqual(sorted_points[i], point)

    def test_change_position(self):
        state_structure = StateStructure(self.points)
        return 0


if __name__ == "__main__":
    unittest.main()
