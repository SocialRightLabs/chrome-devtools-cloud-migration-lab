import os
import datetime
import webapp2
import jinja2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    autoescape=True,
)


visits = []


class MainPage(webapp2.RequestHandler):
    def get(self):
        user_agent = self.request.headers.get('User-Agent', 'unknown')
        now = datetime.datetime.utcnow().strftime('%a %b %d %H:%M:%S %Y')
        visits.insert(0, '{} from {}'.format(now, user_agent))
        del visits[10:]

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render({'visits': visits}))


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
