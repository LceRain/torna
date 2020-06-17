# _*_ coding: utf8 _*_
from abase.baseorm._sqlalchemy.basesqlal import Base, session, Session
from abase.baseorm.fields.basefield import Field, StringField, IntField


# class ModelMetaClass(type):
#     __table__ = 'person'
#
#     def __new__(cls, name, bases, attrs):
#         if name == 'Model':
#             return type.__new__(cls, name, bases, attrs)
#         __mappings__ = dict()
#         for k, v in attrs.items():
#             if isinstance(v, Field):
#                 __mappings__[k] = v
#         attrs['__mappings__'] = __mappings__
#
#         return type.__new__(cls, name, bases, attrs)
class Objects():

    def query(self):
        return session.query(self._cls)

    def __get__(self, instance, owner):
        self._cls = owner
        return self.query()

Base.objects = Objects()
Model = Base


if __name__ == '__main__':
    class Objects():

        def query(self):
            return session.query(self._cls)

        def __get__(self, instance, owner):
            self._cls = owner
            return self.query()


    class Person(Model):
        __tablename__ = 'person'
        id = IntField(primary_key=True)
        name = StringField(length=30)
        age = IntField()

        # class ObjMataclss(type):
        #
        #     def __init__(cls, classname, bases, dict_):
        #         print(cls)
        #         type.__init__(cls, classname, bases, dict_)
        #
        # def xxx(self, name="Base", cls=object, metaclass=ObjMataclss):
        #
        #     bases = not isinstance(cls, tuple) and (cls,) or cls
        #     dict_ = dict()
        #     if isinstance(cls, type):
        #         dict_["__doc__"] = cls.__doc__
        #
        #     return metaclass(name,bases, dict_)
        #
        # class Objects(xxx):
        #
        #     def objects(self):
        #         return session.query(self._cls)

        # objects = Objects()


    s = Person.objects.filter(Person.name == 'jerry').all()[0].name


