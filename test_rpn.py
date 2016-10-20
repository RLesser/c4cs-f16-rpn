import unittest
import fractions

import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate("1 1 +")
		self.assertEqual(2, result)
	def test_subtract(self):
		result = rpn.calculate("5 3 -")
		self.assertEqual(2, result)
	def test_multiply(self):
		result = rpn.calculate("5 3 *")
		self.assertEqual(15, result)
	def test_divide(self):
		result = rpn.calculate("6 3 /")
		self.assertEqual(2, result)
	def test_exp(self):
		result = rpn.calculate("5 3 ^")
		self.assertEqual(125, result)
	def test_frac(self):
		result = rpn.calculate("3 12 f")
		self.assertEqual(fractions.Fraction(1,4), result)
	def test_quit(self):
		result = rpn.calculate("q")
		self.assertEqual('quit', result)
	def test_badstring(self):
		with self.assertRaises(TypeError):
			rpn.calculate("1 2 3 +")