# encoding: utf-8

from django.conf import settings

conn = settings.MONGOCLIENT['test']


class User(object):
    db = conn['user']

    @classmethod
    def insert(cls, **params):
        return cls.db.insert(params)

    @classmethod
    def get(cls, **params):
        return cls.db.find(params)

    @classmethod
    def update(cls, _id, **params):
        cls.db.update({'_id': _id}, {'$set': params})


data = {'_id': '123456', 'name': 'tom', 'age': 30}
result = User.insert(**data)

