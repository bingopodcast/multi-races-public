import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

odds = pygame.image.load('thistledowns/assets/odds.png').convert_alpha()
section = pygame.image.load('thistledowns/assets/section.png').convert_alpha()
selection1 = pygame.image.load('thistledowns/assets/selection1.png').convert_alpha()
selection2 = pygame.image.load('thistledowns/assets/selection2.png').convert_alpha()
tilt = pygame.image.load('thistledowns/assets/tilt.png').convert_alpha()
bg_menu = pygame.image.load('thistledowns/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('thistledowns/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('thistledowns/assets/backglass_off.png').convert_alpha()
sweepstakes = pygame.image.load('thistledowns/assets/sweepstakes.png').convert_alpha()

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
            p = [59,702]
            screen.blit(selection1, p)
        if 2 in s.game.selection:
            p = [58,559]
            screen.blit(selection2, p)
        if 3 in s.game.selection:
            p = [183,560]
            screen.blit(selection2, p)
        if 4 in s.game.selection:
            p = [310,560]
            screen.blit(selection2, p)
        if 5 in s.game.selection:
            p = [433,560]
            screen.blit(selection2, p)
        if 6 in s.game.selection:
            p = [558,560]
            screen.blit(selection2, p)
        if 7 in s.game.selection:
            p = [556,705]
            screen.blit(selection1, p)

        p = [22,424]
        screen.blit(section, p)
        if s.game.odds.position == 1:
            p = [478,425]
            screen.blit(odds, p)
        if s.game.odds.position == 2:
            p = [392,426]
            screen.blit(odds, p)
        if s.game.odds.position == 3:
            p = [305,426]
            screen.blit(odds, p)
        if s.game.odds.position == 4:
            p = [216,426]
            screen.blit(odds, p)
        if s.game.odds.position == 5:
            p = [130,426]
            screen.blit(odds, p)

        if s.game.sweepstakes.status == True:
            p = [580,428]
            screen.blit(sweepstakes, p)

    if s.game.tilt.status == True:
        p = [336,778]
        screen.blit(tilt, p)

    pygame.display.update()

def selection_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if 1 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (59,702), pygame.Rect(59,702,112,131)))
    if 2 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (58,559), pygame.Rect(58,559,109,131)))
    if 3 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (183,560), pygame.Rect(183,560,109,131)))
    if 4 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (310,560), pygame.Rect(310,560,109,131)))
    if 5 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (433,560), pygame.Rect(433,560,109,131)))
    if 6 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (558,560), pygame.Rect(558,560,109,131)))
    if 7 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (556,705), pygame.Rect(556,705,112,131)))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [59,702]
            dirty_rects.append(screen.blit(selection1, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [58,559]
            dirty_rects.append(screen.blit(selection2, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection:
            p = [183,560]
            dirty_rects.append(screen.blit(selection2, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection:
            p = [310,560]
            dirty_rects.append(screen.blit(selection2, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection:
            p = [433,560]
            dirty_rects.append(screen.blit(selection2, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [558,560]
            dirty_rects.append(screen.blit(selection2, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [556,705]
            dirty_rects.append(screen.blit(selection1, p))

    pygame.display.update(dirty_rects)
    return

def star_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (478,425), pygame.Rect(478,425,83,111)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (392,426), pygame.Rect(392,426,83,111)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (305,426), pygame.Rect(305,426,83,111)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (216,426), pygame.Rect(216,426,83,111)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (130,426), pygame.Rect(130,426,83,111)))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [478,425]
            dirty_rects.append(screen.blit(odds, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [392,426]
            dirty_rects.append(screen.blit(odds, p))
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [305,426]
            dirty_rects.append(screen.blit(odds, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [216,426]
            dirty_rects.append(screen.blit(odds, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [130,426]
            dirty_rects.append(screen.blit(odds, p))

    pygame.display.update(dirty_rects)
    return

