#!/usr/bin/env python3
"""
Guess the Code game

This is a simple game where the player has to guess a secret code. The code is
composed of 4 colors, and the player has to guess it with infinite attempts. The
game will give feedback on the guess, telling the player how many colors are
correct and how many are in the correct position.

The game ends when the player guesses the code.
"""
import pygame
import random
import player
from colors import *

# Initialize Pygame
pygame.init()

# Define screen dimensions
WIDTH, HEIGHT = 300, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guess the Code")

# Define color options
COLORS = [RED, GREEN, BLUE, YELLOW, ORANGE, BLACK, WHITE]
CODE_LENGTH = 4

HIST = []
RES = []
CODE = random.sample(COLORS, CODE_LENGTH)


def guess(guessed_code):
    HIST.append(guessed_code)
    RES.append(check_guess(CODE, guessed_code))

    # print colors names
    print(
        f"({len(HIST)}): {[reverse_colors[color] for color in guessed_code]} => {RES[-1]}"
    )
    return RES[-1]


def check_guess(code, guess):
    """
    Check how many colors are correct and how many are in the correct position.
    """
    correct_colors = sum(c in code for c in guess)
    correct_positions = sum(c == g for c, g in zip(code, guess))
    return correct_colors, correct_positions


def draw_guesses():
    """
    Draw the previous guesses on the screen from bottom to top,
    always keeping the last guess on the bottom
    """
    for i, (guess, (correct_colors, correct_positions)) in enumerate(
        zip(HIST[::-1], RES[::-1])
    ):
        for j, color in enumerate(guess):
            pygame.draw.rect(
                SCREEN,
                color,
                # 40 x 40 square with a 10 pixel margin
                pygame.Rect(
                    j * 50 + 10,
                    HEIGHT - (i + 1) * 50,
                    40,
                    40,
                ),
            )
            print(j * 50 + 10, HEIGHT - (i + 1) * 50, 40, 40)
        pygame.font.init()
        font = pygame.font.SysFont("Arial", 20)
        text = font.render(f"{correct_colors}/{correct_positions}", True, BLACK)
        SCREEN.blit(text, (210, HEIGHT - (i + 1) * 50 + 10))


def main():
    """
    Main function of the game.
    """
    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw the screen
        SCREEN.fill(GRAY)
        draw_guesses()

        # Guess a random code
        if len(RES) < 10 and not (len(RES) > 0 and RES[-1] == (4, 4)):
            guess(player.player(HIST, RES))

        # Update the screen
        pygame.display.flip()
        pygame.time.wait(1000)

    pygame.quit()


if __name__ == "__main__":
    main()
