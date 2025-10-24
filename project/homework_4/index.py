from __future__ import annotations

from blackjack import Bot, Game, GameStatus, Player

if __name__ == "__main__":
    game = Game([Bot(Player(), "bot1"), Bot(Player(), "bot2"), Bot(Player(), "bot3")])
    game.initialize()

    while game.status() == GameStatus.IN_PROGRESS:
        game.play_round()
