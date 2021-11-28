import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

tilt = pygame.image.load('pimlico/assets/tilt.png').convert_alpha()
feature = pygame.image.load('pimlico/assets/feature.png').convert_alpha()
feature_10 = pygame.image.load('pimlico/assets/feature_10.png').convert_alpha()
feature_15 = pygame.image.load('pimlico/assets/feature_15.png').convert_alpha()
feature_20 = pygame.image.load('pimlico/assets/feature_20.png').convert_alpha()
feature_25 = pygame.image.load('pimlico/assets/feature_25.png').convert_alpha()
feature_30 = pygame.image.load('pimlico/assets/feature_30.png').convert_alpha()
feature_35 = pygame.image.load('pimlico/assets/feature_35.png').convert_alpha()
feature_40 = pygame.image.load('pimlico/assets/feature_40.png').convert_alpha()
feature_45 = pygame.image.load('pimlico/assets/feature_45.png').convert_alpha()
multiplier = pygame.image.load('pimlico/assets/multiplier.png').convert_alpha()
letter_p = pygame.image.load('pimlico/assets/letter_p.png').convert_alpha()
letter_i = pygame.image.load('pimlico/assets/letter_i.png').convert_alpha()
letter_m = pygame.image.load('pimlico/assets/letter_m.png').convert_alpha()
letter_l = pygame.image.load('pimlico/assets/letter_l.png').convert_alpha()
letter_i2 = pygame.image.load('pimlico/assets/letter_i2.png').convert_alpha()
letter_c = pygame.image.load('pimlico/assets/letter_c.png').convert_alpha()
letter_o = pygame.image.load('pimlico/assets/letter_o.png').convert_alpha()
odds = pygame.image.load('pimlico/assets/odds.png').convert_alpha()
section = pygame.image.load('pimlico/assets/section.png').convert_alpha()
selection = pygame.image.load('pimlico/assets/selection.png').convert_alpha()
left_wreath = pygame.image.load('pimlico/assets/left.png').convert_alpha()
right_wreath = pygame.image.load('pimlico/assets/right.png').convert_alpha()
bg_menu = pygame.image.load('pimlico/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('pimlico/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('pimlico/assets/backglass_off.png').convert_alpha()

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

    p = [179,364]
    screen.blit(letter_p, p)
    p = [225,357]
    screen.blit(letter_i, p)

    if s.game.name.position >= 1:
        p = [260,344]
        screen.blit(letter_m, p)
    if s.game.name.position >= 2:
        p = [336,342]
        screen.blit(letter_l, p)
    if s.game.name.position >= 3:
        p = [384,340]
        screen.blit(letter_i2, p)
    if s.game.name.position >= 4:
        p = [416,346]
        screen.blit(letter_c, p)
    if s.game.name.position == 5:
        p = [473,357]
        screen.blit(letter_o, p)

    if s.game.tilt.status == False:
        if s.game.feature_unit.position == 1:
            p = [457,446]
            screen.blit(feature_10, p)
        if s.game.feature_unit.position == 2:
            p = [457,446]
            screen.blit(feature_15, p)
        if s.game.feature_unit.position == 3:
            p = [457,446]
            screen.blit(feature_20, p)
        if s.game.feature_unit.position == 4:
            p = [457,446]
            screen.blit(feature_25, p)
        if s.game.feature_unit.position == 5:
            p = [457,446]
            screen.blit(feature_30, p)
        if s.game.feature_unit.position == 6:
            p = [457,446]
            screen.blit(feature_35, p)
        if s.game.feature_unit.position == 7:
            p = [457,446]
            screen.blit(feature_40, p)
        if s.game.feature_unit.position == 8:
            p = [457,446]
            screen.blit(feature_45, p)

        if s.game.pennant.status == True:
            p = [504,442]
            screen.blit(feature, p)

        if s.game.left.status == True:
            p = [8,335]
            screen.blit(left_wreath, p)
        if s.game.right.status == True:
            p = [631,330]
            screen.blit(right_wreath, p)

        if 1 in s.game.selection:
            p = [16,716]
            screen.blit(selection, p)
        if 2 in s.game.selection:
            p = [15,840]
            screen.blit(selection, p)
        if 3 in s.game.selection:
            p = [156,836]
            screen.blit(selection, p)
        if 4 in s.game.selection:
            p = [296,834]
            screen.blit(selection, p)
        if 5 in s.game.selection:
            p = [438,833]
            screen.blit(selection, p)
        if 6 in s.game.selection:
            p = [580,833]
            screen.blit(selection, p)
        if 7 in s.game.selection:
            p = [581,713]
            screen.blit(selection, p)

        p = [130,486]
        screen.blit(section, p)
        if s.game.odds.position == 1:
            p = [526,483]
            screen.blit(odds, p)
        if s.game.odds.position == 2:
            p = [454,484]
            screen.blit(odds, p)
        if s.game.odds.position == 3:
            p = [381,484]
            screen.blit(odds, p)
        if s.game.odds.position == 4:
            p = [310,484]
            screen.blit(odds, p)
        if s.game.odds.position == 5:
            p = [238,485]
            screen.blit(odds, p)

        if s.game.coin.position == 1:
            p = [282,439]
            screen.blit(multiplier, p)
        if s.game.coin.position == 2:
            p = [324,438]
            screen.blit(multiplier, p)
        if s.game.coin.position == 3:
            p = [366,438]
            screen.blit(multiplier, p)
        if s.game.coin.position == 4:
            p = [408,437]
            screen.blit(multiplier, p)

    if s.game.tilt.status == True:
        tilt_position = [234,448]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def selection_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if 1 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (16,716), pygame.Rect(16,716,123,112)))
    if 2 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (15,840), pygame.Rect(15,840,123,112)))
    if 3 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (156,836), pygame.Rect(156,836,123,112)))
    if 4 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (296,834), pygame.Rect(296,834,123,112)))
    if 5 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (438,833), pygame.Rect(438,833,123,112)))
    if 6 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (580,833), pygame.Rect(580,833,123,112)))
    if 7 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (581,713), pygame.Rect(581,713,123,112)))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [16,716]
            dirty_rects.append(screen.blit(selection, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [15,840]
            dirty_rects.append(screen.blit(selection, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection:
            p = [156,836]
            dirty_rects.append(screen.blit(selection, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection:
            p = [296,834]
            dirty_rects.append(screen.blit(selection, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection:
            p = [438,833]
            dirty_rects.append(screen.blit(selection, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [580,833]
            dirty_rects.append(screen.blit(selection, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [581,713]
            dirty_rects.append(screen.blit(selection, p))

    pygame.display.update(dirty_rects)
    return

def star_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (526,483), pygame.Rect(526,483,65,214)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (454,484), pygame.Rect(454,484,65,214)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (381,484), pygame.Rect(381,484,65,214)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (310,484), pygame.Rect(310,484,65,214)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (238,485), pygame.Rect(238,485,65,214)))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [526,483]
            dirty_rects.append(screen.blit(odds, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [454,484]
            dirty_rects.append(screen.blit(odds, p))
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [381,484]
            dirty_rects.append(screen.blit(odds, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [310,484]
            dirty_rects.append(screen.blit(odds, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [238,485]
            dirty_rects.append(screen.blit(odds, p))

    pygame.display.update(dirty_rects)
    return

