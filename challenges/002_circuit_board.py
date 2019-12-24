#!/usr/bin/env python3


def get_intersections(wire1, wire2):
    """
    Get intersections points between wire1 and wire2
    """
    pass


def get_closest_intersection(wire1, wire2):
    """
    Get closest intersection points between wire1 and wire2
    from origin
    """
    pass


# TEST1
# PART A
wire1 = ["R8", "U5", "L5", "D3"]
wire2 = ["U7", "R6", "D4", "L4"]

intersections = get_intersections(wire1, wire2)
assert (3, 3) in intersections
assert (6, 5) in intersections

# PART B
assert get_closest_intersection(wire1, wire2) == (3, 3)

# TEST2
# PART A
wire1 = ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"]
wire2 = ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]

intersections = get_intersections(wire1, wire2)

points = [(158, -12), (146, 46), (155, 4), (155, 11)]
for point in points:
    assert point in intersections

# PART B
assert get_closest_intersection(wire1, wire2) == (155, 4)
