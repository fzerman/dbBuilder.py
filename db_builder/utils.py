def get_classes(module):
    clsmembers = inspect.getmembers(sys.modules[module], inspect.isclass)
    return clsmembers