import unittest

import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate("1 1 +")
		self.assertEqual(2, result)
        # result = rpn.calculate("263 100 +")
        # self.assertEqual(363,result)