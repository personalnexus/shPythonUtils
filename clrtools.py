from typing import Callable
import contextlib


@contextlib.contextmanager
def disposable(disposable_object):
    """
    Wraps a .NET object implementing IDisposable into a context manager for use in the with-statement
    :param disposable_object: the object implementing IDisposable (or more accurately, having an Dispose() method
    """
    try:
        yield disposable_object
    finally:
        disposable_object.Dispose()


@contextlib.contextmanager
def new_disposable(disposable_class: Callable, *args, **kwargs):
    """
    Wraps a .NET class implementing IDisposable (or more accurately, having an Dispose() method) into a context manager
    for use in the with-statement
    :param disposable_class: the class implementing IDisposable that is instantiated
    """
    disposable_object = disposable_class(*args, **kwargs)
    try:
        yield disposable_object
    finally:
        disposable_object.Dispose()
