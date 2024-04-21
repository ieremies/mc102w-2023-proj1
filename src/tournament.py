#!/usr/bin/env python3
"""
Módulo que simula o jogo de Senha diversas vezes e mede a taxa de acerto da estratégia do jogador.
"""

from random import sample
from time import time

try:
    from tqdm import trange
except ImportError:
    trange = None


def run_game(max_guesses=10, n_games=10000):
    """
    Função que roda o jogo de Senha diversas vezes e mede a taxa de acerto da estratégia do jogador.
    """
    from codes import guess_code, COLORS, CODE_LENGTH, HIST, RES

    wins = 0
    games_iterator = (
        range(n_games)
        if trange is None
        else trange(n_games, desc="Games", unit=" games", leave=True)
    )

    start = time()

    for i in games_iterator:
        from player import player

        code = sample(COLORS, CODE_LENGTH)
        HIST = []
        RES = []

        for _ in range(max_guesses):
            guess = player(HIST, RES)
            result = guess_code(guess, print_result=False, code=code)
            HIST.append(guess)
            RES.append(result)
            if result == (4, 4):
                wins += 1
                break

        win_rate = wins / (i + 1)
        if trange is not None:
            games_iterator.set_description(f"Games (Win rate: {win_rate* 100:.3f}%)")
        else:
            print(
                f"       win rate {win_rate* 100:.3f}%",
                f"Game {i} of {n_games} ({i/n_games * 100:.3f}%)",
                f"Time {time() - start:.3f}s (estimated {(time() - start)/(i+1) * n_games:.3f}s)",
                sep=" | ",
            )
            print("\033[F", end="")

    print(
        "\033[F",
        f"Final: win rate {(wins/n_games)* 100:.3f}%",
        f" | Game {n_games} of {n_games} ({n_games/n_games * 100:.3f}%)",
        f" | Time {time() - start:.3f}s",
        sep="",
    )


if __name__ == "__main__":
    run_game()
