from __future__ import annotations
from typing import Literal
import random


class Card:
    """Class representing a playing card in a card game"""

    suit: Literal["♥", "♦", "♣", "♠"]
    rank: Literal["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(
        self,
        suit: Literal["♥", "♦", "♣", "♠"],
        rank: Literal["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"],
    ):
        """Initializes a card with the given suit and rank"""
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Returns a string representation of the card"""
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        """Returns a string representation of the card"""
        return f"Card({self.suit}, {self.rank})"

    def __eq__(self, other: object) -> bool:
        """Checks if two cards are equal"""
        if not isinstance(other, Card):
            raise NotImplementedError("Can only compare cards with other cards")
        return self.suit == other.suit and self.rank == other.rank


class Deck:
    """Class that represents a deck of cards"""

    _cards: list[Card] = []

    def __init__(self):
        """Initializes a deck of cards"""
        self._cards = []

        for suit in ["♥", "♦", "♣", "♠"]:
            for rank in [
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "J",
                "Q",
                "K",
                "A",
            ]:
                self._cards.append(Card(suit, rank))

    def draw(self) -> Card:
        """Draws a card from the deck"""
        return self._cards.pop()

    def shuffle(self):
        """Shuffles the cards in the deck"""
        random.shuffle(self._cards)

    def __add__(self, other: Deck) -> Deck:
        """Adds two decks together"""
        result = Deck()

        result._cards = self._cards + other._cards
        return result

    def __len__(self) -> int:
        """Returns the number of cards in the deck"""
        return len(self._cards)
