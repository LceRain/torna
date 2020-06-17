from sqlalchemy import Column, String, Integer


class Field(Column):

    def __init__(self, *args, **kwargs ):

        super().__init__(*args, **kwargs)

    def __str__(self):
        return super().__str__()


class StringField(Field):

    def __init__(self, length, *args, **kwargs):
        if not length:
            raise ValueError('must be have length')

        super().__init__(String(length=length), *args, **kwargs)


class IntField(Field):

    def __init__(self, *args, **kwargs):

        super().__init__(Integer, *args, **kwargs)






