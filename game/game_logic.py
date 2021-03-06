import json
import re


class GameMaster(object):
    def __init__(self, name, game_id=0):
        self.name = name
        self._load(game_id)
        self.current_question = None

    def _load(self, game_id):
        self.game_json = json.load(game_id)
        self.credits = self.game_json['credits']
        self.game_json = self.game_json['questions']

    def start(self):
        self.current_question = q = self.game_json['start']
        return q['question']

    def get_game_response(self, user_input):
        try:
            answer = self.current_question['answers'][user_input.lower()]
            self.current_question = self.game_json[answer["next_question"]]
            return (answer['response'] + '\n' + self.current_question['question']).strip()
        except KeyError:
            q = self.current_question["question"]
            return "Please respond with an appropriate answer " + \
                   re.search(r".*\((.+)\)", q).group(1)

