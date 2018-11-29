import json

import falcon


class Answer:
    @staticmethod
    def on_get(req, resp):
        uuid = req.params.get("uuid")
        our_question = 'What is the answer to life the universe and everything'
        data = [
            {
                "action": "talk",
                "text": "Welcome to ONE CAKE Kangbo",
                "voiceName": "Amy",
                "bargeIn": False
            },
            {
                "action": "talk",
                "text": f"{our_question}.",
                "voiceName": "Amy",
                "bargeIn": True
            },
            {
                "action": "input",
                "speech": {
                    "context": ["forty two"],
                    "language": "en-gb",
                    "uuid": [f"{uuid}"],
                    "endOnSilence": 2  # 2<=endOnSilence<=10 default 2
                },
                "eventUrl": ["http://6e3d2257.ngrok.io/event"],
                "eventMethod": "POST"  # POST/GET default POST
            },
            {
                "action": "talk",
                "text": "Thanks for your input, please hold.",
                "voiceName": "Amy"
            }
        ]

        resp.body = json.dumps(data, ensure_ascii=False)
        resp.status = falcon.HTTP_200
