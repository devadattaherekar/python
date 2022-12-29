from unittest import TestCase
import unittest
import arithmetic as ar

class TestArithmetic(TestCase):
    def test_add(self):
        var1=10
        var2=20
        expected=30
        self.assertEqual(expected,ar.add(var1,var2))

    def test_sub(self):
        var1 = 10
        var2 = 20
        expected = -10
        self.assertEqual(expected, ar.sub(var1, var2))
        var1 = -10
        var2 = -1
        expected = -9
        self.assertEqual(expected, ar.sub(var1, var2))

#var1=10
#var2="sachin"
#print(f"Addition {var1}  and {var2} is {ar.add(var1,var2)}")