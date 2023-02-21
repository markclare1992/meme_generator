class QuoteModel:
    """
    A class to represent a Quote.
    """

    def __init__(self, body: str, author: str):
        """
        :param body: The body of the quote itself.
        :param author: The author of the quote.
        """
        self.body = body
        self.author = author

    def __repr__(self):
        return f"Quote: {self.body}, Author: {self.author}"

    def __eq__(self, other):
        return self.body == other.body and self.author == other.author

    def __hash__(self):
        return hash(self.body + self.author)

    def __str__(self):
        return f"Quote: {self.body} by {self.author}"
