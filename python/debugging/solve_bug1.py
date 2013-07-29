import numpy as np

start_char = "S"
end_char = "E"
wall_char = "#"

#direction strings
n = "n"
s = "s"
e = "e"
w = "w"

reversed_directions = {n:s, s:n, e:w, w:e}

def reverse_path(path_str):
    reversed_path = ""
    for dir_ in path_str:
        reversed_path += reversed_directions[dir_]
    return reversed_path

class Maze:

    def __init__(self, walls, start_position, end_position):
        """an object that represents a maze.
        walls should be a 2d array of truth values true where there are walls
        and false where there are none.
        start_position and end_position are the locations of the 
        start and end of the maze.
        """
        self.walls = walls
        self.start = start_position
        self.end = end_position
        self.direction_deltas = {n:(-1, 0), s:(1, 0), e:(0, 1), w:(0, -1)}

    def validate_move(self, position, direction):
        """return true if you can move direction dir_ from position pos"""
        new_x, new_y = self.move(positoinn, direction)
        return not self.walls[new_x, new_y]

    def move(self, position, direction):
        x, y = position
        delta_x, delta_y = self.direction_deltas[direction]
        return x+delta_x, y+delta_y
        
    def get_neighbors(self, position):
        """return a list of all open neighboring positions and their directions"""
        neighbors = []
        directions = []
        for dir_ in [n, s, e, w]:
            if self.validate_move(position, dir_):
                neighbors.append(self.move(position, dir_))
                directions.append(dir_)
        return neighbors, directions

    def solve_me():
        positions = [self.start]
        paths = [""]
        visited = set([self.start])
        while len(positions) > 0:
            cur_pos = positions.pop()
            cur_path = paths.pop()
            neighbors, directions = self.get_neighbors(cur_pos)
            for neighbor_idx in range(len(neighbors)):
                cur_neighbor = neighbors[neighbor_idx]
                cur_direction = directions[neighbor_idx]
                if cur_neighbor not in visited:
                    new_path = cur_path + cur_direction
                    if cur_neighbor == self.end:
                        return new_path
                    visited.add(cur_neighbor)
                    positions.append(cur_neighbor)
                    paths.append(new_path)
        print "I'm Unsolvable!"
        return None
                    

def load_maze(file_name):
    maze_lines = open(file_name).readlines()
    n_rows = len(maze_lines)
    n_cols = len(maze_lines[0])
    walls = []
    for row_idx in range(n_rows):
        cur_walls = []
        for col_idx in range(n_cols):
            cur_char = maze_lines[row_idx][col_idx]
            if cur_char == wall_char:
                cur_walls.append(True)
            else:
                cur_walls.append(False)
                if cur_char == start_char:
                    start_pos = row_idx, col_idx
                elif cur_char == end_char:
                    end_pos = row_idx, col_idx
        walls.append(cur_walls)
    walls = np.array(walls)
    return Maze(walls, start_pos, end_pos)


if __name__ == "__main__":
    maze = load_maze("maze_data/big.maze")
    print maze.solve_me()
