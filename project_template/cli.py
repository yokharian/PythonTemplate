"""
Expose functions as CLI commands.
"""

from sys import exit


import argparse
from importlib.metadata import version
from typing import Any

from project_template import __doc__ as package_docstring
from project_template.core import StringManipulator


def main() -> int:
    """
    CLI entry point.
    """

    # Parser setup.
    parser = argparse.ArgumentParser(
        description=package_docstring,
        add_help=False,
    )
    subparsers = parser.add_subparsers(title="command")

    parser.set_defaults(command=lambda **_: parser.print_usage())
    parser.add_argument("-h", "--help", action="help", help="Show this help message.")
    parser.add_argument(
        "--version",
        action="version",
        version=f"{parser.prog} {version(__package__)}",
        help="Show program's version number.",
    )

    # Commands.
    invert_parser = subparsers.add_parser(
        "invert",
        help=invert.__doc__,
        description=invert.__doc__,
    )
    invert_parser.set_defaults(command=invert)
    invert_parser.add_argument("message", help="Message that will be displayed.")

    # Run.
    args = parser.parse_args()

    return args.command(**vars(args))


#
# Commands.
# -------------------------------------------------------------------------------
def invert(message: str, **_kwargs: Any) -> int:
    """
    TODO CLI command docstring.
    """

    inverted = StringManipulator.invert_case(message)
    print(inverted)

    return 0


if __name__ == "__main__":
    exit(main())
