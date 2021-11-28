import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

tilt = pygame.image.load('derby_41/assets/tilt.png').convert_alpha()
feature = pygame.image.load('derby_41/assets/feature.png').convert_alpha()
horseshoe = pygame.image.load('derby_41/assets/horseshoe.png').convert_alpha()
letter_d = pygame.image.load('derby_41/assets/letter_d.png').convert_alpha()
letter_e = pygame.image.load('derby_41/assets/letter_e.png').convert_alpha()
letter_r = pygame.image.load('derby_41/assets/letter_r.png').convert_alpha()
letter_b = pygame.image.load('derby_41/assets/letter_b.png').convert_alpha()
letter_y = pygame.image.load('derby_41/assets/letter_y.png').convert_alpha()
multiplier = pygame.image.load('derby_41/assets/multiplier.png').convert_alpha()
odds = pygame.image.load('derby_41/assets/odds.png').convert_alpha()
section = pygame.image.load('derby_41/assets/section.png').convert_alpha()
selection = pygame.image.load('derby_41/assets/selection.png').convert_alpha()
bg_menu = pygame.image.load('derby_41/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('derby_41/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('derby_41/assets/backglass_off.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert_alpha()

reel1 = scorereel([160,446], "graphics/assets/transparent_reel.png")
reel10 = scorereel([150,446], "graphics/assets/transparent_reel.png")
reel100 = scorereel([140,446], "graphics/assets/transparent_reel.png")

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
        reel1.position[0] = 150
    elif s.game.replays < 100 and s.game.replays > 10:
        reel1.position[0] = 155
    else:
        reel1.position[0] = 160
    screen.blit(reel1.image, reel1.position)
    if s.game.replays > 9 and s.game.replays < 100:
        reel10.position[0] = 140
        screen.blit(reel10.image, reel10.position)
    elif s.game.replays > 100:
        reel10.position[0] = 150
        screen.blit(reel10.image, reel10.position)
    if s.game.replays > 99:
        screen.blit(reel100.image, reel100.position)

    screen.blit(bg_gi, (140,468), pygame.Rect(140,468,44,357))
    screen.blit(bg_gi, (140,0), pygame.Rect(140,0,64,450))

    if s.game.name.position >= 1:
        p = [389,327]
        screen.blit(letter_d, p)
    if s.game.name.position >= 2:
        p = [444,327]
        screen.blit(letter_e, p)
    if s.game.name.position >= 3:
        p = [488,327]
        screen.blit(letter_r, p)
    if s.game.name.position >= 4:
        p = [540,327]
        screen.blit(letter_b, p)
    if s.game.name.position >= 5:
        p = [582,327]
        screen.blit(letter_y, p)

   

    if s.game.tilt.status == False:
        if 1 in s.game.selection:
            p = [7,468]
            screen.blit(selection, p)
        if 2 in s.game.selection:
            p = [7,633]
            screen.blit(selection, p)
        if 3 in s.game.selection:
            p = [6,788]
            screen.blit(selection, p)
        if 4 in s.game.selection:
            p = [146,788]
            screen.blit(selection, p)
        if 5 in s.game.selection:
            p = [287,788]
            screen.blit(selection, p)
        if 6 in s.game.selection:
            p = [428,788]
            screen.blit(selection, p)
        if 7 in s.game.selection:
            p = [569,788]
            screen.blit(selection, p)

        p = [250,389]
        screen.blit(section, p)
        p = [252,444]
        screen.blit(section, p)
        p = [249,499]
        screen.blit(section, p)
        p = [250,556]
        screen.blit(section, p)
        if s.game.odds.position == 1:
            p = [642,388]
            screen.blit(odds, p)
            p = [642,443]
            screen.blit(odds, p)
            p = [642,500]
            screen.blit(odds, p)
            p = [642,558]
            screen.blit(odds, p)
        if s.game.odds.position == 2:
            p = [570,388]
            screen.blit(odds, p)
            p = [570,443]
            screen.blit(odds, p)
            p = [570,500]
            screen.blit(odds, p)
            p = [570,558]
            screen.blit(odds, p)
        if s.game.odds.position == 3:
            p = [499,388]
            screen.blit(odds, p)
            p = [499,443]
            screen.blit(odds, p)
            p = [499,500]
            screen.blit(odds, p)
            p = [499,558]
            screen.blit(odds, p)
        if s.game.odds.position == 4:
            p = [427,388]
            screen.blit(odds, p)
            p = [427,443]
            screen.blit(odds, p)
            p = [427,500]
            screen.blit(odds, p)
            p = [427,558]
            screen.blit(odds, p)
        if s.game.odds.position == 5:
            p = [360,388]
            screen.blit(odds, p)
            p = [360,443]
            screen.blit(odds, p)
            p = [360,500]
            screen.blit(odds, p)
            p = [360,558]
            screen.blit(odds, p)

        if s.game.pennant.status == True:
            p = [25,413]
            screen.blit(feature, p)
        if s.game.left.status == True:
            p = [178,331]
            screen.blit(horseshoe, p)
        if s.game.right.status == True:
            p = [649,330]
            screen.blit(horseshoe, p)

        if s.game.coin.position == 1:
            p = [9,368]
            screen.blit(multiplier, p)
        if s.game.coin.position == 2:
            p = [43,332]
            screen.blit(multiplier, p)
        if s.game.coin.position == 3:
            p = [85,332]
            screen.blit(multiplier, p)
        if s.game.coin.position == 4:
            p = [119,366]
            screen.blit(multiplier, p)

    if s.game.tilt.status == True:
        tilt_position = [664,617]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def selection_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.left.status == False:
        dirty_rects.append(screen.blit(bg_gi, (178,331), pygame.Rect(178,331,64,55)))
    if s.game.right.status == False:
        dirty_rects.append(screen.blit(bg_gi, (649,330), pygame.Rect(649,330,64,55)))

    if 1 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (7,468), pygame.Rect(7,468,144,164)))
    if 2 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (7,633), pygame.Rect(7,633,144,164)))
    if 3 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (6,788), pygame.Rect(6,788,144,164)))
    if 4 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (146,788), pygame.Rect(146,788,144,164)))
    if 5 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (287,788), pygame.Rect(287,788,144,164)))
    if 6 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (428,788), pygame.Rect(428,788,144,164)))
    if 7 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (569,788), pygame.Rect(569,788,144,164)))

    if num in [5,20,30,40]:
        if s.game.left.status == False:
            p = [178,331]
            dirty_rects.append(screen.blit(horseshoe, p))
    if num in [0,10,25,35,45]:
        if s.game.right.status == False:
            p = [649,330]
            dirty_rects.append(screen.blit(horseshoe, p))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [7,468]
            dirty_rects.append(screen.blit(selection, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [7,633]
            dirty_rects.append(screen.blit(selection, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection:
            p = [6,788]
            dirty_rects.append(screen.blit(selection, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection:
            p = [146,788]
            dirty_rects.append(screen.blit(selection, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection:
            p = [287,788]
            dirty_rects.append(screen.blit(selection, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [428,788]
            dirty_rects.append(screen.blit(selection, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [569,788]
            dirty_rects.append(screen.blit(selection, p))

    pygame.display.update(dirty_rects)
    return

def star_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (642,388), pygame.Rect(642,388,66,52)))
        dirty_rects.append(screen.blit(bg_gi, (642,443), pygame.Rect(642,443,66,52)))
        dirty_rects.append(screen.blit(bg_gi, (642,500), pygame.Rect(642,500,66,52)))
        dirty_rects.append(screen.blit(bg_gi, (642,558), pygame.Rect(642,558,66,52)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (570,388), pygame.Rect(570,388,66,52)))
        dirty_rects.append(screen.blit(bg_gi, (570,443), pygame.Rect(570,443,66,52)))
        dirty_rects.append(screen.blit(bg_gi, (570,500), pygame.Rect(570,500,66,52)))
        dirty_rects.append(screen.blit(bg_gi, (570,558), pygame.Rect(570,558,66,52)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (499,388), pygame.Rect(499,388,66,52)))
        dirty_rects.append(screen.blit(bg_gi, (499,443), pygame.Rect(499,443,66,52)))
        dirty_rects.append(screen.blit(bg_gi, (499,500), pygame.Rect(499,500,66,52)))
        dirty_rects.append(screen.blit(bg_gi, (499,558), pygame.Rect(499,558,66,52)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (427,388), pygame.Rect(427,388,66,52)))
        dirty_rects.append(screen.blit(bg_gi, (427,443), pygame.Rect(427,443,66,52)))
        dirty_rects.append(screen.blit(bg_gi, (427,500), pygame.Rect(427,500,66,52)))
        dirty_rects.append(screen.blit(bg_gi, (427,558), pygame.Rect(427,558,66,52)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (360,388), pygame.Rect(360,388,66,52)))
        dirty_rects.append(screen.blit(bg_gi, (360,443), pygame.Rect(360,443,66,52)))
        dirty_rects.append(screen.blit(bg_gi, (360,500), pygame.Rect(360,500,66,52)))
        dirty_rects.append(screen.blit(bg_gi, (360,558), pygame.Rect(360,558,66,52)))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [642,388]
            dirty_rects.append(screen.blit(odds, p))
            p = [642,443]
            dirty_rects.append(screen.blit(odds, p))
            p = [642,500]
            dirty_rects.append(screen.blit(odds, p))
            p = [642,558]
            dirty_rects.append(screen.blit(odds, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [570,388]
            dirty_rects.append(screen.blit(odds, p))
            p = [570,443]
            dirty_rects.append(screen.blit(odds, p))
            p = [570,500]
            dirty_rects.append(screen.blit(odds, p))
            p = [570,558]
            dirty_rects.append(screen.blit(odds, p))
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [499,388]
            dirty_rects.append(screen.blit(odds, p))
            p = [499,443]
            dirty_rects.append(screen.blit(odds, p))
            p = [499,500]
            dirty_rects.append(screen.blit(odds, p))
            p = [499,558]
            dirty_rects.append(screen.blit(odds, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [427,388]
            dirty_rects.append(screen.blit(odds, p))
            p = [427,443]
            dirty_rects.append(screen.blit(odds, p))
            p = [427,500]
            dirty_rects.append(screen.blit(odds, p))
            p = [427,558]
            dirty_rects.append(screen.blit(odds, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [360,388]
            dirty_rects.append(screen.blit(odds, p))
            p = [360,443]
            dirty_rects.append(screen.blit(odds, p))
            p = [360,500]
            dirty_rects.append(screen.blit(odds, p))
            p = [360,558]
            dirty_rects.append(screen.blit(odds, p))

    pygame.display.update(dirty_rects)
    return

