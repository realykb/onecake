import falcon


class Status:
    @staticmethod
    def on_get(req, resp):
        print("In status method get")
        resp.status = falcon.HTTP_200

    @staticmethod
    def on_post(req, resp):
        print("In status method post")
        resp.status = falcon.HTTP_200

