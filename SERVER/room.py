from colors import Colors

class Room:
    MAX_PLAYERS = 4

    def __init__(self, identifier):
        self.identifier = identifier
        self.players = []
        self.players_colors = []

    def add_player(self, player):
        if len(self.players) < self.MAX_PLAYERS:
            player.color = self.assign_color()
            self.players.append(player)
            return f"{player.color} joined room {self.identifier}"
        else:
            return f"Room {self.identifier} is full"

    def get_players(self):
        return [player.color for player in self.players]
        
    def assign_color(self):
        for color in Colors.existing_colors:
            if not (color in self.players_colors):
                self.players_colors.append(color)
                return color
            
        return ""
        