import json
import logging
import requests
import os

log = logging.getLogger(__name__)  # initialize the logger
log.setLevel(logging.INFO)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s: '
                              '%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
ch.setFormatter(formatter)
log.addHandler(ch)

if 'API_KEY' not in os.environ:
    log.error("API_KEY env variable not set")
if 'API_SECRET' not in os.environ:
    log.error("API_SECRET env variable not set")
if 'JWT' not in os.environ:
    log.error("JWT env variable not set")
if 'APPLICATION_ID' not in os.environ:
    log.error("APPLICATION_ID env variable not set")
API_KEY = os.environ['API_KEY']
API_SECRET = os.environ['API_SECRET']
JWT = os.environ['JWT']
APPLICATION_ID = os.environ['APPLICATION_ID']


def list_conversation():
    url = 'https://api.nexmo.com/beta/conversations'
    # Change msisdn and country to match your virtual number
    headers = {'Authorization': 'Bearer ' + JWT,
               'Content-Type': 'application/json'}
    resp = requests.get(url, headers=headers)
    try:
        if resp.status_code == 200:
            log.info("SUCESSS!")
        else:
            print("HTTP Response: " + resp.status_code)
        print(json.dumps(resp.json(), indent=4))
    except requests.exceptions.HTTPError as e:
        print(e)


def create_conversation():
    url = 'https://api.nexmo.com/beta/conversations'
    # Change msisdn and country to match your virtual number
    headers = {'Authorization': 'Bearer ' + JWT,
               'Content-Type': 'application/json'}
    data = {'name': 'dummyConversation',
            'display_name': 'dummyConversation',
            'numbers': {
                'sms': '447520633345',
                'pstn': '447520633345'
                }
            }
    resp = requests.post(url, headers=headers, data=json.dumps(data))
    try:
        if resp.status_code == 200:
            log.info("SUCESSS!")
        else:
            print("HTTP Response: {}".format(resp.status_code))
        print(json.dumps(resp.json(), indent=4))
    except requests.exceptions.HTTPError as e:
        print(e)


def main():
    list_conversation()
    # create_conversation()


if __name__ == "__main__":
    main()
