from project.homework_4.blackjack import (
    BlackJackCard,
    BlackJackDecision,
    BlackJackHand,
    Player,
    Bot,
    Game,
    GameStatus,
)
from project.homework_4.card_game_basics import Card

# Card


def test_blackjack_card_initialization():
    card = BlackJackCard(Card("♥", "A"))
    assert card.get_value() == 11
    assert card.get_card_rank() == "A"


def test_blackjack_card_initialization_for_10value_cards():
    card = BlackJackCard(Card("♥", "K"))
    assert card.get_value() == 10
    assert card.get_card_rank() == "K"


# Hand


def test_blackjack_hand_initialization():
    hand = BlackJackHand([BlackJackCard(Card("♥", "A")), BlackJackCard(Card("♥", "K"))])
    assert hand.get_sum() == 21


def test_blackjack_hand_add_bet():
    hand = BlackJackHand([BlackJackCard(Card("♥", "A")), BlackJackCard(Card("♥", "K"))])
    hand.add_bet()
    assert hand.get_bet_count() == 2


def test_blackjack_hand_split():
    hand = BlackJackHand([BlackJackCard(Card("♥", "A")), BlackJackCard(Card("♥", "A"))])
    split_hand = hand.split()
    assert len(split_hand) == 2
    assert split_hand[0].get_sum() == 11
    assert split_hand[1].get_sum() == 11


def test_blackjack_hand_add_card():
    hand = BlackJackHand([BlackJackCard(Card("♥", "A"))])
    hand.add_card(BlackJackCard(Card("♥", "K")))
    assert hand.get_sum() == 21


def test_blackjack_hand_with_aces():
    hand = BlackJackHand([])
    hand.add_card(BlackJackCard(Card("♥", "5")))
    hand.add_card(BlackJackCard(Card("♦", "5")))
    hand.add_card(BlackJackCard(Card("♥", "A")))
    hand.add_card(BlackJackCard(Card("♦", "A")))
    assert hand.get_sum() == 12


def test_blackjack_hand_give_up_half_of_bet():
    hand = BlackJackHand([BlackJackCard(Card("♥", "A")), BlackJackCard(Card("♥", "K"))])
    hand.add_bet()
    hand.give_up_half_of_bet()
    assert hand.get_bet_count() == 1


# Player


def test_player_initialization():
    player = Player()
    assert player.get_player_sums() == [0]
    assert player.can_move == True
    assert player.is_disabled() == False
    assert len(player.get_hands()) == 1
    assert player.get_hands()[0].get_sum() == 0


def test_player_hit():
    player = Player()
    player.hit(BlackJackCard(Card("♥", "A")), 0)
    assert player.get_player_sums() == [11]


def test_player_split():
    player = Player()
    player.hit(BlackJackCard(Card("♥", "A")), 0)
    player.split(BlackJackCard(Card("♥", "A")), 0)
    assert player.get_player_sums() == [11, 11]


def test_player_double_down():
    player = Player()
    player.double_down(BlackJackCard(Card("♥", "A")), 0)
    assert player.get_player_sums() == [11]
    assert player.get_hands()[0].get_bet_count() == 2


def test_surrender():
    player = Player()
    player.hit(BlackJackCard(Card("♥", "A")), 0)

    player.surrender()
    assert player.get_player_sums() == [11]
    assert player.get_hands()[0].get_bet_count() == 0.5
    assert player.is_disabled() == True


# Bot
def test_bot_initialization():
    bot = Bot(Player(), "bot")
    assert bot.name == "bot"
    assert bot.get_player().get_player_sums() == [0]


def test_bot_returns_stand_when_sum_is_over_17():
    bot = Bot(Player(), "bot")
    bot.get_player().hit(BlackJackCard(Card("♥", "K")), 0)
    bot.get_player().hit(BlackJackCard(Card("♥", "8")), 0)
    assert bot.make_decision(bot.get_player()) == (0, BlackJackDecision.STAND)


def test_bot_returns_stand_when_sum_is_21():
    bot = Bot(Player(), "bot")
    bot.get_player().hit(BlackJackCard(Card("♥", "A")), 0)
    bot.get_player().hit(BlackJackCard(Card("♥", "K")), 0)
    assert bot.make_decision(bot.get_player()) == (0, BlackJackDecision.STAND)


def test_bot_returns_stand_when_disabled():
    bot = Bot(Player(), "bot")
    bot.get_player().hit(BlackJackCard(Card("♥", "A")), 0)
    bot.get_player().hit(BlackJackCard(Card("♥", "K")), 0)
    bot.get_player().disable_moves()
    assert bot.make_decision(bot.get_player()) == (0, BlackJackDecision.STAND)


# Game
def test_game_initialization():
    game = Game([Bot(Player(), "bot1"), Bot(Player(), "bot2"), Bot(Player(), "bot3")])
    game.initialize()
    assert game.status() == GameStatus.IN_PROGRESS

    # all players must have 2 cards
    assert len(game.get_actors()[0].get_player().get_hands()[0]._cards) == 2
    assert len(game.get_actors()[1].get_player().get_hands()[0]._cards) == 2
    assert len(game.get_actors()[2].get_player().get_hands()[0]._cards) == 2


def test_game_play_round():
    game = Game([Bot(Player(), "bot1"), Bot(Player(), "bot2"), Bot(Player(), "bot3")])
    game.play_round()

    assert game._current_round == 1


def test_game_end():
    game = Game([Bot(Player(), "bot1"), Bot(Player(), "bot2"), Bot(Player(), "bot3")])
    game.end()
    assert game.status() == GameStatus.GAME_END
