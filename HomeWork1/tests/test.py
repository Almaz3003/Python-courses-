from unittest import TestCase
from HomeWork1.hello_world import Hello


class HelloTest(TestCase):
    def test_greeting_true(self):
        greeting = Hello()
        self.assertEqual(greeting.hi_message, "Hello World!")

    def test_greeting_false(self):
        greeting = Hello()
        self.assertNotEqual(greeting.hi_message, "World helllo")
