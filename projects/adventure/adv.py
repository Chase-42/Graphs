from room import Room
from player import Player
from world import World

import random
# This is how everything is made possible. This maps out everything , it is actually
# showing us that the room 494 is east of 457
from ast import literal_eval

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"
# print(f' THIS IS THE ROOMS ------{room_graph}')

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)
# Print an ASCII map
world.print_rooms()
player = Player(world.starting_room)

traversal_path = []
roomstack = []
roomstack.append(player.current_room.id)
visitedrooms = set()

while len(visitedrooms) != len(world.rooms):
    # Grab the last thing , like we do in a bfs and append it to visited rooms.
    # We made roomstacks initial value to be the starting location, but wrote it outside the function
    currentroom = roomstack[-1]
    visitedrooms.add(currentroom)
    # We're going to need a list to act as queue
    queue = []
    # With the way the literal thing works, the second index, is the direction we KNOW another room is in

    neighbors = room_graph[currentroom][1]
    # We don't need to use get exit, because we already have the direction we know we need to go

    # For every room available, if we haven't been there , slap the room on the queue
    print(neighbors.values())
    for room in neighbors.values():
        if room not in visitedrooms:
            queue.append(room)
    # If queue exist, add the first thing in the queue to our roomstack
    if len(queue) > 0:
        roomstack.append(queue[0])
    else:
        roomstack.pop()
    for room in neighbors.items():
        # If the the room(at index one) is the same as the last thing in our roomstack, add the direction
        # index of 0, to the whole traversal path. Traversal path only understands strings.
        # to the traversal path
        if room[1] == roomstack[-1]:
            traversal_path.append(room[0])


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
