class Room:
    id_counter = 0
    room_dict = {} #eventually make different dungeons w/ own room dict possible?

    def __init__(self):
        print("init room")
        self.id = Room.id_counter
        Room.id_counter += 1

        Room.room_dict.update({self.id : self})

        self.color = "red"
        self.connection_set = set() #ooo I can make connections non-mutual to make one-way connections
        self.occupant_set = set()

    def __str__(self):
        return "room {}".format(self.id)

r1 = Room()
r2 = Room()

"""print(r1.id)
print(r2.id)
print(r1.color)"""


def generate_default_rooms():
    #generates rooms
    final_room_connection_set = set()

    for i in range(0, 6):
        new_room = Room()
        new_room.connection_set.add(new_room.id + 1)
        final_room_connection_set.add(new_room.id)
        new_room.add_occupants({fight.Enemy()})

    new_room.connection_set = final_room_connection_set



"""generate_default_rooms()
active_room = Room.room_list[2]
active_room.print_room_info()"""

#naviagte rooms
def navigate_rooms():
    global active_room #future: fix this being global


    while True:
        try:
            response = int(input("Enter destination: "))
            break
        except ValueError:
            print("that's not an integer \n")
            continue

    if response in active_room.connection_set:
        active_room = Room.room_dict[response]
    else:
        print("that isn't in the destination list \n")
