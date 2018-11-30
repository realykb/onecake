import json

import falcon


class Answer:
    question_dict = {}
    
    def on_get(self, req, resp):
        uuid = req.params.get("uuid")
        our_question = 'What is the answer to life the universe and everything'
        self.question_dict[uuid] = our_question
        data = [
            {
                "action": "talk",
                "text": f"Welcome to ONE CAKE Kangbo. {our_question}",
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
            },
            {
                "action": "talk",
                "text": "Thanks for your input, please hold.",
                "voiceName": "Amy"
            }
        ]

        resp.body = json.dumps(data, ensure_ascii=False)
        resp.status = falcon.HTTP_200
