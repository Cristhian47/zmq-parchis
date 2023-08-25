import json
from server import Boards

class InGameRequestHandler:
    def __init__(self):
        self.game_data = {}

    def load_game_data(self):
        with open("game_board.json", "r") as file:
            self.game_data = json.load(file)

    def handle_game_request(self, message):
        parts = message.split(" ")

        if len(parts) < 3:
            return "Invalid request"

        game_id = int(parts[0])
        color = parts[1]
        position = int(parts[2])
        piece_id = int(parts[3])

        if game_id not in Boards:
            return "Game not found"

        board, _, _ = Boards[game_id]

        if color not in board or position not in board["seguros"]:
            return "Invalid move"

        player_data = board[color]
        player_pieces = player_data["fichas"]

        for piece in player_pieces:
            if piece["id"] == piece_id:
                piece["posicion"] = position
                break

        self.save_game_data()

        return self.get_updated_board_json(board)

    def save_game_data(self):
        with open("game_board.json", "w") as file:
            json.dump(self.game_data, file, indent=4)

    def get_updated_board_json(self, board):
        return json.dumps(board, indent=4)

if __name__ == "__main__":
    handler = InGameRequestHandler()
    handler.load_game_data()

    while True:
        message = input("Enter game request: ")
        response = handler.handle_game_request(message)
        print("Response:", response)