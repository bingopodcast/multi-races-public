import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

odds1 = pygame.image.load('arlington/assets/odds1.png').convert_alpha()
odds2 = pygame.image.load('arlington/assets/odds2.png').convert_alpha()
odds3 = pygame.image.load('arlington/assets/odds3.png').convert_alpha()
odds4 = pygame.image.load('arlington/assets/odds4.png').convert_alpha()
odds5 = pygame.image.load('arlington/assets/odds5.png').convert_alpha()
selection1 = pygame.image.load('arlington/assets/selection1.png').convert_alpha()
selection2 = pygame.image.load('arlington/assets/selection2.png').convert_alpha()
selection3 = pygame.image.load('arlington/assets/selection3.png').convert_alpha()
selection4 = pygame.image.load('arlington/assets/selection4.png').convert_alpha()
selection5 = pygame.image.load('arlington/assets/selection5.png').convert_alpha()
selection6 = pygame.image.load('arlington/assets/selection6.png').convert_alpha()
selection7 = pygame.image.load('arlington/assets/selection7.png').convert_alpha()
bg_menu = pygame.image.load('arlington/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('arlington/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('arlington/assets/backglass_off.png').convert_alpha()

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
            p = [4,645]
            screen.blit(selection1, p)
        if 2 in s.game.selection:
            p = [2,422]
            screen.blit(selection2, p)
        if 3 in s.game.selection:
            p = [146,422]
            screen.blit(selection3, p)
        if 4 in s.game.selection:
            p = [292,422]
            screen.blit(selection4, p)
        if 5 in s.game.selection:
            p = [436,422]
            screen.blit(selection5, p)
        if 6 in s.game.selection:
            p = [579,422]
            screen.blit(selection6, p)
        if 7 in s.game.selection:
            p = [579,641]
            screen.blit(selection7, p)

        if s.game.odds.position == 1:
            p = [443,670]
            screen.blit(odds1, p)
        if s.game.odds.position == 2:
            p = [405,670]
            screen.blit(odds2, p)
        if s.game.odds.position == 3:
            p = [367,671]
            screen.blit(odds3, p)
        if s.game.odds.position == 4:
            p = [332,670]
            screen.blit(odds4, p)
        if s.game.odds.position == 5:
            p = [292,670]
            screen.blit(odds5, p)

    pygame.display.update()

def selection_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if 1 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (4,645), pygame.Rect(4,645,143,205)))
    if 2 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (2,422), pygame.Rect(2,422,143,205)))
    if 3 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (146,422), pygame.Rect(146,422,141,207)))
    if 4 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (292,422), pygame.Rect(292,422,140,203)))
    if 5 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (436,422), pygame.Rect(436,422,139,203)))
    if 6 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (579,422), pygame.Rect(579,422,138,203)))
    if 7 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (579,641), pygame.Rect(579,641,139,206)))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [4,645]
            dirty_rects.append(screen.blit(selection1, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [2,422]
            dirty_rects.append(screen.blit(selection2, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection:
            p = [146,422]
            dirty_rects.append(screen.blit(selection3, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection:
            p = [292,422]
            dirty_rects.append(screen.blit(selection4, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection:
            p = [436,422]
            dirty_rects.append(screen.blit(selection5, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [579,422]
            dirty_rects.append(screen.blit(selection6, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [579,641]
            dirty_rects.append(screen.blit(selection7, p))

    pygame.display.update(dirty_rects)
    return

def star_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (443,670), pygame.Rect(443,670,39,183)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (405,670), pygame.Rect(405,670,39,183)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (367,671), pygame.Rect(367,671,39,183)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (332,670), pygame.Rect(332,670,39,183)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (292,670), pygame.Rect(292,670,39,183)))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [443,670]
            dirty_rects.append(screen.blit(odds1, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [405,670]
            dirty_rects.append(screen.blit(odds2, p))
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [367,671]
            dirty_rects.append(screen.blit(odds3, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [332,670]
            dirty_rects.append(screen.blit(odds4, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [292,670]
            dirty_rects.append(screen.blit(odds5, p))

    pygame.display.update(dirty_rects)
    return

