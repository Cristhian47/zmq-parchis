import zmq

class jugador:
    def __init__(self, color, game_id, port_brodcast):
        self.color = color
        self.game_id = game_id
        self.port_brodcast = port_brodcast