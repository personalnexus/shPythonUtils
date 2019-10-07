import unittest
import inspectiontools


class ImportTest(unittest.TestCase):

    def test_import_functions_into_this_module(self):
        self.import_functions_core(
            lambda: inspectiontools.import_functions(inspectiontools))

    def test_import_all_functions_into_this_module(self):
        self.import_functions_core(
            lambda: inspectiontools.import_functions(inspectiontools, lambda n: n.startswith('import_')))

    def import_functions_core(self, core_func):
        import sys
        current_module = sys.modules[__name__]
        # make sure no import is left over from a previous call
        if hasattr(current_module, 'import_functions'):
            delattr(current_module, 'import_functions')
        core_func()
        self.assertTrue('import_functions' in dir(current_module))


if __name__ == '__main__':
    unittest.main()
