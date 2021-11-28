import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

tilt = pygame.image.load('long_shot/assets/tilt.png').convert_alpha()
feature = pygame.image.load('long_shot/assets/feature.png').convert_alpha()
multiplier = pygame.image.load('long_shot/assets/multiplier.png').convert_alpha()
odds = pygame.image.load('long_shot/assets/odds.png').convert_alpha()
selection = pygame.image.load('long_shot/assets/selection.png').convert_alpha()
selection2 = pygame.image.load('long_shot/assets/selection2.png').convert_alpha()
bg_menu = pygame.image.load('long_shot/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('long_shot/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('long_shot/assets/backglass_off.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert_alpha()

reel1 = scorereel([140,830], "graphics/assets/transparent_reel.png")
reel10 = scorereel([130,830], "graphics/assets/transparent_reel.png")
reel100 = scorereel([120,830], "graphics/assets/transparent_reel.png")

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
 
    if s.game.replays < 10:
        reel1.position[0] = 130
    elif s.game.replays < 100 and s.game.replays > 10:
        reel1.position[0] = 135
    else:
        reel1.position[0] = 140
    screen.blit(reel1.image, reel1.position)
    if s.game.replays > 9 and s.game.replays < 100:
        reel10.position[0] = 125
        screen.blit(reel10.image, reel10.position)
    elif s.game.replays > 100:
        reel10.position[0] = 130
        screen.blit(reel10.image, reel10.position)
    if s.game.replays > 99:
        screen.blit(reel100.image, reel100.position)
   
    screen.blit(bg_gi, (120,854), pygame.Rect(120,854,44,357))
    screen.blit(bg_gi, (120,0), pygame.Rect(120,0,44,833))

    if s.game.tilt.status == False:
        if 1 in s.game.selection:
            p = [9,270]
            screen.blit(selection, p)
        if 2 in s.game.selection:
            p = [7,407]
            screen.blit(selection, p)
        if 3 in s.game.selection:
            p = [146,550]
            screen.blit(selection2, p)
        if 4 in s.game.selection:
            p = [291,550]
            screen.blit(selection2, p)
        if 5 in s.game.selection:
            p = [436,550]
            screen.blit(selection2, p)
        if 6 in s.game.selection:
            p = [585,405]
            screen.blit(selection, p)
        if 7 in s.game.selection:
            p = [585,267]
            screen.blit(selection, p)

        p = [148,266]
        screen.blit(odds, p)
        if s.game.odds.position == 1:
            p = [505,265]
            screen.blit(odds, p)
        if s.game.odds.position == 2:
            p = [435,265]
            screen.blit(odds, p)
        if s.game.odds.position == 3:
            p = [361,265]
            screen.blit(odds, p)
        if s.game.odds.position == 4:
            p = [290,265]
            screen.blit(odds, p)
        if s.game.odds.position == 5:
            p = [218,265]
            screen.blit(odds, p)

        if s.game.pennant.status == True:
            p = [570,827]
            screen.blit(feature, p)

        if s.game.coin.position == 1:
            p = [21,567]
            screen.blit(multiplier, p)
        if s.game.coin.position == 2:
            p = [72,567]
            screen.blit(multiplier, p)
        if s.game.coin.position == 3:
            p = [602,566]
            screen.blit(multiplier, p)
        if s.game.coin.position == 4:
            p = [652,566]
            screen.blit(multiplier, p)

    if s.game.tilt.status == True:
        tilt_position = [185,919]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def selection_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if 1 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (9,270), pygame.Rect(9,270,122,127)))
    if 2 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (7,407), pygame.Rect(7,407,122,127)))
    if 3 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (146,550), pygame.Rect(146,550,136,130)))
    if 4 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (291,550), pygame.Rect(291,550,136,130)))
    if 5 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (436,550), pygame.Rect(436,550,136,130)))
    if 6 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (585,405), pygame.Rect(585,405,122,127)))
    if 7 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (585,267), pygame.Rect(585,267,122,127)))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [9,270]
            dirty_rects.append(screen.blit(selection, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [7,407]
            dirty_rects.append(screen.blit(selection, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection:
            p = [146,550]
            dirty_rects.append(screen.blit(selection2, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection:
            p = [291,550]
            dirty_rects.append(screen.blit(selection2, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection:
            p = [436,550]
            dirty_rects.append(screen.blit(selection2, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [585,405]
            dirty_rects.append(screen.blit(selection, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [585,267]
            dirty_rects.append(screen.blit(selection, p))

    pygame.display.update(dirty_rects)
    return

def star_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (505,265), pygame.Rect(505,265,64,267)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (435,265), pygame.Rect(435,265,64,267)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (361,265), pygame.Rect(361,265,64,267)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (290,265), pygame.Rect(290,265,64,267)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (218,265), pygame.Rect(218,265,64,267)))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [505,265]
            dirty_rects.append(screen.blit(odds, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [435,265]
            dirty_rects.append(screen.blit(odds, p))
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [361,265]
            dirty_rects.append(screen.blit(odds, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [290,265]
            dirty_rects.append(screen.blit(odds, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [218,265]
            dirty_rects.append(screen.blit(odds, p))

    pygame.display.update(dirty_rects)
    return

