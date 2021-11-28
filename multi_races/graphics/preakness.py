import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

odds = pygame.image.load('preakness/assets/odds.png').convert_alpha()
section = pygame.image.load('preakness/assets/section.png').convert_alpha()
selection1 = pygame.image.load('preakness/assets/selection1.png').convert_alpha()
selection2 = pygame.image.load('preakness/assets/selection2.png').convert_alpha()
selection3 = pygame.image.load('preakness/assets/selection3.png').convert_alpha()
selection4 = pygame.image.load('preakness/assets/selection4.png').convert_alpha()
selection5 = pygame.image.load('preakness/assets/selection5.png').convert_alpha()
selection6 = pygame.image.load('preakness/assets/selection6.png').convert_alpha()
selection7 = pygame.image.load('preakness/assets/selection7.png').convert_alpha()
bg_menu = pygame.image.load('preakness/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('preakness/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('preakness/assets/backglass_off.png').convert_alpha()

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
        if 1 in s.game.selection:
            p = [5,672]
            screen.blit(selection1, p)
        if 2 in s.game.selection:
            p = [28,540]
            screen.blit(selection2, p)
        if 3 in s.game.selection:
            p = [132,460]
            screen.blit(selection3, p)
        if 4 in s.game.selection:
            p = [276,450]
            screen.blit(selection4, p)
        if 5 in s.game.selection:
            p = [400,460]
            screen.blit(selection5, p)
        if 6 in s.game.selection:
            p = [481,537]
            screen.blit(selection6, p)
        if 7 in s.game.selection:
            p = [525,675]
            screen.blit(selection7, p)

        p = [228,672]
        screen.blit(section, p)
        if s.game.odds.position == 1:
            p = [436,666]
            screen.blit(odds, p)
        if s.game.odds.position == 2:
            p = [401,666]
            screen.blit(odds, p)
        if s.game.odds.position == 3:
            p = [358,666]
            screen.blit(odds, p)
        if s.game.odds.position == 4:
            p = [324,666]
            screen.blit(odds, p)
        if s.game.odds.position == 5:
            p = [287,666]
            screen.blit(odds, p)

    pygame.display.update()

def selection_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if 1 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (5,672), pygame.Rect(5,672,176,160)))
    if 2 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (28,540), pygame.Rect(28,540,202,197)))
    if 3 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (132,460), pygame.Rect(132,460,181,204)))
    if 4 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (276,450), pygame.Rect(276,450,159,180)))
    if 5 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (400,460), pygame.Rect(400,460,183,204)))
    if 6 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (481,537), pygame.Rect(481,537,195,190)))
    if 7 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (525,675), pygame.Rect(525,675,189,151)))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [5,672]
            dirty_rects.append(screen.blit(selection1, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [28,540]
            dirty_rects.append(screen.blit(selection2, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection:
            p = [132,460]
            dirty_rects.append(screen.blit(selection3, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection:
            p = [276,450]
            dirty_rects.append(screen.blit(selection4, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection:
            p = [400,460]
            dirty_rects.append(screen.blit(selection5, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [481,537]
            dirty_rects.append(screen.blit(selection6, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [525,675]
            dirty_rects.append(screen.blit(selection7, p))

    pygame.display.update(dirty_rects)
    return

def star_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (436,666), pygame.Rect(436,666,45,164)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (401,666), pygame.Rect(401,666,45,164)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (358,666), pygame.Rect(358,666,45,164)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (324,666), pygame.Rect(324,666,45,164)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (284,666), pygame.Rect(287,666,45,164)))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [436,666]
            dirty_rects.append(screen.blit(odds, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [401,666]
            dirty_rects.append(screen.blit(odds, p))
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [358,666]
            dirty_rects.append(screen.blit(odds, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [324,666]
            dirty_rects.append(screen.blit(odds, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [284,666]
            dirty_rects.append(screen.blit(odds, p))

    pygame.display.update(dirty_rects)
    return

