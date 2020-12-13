import functools
import operator


class ExpensiveClass:
    def __init__(self):
        self.content = []

    def append(self, resource):
        self.content.append(resource)


def using_class(expensive_class: ExpensiveClass):
    expensive_class.append("a")
    return expensive_class


def run_external_func(x):
    return functools.reduce(operator.add, x)
