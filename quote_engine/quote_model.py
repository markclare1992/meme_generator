"""A module to represent a Quote."""


class QuoteModel:
    """A class to represent a Quote."""

    def __init__(self, body: str, author: str):
        """
        Initialise the QuoteModel class.

        :param body: The body of the quote itself.
        :param author: The author of the quote.
        """
        self.body = body
        self.author = author

    def __repr__(self):
        """:return: A string representation of the quote."""
        return f"Quote: {self.body}, Author: {self.author}"

    def __eq__(self, other):
        """:return: True if the body and author are the same."""
        return self.body == other.body and self.author == other.author

    def __hash__(self):
        """:return: A hash of the body and author."""
        return hash(self.body + self.author)

    def __str__(self):
        """:return: A string representation of the quote."""
        return f"Quote: {self.body} by {self.author}"
