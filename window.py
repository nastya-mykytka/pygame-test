import pygame
from pygame import display, transform, image

from constants import WINDOW_WIDTH, WINDOW_HEIGHT

WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

window = display.set_mode(WINDOW_SIZE)
display.set_caption("CATCH UP | LEVEL 1")
pygame_icon = pygame.image.load('images/window-icon.png') # TODO: add window icon
background = transform.scale(image.load("images/bg.jpg"), WINDOW_SIZE)
pygame.display.set_icon(pygame_icon)