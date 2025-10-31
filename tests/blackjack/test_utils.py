from project.homework_4.utils import calculate_ace_blackjack_value


def test_calculate_ace_blackjack_value():
    assert calculate_ace_blackjack_value(0) == 11
    assert calculate_ace_blackjack_value(1) == 11
    assert calculate_ace_blackjack_value(2) == 11
    assert calculate_ace_blackjack_value(3) == 11
    assert calculate_ace_blackjack_value(10) == 11
    assert calculate_ace_blackjack_value(11) == 1
    assert calculate_ace_blackjack_value(12) == 1
