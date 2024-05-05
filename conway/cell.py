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
