from __future__ import annotations
from typing import Tuple
from abc import ABC, abstractmethod
from enum import Enum, auto
import random
import time

from .card_game_basics import Card, Deck
from .exceptions import SplitError
from .utils import calculate_ace_blackjack_value, pretty_print


class BlackJackCard:
    """Class that takes a standard playing card and creates an object with attributes and methods spefific to blackjack"""

    _value: int
    _card: Card

    def __init__(self, card: Card):
        """Initializes a blackjack card with the given card"""
        self._value = self.match_value(card)
        self._card = card

    def match_value(self, card: Card) -> int:
        """Matches the value of the card to the value of the blackjack card"""
        if card.rank == "A":
            return 11
        elif card.rank == "K":
            return 10
        elif card.rank == "Q":
            return 10
        elif card.rank == "J":
            return 10
        else:
            return int(card.rank)

    def get_value(self) -> int:
        """Returns the value of the blackjack card"""
        return self._value

    def set_value(self, value: int):
        """Sets the value of the blackjack card"""
        self._value = value

    def get_card_rank(self) -> str:
        """Returns the rank of the card"""
        return self._card.rank

    def __str__(self):
        """Returns a string representation of the card"""
        return f"Card: {self.value}"

    def __repr__(self):
        """Returns a string representation of the card"""
        return f"BlackJackCard({self._value})"


class BlackJackHand:
    """Class that represents a hand of blackjack cards"""

    _cards: list[BlackJackCard] = []
    bet_count = 1

    def __init__(self, cards: list[BlackJackCard]):
        """Initializes a hand of blackjack cards"""
        self._cards = cards

    def get_sum(self) -> int:
        """Returns the sum of the cards in the hand"""
        card_sum = 0
        aces = list(filter(lambda card: card.get_card_rank() == "A", self._cards))
        cards_not_aces = list(
            filter(lambda card: card.get_card_rank() != "A", self._cards)
        )

        for card in cards_not_aces:
            card_sum += card.get_value()

        if card_sum + len(aces) * 11 <= 21:
            card_sum += len(aces) * 11
        else:
            for index, card in enumerate(aces):
                if card_sum + (len(aces) - index) * 11 <= 21:
                    card_sum += 11
                else:
                    card_sum += 1

        return card_sum

    def add_card(self, card: BlackJackCard):
        """Adds a card to the hand"""
        self._cards.append(card)

    def add_bet(self):
        """Adds a bet to the hand"""
        self.bet_count += 1

    def give_up_half_of_bet(self):
        """Gives up half of the bet to the player"""
        self.bet_count = self.bet_count / 2

    def get_bet_count(self) -> int:
        """Returns the bet count of the hand"""
        return self.bet_count

    def split(self) -> Tuple[BlackJackHand, BlackJackHand]:
        """Splits the hand into two if possible"""
        if (
            len(self._cards) != 2
            or self._cards[0].get_value() != self._cards[1].get_value()
        ):
            raise SplitError()

        return (BlackJackHand(self._cards[:1]), BlackJackHand(self._cards[1:]))


class Player:
    """Class that represents a player in a blackjack game"""

    can_move = True

    def __init__(self):
        """Initializes a player"""
        self._hands = [BlackJackHand([])]

    def hit(self, card: BlackJackCard, hand_index: int = 0):
        """Hits a card in the player's hand"""

        self._hands[hand_index].add_card(card)

    def split(self, card: BlackJackCard, hand_index: int = 0):
        """Splits the player's hand"""
        self._hands[hand_index].add_card(card)
        hand1, hand2 = self._hands[hand_index].split()
        self._hands[hand_index] = hand1
        self._hands.append(hand2)

    def double_down(self, card: BlackJackCard, hand_index: int = 0):
        """Doubles down the player's hand"""
        self._hands[hand_index].add_bet()
        self.hit(card, hand_index)

    def surrender(self):
        """Surrenders the player's hand"""
        for hand in self._hands:
            hand.give_up_half_of_bet()
        self.disable_moves()

    def get_player_sums(self) -> list[int]:
        """Returns the sums of the cards in the player's hands"""
        return [hand.get_sum() for hand in self._hands]

    def is_disabled(self) -> bool:
        """Returns whether the player is disabled"""
        return not self.can_move

    def disable_moves(self):
        """Disables moves for the player"""
        self.can_move = False

    def get_hands(self) -> list[BlackJackHand]:
        """Returns the hands of the player"""
        return self._hands


