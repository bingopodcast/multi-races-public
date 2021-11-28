import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

odds = pygame.image.load('seabiscuit/assets/odds.png').convert_alpha()
section = pygame.image.load('seabiscuit/assets/section.png').convert_alpha()
selection1 = pygame.image.load('seabiscuit/assets/selection1.png').convert_alpha()
selection2 = pygame.image.load('seabiscuit/assets/selection2.png').convert_alpha()
tilt = pygame.image.load('seabiscuit/assets/tilt.png').convert_alpha()
bg_menu = pygame.image.load('seabiscuit/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('seabiscuit/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('seabiscuit/assets/backglass_off.png').convert_alpha()
sweepstakes = pygame.image.load('seabiscuit/assets/sweepstakes.png').convert_alpha()

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
            p = [52,714]
            screen.blit(selection1, p)
        if 2 in s.game.selection:
            p = [52,548]
            screen.blit(selection2, p)
        if 3 in s.game.selection:
            p = [178,550]
            screen.blit(selection2, p)
        if 4 in s.game.selection:
            p = [304,550]
            screen.blit(selection2, p)
        if 5 in s.game.selection:
            p = [428,548]
            screen.blit(selection2, p)
        if 6 in s.game.selection:
            p = [556,546]
            screen.blit(selection2, p)
        if 7 in s.game.selection:
            p = [551,713]
            screen.blit(selection1, p)

        p = [14,388]
        screen.blit(section, p)
        if s.game.odds.position == 1:
            p = [476,384]
            screen.blit(odds, p)
        if s.game.odds.position == 2:
            p = [388,386]
            screen.blit(odds, p)
        if s.game.odds.position == 3:
            p = [299,386]
            screen.blit(odds, p)
        if s.game.odds.position == 4:
            p = [210,386]
            screen.blit(odds, p)
        if s.game.odds.position == 5:
            p = [122,387]
            screen.blit(odds, p)

        if s.game.sweepstakes.status == True:
            p = [578,392]
            screen.blit(sweepstakes, p)

    if s.game.tilt.status == True:
        p = [323,803]
        screen.blit(tilt, p)

    pygame.display.update()

def selection_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if 1 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (52,714), pygame.Rect(52,714,119,157)))
    if 2 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (52,548), pygame.Rect(52,548,114,155)))
    if 3 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (178,550), pygame.Rect(178,550,114,155)))
    if 4 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (304,550), pygame.Rect(304,550,114,155)))
    if 5 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (428,548), pygame.Rect(428,548,114,155)))
    if 6 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (556,546), pygame.Rect(556,546,114,155)))
    if 7 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (551,713), pygame.Rect(551,713,119,157)))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [52,714]
            dirty_rects.append(screen.blit(selection1, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [52,548]
            dirty_rects.append(screen.blit(selection2, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection:
            p = [178,550]
            dirty_rects.append(screen.blit(selection2, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection:
            p = [304,550]
            dirty_rects.append(screen.blit(selection2, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection:
            p = [428,548]
            dirty_rects.append(screen.blit(selection2, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [556,546]
            dirty_rects.append(screen.blit(selection2, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [551,713]
            dirty_rects.append(screen.blit(selection1, p))

    pygame.display.update(dirty_rects)
    return

def star_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (476,384), pygame.Rect(476,384,88,136)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (388,386), pygame.Rect(388,386,88,136)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (299,386), pygame.Rect(299,386,88,136)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (210,386), pygame.Rect(210,386,88,136)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (122,387), pygame.Rect(122,387,88,136)))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [476,384]
            dirty_rects.append(screen.blit(odds, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [388,386]
            dirty_rects.append(screen.blit(odds, p))
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [299,386]
            dirty_rects.append(screen.blit(odds, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [210,386]
            dirty_rects.append(screen.blit(odds, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [122,387]
            dirty_rects.append(screen.blit(odds, p))

    pygame.display.update(dirty_rects)
    return

