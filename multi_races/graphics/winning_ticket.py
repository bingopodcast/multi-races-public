import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

odds = pygame.image.load('winning_ticket/assets/odds.png').convert_alpha()
selection = pygame.image.load('winning_ticket/assets/selection.png').convert_alpha()
multiplier = pygame.image.load('winning_ticket/assets/multiplier.png').convert_alpha()
bg_menu = pygame.image.load('winning_ticket/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('winning_ticket/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('winning_ticket/assets/backglass_off.png').convert_alpha()
tilt = pygame.image.load('winning_ticket/assets/tilt.png').convert_alpha()
parlay2 = pygame.image.load('winning_ticket/assets/parlay2.png').convert_alpha()
parlay3 = pygame.image.load('winning_ticket/assets/parlay3.png').convert_alpha()
parlay4 = pygame.image.load('winning_ticket/assets/parlay4.png').convert_alpha()
parlay5 = pygame.image.load('winning_ticket/assets/parlay5.png').convert_alpha()
parlay6 = pygame.image.load('winning_ticket/assets/parlay6.png').convert_alpha()

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
            p = [14,347]
            screen.blit(selection, p)
        if 2 in s.game.selection:
            p = [110,347]
            screen.blit(selection, p)
        if 3 in s.game.selection:
            p = [212,345]
            screen.blit(selection, p)
        if 4 in s.game.selection:
            p = [312,345]
            screen.blit(selection, p)
        if 5 in s.game.selection:
            p = [408,345]
            screen.blit(selection, p)
        if 6 in s.game.selection:
            p = [507,345]
            screen.blit(selection, p)
        if 7 in s.game.selection:
            p = [611,343]
            screen.blit(selection, p)

        if s.game.odds.position == 1:
            p = [521,447]
            screen.blit(odds, p)
        if s.game.odds.position == 2:
            p = [462,449]
            screen.blit(odds, p)
        if s.game.odds.position == 3:
            p = [404,449]
            screen.blit(odds, p)
        if s.game.odds.position == 4:
            p = [347,449]
            screen.blit(odds, p)
        if s.game.odds.position == 5:
            p = [287,449]
            screen.blit(odds, p)

        if s.game.coin.position == 1:
            p = [23,570]
            screen.blit(multiplier, p)
        if s.game.coin.position == 2:
            p = [21,614]
            screen.blit(multiplier, p)
        if s.game.coin.position == 3:
            p = [23,659]
            screen.blit(multiplier, p)
        if s.game.coin.position == 4:
            p = [633,569]
            screen.blit(multiplier, p)
        if s.game.coin.position == 5:
            p = [633,614]
            screen.blit(multiplier, p)
        if s.game.coin.position == 6:
            p = [633,657]
            screen.blit(multiplier, p)

        if s.game.parlay.position == 1:
            p = [222,918]
            screen.blit(parlay2, p)
        if s.game.parlay.position == 2:
            p = [297,918]
            screen.blit(parlay3, p)
        if s.game.parlay.position == 3:
            p = [372,918]
            screen.blit(parlay4, p)
        if s.game.parlay.position == 4:
            p = [434,918]
            screen.blit(parlay5, p)
        if s.game.parlay.position == 5:
            p = [503,918]
            screen.blit(parlay6,p)

    else:
        backglass_position = [0, 0]
        screen.blit(bg_off, backglass_position)
        p = [618,872]
        screen.blit(tilt, p)

    pygame.display.update()

def selection_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if 1 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (14,347), pygame.Rect(14,347,99,97)))
    if 2 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (110,347), pygame.Rect(110,347,99,97)))
    if 3 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (212,345), pygame.Rect(212,345,99,97)))
    if 4 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (312,345), pygame.Rect(312,345,99,97)))
    if 5 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (408,345), pygame.Rect(408,345,99,97)))
    if 6 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (507,345), pygame.Rect(507,345,99,97)))
    if 7 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (611,343), pygame.Rect(611,343,99,97)))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [14,347]
            dirty_rects.append(screen.blit(selection, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [110,347]
            dirty_rects.append(screen.blit(selection, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection:
            p = [212,345]
            dirty_rects.append(screen.blit(selection, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection:
            p = [312,345]
            dirty_rects.append(screen.blit(selection, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection:
            p = [408,345]
            dirty_rects.append(screen.blit(selection, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [507,345]
            dirty_rects.append(screen.blit(selection, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [611,343]
            dirty_rects.append(screen.blit(selection, p))

    pygame.display.update(dirty_rects)
    return

def star_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (521,447), pygame.Rect(521,447,61,198)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (462,449), pygame.Rect(462,449,61,198)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (404,449), pygame.Rect(404,449,61,198)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (347,449), pygame.Rect(347,449,61,198)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (287,449), pygame.Rect(287,449,61,198)))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [521,447]
            dirty_rects.append(screen.blit(odds, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [462,449]
            dirty_rects.append(screen.blit(odds, p))
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [404,449]
            dirty_rects.append(screen.blit(odds, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [347,449]
            dirty_rects.append(screen.blit(odds, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [287,449]
            dirty_rects.append(screen.blit(odds, p))

    pygame.display.update(dirty_rects)
    return

