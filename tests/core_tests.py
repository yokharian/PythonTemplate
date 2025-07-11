"""
Unit tests for `project_template.core`.
"""

from unittest import TestCase

from src.core import MyClass


class MyClassTests(TestCase):
    def testInvertCaseLower(self) -> None:
        text = MyClass.invert_case("hello world")

        self.assertEqual(text, "HELLO WORLD")

    def testInvertCaseUpper(self) -> None:
        text = MyClass.invert_case("HELLO WORLD")

        self.assertEqual(text, "hello world")

    def testInvertCaseMixed(self) -> None:
        text = MyClass.invert_case("HelLo WoRld")

        self.assertEqual(text, "hELlO wOrLD")
