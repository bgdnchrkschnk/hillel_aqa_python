import abc

class BaseApiService(abc.ABC):


    @abc.abstractmethod
    def _post(self, **kwargs):
        ...

    @abc.abstractmethod
    def _get(self, **kwargs):
        ...

    @abc.abstractmethod
    def _put(self, **kwargs):
        ...

    @abc.abstractmethod
    def _delete(self, **kwargs):
        ...
