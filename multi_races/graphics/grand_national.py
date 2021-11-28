import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

odds = pygame.image.load('grand_national/assets/odds.png').convert_alpha()
section = pygame.image.load('grand_national/assets/section.png').convert_alpha()
selection = pygame.image.load('grand_national/assets/selection.png').convert_alpha()
multiplier = pygame.image.load('grand_national/assets/multiplier.png').convert_alpha()
tilt = pygame.image.load('grand_national/assets/tilt.png').convert_alpha()
bg_menu = pygame.image.load('grand_national/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('grand_national/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('grand_national/assets/backglass_off.png').convert_alpha()
sweepstakes = pygame.image.load('grand_national/assets/sweepstakes.png').convert_alpha()

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
            p = [17,594]
            screen.blit(selection, p)
        if 2 in s.game.selection:
            p = [19,452]
            screen.blit(selection, p)
        if 3 in s.game.selection:
            p = [160,389]
            screen.blit(selection, p)
        if 4 in s.game.selection:
            p = [301,389]
            screen.blit(selection, p)
        if 5 in s.game.selection:
            p = [441,386]
            screen.blit(selection, p)
        if 6 in s.game.selection:
            p = [584,449]
            screen.blit(selection, p)
        if 7 in s.game.selection:
            p = [581,592]
            screen.blit(selection, p)

        p = [164,546]
        screen.blit(section, p)
        if s.game.odds.position == 1:
            p = [491,547]
            screen.blit(odds, p)
        if s.game.odds.position == 2:
            p = [424,547]
            screen.blit(odds, p)
        if s.game.odds.position == 3:
            p = [360,547]
            screen.blit(odds, p)
        if s.game.odds.position == 4:
            p = [290,547]
            screen.blit(odds, p)
        if s.game.odds.position == 5:
            p = [221,547]
            screen.blit(odds, p)

        if s.game.coin.position == 1:
            p = [209,850]
            screen.blit(multiplier, p)
        if s.game.coin.position == 2:
            p = [273,850]
            screen.blit(multiplier, p)
        if s.game.coin.position == 3:
            p = [399,850]
            screen.blit(multiplier, p)
        if s.game.coin.position == 4:
            p = [461,850]
            screen.blit(multiplier, p)

        if s.game.sweepstakes.status == True:
            p = [21,396]
            screen.blit(sweepstakes, p)

    if s.game.tilt.status == True:
        p = [663,409]
        screen.blit(tilt, p)

    pygame.display.update()

def selection_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if 1 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (17,594), pygame.Rect(17,594,127,125)))
    if 2 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (19,452), pygame.Rect(19,452,127,125)))
    if 3 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (160,389), pygame.Rect(160,389,127,125)))
    if 4 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (301,389), pygame.Rect(301,389,127,125)))
    if 5 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (441,386), pygame.Rect(441,386,127,125)))
    if 6 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (584,449), pygame.Rect(584,449,127,125)))
    if 7 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (581,592), pygame.Rect(581,592,127,125)))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [17,594]
            dirty_rects.append(screen.blit(selection, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [19,452]
            dirty_rects.append(screen.blit(selection, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection:
            p = [160,389]
            dirty_rects.append(screen.blit(selection, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection:
            p = [301,389]
            dirty_rects.append(screen.blit(selection, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection:
            p = [441,386]
            dirty_rects.append(screen.blit(selection, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [584,449]
            dirty_rects.append(screen.blit(selection, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [581,592]
            dirty_rects.append(screen.blit(selection, p))

    pygame.display.update(dirty_rects)
    return

def star_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (491,547), pygame.Rect(491,547,64,194)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (424,547), pygame.Rect(424,547,64,194)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (360,547), pygame.Rect(360,547,64,194)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (290,547), pygame.Rect(290,547,64,194)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (221,547), pygame.Rect(221,547,64,194)))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [491,547]
            dirty_rects.append(screen.blit(odds, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [424,547]
            dirty_rects.append(screen.blit(odds, p))
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [360,547]
            dirty_rects.append(screen.blit(odds, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [290,547]
            dirty_rects.append(screen.blit(odds, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [221,547]
            dirty_rects.append(screen.blit(odds, p))

    pygame.display.update(dirty_rects)
    return

