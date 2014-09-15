import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader= jinja2.FileSystemLoader(os.path.dirname(__file__)+"/templates"))

form = """      <form method="post">
                    Cuando es tu cumpleanos?
                    <br>
                    <label>Mes
                    <input type="text" name="mes">
                    </label>
                    <label>Dia
                    <input type="text" name="dia">
                    </label>
                    <label>ano
                    <input type="text" name="ano">
                    </label>
                    <br>
                    <input type="submit">
                </form>
                """
class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)

    def post(self):
        self.response.write("Gracias")


app = webapp2.WSGIApplication([('/', MainHandler)], debug=True)
