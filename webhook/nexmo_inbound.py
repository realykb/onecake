import json
import logging
import os
import falcon
import requests

log = logging.getLogger(__name__)  # initialize the logger
log.setLevel(logging.INFO)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s: '
                              '%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
ch.setFormatter(formatter)
log.addHandler(ch)


class NexmoWebHook:
    def __init__(self):
        if 'JWT' not in os.environ:
            log.error("JWT env variable not set")
        if 'APPLICATION_ID' not in os.environ:
            log.error("APPLICATION_ID env variable not set")
        self.application_id = os.environ['APPLICATION_ID']
        self.jwt = os.environ['JWT']

    def send_text_message(self, from_id, to_id, text_content):
        url = 'https://api.nexmo.com/v0.1/messages'
        headers = {'Authorization': 'Bearer ' + self.jwt,
                   'Content-Type': 'application/json',
                   'Accept': 'application/json'}
        data = {
            "from": {"type": "messenger", "id": from_id},
            "to": {"type": "messenger", "id": to_id},
            "message": {
                "content": {
                    "type": "text",
                    "text": "Kangbo is a bitch"
                }
            }
        }

        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
        if resp.status_code == 202:
            log.info('message sent')
        else:
            log.error(f"error {resp.status_code} while sending message: {resp.json()}")

    def on_post(self, req, resp):
        body = req.stream.read()
        if not body:
            raise falcon.HTTPBadRequest('Empty request body',
                                        'A valid JSON document is required.')

        try:
            body = json.loads(body.decode('utf-8'))
            from_id = body['to']['id']
            to_id = body['from']['id']
            self.send_text_message(from_id, to_id, 'my message')
        except (ValueError, UnicodeDecodeError):
            raise falcon.HTTPError(falcon.HTTP_753,
                                   'Malformed JSON',
                                   'Could not decode the request body. The '
                                   'JSON was incorrect or not encoded as '
                                   'UTF-8.')

        resp.status = falcon.HTTP_200

    def on_get(self, req, resp):
        body = req.stream.read()
        if not body:
            raise falcon.HTTPBadRequest('Empty request body',
                                        'A valid JSON document is required.')

        try:
            req.context['body'] = json.loads(body.decode('utf-8'))
        except (ValueError, UnicodeDecodeError):
            raise falcon.HTTPError(falcon.HTTP_753,
                                   'Malformed JSON',
                                   'Could not decode the request body. The '
                                   'JSON was incorrect or not encoded as '
                                   'UTF-8.')

        resp.status = falcon.HTTP_200
