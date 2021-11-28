import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

tilt = pygame.image.load('hawthorne/assets/tilt.png').convert_alpha()
feature = pygame.image.load('hawthorne/assets/feature.png').convert_alpha()
feature_50 = pygame.image.load('hawthorne/assets/feature_50.png').convert_alpha()
feature_100 = pygame.image.load('hawthorne/assets/feature_100.png').convert_alpha()
feature_150 = pygame.image.load('hawthorne/assets/feature_150.png').convert_alpha()
feature_200 = pygame.image.load('hawthorne/assets/feature_200.png').convert_alpha()
feature_400 = pygame.image.load('hawthorne/assets/feature_400.png').convert_alpha()
feature_600 = pygame.image.load('hawthorne/assets/feature_600.png').convert_alpha()
feature_800 = pygame.image.load('hawthorne/assets/feature_800.png').convert_alpha()
feature_1000 = pygame.image.load('hawthorne/assets/feature_1000.png').convert_alpha()
multiple = pygame.image.load('hawthorne/assets/multiple.png').convert_alpha()
multiplier_1 = pygame.image.load('hawthorne/assets/multiplier_1.png').convert_alpha()
multiplier_2 = pygame.image.load('hawthorne/assets/multiplier_2.png').convert_alpha()
multiplier_3 = pygame.image.load('hawthorne/assets/multiplier_3.png').convert_alpha()
multiplier_4 = pygame.image.load('hawthorne/assets/multiplier_4.png').convert_alpha()
multiplier_5 = pygame.image.load('hawthorne/assets/multiplier_5.png').convert_alpha()
multiplier_6 = pygame.image.load('hawthorne/assets/multiplier_6.png').convert_alpha()
multiplier_7 = pygame.image.load('hawthorne/assets/multiplier_7.png').convert_alpha()
multiplier_8 = pygame.image.load('hawthorne/assets/multiplier_8.png').convert_alpha()
multiplier_9 = pygame.image.load('hawthorne/assets/multiplier_9.png').convert_alpha()
multiplier_10 = pygame.image.load('hawthorne/assets/multiplier_10.png').convert_alpha()
odds = pygame.image.load('hawthorne/assets/odds.png').convert_alpha()
section = pygame.image.load('hawthorne/assets/section.png').convert_alpha()
selection = pygame.image.load('hawthorne/assets/selection.png').convert_alpha()
bg_menu = pygame.image.load('hawthorne/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('hawthorne/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('hawthorne/assets/backglass_off.png').convert_alpha()

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
 
    if s.game.tilt.status == False:
        if s.game.feature_unit.position == 1:
            p = [631,745]
            screen.blit(feature_50, p)
        if s.game.feature_unit.position == 2:
            p = [632,777]
            screen.blit(feature_100, p)
        if s.game.feature_unit.position == 3:
            p = [632,810]
            screen.blit(feature_150, p)
        if s.game.feature_unit.position == 4:
            p = [632,838]
            screen.blit(feature_200, p)
        if s.game.feature_unit.position == 5:
            p = [632,871]
            screen.blit(feature_400, p)
        if s.game.feature_unit.position == 6:
            p = [632,901]
            screen.blit(feature_600, p)
        if s.game.feature_unit.position == 7:
            p = [632,932]
            screen.blit(feature_800, p)
        if s.game.feature_unit.position == 8:
            p = [626,964]
            screen.blit(feature_1000, p)
        if s.game.feature_unit_left.position == 1:
            p = [47,742]
            screen.blit(feature_50, p)
        if s.game.feature_unit_left.position == 2:
            p = [42,774]
            screen.blit(feature_100, p)
        if s.game.feature_unit_left.position == 3:
            p = [42,806]
            screen.blit(feature_150, p)
        if s.game.feature_unit_left.position == 4:
            p = [42,837]
            screen.blit(feature_200, p)
        if s.game.feature_unit_left.position == 5:
            p = [42,869]
            screen.blit(feature_400, p)
        if s.game.feature_unit_left.position == 6:
            p = [43,900]
            screen.blit(feature_600, p)
        if s.game.feature_unit_left.position == 7:
            p = [42,931]
            screen.blit(feature_800, p)
        if s.game.feature_unit_left.position == 8:
            p = [40,962]
            screen.blit(feature_1000, p)

        if s.game.left.status == True:
            p = [32,656]
            screen.blit(feature, p)
        if s.game.right.status == True:
            p = [622,658]
            screen.blit(feature, p)

        if 1 in s.game.selection:
            p = [289,295]
            screen.blit(selection, p)
        if 2 in s.game.selection:
            p = [112,343]
            screen.blit(selection, p)
        if 3 in s.game.selection:
            p = [467,346]
            screen.blit(selection, p)
        if 4 in s.game.selection:
            p = [20,503]
            screen.blit(selection, p)
        if 5 in s.game.selection:
            p = [199,504]
            screen.blit(selection, p)
        if 6 in s.game.selection:
            p = [377,504]
            screen.blit(selection, p)
        if 7 in s.game.selection:
            p = [554,504]
            screen.blit(selection, p)

        p = [132,664]
        screen.blit(section, p)
        if s.game.odds.position == 1:
            p = [526,666]
            screen.blit(odds, p)
        if s.game.odds.position == 2:
            p = [456,666]
            screen.blit(odds, p)
        if s.game.odds.position == 3:
            p = [386,666]
            screen.blit(odds, p)
        if s.game.odds.position == 4:
            p = [314,666]
            screen.blit(odds, p)
        if s.game.odds.position == 5:
            p = [244,666]
            screen.blit(odds, p)

        p = [100,974]
        screen.blit(multiple, p)
        if s.game.coin.position == 1:
            p = [187,970]
            screen.blit(multiplier_1, p)
        if s.game.coin.position == 2:
            p = [225,970]
            screen.blit(multiplier_2, p)
        if s.game.coin.position == 3:
            p = [270,970]
            screen.blit(multiplier_3, p)
        if s.game.coin.position == 4:
            p = [312,970]
            screen.blit(multiplier_4, p)
        if s.game.coin.position == 5:
            p = [360,970]
            screen.blit(multiplier_5, p)
        if s.game.coin.position == 6:
            p = [406,970]
            screen.blit(multiplier_6, p)
        if s.game.coin.position == 7:
            p = [452,970]
            screen.blit(multiplier_7, p)
        if s.game.coin.position == 8:
            p = [492,970]
            screen.blit(multiplier_8, p)
        if s.game.coin.position == 9:
            p = [540,970]
            screen.blit(multiplier_9, p)
        if s.game.coin.position == 10:
            p = [574,970]
            screen.blit(multiplier_10, p)

    if s.game.tilt.status == True:
        tilt_position = [658,299]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def selection_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if 1 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (289,295), pygame.Rect(289,295,155,142)))
    if 2 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (112,343), pygame.Rect(112,343,155,142)))
    if 3 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (467,346), pygame.Rect(467,346,155,142)))
    if 4 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (20,503), pygame.Rect(20,503,155,142)))
    if 5 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (199,504), pygame.Rect(199,504,155,142)))
    if 6 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (377,504), pygame.Rect(377,504,155,142)))
    if 7 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (554,504), pygame.Rect(554,504,155,142)))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [289,295]
            dirty_rects.append(screen.blit(selection, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [112,343]
            dirty_rects.append(screen.blit(selection, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection:
            p = [467,346]
            dirty_rects.append(screen.blit(selection, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection:
            p = [20,503]
            dirty_rects.append(screen.blit(selection, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection:
            p = [199,504]
            dirty_rects.append(screen.blit(selection, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [377,504]
            dirty_rects.append(screen.blit(selection, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [554,504]
            dirty_rects.append(screen.blit(selection, p))

    pygame.display.update(dirty_rects)
    return

def star_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (526,666), pygame.Rect(526,666,67,219)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (456,666), pygame.Rect(456,666,67,219)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (386,666), pygame.Rect(386,666,67,219)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (314,666), pygame.Rect(314,666,67,219)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (244,666), pygame.Rect(244,666,67,219)))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [526,666]
            dirty_rects.append(screen.blit(odds, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [456,666]
            dirty_rects.append(screen.blit(odds, p))
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [386,666]
            dirty_rects.append(screen.blit(odds, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [314,666]
            dirty_rects.append(screen.blit(odds, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [244,666]
            dirty_rects.append(screen.blit(odds, p))

    pygame.display.update(dirty_rects)
    return

