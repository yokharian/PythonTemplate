"""
Core utility functions for the InfluxHelper project.
"""

"""
Core utility functions
"""


class StringManipulator:
    """
    A class that provides string manipulation utilities.
    """

    @classmethod
    def invert_case(cls, text: str) -> str:
        """
        Inverts the case of each character in the given string.

        :param text: The input string whose characters' cases need to be inverted.
        :return: A new string with inverted case for each character.
        """

        inverted_text: list[str] = []

        for letter in text:
            if letter.isupper():
                inverted_text.append(letter.lower())
            else:
                inverted_text.append(letter.upper())

        return "".join(inverted_text)
