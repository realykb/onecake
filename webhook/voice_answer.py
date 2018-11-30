import json

import falcon


class Answer:
    def __init__(self, game):
        self.game = game

    def on_get(self, req, resp):
        uuid = req.params.get("uuid")
        success, q_type, q = self.game.get_next_step(id, 'text', None)
        #question = self.game.first_question[uuid].get('question')
        question = 'What is the answer to life the universe and everything'
        data = [
            {
                "action": "talk",
                "text": f"Welcome to ONE CAKE Kangbo. {question}",
                "voiceName": "Amy",
                "bargeIn": False
            },
            {
                "action": "input",
                "speech": {
                    "context": ["forty two"],
                    "language": "en-gb",
                    "uuid": [f"{uuid}"],
                    "endOnSilence": 2
                },
                "eventUrl": ["http://6e3d2257.ngrok.io/stt"],
            }
        ]

        resp.body = json.dumps(data, ensure_ascii=False)
        resp.status = falcon.HTTP_200
