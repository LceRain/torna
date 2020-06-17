import tornado.web

from apps.index.models import Person


class IndextHandler2(tornado.web.RequestHandler):

    def get(self):
        persons = Person.objects.all()
        jso = {'data': persons}
        self.write('im ok')