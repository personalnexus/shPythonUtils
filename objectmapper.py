from typing import Callable, TypeVar
import datetime

T = TypeVar('T')


def create_mapped_object(target_type: Callable[[], T], value_dictionary: dict) -> T:
    """
    Creates an instance of target_type and calls map_object on it
    :param target_type: Callable[[], T]
    :param value_dictionary: dict
    :return: an instance of target_type
    """
    result = target_type()
    map_object(result, value_dictionary)
    return result


def map_object(target_object: T, value_dictionary: dict) -> None:
    """
    Looks for attributes on target_object that map to keys found in value_dictionary. If the attribute on target_object
    is not None the value from value_dictionary is converted to the type of that attribute. If the key in
    value_value_dictionary starts with a type prefix that type is used for conversion
    :param target_object: T
    :param value_dictionary: dict
    """
    for attribute_name, current_attribute_value in target_object.__dict__.items():
        if attribute_name in value_dictionary:
            target_type = current_attribute_value.__class__ if current_attribute_value is not None else None
            key = attribute_name
        else:
            target_type, key = detect_type(attribute_name, value_dictionary)

        if key is not None:
            value = value_dictionary[key]
            new_value = value if target_type is None else convert(value, target_type)
            target_object.__setattr__(attribute_name, new_value)


type_prefixes = {'b': bool,
                 'd': float,
                 'dt': datetime.datetime,
                 'i': int,
                 's': str}


def detect_type(s: str, value_dictionary: dict):
    target_type = None
    key = None
    if s:
        for (prefix, type_) in type_prefixes.items():
            key_ = prefix + s[0].upper() + s[1:]
            if key_ in value_dictionary:
                target_type = type_
                key = key_
                break
    return target_type, key


def convert(s: str, target_type: type) -> object:
    result = None
    if s is not None:
        if target_type == bool:
            result = s.upper() in ('1', 'TRUE', 'YES', 'Y')
        else:
            result = target_type(s)
    return result
