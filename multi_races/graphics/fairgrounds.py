import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

odds = pygame.image.load('fairgrounds/assets/odds.png').convert_alpha()
section1 = pygame.image.load('fairgrounds/assets/section1.png').convert_alpha()
section2 = pygame.image.load('fairgrounds/assets/section2.png').convert_alpha()
selection1 = pygame.image.load('fairgrounds/assets/selection1.png').convert_alpha()
selection2 = pygame.image.load('fairgrounds/assets/selection2.png').convert_alpha()
selection3 = pygame.image.load('fairgrounds/assets/selection3.png').convert_alpha()
selection4 = pygame.image.load('fairgrounds/assets/selection4.png').convert_alpha()
selection5 = pygame.image.load('fairgrounds/assets/selection5.png').convert_alpha()
selection6 = pygame.image.load('fairgrounds/assets/selection6.png').convert_alpha()
selection7 = pygame.image.load('fairgrounds/assets/selection7.png').convert_alpha()
multiplier1 = pygame.image.load('fairgrounds/assets/multiplier1.png').convert_alpha()
multiplier2 = pygame.image.load('fairgrounds/assets/multiplier2.png').convert_alpha()
multiplier3 = pygame.image.load('fairgrounds/assets/multiplier3.png').convert_alpha()
multiplier4 = pygame.image.load('fairgrounds/assets/multiplier4.png').convert_alpha()
bg_menu = pygame.image.load('fairgrounds/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('fairgrounds/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('fairgrounds/assets/backglass_off.png').convert_alpha()

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
            p = [18,734]
            screen.blit(selection1, p)
        if 2 in s.game.selection:
            p = [36,617]
            screen.blit(selection2, p)
        if 3 in s.game.selection:
            p = [138,552]
            screen.blit(selection3, p)
        if 4 in s.game.selection:
            p = [280,543]
            screen.blit(selection4, p)
        if 5 in s.game.selection:
            p = [413,555]
            screen.blit(selection5, p)
        if 6 in s.game.selection:
            p = [484,618]
            screen.blit(selection6, p)
        if 7 in s.game.selection:
            p = [534,731]
            screen.blit(selection7, p)

        p = [605,395]
        screen.blit(section1, p)
        p = [13,394]
        screen.blit(section2, p)
        if s.game.odds.position == 1:
            p = [511,393]
            screen.blit(odds, p)
        if s.game.odds.position == 2:
            p = [415,392]
            screen.blit(odds, p)
        if s.game.odds.position == 3:
            p = [318,392]
            screen.blit(odds, p)
        if s.game.odds.position == 4:
            p = [220,392]
            screen.blit(odds, p)
        if s.game.odds.position == 5:
            p = [129,393]
            screen.blit(odds, p)

        if s.game.coin.position == 1:
            p = [202,773]
            screen.blit(multiplier1, p)
        if s.game.coin.position == 2:
            p = [269,745]
            screen.blit(multiplier2, p)
        if s.game.coin.position == 3:
            p = [360,743]
            screen.blit(multiplier3, p)
        if s.game.coin.position == 4:
            p = [416,772]
            screen.blit(multiplier4, p)

    pygame.display.update()

def selection_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if 1 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (18,734), pygame.Rect(18,734,163,136)))
    if 2 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (36,617), pygame.Rect(36,617,191,172)))
    if 3 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (138,552), pygame.Rect(138,552,174,175)))
    if 4 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (280,543), pygame.Rect(280,543,155,148)))
    if 5 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (413,555), pygame.Rect(413,555,173,174)))
    if 6 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (484,618), pygame.Rect(484,618,190,171)))
    if 7 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (534,731), pygame.Rect(534,731,168,135)))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [18,734]
            dirty_rects.append(screen.blit(selection1, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [36,617]
            dirty_rects.append(screen.blit(selection2, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection:
            p = [138,552]
            dirty_rects.append(screen.blit(selection3, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection:
            p = [280,543]
            dirty_rects.append(screen.blit(selection4, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection:
            p = [413,555]
            dirty_rects.append(screen.blit(selection5, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [484,618]
            dirty_rects.append(screen.blit(selection6, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [534,731]
            dirty_rects.append(screen.blit(selection7, p))

    pygame.display.update(dirty_rects)
    return

def star_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (511,393), pygame.Rect(511,393,82,134)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (415,392), pygame.Rect(415,392,82,134)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (318,392), pygame.Rect(318,392,82,134)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (220,392), pygame.Rect(220,392,82,134)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (129,393), pygame.Rect(129,393,82,134)))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [511,393]
            dirty_rects.append(screen.blit(odds, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [415,392]
            dirty_rects.append(screen.blit(odds, p))
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [318,392]
            dirty_rects.append(screen.blit(odds, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [220,392]
            dirty_rects.append(screen.blit(odds, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [129,393]
            dirty_rects.append(screen.blit(odds, p))

    pygame.display.update(dirty_rects)
    return

