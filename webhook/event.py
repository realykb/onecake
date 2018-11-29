import falcon


class Event:
    @staticmethod
    def on_get(req, resp):
        resp.status = falcon.HTTP_200

    @staticmethod
    def on_post(req, resp):
        resp.status = falcon.HTTP_200
