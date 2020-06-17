# _*_ coding: utf8 _*_
import json
from json import JSONEncoder

from abase.baseorm.models.basemodels import Model


class Response():

    def __init__(self, jsc):
        self.jsc = jsc

    def __call__(self, *args, **kwargs):
        return self.jsc

    def __repr__(self):
        return self.jsc


class JsonResponse(Response):

    class A(JSONEncoder):
        def default(self, o):
            if isinstance(o, Model):
                dic = o.__dict__
                dic.pop("_sa_instance_state")
                return dic

    def __init__(self, dic):
        if type(dic) == dict:
            jsc = json.dumps(dic, cls=self.A)
        else:
            raise ValueError('the argument must be dict')
        super().__init__(jsc)


if __name__ == '__main__':
    c = JsonResponse({1: 1, 2: 3, 3: 4})
    print(c, isinstance(c, str))




