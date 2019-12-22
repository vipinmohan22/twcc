# Week 02

[Template File](./002_circuit_board.py)

You may add helper functions as needed

## Circuit Board
A circuit board has a jumble of wires. Specifically, two wires are
connected to a central port and extend outward on a grid. You trace the path
each wire takes as it leaves the central port.

The wires twist and turn, but the two wires occasionally cross paths. To fix the
circuit, you need to find the intersection point closest to the central port.
While the wires do technically cross right at the central port where they both
start, this point does not count, nor does a wire count as crossing with itself.

For example, if the first wire's path is `R8,U5,L5,D3`, then starting from the
central port (o), it goes right 8, up 5, left 5, and finally down 3:

```
...........
...........
...........
....+----+.
....|....|.
....|....|.
....|....|.
.........|.
.o-------+.
...........
```

Then, if the second wire's path is `U7,R6,D4,L4`, it goes up 7, right 6, down 4, and left 4:

```
...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
```

### PART A
Find all the intersection points

For the above example, the wires cross at two locations (marked X)
(3,3) and (6,5)


### PART B
Find the intersection point closest to the central port.
Because the wires are on a grid, use the [Manhattan
distance](https://en.wikipedia.org/wiki/Taxicab_geometry)[^1]
for this measurement.

For the above example, the wires cross at two locations (marked X) (3,3) and
(6,5), but the lower-left one (3,3) is closer to the central port: its distance is 3 +
3 = 6.


[^1]: Manhattan Distance from a point (x, y) to origin is |x| + |y|