class BlackJackDecision(Enum):
    """Enum that represents the possible decisions in a blackjack game"""

    HIT = auto()
    DOUBLE_DOWN = auto()
    SPLIT = auto()
    SURRENDER = auto()
    STAND = auto()


class BlackJackActor(ABC):
    """Abstract class that represents an actor in a blackjack game (like a real player or bot). Makes decisions"""

    name: str
    _player: Player

    def __init__(self, player: Player, name: str):
        """Initializes an actor with the given hand"""
        pass

    @abstractmethod
    def make_decision(self, dealer: BlackJackActor) -> Tuple[int, BlackJackDecision]:
        pass

    @abstractmethod
    def get_player(self) -> Player:
        """Returns the player of the actor"""
        pass


class Bot(BlackJackActor):
    """Class that represents a bot in a blackjack game"""

    def __init__(self, player: Player, name: str):
        """Initializes a bot with the given hand"""
        super().__init__(player, name)
        self.name = name
        self._player = player

    def make_decision(self, dealer: BlackJackActor) -> Tuple[int, BlackJackDecision]:
        """Makes a decision for the bot"""
        hand_index = random.randint(0, len(self._player.get_hands()) - 1)
        hand = self._player.get_hands()[hand_index]
        # time.sleep(random.randint(1, 3))

        if self._player.is_disabled():
            return (hand_index, BlackJackDecision.STAND)

        if hand.get_sum() >= 17:
            return (hand_index, BlackJackDecision.STAND)

        if any(hand.get_sum() == 21 for hand in self._player.get_hands()):
            return (hand_index, BlackJackDecision.STAND)

        strategies = [
            BlackJackDecision.STAND,
            BlackJackDecision.SURRENDER,
            BlackJackDecision.HIT,
            BlackJackDecision.DOUBLE_DOWN,
        ]
        random.shuffle(strategies)

        return (hand_index, strategies[0])

    def get_player(self) -> Player:
        """Returns the player of the actor"""
        return self._player


class GameStatus(Enum):
    """Enum that represents the status of the game"""

    IN_PROGRESS = auto()
    GAME_END = auto()


