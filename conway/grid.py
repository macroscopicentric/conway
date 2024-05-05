from conway.cell import Cell


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
