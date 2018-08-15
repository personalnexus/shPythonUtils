import unittest
from clrtools import *


class MockDisposable:
    """
    Mock for a .NET class implementing IDisposable
    """
    def __init__(self):
        self.dispose_called = 0

    # noinspection PyPep8Naming
    def Dispose(self):
        self.dispose_called += 1


class MockDisposable2(MockDisposable):
    def __init__(self, text):
        super(MockDisposable2, self).__init__()
        self.text = text


class ClrToolsTestException(Exception):
    pass


class DisposableTest(unittest.TestCase):
    def test_disposable(self):
        with disposable(MockDisposable()) as mock:
            self.assertEquals(0, mock.dispose_called)
        self.assertEquals(1, mock.dispose_called)

    def test_disposable_on_exception(self):
        try:
            with disposable(MockDisposable()) as mock:
                self.assertEquals(0, mock.dispose_called)
                raise ClrToolsTestException()
        except ClrToolsTestException:
            pass
        self.assertEquals(1, mock.dispose_called)

    def test_new_disposable(self):
        with new_disposable(MockDisposable2, 'other text') as mock:
            self.assertEquals(0, mock.dispose_called)
            self.assertEquals('other text', mock.text)
        self.assertEquals(1, mock.dispose_called)

    def test_new_disposable_on_exception(self):
        try:
            with new_disposable(MockDisposable2, text='some text') as mock:
                self.assertEquals(0, mock.dispose_called)
                self.assertEquals('some text', mock.text)
                raise ClrToolsTestException()
        except ClrToolsTestException:
            pass
        self.assertEquals(1, mock.dispose_called)


if __name__ == '__main__':
    unittest.main()
