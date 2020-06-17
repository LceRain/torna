from abase.baseorm.fields.basefield import IntField, StringField
from abase.baseorm.models.basemodels import Model


class Person(Model):
    __tablename__ = 'person'
    id = IntField(primary_key=True)
    name = StringField(length=30)
    age = IntField()

