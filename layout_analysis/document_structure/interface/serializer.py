# coding:utf-8
import abc


class Serializer(object):

    @abc.abstractmethod
    def serialization(self, resource):
        pass

    @classmethod
    @abc.abstractmethod
    def deserialization(cls, resource):
        pass
