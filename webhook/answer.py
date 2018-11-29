import json

import falcon


class Answer:
    @staticmethod
    def on_get(req, resp):
        uuid = req.params.get("uuid")
        data = [
            {
                "action": "talk",
                "text": "Welcome to ONE CAKE Kangbo",
                "voiceName": "Amy",
                "bargeIn": False
            },
            {
                "action": "talk",
                "text": "What is 5 time 2378492.",
                "voiceName": "Amy",
                "bargeIn": True
            },
            {
                "action": "input",
                "submitOnHash": True,
                "timeOut": 10
            },
            {
                "action": "talk",
                "text": "Thanks for your input, goodbye.",
                "voiceName": "Amy"
            }
        ]

        resp.body = json.dumps(data, ensure_ascii=False)
        resp.status = falcon.HTTP_200
