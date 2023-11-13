import pygame
from pygame import display, time, QUIT, image, transform, sprite, font, surface, KEYDOWN, K_SPACE, K_q, mixer

from constants import FPS, WINDOW_WIDTH, WINDOW_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT
from enemy import Enemy
from gift import Gift
from music import game_sound, game_over_sound, win_sound
from player import Player
from tree import Tree
from wall import Wall

pygame.init()
font.init()
mixer.init()
clock = time.Clock()

WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

window = display.set_mode(WINDOW_SIZE)
display.set_caption("CATCH UP | LEVEL 1")
background = transform.scale(image.load("images/bg.jpg"), WINDOW_SIZE)


walls = sprite.Group()


def add_wall(x, y, ice_count, direction, width=25, height=25):
    if direction == 'h':
        for n in range(ice_count):
            walls.add(Wall(x + (n * width), y, ice_count, 'h', window))
    if direction == 'v':
        for n in range(ice_count):
            walls.add(Wall(x, y + (n * height), ice_count, 'v', window))


# LABIRINT 1
add_wall(0, 100, 32, 'h')
add_wall(0, 100, 32, 'v')
add_wall(0, 875, 32, 'h')
add_wall(775, 100, 27, 'v')

add_wall(645, 600, 11, 'v')
add_wall(645, 350, 5, 'v')
add_wall(510, 350, 10, 'v')
add_wall(375, 600, 6, 'v')
add_wall(250, 475, 16, 'v')
add_wall(250, 225, 6, 'v')
add_wall(125, 475, 11, 'v')

add_wall(125, 225, 5, 'h')
add_wall(375, 225, 16, 'h')
add_wall(375, 225, 16, 'h')
add_wall(0, 350, 6, 'h')
add_wall(250, 350, 11, 'h')
add_wall(125, 475, 5, 'h')
add_wall(520, 475, 6, 'h')
add_wall(260, 600, 11, 'h')
add_wall(375, 750, 6, 'h')


# GIFTS
gifts = sprite.Group()
gift_1 = Gift(680, 150, window)
gift_2 = Gift(565, 400, window)
gift_3 = Gift(300, 660, window)
gift_4 = Gift(175, 520, window)
gifts.add(gift_1)
gifts.add(gift_2)
gifts.add(gift_3)
gifts.add(gift_4)


# GRINCHES
grinches = sprite.Group()
grinch_1 = Enemy(200, 190, 'images/grinch.png', 35, 35, window, 2, 400, 210)
grinch_2 = Enemy(270, 775, 'images/grinch.png', 35, 35, window, 2, 610, 275)
grinch_3 = Enemy(0, 440, 'images/grinch.png', 35, 35, window, 2, 250, 25)
grinches.add(grinch_1)
grinches.add(grinch_2)
grinches.add(grinch_3)

player = Player(750, 815, 'images/santa.png', PLAYER_WIDTH, PLAYER_HEIGHT, window, 2, walls)
tree = Tree(325, 390, window)

gift_font = pygame.font.Font('fonts/gunplay_3d.otf', 24, )
pause_font = pygame.font.Font('fonts/gunplay_3d.otf', 32, )
win_font = pygame.font.Font('fonts/gunplay_3d.otf', 48, )

gift_count_icon = Gift(500, 15, window, 30, 30)

running = True
finish = False
paused = False
gifts_collected = 0

def reset_game():
    global gifts_collected
    gifts_collected = 0

    # Reset player position
    player.move_to(750, 815)

    # Reset gifts
    gifts.empty()
    gifts.add(gift_1)
    gifts.add(gift_2)
    gifts.add(gift_3)
    gifts.add(gift_4)

    # Reset grinches
    grinches.empty()
    grinches.add(grinch_1)
    grinches.add(grinch_2)
    grinches.add(grinch_3)


def set_pause():
    pygame.draw.rect(window, (40, 223, 218), (150, 250, 500, 400))
    window.blit(pause_font.render("Game Paused", True, (47, 79, 79)), (280, 280))
    window.blit(pause_font.render("Press SPACE to Continue", True, (25, 25, 112)), (205, 400))
    window.blit(pause_font.render("Press Q to Start Over", True, (165, 42, 42)), (230, 480))

def draw_gifts_counter():
    global gifts_collected

    pygame.draw.circle(window, (100, 220, 40), (500, 30), 25)
    pygame.draw.rect(window, (100, 220, 40), (500, 5, 250, 50))
    pygame.draw.circle(window, (100, 220, 40), (750, 30), 25)
    window.blit(gift_font.render(f'Collected gifts: {gifts_collected}', False, (15, 122, 205)), (550, 15))
    gift_count_icon.draw()


def draw_win():
    pygame.draw.rect(window, (40, 223, 218), (150, 250, 500, 400))
    window.blit(win_font.render("YOU WIN!!!", True, (47, 79, 79)), (280, 300))

# Add a reset button
reset_button_rect = pygame.Rect(250, 550, 300, 100)
reset_button_font = pygame.font.Font('fonts/gunplay_3d.otf', 32)

def draw_reset_button():
    pygame.draw.rect(window, (255, 0, 0), reset_button_rect)
    window.blit(reset_button_font.render("Try Again", True, (255, 255, 255)), (290, 570))

def check_reset_button_click(mouse_pos):
    return reset_button_rect.collidepoint(mouse_pos)

def draw_game_over():
    pygame.draw.rect(window, (40, 223, 218), (150, 250, 500, 400))
    window.blit(win_font.render("GAME OVER (((", True, (47, 79, 79)), (250, 300))


while running:
    window.blit(background, (0, 0))
    # close
    for e in pygame.event.get():
        if e.type == QUIT:
            running = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE and finish != True:
                paused = not paused
            if e.key == K_q and paused:
                paused = False
                reset_game()
        elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            if check_reset_button_click(pygame.mouse.get_pos()) and finish:
                finish = False
                reset_game()

    if paused:
        set_pause()

    else:
        if finish != True:
            game_sound.play()
            for wall in walls:
                wall.draw()

            for gift in gifts:
                gift.draw()

            for grinch in grinches:
                grinch.moving()
                grinch.draw()

            tree.draw()

            draw_gifts_counter()

            player.moving()
            player.draw()

        if sprite.spritecollide(player, gifts, True):
            gifts_collected += 1

        # Програш
        if sprite.spritecollide(player, grinches, False):
            draw_game_over()
            if finish == False:
                game_sound.stop()
                game_over_sound.play()
            finish = True


        #Перемога
        if sprite.collide_rect(player, tree) and gifts_collected == 4:
            draw_win()
            if finish == False:
                game_sound.stop()
                win_sound.play()
            finish = True

    display.update()
    clock.tick(FPS)
