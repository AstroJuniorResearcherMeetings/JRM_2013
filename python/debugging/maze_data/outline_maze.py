#makes empty maze files which have wall characters all along the outside edge

import sys

nx, ny, out_file_name = sys.argv[1:]

nx = int(nx)
ny = int(ny)

wall_char = "#"
path_char = " "

out_file = open(out_file_name, "w")

#write out the top edge
out_file.write(wall_char*(nx+2) + "\n")

#write out the middle
for row in range(ny):
    out_file.write(wall_char + (nx)*path_char + wall_char + "\n")

#write out the bottom edge
out_file.write(wall_char*(nx+2) + "\n")

out_file.close()
