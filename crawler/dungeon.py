class Room:
    id_counter = 0
    room_list = []

    def __init__(self):
        print("init room")
        self.id = Room.id_counter
        Room.id_counter += 1

        Room.room_list.append(self)

        self.color = "red"
        self.connection_list = list() #ooo I can make connections non-mutual to make one-way connections

    def __str__(self):
        return "room {}".format(self.id)

r1 = Room()
r2 = Room()

"""print(r1.id)
print(r2.id)
print(r1.color)"""


#generates rooms
for i in range(0, 6):
    new_room = Room()
    new_room.connection_list.append(new_room.id + 1)
    #Room.room_list.append(new_room)


#naviagte rooms
active_room = Room.room_list[2]
for asdf in range(0, 10):
    print("You are in room {}".format(active_room.id))
    print("Possible destinations: {}".format(active_room.connection_list))
    try:
        response = int(input("Enter destination: "))
    except ValueError:
        print("that's not an integer \n")
        continue

    if response in active_room.connection_list:
        active_room = Room.room_list[response]
    else:
        print("that isn't in the destination list \n")
