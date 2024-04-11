#!/usr/bin/env python3
"""
Front-end do jogo utilizando o terminal.

Este arquivo é responsável por imprimir o jogo no terminal e chamar a função `player` do arquivo `player.py`.
"""

import player
from colors import *
from codes import *
from time import sleep


def main(max_guesses=10, speed=0.5):
    """
    Função principal do jogo.

    Esta função é responsável por imprimir o jogo no terminal e chamar a função `player` do arquivo `player.py`.

    Parâmetros:
    - max_guesses: número máximo de palpites
    - speed: velocidade de cada palpite
    """
    print("( ):\t Code    => (colors, positions)")
    while len(RES) < max_guesses and not (len(RES) > 0 and RES[-1] == (4, 4)):
        guess_code(player.player(HIST, RES))
        sleep(speed)
    if len(RES) == max_guesses:
        print("You lost!\nCorrect:", *CODE)
    else:
        print("You won! With only", len(RES), "guesses!")


if __name__ == "__main__":
    main()
