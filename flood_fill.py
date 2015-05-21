#-------------------------------------------------------------------------------
# Name:        flood_fill.py
#
# Author:      Akshay
#
# Created:     21-05-2015
#-------------------------------------------------------------------------------

import sys


text_map = """
........................#.....
........................#.....
........................#.....
.....######.............######
.....#....#....######.........
.....#....#....#....#.....#...
.....######....##.###.....#...
................#.#.......####
................#.#...........
######.....######.#######.....
#....#.....#............#.....
###..#.....#............#.....
###..#.....##############.....
#....#........................
######........................

"""

lines = text_map.strip().split('\n')
assert [x for x in lines if len(x) != len(lines[0])] == [], "WORLD string must be rectangular"

def create_world(textmap):
    lines = textmap.strip().split('\n')
    world = []
    world_width = len(lines[0])
    world_height = len(lines)

    for i in range(world_height):
        world.append(['']*world_width)

    for i in range(world_height):
        for j in range(world_width):
            world[i][j] = lines[i][j]
    return world


def print_world(world):
    world_height = len(world)
    world_width = len(world[0])


    for i in range(world_height):
        for j in range(world_width):
            sys.stdout.write(world[i][j])
        sys.stdout.write('\n')


def flood_fill(world, x, y, old_char, new_char):
    if old_char == None:
        old_char = world[x][y]

    if world[x][y] != old_char:
        return

    world_width = len(world[0])
    world_height = len(world)

    world[x][y] = new_char
    if x > 0:
        flood_fill(world,x-1,y,old_char,new_char)
    if y > 0:
        flood_fill(world,x,y-1,old_char,new_char)
    if x < world_height - 1:
        flood_fill(world, x+1,y,old_char,new_char)
    if y < world_width - 1:
        flood_fill(world, x,y+1,old_char, new_char)


def room_count(world):
    """Count number of rooms in world, where world is 2d character list."""
    world_height = len(world)
    world_width = len(world[0])

    count = -1 #outside area is not room.

    for x in range(world_height):
        for y in range(world_width):
            if world[x][y] == '.':
                flood_fill(world,x,y,'.','X')
                count += 1
    return count

def main():
    world = create_world(text_map)
    print_world(world)
    print ('\n\n\n')
##    flood_fill(world, 5, 6, '.', 'X')
    print ('Num of rooms ' + str(room_count(world)))

if __name__ == '__main__':
    main()
