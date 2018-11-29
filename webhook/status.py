import falcon


class Status:
    @staticmethod
    def on_post(req, resp):
        print("In status method")
        resp.status = falcon.HTTP_200
