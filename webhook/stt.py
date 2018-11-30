import falcon
import json


game = {'What is the answer to life the universe and everything': 'forty two'}

class STT:
    def __init__(self, answer_class):
        self.ans_class = answer_class

    @staticmethod
    def on_get(req, resp):
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        body = req.stream.read()
        json_body = json.loads(body.decode('utf-8'))
        uuid = json_body['uuid']
        question = self.ans_class.question_dict[uuid]
        answer = game.get(question)
        correct_answer = False
        for answers in json_body['speech']['results']:
            if answers['text'] == answer:
                print(f'play audio to call "{uuid}" (next question)')
                correct_answer = True
                break
        if not correct_answer:
            print(f'play audio to call "{uuid}" (repeat question)')
        # TODO somehow get back to new ncco
        resp.status = falcon.HTTP_200
