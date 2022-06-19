from __future__ import annotations
from abc import ABC, abstractmethod
from xmlrpc.client import Boolean
from django.conf import settings
from django.core.files.storage import FileSystemStorage


class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def upload_file(self, file):
        pass


class Context:
    """
    The Context defines the interface of interest to clients.
    """

    def __init__(self, strategy: Strategy) -> None:
        """
        Usually, the Context accepts a strategy through the constructor, but
        also provides a setter to change it at runtime.
        """

        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """

        self._strategy = strategy

    def uploading_file(self, file) -> Boolean:
        """
        The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        """

        result = self._strategy.upload_file(file)
        return result


"""
Concrete Strategies implement the algorithm while following the base Strategy
interface. The interface makes them interchangeable in the Context.
"""


"""
    Strategy to upload file into the localdrive or local directory, as per given path in MEDIA_ROOT in django settings file.
Raises:
    ValueError: will be raise if there will be any issue in stroing or uploading file.

Returns:
    str: will return the path where of uploaded file.
"""


class LocalDriveUploadStrategy(Strategy):
    def upload_file(self, file) -> str:
        try:
            fs = FileSystemStorage(location=settings.MEDIA_ROOT)
            file = fs.save(file.name, file)
            fileurl = fs.url(file)
            return fileurl
        except Exception:
            raise ValueError({"error": "Issue while uploading file"})


""" 
    Mock Strategy for future implementation for uploading file over Cloud.
Returns:
    str: dummy_url
"""


class CloudFileUploadStrategy(Strategy):
    def upload_file(self, file) -> str:
        dummy_url = "local/testing_file"
        return dummy_url
