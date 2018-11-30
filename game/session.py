from location import Locator


class Session:
    def __init__(self, game_json):
        self.game_json = game_json
        self.current_step = self.get_step(1)
        self.locator = Locator()

    def get_step(self, id):
        for step in self.game_json['steps']:
            if step['id'] == id:
                return step
        return None

    def get_current_step(self):
        return self.current_step['message']['type'], self.current_step['message']['content']

    def get_next_step(self, answer_type, answer_content):
        expected_type = self.current_step['expected']['type']
        expected_content = self.current_step['expected']['content']

        if answer_type not in expected_type:
            return self.get_next_step_faillure()

        if 'location' in expected_type and 'location' in answer_type:
            if self.location_match(expected_content, answer_content):
                return self.get_next_step_success()
            else:
                return self.get_next_step_faillure()
        if 'text' in expected_type:
            if self.text_match(expected_content, answer_content):
                return self.get_next_step_success()
            else:
                return self.get_next_step_faillure()

    def location_match(self, expected, actual):
        lat, long = actual
        try:
            city = self.locator.get_city(lat, long)
        except KeyError:
            return False
        if city in expected:
            return True
        return False

    def single_text_match(self, expected, actual):
        words = actual.split()
        for word in words:
            if word.lower() in expected:
                print('true')
                return True
        print('false')
        return False

    def text_match(self, expected, actual):
        if isinstance(actual, list):
            for word in actual:
                if(self.single_text_match(expected, word)):
                    return True
            return False
        return self.single_text_match(expected, actual)

    def get_next_step_success(self):
        if 'on_success' not in self.current_step:
            return True, None, None
        if 'content' in self.current_step['on_success']:
            next_step_id = self.current_step['on_success']['content']
            self.current_step = self.get_step(next_step_id)
            return True, self.current_step['message']['type'], self.current_step['message']['content']
        else:
            return True, None, None

    def get_next_step_faillure(self):
        if 'on_failure' not in self.current_step:
            return False, None, None
        if 'content' in self.current_step['on_failure']:
            next_step_id = self.current_step['on_failure']['content']
            self.current_step = self.get_step(next_step_id)
            return False, self.current_step['message']['type'], self.current_step['message']['content']
        else:
            return False, None, None
