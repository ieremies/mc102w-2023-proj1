#!/usr/bin/env python3
"""
Implemente aqui o seu código para o jogador.

Você irá utilizar a função `check_guess` para verificar se o seu palpite está correto.
Toda vez que esta função for chamada, o seu palpite será comparado com o código secreto
e você receberá uma tupla com a quantidade de cores corretas e a quantidade de cores
na posição correta.

Além disso, o display será atualizado.
"""
from colors import *
from random import sample


def player(guess_hist, res_hist):
    """
    Função principal do jogador.

    Esta função deve retornar o seu palpite, que deve ser uma lista de 4 cores.
    As cores disponíveis são: RED, GREEN, BLUE, YELLOW, ORANGE, BLACK, WHITE.
    """

    return sample([RED, GREEN, BLUE, YELLOW, ORANGE, BLACK, WHITE], 4)
