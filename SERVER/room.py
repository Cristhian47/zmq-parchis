class Room:
    MAX_PLAYERS = 4

    def __init__(self, identifier):
        self.identifier = identifier
        self.players = []

    def add_player(self, player):
        if len(self.players) < self.MAX_PLAYERS:
            self.players.append(player)
            return f"{player.color} joined room {self.identifier}"
        else:
            return f"Room {self.identifier} is full"

    def get_players(self):
        return [player.color for player in self.players]