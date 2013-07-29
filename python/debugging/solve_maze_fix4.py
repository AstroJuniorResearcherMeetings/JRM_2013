

#  import modules
import numpy as np

# direction strings
n = "n"
s = "s"
e = "e"
w = "w"

class Maze:
    """a class that encapsulates the idea of a simple maze
    """

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
        """return true if you can move direction from position"""
        new_x, new_y = self.move(position, direction)
        check_direction = not self.walls[new_x, new_y]
        return check_direction

    def move(self, position, direction):
        """get your position after moving a direction"""
        x, y = position
        delta_x, delta_y = self.direction_deltas[direction]
        return x+delta_x, y+delta_y
        
    def get_neighbors(self, position):
        """return a list of all open neighboring positions and their directions"""
        neighbors = []
        directions = []
        # note we used dir_ instead of dir as short for direction
        # this is because dir is a reserved python key word
        # so to avoid overwriting it we have appended an underscore 
        # which is standard python
        for dir_ in [n, s, e, w]: # for each direction
            # check if we can go that direction
            if self.validate_move(position, dir_):
                # if we can add the new position to our neighbors list
                neighbors.append(self.move(position, dir_))
                directions.append(dir_)
        # return a list of neighbors and directions for getting there
        return neighbors, directions
    
    def solve_me(self):
        #  add the start to positions to process
        positions = [self.start]
        #  the path to the start node is the null string
        paths = [""]
        #  we should keep track of where we have visited
        visited = np.zeros(self.walls.shape, dtype = bool)
        visited[self.start] = True
        #import pdb; pdb.set_trace()
        while len(positions) > 0:
            # get the next position to check
            cur_pos = positions.pop()
            # and the associated path to it
            cur_path = paths.pop()
            # get all valid moves from that position
            neighbors, directions = self.get_neighbors(cur_pos)
            for neighbor_idx in range(len(neighbors)):
                cur_neighbor = neighbors[neighbor_idx]
                cur_direction = directions[neighbor_idx]
                # if the neighbor is not one we have visited before
                if visited[cur_neighbor]:
                    # form the path from the start to the neighbor
                    new_path = cur_path + cur_direction
                    # if this neighbor is the end position we found a solution
                    if cur_neighbor == self.end:
                        return new_path
                    # mark the new position as visited
                    visited[cur_neighbor] = True
                    # and add it to the positions to be processed
                    positions.append(cur_neighbor)
                    # along with the path to it
                    paths.append(new_path)
        # if we don't find a solution there isn't one
        print "I'm Unsolvable!"
        return None
                    

def load_maze(file_name, wall_char="#", start_char="S", end_char="E"):
    """loads a maze from a file,
    The mazes must be rectangular and bordered with the wall char.
    a maze file must have only a single start_char and a single end_char
    defining the start and finish points of the maze.
    """
    # open the file and read the lines
    maze_lines = open(file_name).readlines()
    # find the dimensions of the maze
    n_rows = len(maze_lines)
    n_cols = len(maze_lines[0].rstrip())
    #import pdb; pdb.set_trace()
    walls = [[] for i in range(n_rows)]
    # iterate over the rows and columns
    for row_idx in range(n_rows):
        for col_idx in range(n_cols):
            cur_char = maze_lines[row_idx][col_idx]
            # if we have a wall character mark wall as true
            if cur_char == wall_char:
                #import pdb; pdb.set_trace()
                walls[row_idx].append(True)
            else:
                walls[row_idx].append(False)
                # check for start and finish points
                if cur_char == start_char:
                    start_pos = row_idx, col_idx
                elif cur_char == end_char:
                    end_pos = row_idx, col_idx
    walls = np.array(walls, dtype = bool)

    # creating an instance/object of the Maze class
    maze_object = Maze(walls, start_pos, end_pos)
    return maze_object

if __name__ == "__main__":
    import sys
    # check that we have a maze file name passed in and only one
    assert len(sys.argv) == 2
    # get the filename from the command line
    maze_name = sys.argv[1]
    # load the maze
    maze = load_maze(maze_name)
    # make it solve itself
    soln =  maze.solve_me()
    print "a solution is", soln
