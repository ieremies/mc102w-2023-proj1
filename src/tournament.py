#!/usr/bin/env python3
"""
Módulo que simula o jogo de Senha diversas vezes e mede a taxa de acerto da estratégia do jogador.
"""

from random import sample

try:
    from tqdm import trange
except ImportError:
    trange = None


def run_game(max_guesses=10, n_games=1000000):
    """
    Função que roda o jogo de Senha diversas vezes e mede a taxa de acerto da estratégia do jogador.
    """
    from codes import guess_code, COLORS, CODE_LENGTH
    from player import player

    wins = 0
    if trange is None:
        games_iterator = range(n_games)
    else:
        games_iterator = trange(n_games, desc="Games", unit=" games", leave=True)

    for i in games_iterator:
        global CODE, HIST, RES
        CODE = sample(COLORS, CODE_LENGTH)
        HIST = []
        RES = []

        for _ in range(max_guesses):
            guess = player(HIST, RES)
            result = guess_code(guess, print_result=False)
            if result == (4, 4):
                wins += 1
                break

        win_rate = wins / i if i > 0 else 0
        if trange is not None:
            games_iterator.set_description(f"Games (Win rate: {win_rate* 100:.3f}%)")

    print(f"Final Win rate: {wins/n_games * 100:.3f}%")


if __name__ == "__main__":
    run_game()
