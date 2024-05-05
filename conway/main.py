import argparse
import sys
import time

from conway.parser import Parser


class Cell:
    neighbors = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

    def __init__(self, liveness: int):
        self.liveness = liveness

    def __str__(self):
        if self.live():
            return "🟢"
        else:
            return "⚪️"

    def live(self):
        if self.liveness == 1:
            return True
        else:
            return False

    def find_neighbors(self, x, y, grid_width, grid_length):
        neighbors = []
        for neighbor_mod in Cell.neighbors:
            neighbor_x = x + neighbor_mod[0]
            neighbor_y = y + neighbor_mod[1]

            x_within_bounds = neighbor_x >= 0 and neighbor_x < grid_width
            y_within_bounds = neighbor_y >= 0 and neighbor_y < grid_length

            # if it's a valid neighbor (within bounds), add it to the array
            if x_within_bounds and y_within_bounds:
                neighbors.append({"x": neighbor_x, "y": neighbor_y})
        return neighbors

    def new_liveness(self, live_neighbor_count: int):
        # is the cell dead or alive?
        if live_neighbor_count < 2:
            cell_state = 0
        elif live_neighbor_count > 3:
            cell_state = 0
        elif live_neighbor_count == 3:
            cell_state = 1
        else:
            cell_state = self.liveness
        return cell_state


# grid is finite, must be length x and width y
class Grid:

    def __init__(self, starting_grid: list[list[int]]):
        self.grid = [[Cell(liveness) for liveness in row] for row in starting_grid]
        self.row_length = len(self.grid)
        self.column_length = len(self.grid[0])

    def __str__(self):
        stringified_rows = []
        for row in self.grid:
            string_of_row = f""
            for cell in row:
                string_of_row += str(cell)
            stringified_rows.append(string_of_row)
        return "\n".join(stringified_rows)

    # return entire grid after a single step
    def transition(self):
        new_grid = []
        # x is rows, y is columns
        current_x = 0
        current_y = 0

        while current_y < self.row_length:
            while current_x < self.column_length:
                # primary logic check
                # find all neighbors and check them for liveness
                cell = self.grid[current_y][current_x]
                neighbors = cell.find_neighbors(
                    current_x, current_y, self.column_length, self.row_length
                )
                live_neighbor_count = 0
                for neighbor_coordinates in neighbors:
                    neighbor = self.grid[neighbor_coordinates["y"]][
                        neighbor_coordinates["x"]
                    ]
                    if neighbor.live():
                        live_neighbor_count += 1

                # create and insert cell into temporary_grid in correct location
                if current_y == len(new_grid):
                    new_grid.append([])

                # print(f"new cell at {current_x}, {current_y} has {live_neighbor_count} live neighbors. all neighbors: {neighbors}")
                new_cell = Cell(cell.new_liveness(live_neighbor_count))
                new_grid[current_y].append(new_cell)

                current_x += 1

            current_y += 1
            current_x = 0

        self.grid = new_grid
        return self.grid


# this was mostly stolen off stack overflow
# (here: https://stackoverflow.com/questions/66615552/display-multi-line-python-console-ascii-animation)
# small helper function to remember the number of lines
# and cursor position after printing a grid
# so we can go back to the top when printing the next grid
def prep_terminal_for_animated_output(number_of_lines):
    # scroll up to make room for output
    print(f"\033[{number_of_lines}S", end="")
    # move cursor back up
    print(f"\033[{number_of_lines}A", end="")
    # save current cursor position
    print("\033[s", end="")


# similar to the above,
# small helper method to actually go back to the
# saved cursor position before printing the
# newest version of the grid
def treadmill_print(thingy):
    # restore saved cursor position
    print("\033[u", end="")
    print(thingy)


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "-f",
        help="the location of the json-formatted starter file",
        type=str,
        default="examples/blinker.json",
    )
    args = arg_parser.parse_args()

    parser = Parser(args.f)
    grid = Grid(parser.parse())
    prep_terminal_for_animated_output(grid.column_length)
    while True:
        treadmill_print(grid)
        grid.transition()
        time.sleep(1)


if __name__ == "__main__":
    main()
