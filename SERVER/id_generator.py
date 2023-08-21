import random
import string

class Identifier_Generator:

    def __init__(self):
        self.length = 4

    def generate_random_identifier(self):
        characters = string.ascii_letters + string.digits
        random_identifier = ''.join(random.choice(characters) for _ in range(self.length))
        return random_identifier
