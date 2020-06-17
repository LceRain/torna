import json
import time
from json import JSONEncoder

import tornado.web

from abase.baseResponse.baseresponse import JsonResponse
from abase.baseorm._sqlalchemy.basesqlal import session
from abase.baseorm.models.basemodels import Model
from apps.index.models import Person


class A(JSONEncoder):
    def default(self, o):
        if isinstance(o, Model):
            dic = o.__dict__
            print(dic)
            dic.pop("_sa_instance_state")
            return dic


class IndextHandler(tornado.web.RequestHandler):

    async def get(self):
        persons = Person.objects.filter(Person.name == 'jerry').all()
        print(persons)
        # p = Person(name='jerry', age=13)
        # session.add(p)
        # session.commit()
        jso = {'data': persons}
        print(jso)
        self.write(json.dumps(jso, cls=A))

