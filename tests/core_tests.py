"""
Unit tests for `project_template.core`.
"""

from unittest import TestCase

from project_template.core import StringManipulator


class StringManipulatorTests(TestCase):
    def testInvertCaseLower(self) -> None:
        text = StringManipulator.invert_case("hello world")

        self.assertEqual(text, "HELLO WORLD")

    def testInvertCaseUpper(self) -> None:
        text = StringManipulator.invert_case("HELLO WORLD")

        self.assertEqual(text, "hello world")

    def testInvertCaseMixed(self) -> None:
        text = StringManipulator.invert_case("HelLo WoRld")

        self.assertEqual(text, "hELlO wOrLD")
