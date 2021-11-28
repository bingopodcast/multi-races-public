import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

odds = pygame.image.load('sport_page/assets/odds.png').convert_alpha()
section = pygame.image.load('sport_page/assets/section.png').convert_alpha()
selection1 = pygame.image.load('sport_page/assets/selection1.png').convert_alpha()
selection2 = pygame.image.load('sport_page/assets/selection2.png').convert_alpha()
selection3 = pygame.image.load('sport_page/assets/selection3.png').convert_alpha()
selection4 = pygame.image.load('sport_page/assets/selection4.png').convert_alpha()
selection5 = pygame.image.load('sport_page/assets/selection5.png').convert_alpha()
selection6 = pygame.image.load('sport_page/assets/selection6.png').convert_alpha()
selection7 = pygame.image.load('sport_page/assets/selection7.png').convert_alpha()
multiplier = pygame.image.load('sport_page/assets/multiplier.png').convert_alpha()
bg_menu = pygame.image.load('sport_page/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('sport_page/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('sport_page/assets/backglass_off.png').convert_alpha()
tilt = pygame.image.load('sport_page/assets/tilt.png').convert_alpha()

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
            p = [102,479]
            screen.blit(selection1, p)
        if 2 in s.game.selection:
            p = [26,570]
            screen.blit(selection2, p)
        if 3 in s.game.selection:
            p = [39,688]
            screen.blit(selection3, p)
        if 4 in s.game.selection:
            p = [157,721]
            screen.blit(selection4, p)
        if 5 in s.game.selection:
            p = [309,725]
            screen.blit(selection5, p)
        if 6 in s.game.selection:
            p = [441,727]
            screen.blit(selection6, p)
        if 7 in s.game.selection:
            p = [577,729]
            screen.blit(selection7, p)

        p = [243,473]
        screen.blit(section, p)
        if s.game.odds.position == 1:
            p = [642,473]
            screen.blit(odds, p)
        if s.game.odds.position == 2:
            p = [571,473]
            screen.blit(odds, p)
        if s.game.odds.position == 3:
            p = [501,473]
            screen.blit(odds, p)
        if s.game.odds.position == 4:
            p = [431,473]
            screen.blit(odds, p)
        if s.game.odds.position == 5:
            p = [358,473]
            screen.blit(odds, p)

        if s.game.coin.position == 1:
            p = [459,675]
            screen.blit(multiplier, p)
        if s.game.coin.position == 2:
            p = [522,675]
            screen.blit(multiplier, p)
        if s.game.coin.position == 3:
            p = [587,675]
            screen.blit(multiplier, p)
        if s.game.coin.position == 4:
            p = [650,675]
            screen.blit(multiplier, p)

    else:
        p = [35,816]
        screen.blit(tilt, p)

    pygame.display.update()

def selection_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if 1 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (102,479), pygame.Rect(102,479,136,143)))
    if 2 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (26,570), pygame.Rect(26,570,161,124)))
    if 3 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (39,688), pygame.Rect(39,688,164,130)))
    if 4 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (157,721), pygame.Rect(157,721,151,146)))
    if 5 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (309,725), pygame.Rect(309,725,129,143)))
    if 6 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (441,727), pygame.Rect(441,727,131,145)))
    if 7 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (577,729), pygame.Rect(577,729,132,142)))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [102,479]
            dirty_rects.append(screen.blit(selection1, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [26,570]
            dirty_rects.append(screen.blit(selection2, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection:
            p = [39,688]
            dirty_rects.append(screen.blit(selection3, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection:
            p = [157,721]
            dirty_rects.append(screen.blit(selection4, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection:
            p = [309,725]
            dirty_rects.append(screen.blit(selection5, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [441,727]
            dirty_rects.append(screen.blit(selection6, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [577,729]
            dirty_rects.append(screen.blit(selection7, p))

    pygame.display.update(dirty_rects)
    return

def star_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (642,473), pygame.Rect(642,473,70,198)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (571,473), pygame.Rect(571,473,70,198)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (501,473), pygame.Rect(501,473,70,198)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (431,473), pygame.Rect(431,473,70,198)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (358,473), pygame.Rect(358,473,70,198)))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [642,473]
            dirty_rects.append(screen.blit(odds, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [571,473]
            dirty_rects.append(screen.blit(odds, p))
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [501,473]
            dirty_rects.append(screen.blit(odds, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [431,473]
            dirty_rects.append(screen.blit(odds, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [358,473]
            dirty_rects.append(screen.blit(odds, p))

    pygame.display.update(dirty_rects)
    return

