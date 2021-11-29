from unittest import TestCase
from HelloWorld import Hello


class HelloTest(TestCase):
    def test_Greeting_True(self):
        greeting = Hello()
        self.assertEqual(greeting.hi_message, "Hello World!")

    def test_Greeting_False(self):
        greeting = Hello()
        self.assertNotEqual(greeting.hi_message, "World helllo")
