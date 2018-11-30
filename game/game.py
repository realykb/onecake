import json
from session import Session


class Game(object):
    def __init__(self, file_path='resources/game_1.json'):
        self._load(file_path)
        self.sessions = {}

    def _load(self, file_path):
        with open(file_path, 'rt') as file_content:
            self.game_json = json.load(file_content)
            self.credits = self.game_json['credits']
            self.game_json = self.game_json['questions']

    def get_next_step(self, id, content_type, content):
        if id in self.sessions:
            return self.sessions[id].get_next_step(content_type, content)
        else:
            self.sessions[id] = Session(self.game_json)
            return self.sessions[id]
