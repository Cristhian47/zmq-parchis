from room import Room

class Lobby:
    def __init__(self):
        self.rooms = {}

    def create_room(self, identifier):
        self.rooms[identifier] = Room(identifier)
        return f"Room {identifier} created"

    def join_room(self, identifier, player):
        if identifier in self.rooms:
            room = self.rooms[identifier]
            return room.add_player(player)
        else:
            return f"Room {identifier} does not exist"