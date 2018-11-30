class Session:
    def __init__(self, game_json):
        self.game_json = game_json
        self.current_step_id = self.game_json['steps'][0]['id']

    def get_next_step(self, answer_type, answer_content):
        steps = self.game_json['steps']
        current_step = steps[self.current_step_id]
        expected_type = current_step['expected']['type']
        expected_content = current_step['expected']['content']

        if expected_type != answer_type:
            return self.get_next_step_faillure()

        if expected_content == 'text':
            if self.text_match(expected_content, answer_content):
                return self.get_next_step_success()

    def text_match(self, expected, actual):
        words = actual.split("")
        for word in words:
            if expected.lower() == word.lower():
                return True
        return False

    def get_next_step_success(self):
        steps = self.game_json['steps']
        current_step = steps[self.current_step_id]
        if 'content' in current_step['on_success']:
            self.current_step_id = current_step['on_success']['content']
            current_step = steps[self.current_step_id]
            return current_step['type'], current_step['message']
        else:
            return None

    def get_next_step_faillure(self):
        steps = self.game_json['steps']
        current_step = steps[self.current_step_id]
        if 'content' in current_step['on_failure']:
            self.current_step_id = current_step['on_failure']['content']
            current_step = steps[self.current_step_id]
            return current_step['type'], current_step['message']
        else:
            return None