class Game:
    """Class that represents a game of blackjack"""

    _actors: list[BlackJackActor] = []
    _dealer = Player()
    _deck: Deck = Deck()
    _current_round: int = 0
    _status: GameStatus = GameStatus.IN_PROGRESS

    def __init__(self, actors: list[BlackJackActor]):
        """Initializes a game of blackjack"""
        self._actors = actors
        self._deck = Deck()
        self._current_round = 0
        self._deck.shuffle()

    def initialize(self):
        """Initializes the game"""

        for index in range(len(self._actors)):
            self._actors[index].get_player().hit(BlackJackCard(self._deck.draw()))
            self._actors[index].get_player().hit(BlackJackCard(self._deck.draw()))

        self._dealer.hit(BlackJackCard(self._deck.draw()))
        self._dealer.hit(BlackJackCard(self._deck.draw()))
        print("Welcome to the game of blackjack!")

        visible_dealer_cards = self.get_visible_dealer_cards()

        print("Dealer's cards:")
        print("[HIDDEN]")
        for card in visible_dealer_cards:
            pretty_print(card)

        for player in self._actors:
            print(f"Player {player.name} has {player.get_player().get_player_sums()}")

    def get_visible_dealer_cards(self) -> list[Card]:
        """Returns the visible cards of the dealer"""

        blackjack_cards = []
        if self._current_round <= 1:
            blackjack_cards = self._dealer.get_hands()[0]._cards[1:]
        else:
            blackjack_cards = self._dealer.get_hands()[0]._cards

        return [card._card for card in blackjack_cards]

    def get_dealer_visible_sum(self) -> int:
        """Returns the sum of the visible cards of the dealer"""
        return sum(
            BlackJackCard(card).get_value() for card in self.get_visible_dealer_cards()
        )

    def play_round(self):
        """Plays a round of blackjack"""
        self._current_round += 1
        visible_dealer_cards = self.get_visible_dealer_cards()
        print("Dealer's cards:")
        for card in visible_dealer_cards:
            pretty_print(card)

        if self.get_dealer_visible_sum() >= 17:
            self.end()
            return

        if self._current_round >= 3 and self.get_dealer_visible_sum() != 21:
            print(f"Dealer draws...")
            dealer_card = self._deck.draw()
            pretty_print(dealer_card)
            self._dealer.hit(BlackJackCard(dealer_card))

        if self.get_dealer_visible_sum() >= 17:
            self.end()
            return

        for actor in self._actors:
            if actor.get_player().is_disabled():
                continue

            print(f"{actor.name} is making a decision now")
            decision = actor.make_decision(self._dealer)
            if decision[1] == BlackJackDecision.HIT:
                print(f"{actor.name} hits...")
                actor.get_player().hit(BlackJackCard(self._deck.draw()), decision[0])
            elif decision[1] == BlackJackDecision.DOUBLE_DOWN:
                print(f"{actor.name} doubles down...")
                actor.get_player().double_down(
                    BlackJackCard(self._deck.draw()), decision[0]
                )
                print(f"{actor.name} splits...")
            elif decision[1] == BlackJackDecision.SPLIT:
                print(f"{actor.name} splits...")
                actor.get_player().split(decision[0])
            elif decision[1] == BlackJackDecision.SURRENDER:
                print(f"{actor.name} surrenders...")
                actor.get_player().surrender()
            else:
                print(f"Player {actor.name} stands...")
                pass

            hand_over_21 = list(
                filter(lambda hand: hand.get_sum() > 21, actor.get_player().get_hands())
            )
            if len(hand_over_21) > 0:
                print(f"Player {actor.name} has {hand_over_21[0].get_sum()}")
                print(
                    f"Player {actor.name} loses his bet {hand_over_21[0].get_bet_count()}"
                )

            print(f"current state of ${actor.name} hands:")
            for hand, index in zip(
                actor.get_player().get_hands(),
                range(len(actor.get_player().get_hands())),
            ):
                print(f"Hand {index}: {hand.get_sum()}")

    def end(self):
        """Ends the game"""
        self._status = GameStatus.GAME_END
        print(
            "Game is done, dealer got over 16 points (",
            self._dealer.get_player_sums()[0],
            ")",
        )
        print("Results:")
        for actor in self._actors:
            print(f"{actor.name} got {actor.get_player().get_player_sums()}")

        for actor in self._actors:
            for hand in actor.get_player().get_hands():
                if self._dealer.get_player_sums()[0] > 21:
                    # Wins
                    print(
                        f"Player {actor.name} wins {hand.get_bet_count()} bet on hand {hand.get_sum()}"
                    )
                    continue
                if hand.get_sum() > self._dealer.get_player_sums()[0]:
                    print(
                        f"{actor.name} wins bet {hand.get_bet_count()} on hand {hand.get_sum()}"
                    )
                    continue
                elif hand.get_sum() == self._dealer.get_player_sums()[0]:
                    print(f"{actor.name} draws on hand {hand.get_sum()}")
                    continue
                elif hand.get_sum() < self._dealer.get_player_sums()[0]:
                    print(
                        f"{actor.name} loses {hand.get_bet_count()} bet on hand {hand.get_sum()}"
                    )
                    continue

    def status(self):
        """Returns the status of the game"""
        return self._status

    def get_actors(self):
        """Returns the actors of the game"""
        return self._actors
