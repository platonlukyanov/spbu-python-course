from project.homework_4.card_game_basics import Card, Deck


def test_card():
    card = Card("♥", "A")
    assert card.suit == "♥"
    assert card.rank == "A"


def test_deck():
    deck = Deck()
    assert len(deck) == 52


def test_card_equality():
    card1 = Card("♥", "A")
    card2 = Card("♥", "A")
    assert card1 == card2


def test_card_inequality():
    card1 = Card("♥", "A")
    card2 = Card("♥", "K")
    assert card1 != card2


def test_deck_addition():
    deck1 = Deck()
    deck2 = Deck()
    deck3 = deck1 + deck2
    assert len(deck3) == 104
