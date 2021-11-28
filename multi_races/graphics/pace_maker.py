import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

odds = pygame.image.load('pace_maker/assets/odds.png').convert_alpha()
section = pygame.image.load('pace_maker/assets/section.png').convert_alpha()
selection1 = pygame.image.load('pace_maker/assets/selection1.png').convert_alpha()
selection2 = pygame.image.load('pace_maker/assets/selection2.png').convert_alpha()
selection3 = pygame.image.load('pace_maker/assets/selection3.png').convert_alpha()
selection4 = pygame.image.load('pace_maker/assets/selection4.png').convert_alpha()
selection5 = pygame.image.load('pace_maker/assets/selection5.png').convert_alpha()
selection6 = pygame.image.load('pace_maker/assets/selection6.png').convert_alpha()
selection7 = pygame.image.load('pace_maker/assets/selection7.png').convert_alpha()
multiplier1 = pygame.image.load('pace_maker/assets/multiplier1.png').convert_alpha()
multiplier2 = pygame.image.load('pace_maker/assets/multiplier2.png').convert_alpha()
multiplier3 = pygame.image.load('pace_maker/assets/multiplier3.png').convert_alpha()
multiplier4 = pygame.image.load('pace_maker/assets/multiplier4.png').convert_alpha()
tilt = pygame.image.load('pace_maker/assets/tilt.png').convert_alpha()
bg_menu = pygame.image.load('pace_maker/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('pace_maker/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('pace_maker/assets/backglass_off.png').convert_alpha()
sweepstakes = pygame.image.load('pace_maker/assets/sweepstakes.png').convert_alpha()

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
            p = [294,418]
            screen.blit(selection1, p)
        if 2 in s.game.selection:
            p = [146,420]
            screen.blit(selection2, p)
        if 3 in s.game.selection:
            p = [45,460]
            screen.blit(selection3, p)
        if 4 in s.game.selection:
            p = [25,581]
            screen.blit(selection4, p)
        if 5 in s.game.selection:
            p = [43,668]
            screen.blit(selection5, p)
        if 6 in s.game.selection:
            p = [144,729]
            screen.blit(selection6, p)
        if 7 in s.game.selection:
            p = [289,735]
            screen.blit(selection7, p)

        p = [427,509]
        screen.blit(section, p)
        if s.game.odds.position == 1:
            p = [426,797]
            screen.blit(odds, p)
        if s.game.odds.position == 2:
            p = [426,738]
            screen.blit(odds, p)
        if s.game.odds.position == 3:
            p = [427,678]
            screen.blit(odds, p)
        if s.game.odds.position == 4:
            p = [427,618]
            screen.blit(odds, p)
        if s.game.odds.position == 5:
            p = [427,558]
            screen.blit(odds, p)

        if s.game.coin.position == 1:
            p = [17,495]
            screen.blit(multiplier1, p)
        if s.game.coin.position == 2:
            p = [40,464]
            screen.blit(multiplier2, p)
        if s.game.coin.position == 3:
            p = [69,438]
            screen.blit(multiplier3, p)
        if s.game.coin.position == 4:
            p = [105,416]
            screen.blit(multiplier4, p)

        if s.game.sweepstakes.status == True:
            p = [16,795]
            screen.blit(sweepstakes, p)

    if s.game.tilt.status == True:
        p = [304,643]
        screen.blit(tilt, p)

    pygame.display.update()

def selection_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if 1 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (294,418), pygame.Rect(294,418,124,126)))
    if 2 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (146,420), pygame.Rect(146,420,138,128)))
    if 3 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (9,415), pygame.Rect(9,415,145,115)))
        dirty_rects.append(screen.blit(bg_gi, (45,460), pygame.Rect(45,460,151,143)))
    if 4 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (25,581), pygame.Rect(25,581,134,119)))
    if 5 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (43,668), pygame.Rect(43,668,156,144)))
    if 6 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (144,729), pygame.Rect(144,729,144,136)))
    if 7 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (289,735), pygame.Rect(289,735,126,128)))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [294,418]
            dirty_rects.append(screen.blit(selection1, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [146,420]
            dirty_rects.append(screen.blit(selection2, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection:
            p = [45,460]
            dirty_rects.append(screen.blit(selection3, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection:
            p = [25,581]
            dirty_rects.append(screen.blit(selection4, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection:
            p = [43,668]
            dirty_rects.append(screen.blit(selection5, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [144,729]
            dirty_rects.append(screen.blit(selection6, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [289,735]
            dirty_rects.append(screen.blit(selection7, p))

    pygame.display.update(dirty_rects)
    return

def star_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (429,797), pygame.Rect(429,797,280,55)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (426,738), pygame.Rect(426,738,280,55)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (427,678), pygame.Rect(427,678,280,55)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (427,618), pygame.Rect(427,618,280,55)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (427,558), pygame.Rect(427,558,280,55)))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [429,797]
            dirty_rects.append(screen.blit(odds, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [426,738]
            dirty_rects.append(screen.blit(odds, p))
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [427,678]
            dirty_rects.append(screen.blit(odds, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [427,618]
            dirty_rects.append(screen.blit(odds, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [427,558]
            dirty_rects.append(screen.blit(odds, p))

    pygame.display.update(dirty_rects)
    return

