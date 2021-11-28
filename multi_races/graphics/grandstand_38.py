import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

odds = pygame.image.load('grandstand_38/assets/odds.png').convert_alpha()
section = pygame.image.load('grandstand_38/assets/section.png').convert_alpha()
selection = pygame.image.load('grandstand_38/assets/selection.png').convert_alpha()
multiplier = pygame.image.load('grandstand_38/assets/multiplier.png').convert_alpha()
tilt = pygame.image.load('grandstand_38/assets/tilt.png').convert_alpha()
bg_menu = pygame.image.load('grandstand_38/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('grandstand_38/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('grandstand_38/assets/backglass_off.png').convert_alpha()
sweepstakes = pygame.image.load('grandstand_38/assets/sweepstakes.png').convert_alpha()

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
            p = [15,730]
            screen.blit(selection, p)
        if 2 in s.game.selection:
            p = [15,587]
            screen.blit(selection, p)
        if 3 in s.game.selection:
            p = [156,590]
            screen.blit(selection, p)
        if 4 in s.game.selection:
            p = [296,589]
            screen.blit(selection, p)
        if 5 in s.game.selection:
            p = [438,590]
            screen.blit(selection, p)
        if 6 in s.game.selection:
            p = [577,590]
            screen.blit(selection, p)
        if 7 in s.game.selection:
            p = [578,731]
            screen.blit(selection, p)

        p = [113,404]
        screen.blit(section, p)
        if s.game.odds.position == 1:
            p = [572,404]
            screen.blit(odds, p)
        if s.game.odds.position == 2:
            p = [494,406]
            screen.blit(odds, p)
        if s.game.odds.position == 3:
            p = [416,406]
            screen.blit(odds, p)
        if s.game.odds.position == 4:
            p = [336,404]
            screen.blit(odds, p)
        if s.game.odds.position == 5:
            p = [258,405]
            screen.blit(odds, p)

        if s.game.coin.position == 1:
            p = [166,760]
            screen.blit(multiplier, p)
        if s.game.coin.position == 2:
            p = [229,760]
            screen.blit(multiplier, p)
        if s.game.coin.position == 3:
            p = [440,763]
            screen.blit(multiplier, p)
        if s.game.coin.position == 4:
            p = [502,763]
            screen.blit(multiplier, p)

        if s.game.sweepstakes.status == True:
            p = [38,446]
            screen.blit(sweepstakes, p)

    if s.game.tilt.status == True:
        p = [662,478]
        screen.blit(tilt, p)

    pygame.display.update()

def selection_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if 1 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (15,730), pygame.Rect(15,730,132,128)))
    if 2 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (15,587), pygame.Rect(15,587,132,128)))
    if 3 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (156,590), pygame.Rect(156,590,132,128)))
    if 4 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (296,589), pygame.Rect(296,589,132,128)))
    if 5 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (438,590), pygame.Rect(438,590,132,128)))
    if 6 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (577,590), pygame.Rect(577,590,132,128)))
    if 7 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (578,731), pygame.Rect(578,731,132,128)))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [15,730]
            dirty_rects.append(screen.blit(selection, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [15,587]
            dirty_rects.append(screen.blit(selection, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection:
            p = [156,590]
            dirty_rects.append(screen.blit(selection, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection:
            p = [296,589]
            dirty_rects.append(screen.blit(selection, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection:
            p = [438,590]
            dirty_rects.append(screen.blit(selection, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [577,590]
            dirty_rects.append(screen.blit(selection, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [578,731]
            dirty_rects.append(screen.blit(selection, p))

    pygame.display.update(dirty_rects)
    return

def star_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (572,404), pygame.Rect(572,404,74,170)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (494,406), pygame.Rect(494,406,74,170)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (416,406), pygame.Rect(416,406,74,170)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (336,404), pygame.Rect(336,404,74,170)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (258,405), pygame.Rect(258,405,74,170)))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [572,404]
            dirty_rects.append(screen.blit(odds, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [494,406]
            dirty_rects.append(screen.blit(odds, p))
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [416,406]
            dirty_rects.append(screen.blit(odds, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [336,404]
            dirty_rects.append(screen.blit(odds, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [258,405]
            dirty_rects.append(screen.blit(odds, p))

    pygame.display.update(dirty_rects)
    return

