import falcon
import json

class STT:
    def __init__(self, game):
        self.game = game

    @staticmethod
    def on_get(req, resp):
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        body = req.stream.read()
        json_body = json.loads(body.decode('utf-8'))
        uuid = json_body['uuid']
        answers = json_body['speech']['results']
        # success = self.game.answer(answers)
        # question, expected_answer = self.game.next_question()
        success = 'forty two' in [a['text'] for a in json_body['speech']['results']]
        question = 'What is the answer to life the universe and everything?'
        expected_answer = ['forty two']
        new_ncco = []
        if success:
            action = {
                "action": "talk",
                "text": f"Good, thank you. Next question: {question}",
                "voiceName": "Amy",
                "bargeIn": False
            }
        else:
            action = {
                "action": "talk",
                "text": f"That didn't work. Next question: {question}",
                "voiceName": "Amy",
                "bargeIn": False
            }
        new_ncco.append(action)
        new_input = [
            {
                "action": "input",
                "speech": {
                    "context": expected_answer,
                    "language": "en-gb",
                    "uuid": [f"{uuid}"],
                    "endOnSilence": 2
                },
                "eventUrl": ["http://6e3d2257.ngrok.io/stt"],
            },
            {
                "action": "talk",
                "text": "Thanks for your input, please hold.",
                "voiceName": "Amy"
            }
        ]
        new_ncco += new_input
        resp.body = json.dumps(new_ncco)
        resp.status = falcon.HTTP_200
