import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

tilt = pygame.image.load('jockey_club_41/assets/tilt.png').convert_alpha()
feature = pygame.image.load('jockey_club_41/assets/feature.png').convert_alpha()
feature_10 = pygame.image.load('jockey_club_41/assets/feature_10.png').convert_alpha()
feature_15 = pygame.image.load('jockey_club_41/assets/feature_15.png').convert_alpha()
feature_20 = pygame.image.load('jockey_club_41/assets/feature_20.png').convert_alpha()
feature_25 = pygame.image.load('jockey_club_41/assets/feature_25.png').convert_alpha()
feature_30 = pygame.image.load('jockey_club_41/assets/feature_30.png').convert_alpha()
feature_35 = pygame.image.load('jockey_club_41/assets/feature_35.png').convert_alpha()
feature_40 = pygame.image.load('jockey_club_41/assets/feature_40.png').convert_alpha()
feature_45 = pygame.image.load('jockey_club_41/assets/feature_45.png').convert_alpha()
multiplier = pygame.image.load('jockey_club_41/assets/multiplier.png').convert_alpha()
letter_j = pygame.image.load('jockey_club_41/assets/letter_j.png').convert_alpha()
letter_o = pygame.image.load('jockey_club_41/assets/letter_o.png').convert_alpha()
letter_c = pygame.image.load('jockey_club_41/assets/letter_c.png').convert_alpha()
letter_k = pygame.image.load('jockey_club_41/assets/letter_k.png').convert_alpha()
letter_e = pygame.image.load('jockey_club_41/assets/letter_e.png').convert_alpha()
letter_y = pygame.image.load('jockey_club_41/assets/letter_y.png').convert_alpha()
odds = pygame.image.load('jockey_club_41/assets/odds.png').convert_alpha()
section = pygame.image.load('jockey_club_41/assets/section.png').convert_alpha()
selection = pygame.image.load('jockey_club_41/assets/selection.png').convert_alpha()
left_wreath = pygame.image.load('jockey_club_41/assets/left.png').convert_alpha()
right_wreath = pygame.image.load('jockey_club_41/assets/right.png').convert_alpha()
bg_menu = pygame.image.load('jockey_club_41/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('jockey_club_41/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('jockey_club_41/assets/backglass_off.png').convert_alpha()

def display(s, replays=0, menu=False):
    global screen

    backglass_position = [0, 0]
    if menu == True:
        screen.blit(bg_menu, backglass_position)
        pygame.display.update()
        return
    else:
        if (s.game.anti_cheat.status == True):
            screen.blit(bg_gi, backglass_position)
        else:
            screen.blit(bg_off, backglass_position)

    p = [153,313]
    screen.blit(letter_j, p)

    if s.game.name.position >= 1:
        p = [188,313]
        screen.blit(letter_o, p)
    if s.game.name.position >= 2:
        p = [229,313]
        screen.blit(letter_c, p)
    if s.game.name.position >= 3:
        p = [266,313]
        screen.blit(letter_k, p)
    if s.game.name.position >= 4:
        p = [304,313]
        screen.blit(letter_e, p)
    if s.game.name.position == 5:
        p = [340,313]
        screen.blit(letter_y, p)

    if s.game.tilt.status == False:
        if s.game.feature_unit.position == 1:
            p = [432,615]
            screen.blit(feature_10, p)
        if s.game.feature_unit.position == 2:
            p = [432,615]
            screen.blit(feature_15, p)
        if s.game.feature_unit.position == 3:
            p = [432,615]
            screen.blit(feature_20, p)
        if s.game.feature_unit.position == 4:
            p = [432,615]
            screen.blit(feature_25, p)
        if s.game.feature_unit.position == 5:
            p = [432,615]
            screen.blit(feature_30, p)
        if s.game.feature_unit.position == 6:
            p = [432,615]
            screen.blit(feature_35, p)
        if s.game.feature_unit.position == 7:
            p = [432,615]
            screen.blit(feature_40, p)
        if s.game.feature_unit.position == 8:
            p = [432,615]
            screen.blit(feature_45, p)

        if s.game.left.status == True:
            p = [8,310]
            screen.blit(left_wreath, p)
        if s.game.right.status == True:
            p = [636,309]
            screen.blit(right_wreath, p)

        if 1 in s.game.selection:
            p = [20,844]
            screen.blit(selection, p)
        if 2 in s.game.selection:
            p = [20,723]
            screen.blit(selection, p)
        if 3 in s.game.selection:
            p = [132,622]
            screen.blit(selection, p)
        if 4 in s.game.selection:
            p = [290,622]
            screen.blit(selection, p)
        if 5 in s.game.selection:
            p = [449,622]
            screen.blit(selection, p)
        if 6 in s.game.selection:
            p = [564,724]
            screen.blit(selection, p)
        if 7 in s.game.selection:
            p = [564,845]
            screen.blit(selection, p)

        p = [132,368]
        screen.blit(section, p)
        if s.game.odds.position == 1:
            p = [526,368]
            screen.blit(odds, p)
        if s.game.odds.position == 2:
            p = [454,368]
            screen.blit(odds, p)
        if s.game.odds.position == 3:
            p = [380,368]
            screen.blit(odds, p)
        if s.game.odds.position == 4:
            p = [310,368]
            screen.blit(odds, p)
        if s.game.odds.position == 5:
            p = [240,368]
            screen.blit(odds, p)

        if s.game.coin.position == 1:
            p = [6,572]
            screen.blit(multiplier, p)
        if s.game.coin.position == 2:
            p = [7,648]
            screen.blit(multiplier, p)
        if s.game.coin.position == 3:
            p = [676,572]
            screen.blit(multiplier, p)
        if s.game.coin.position == 4:
            p = [676,649]
            screen.blit(multiplier, p)

    if s.game.tilt.status == True:
        tilt_position = [84,614]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def selection_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if 1 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (20,844), pygame.Rect(20,844,148,117)))
    if 2 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (20,723), pygame.Rect(20,723,148,117)))
    if 3 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (132,622), pygame.Rect(132,622,148,117)))
    if 4 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (290,622), pygame.Rect(290,622,148,117)))
    if 5 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (449,622), pygame.Rect(449,622,148,117)))
    if 6 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (564,724), pygame.Rect(564,724,148,117)))
    if 7 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (564,845), pygame.Rect(564,845,148,117)))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [20,844]
            dirty_rects.append(screen.blit(selection, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [20,723]
            dirty_rects.append(screen.blit(selection, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection:
            p = [132,622]
            dirty_rects.append(screen.blit(selection, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection:
            p = [290,622]
            dirty_rects.append(screen.blit(selection, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection:
            p = [449,622]
            dirty_rects.append(screen.blit(selection, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [564,724]
            dirty_rects.append(screen.blit(selection, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [564,845]
            dirty_rects.append(screen.blit(selection, p))

    pygame.display.update(dirty_rects)
    return

def star_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (526,368), pygame.Rect(526,368,66,232)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (454,368), pygame.Rect(454,368,66,232)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (380,368), pygame.Rect(380,368,66,232)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (310,368), pygame.Rect(310,368,66,232)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (240,368), pygame.Rect(240,368,66,232)))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [526,368]
            dirty_rects.append(screen.blit(odds, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [454,368]
            dirty_rects.append(screen.blit(odds, p))
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [380,368]
            dirty_rects.append(screen.blit(odds, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [310,368]
            dirty_rects.append(screen.blit(odds, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [240,368]
            dirty_rects.append(screen.blit(odds, p))

    pygame.display.update(dirty_rects)
    return

