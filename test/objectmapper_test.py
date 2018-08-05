import unittest
from objectmapper import *


class MapperTest(unittest.TestCase):
    def test_create_mapped_object(self):
        mapped_object = create_mapped_object(MyMappedObject1,
                                             {'value1': '12',
                                              'value2': 'bye',
                                              'value3': 'nothing',
                                              'valueB': 'false',
                                              'value5': '2.5',
                                              'valueN': None})
        self.assertIsTypedValue(12, mapped_object.value1)
        self.assertIsTypedValue('bye', mapped_object.value2)
        self.assertIsTypedValue(1.2, mapped_object.value4)
        self.assertIsTypedValue(2.5, mapped_object.value5)
        self.assertIsTypedValue(False, mapped_object.valueB)
        self.assertIsTypedValue(None, mapped_object.valueN)

    def test_map_object_with_no_match(self):
        mapped_object = MyMappedObject2()
        map_object(mapped_object, {'value3': '12'})
        self.assertIsNone(mapped_object.value1)
        self.assertRaises(TypeError, lambda: mapped_object.value3)

    def test_map_object_with_match(self):
        mapped_object = MyMappedObject2()
        map_object(mapped_object, {'value1': '12'})
        self.assertIsTypedValue('12', mapped_object.value1)

    def test_map_object_with_type_detection(self):
        mapped_object = MyMappedObject2()
        map_object(mapped_object, {'iValue1': '12'})
        self.assertIsTypedValue(12, mapped_object.value1)

    def test_type_detection(self):
        self.assertTypeDetection('theDate', 'dtTheDate', datetime.datetime)
        self.assertTypeDetection('anInteger', 'iAnInteger', int)
        self.assertTypeDetection('myString', 'sMyString', str)
        self.assertTypeDetection('somethingTrue', 'bSomethingTrue', bool)
        self.assertTypeDetection('s', None, None)
        self.assertTypeDetection('', None, None)
        self.assertTypeDetection(None, None, None)

    def assertTypeDetection(self, attribute_name, key, target_type):
        self.assertTupleEqual((target_type, key), detect_type(attribute_name, {key: None}))

    def assertIsTypedValue(self, expected_value, actual_value):
        self.assertEqual(expected_value, actual_value)
        self.assertIsInstance(actual_value, type(expected_value))


class MyMappedObject1(object):
    def __init__(self):
        super(MyMappedObject1, self).__init__()
        self.value1 = 1
        self.value2 = 'hello'
        self.value4 = 1.2
        self.value5 = 0.0
        self.valueB = True
        self.valueN = False


class MyMappedObject2(object):
    def __init__(self):
        super(MyMappedObject2, self).__init__()
        self.value1 = None

    @property
    def value3(self):
        return 3 * self.value1


if __name__ == '__main__':
    unittest.main()
