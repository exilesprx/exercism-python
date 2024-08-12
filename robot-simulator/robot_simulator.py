# Globals for the directions
# Change the values as you see fit
EAST = "east"
NORTH = "north"
WEST = "west"
SOUTH = "south"

movement_manual = {
    "north": {"left": WEST, "right": EAST, "advance": (0, 1)},
    "east": {"left": NORTH, "right": SOUTH, "advance": (1, 0)},
    "south": {"left": EAST, "right": WEST, "advance": (0, -1)},
    "west": {"left": SOUTH, "right": NORTH, "advance": (-1, 0)},
}


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def move(self, instructions):
        for instruction in instructions:
            if instruction == "L":
                self._turn_left()
            if instruction == "R":
                self._turn_right()
            if instruction == "A":
                self._advance()

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction):
        if direction not in ("north", "east", "south", "west"):
            raise ValueError("Invalid direction")
        self._direction = direction

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        self._coordinates = coordinates

    def _turn_left(self):
        self.direction = movement_manual[self.direction]["left"]

    def _turn_right(self):
        self.direction = movement_manual[self.direction]["right"]

    def _advance(self):
        x, y = self.coordinates
        self.coordinates = (
            x + movement_manual[self.direction]["advance"][0],
            y + movement_manual[self.direction]["advance"][1],
        )
