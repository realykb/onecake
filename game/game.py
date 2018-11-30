import json
from session import Session


class Game(object):
    def __init__(self, file_path='game/resources/game_1.json'):
        self._load(file_path)
        self.sessions = {}

    def _load(self, file_path):
        with open(file_path, 'rt') as file_content:
            self.game_json = json.load(file_content)

    def get_current_step(self, id):
        if id not in self.sessions:
            self.sessions[id] = Session(self.game_json)
        return self.sessions[id].get_current_step()

    def get_next_step(self, id, content_type, content):
        if id not in self.sessions:
            self.sessions[id] = Session(self.game_json)
        return self.sessions[id].get_next_step(content_type, content)
