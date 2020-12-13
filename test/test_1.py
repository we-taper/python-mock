import operator
import unittest
from unittest.mock import MagicMock, patch

from sample1 import ExpensiveClass, using_class, run_external_func


class Tests(unittest.TestCase):
    def test_class(self):
        obj = ExpensiveClass()
        content = MagicMock()
        content.append = MagicMock(return_value=None)
        obj.content = content
        obj.append("a")
        content.append.assert_called_once_with("a")

    def test_method(self):
        obj = ExpensiveClass()
        obj.append = MagicMock(return_value=None)
        obj = using_class(expensive_class=obj)
        obj.append.assert_called_once_with("a")

    def test_external_lib(self):
        with patch('sample1.functools') as functools:
            args = [1, 2, 3]
            # operator.add = MagicMock(return_value=sum(args))
            functools.reduce.return_value = sum(args)
            ret = run_external_func([1, 2, 3])
            functools.reduce.assert_called_with(operator.add, args)
            self.assertEqual(ret, sum(args))
