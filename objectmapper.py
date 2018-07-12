from typing import Callable, TypeVar

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
    is not None the value from value_dictionary is converted to the type of that attribute
    :param target_object: T
    :param value_dictionary: dict
    """
    for attribute_name, current_attribute_value in target_object.__dict__.items():
        if attribute_name in value_dictionary:
            if current_attribute_value is not None:
                new_value = convert(value_dictionary[attribute_name], current_attribute_value.__class__)
            else:
                new_value = value_dictionary[attribute_name]
            target_object.__setattr__(attribute_name, new_value)


def convert(s: str, target_type: type) -> object:
    result = None
    if s is not None:
        if target_type == bool:
            result = s.upper() in ('1', 'TRUE', 'YES', 'Y')
        else:
            result = target_type(s)
    return result
