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
API_KEY = os.environ['API_KEY']
API_SECRET = os.environ['API_SECRET']


url = 'https://api.nexmo.com/v1/applications'
data = {
        'api_key': API_KEY,
        'api_secret': API_SECRET,
        'name' : 'dummyApp',
        'type' : 'jhsvk',
        'answer_url' : 'https://nexmo-community.github.io/ncco-examples/conference.json',
        'event_url' : 'https://example.com/call_status'
}
# In this example, answer_url points to a static NCCO that creates a Conference.

resp = requests.post(url, params=data)

try:
    if resp.status_code == 201:
        application = resp.json()
        log.info("Application " + application['name'] + " has an ID of: " + application['id'])
        print(json.dumps(application, indent=4))
    else:
        log.info("HTTP Response: " + resp.status_code)
        log.info(resp.json())

except requests.exceptions.HTTPError as e:
    log.error(e)
