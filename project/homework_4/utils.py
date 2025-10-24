from card_game_basics import Card


def pretty_print(card: Card):
    """Prints a card in a pretty format"""
    print(f"{card.rank} of {card.suit}")


def calculate_ace_blackjack_value(current_card_sum: int) -> int:
    """Calculates value for a blackjack card, which may vary depending on the sum of the cards in the hand

    Args:
        current_card_sum (int): Sum of the cards in the hand before adding the ace card

    Returns:
        int: value of this particular ace card
    """
    if current_card_sum + 11 <= 21:
        return 11
    else:
        return 1
