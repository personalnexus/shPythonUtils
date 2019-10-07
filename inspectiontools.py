import inspect


def import_functions(source_module, name_predicate=None, target_module=None):
    """
    Imports all functions whose names match the name_predicate from the source into the target module
    :param source_module: Module whose functions are to be imported
    :param name_predicate: a function to which the function name is passed and which returns a bool indicating whether
           to include the function. If this is None, all functions are imported
    :param target_module: the module into which to import functions (default is the caller's own module)
    """

    # default to importing into the caller's module
    if target_module is None:
        caller_frame = inspect.stack()[1]
        caller_module = inspect.getmodule(caller_frame[0])
        target_module = caller_module

    names_and_functions = [(name, function) for (name, function) in
                           inspect.getmembers(source_module, inspect.isfunction)
                           if name_predicate is None or name_predicate(name)]
    for name, function in names_and_functions:
        setattr(target_module, name, function)
