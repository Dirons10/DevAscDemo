"""Basic Python feature module."""

from __future__ import annotations


def format_message(name: str) -> str:
    """Return a friendly greeting for the provided name."""
    cleaned_name = name.strip() or "friend"
    return f"Hello, {cleaned_name}!"


class MyFeature:
    """A tiny feature class with a simple operation."""

    def __init__(self, name: str = "friend") -> None:
        self.name = name.strip() or "friend"

    def run(self) -> str:
        return format_message(self.name)


if __name__ == "__main__":
    print(format_message("World"))
    print("Welcome to DEVASC!")
