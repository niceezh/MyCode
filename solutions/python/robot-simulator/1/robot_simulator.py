# Globals for the directions
# Change the values as you see fit
EAST = "EAST"
NORTH = "NORTH"
WEST = "WEST"
SOUTH = "SOUTH"


class Robot:

    TURN_LEFT = {
        NORTH: WEST,
        EAST: NORTH,
        SOUTH: EAST,
        WEST: SOUTH,
    }

    TURN_RIGHT = {
        NORTH: EAST,
        EAST: SOUTH,
        SOUTH: WEST,
        WEST: NORTH,
    }

    MOVE_FORWARD = {
        NORTH: lambda x, y: (x, y + 1),
        EAST: lambda x, y: (x + 1, y),
        SOUTH: lambda x, y: (x, y - 1),
        WEST: lambda x, y: (x - 1, y),
    }

    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)
    
    def move(self, commands):
        for command in commands:
            if command == 'L':
                self.direction = self.TURN_LEFT[self.direction]
                continue
            if command == 'R':
                self.direction = self.TURN_RIGHT[self.direction]
                continue
            if command == 'A':
                self.coordinates = self.MOVE_FORWARD[self.direction](self.coordinates[0], self.coordinates[1])
                continue


if __name__ == "__main__":
    robot = Robot(EAST, 0, 0)
    robot.move("LAAAA")
    print(robot.coordinates, robot.direction)
