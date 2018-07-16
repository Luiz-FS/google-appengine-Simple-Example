import webapp2
import json


class MainHandler(webapp2.RequestHandler):
    def get(self):
        message = {
            'msg': 'Hello Horld!'
        }

        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(json.dumps(message))


app = webapp2.WSGIApplication([
    ('/api/hello', MainHandler)
], debug=True)