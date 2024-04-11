#!/usr/bin/env python3
"""
Contem o código secreto e a função para verificar o palpite.
"""

from colors import *
from random import sample

# Lista de cores disponíveis
COLORS = [RED, GREEN, BLUE, YELLOW, ORANGE, BLACK, WHITE]
CODE_LENGTH = 4  # Tamanho do código secreto

HIST = []  # Histórico de palpites
RES = []  # Histórico de resultados
CODE = sample(COLORS, CODE_LENGTH)  # Código secreto


def guess_code(guess):
    """
    Função para verificar o palpite do jogador.

    guessed_code: lista de 4 cores

    Retorna uma tupla com a quantidade de cores corretas e a quantidade de cores
    na posição correta.
    """
    correct_colors = sum(c in CODE for c in guess)
    correct_positions = sum(c == g for c, g in zip(CODE, guess))

    HIST.append(guess)
    RES.append((correct_colors, correct_positions))

    # Imprime o palpite e o resultado
    print(f"({len(HIST)}):\t", *guess, f" => {RES[-1]}")

    # Retorna o resultado
    return RES[-1]
