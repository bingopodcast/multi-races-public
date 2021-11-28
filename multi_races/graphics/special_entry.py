import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

tilt = pygame.image.load('special_entry/assets/tilt.png').convert_alpha()
feature = pygame.image.load('special_entry/assets/feature.png').convert_alpha()
left = pygame.image.load('special_entry/assets/left.png').convert_alpha()
odds = pygame.image.load('special_entry/assets/odds.png').convert_alpha()
type_image = pygame.image.load('special_entry/assets/type.png').convert_alpha()
letter_e = pygame.image.load('special_entry/assets/letter_e.png').convert_alpha()
letter_n = pygame.image.load('special_entry/assets/letter_n.png').convert_alpha()
letter_t = pygame.image.load('special_entry/assets/letter_t.png').convert_alpha()
letter_r = pygame.image.load('special_entry/assets/letter_r.png').convert_alpha()
letter_y = pygame.image.load('special_entry/assets/letter_y.png').convert_alpha()
selection = pygame.image.load('special_entry/assets/selection.png').convert_alpha()
bg_menu = pygame.image.load('special_entry/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('special_entry/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('special_entry/assets/backglass_off.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert_alpha()

reel1 = scorereel([532,312], "graphics/assets/transparent_reel.png")
reel10 = scorereel([520,312], "graphics/assets/transparent_reel.png")
reel100 = scorereel([508,312], "graphics/assets/transparent_reel.png")

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
        reel1.position[0] = 532
    elif s.game.replays < 100 and s.game.replays > 10:
        reel1.position[0] = 530
    else:
        reel1.position[0] = 532
    screen.blit(reel1.image, reel1.position)
    if s.game.replays > 9 and s.game.replays < 100:
        reel10.position[0] = 518
        screen.blit(reel10.image, reel10.position)
    elif s.game.replays > 100:
        reel10.position[0] = 520
        screen.blit(reel10.image, reel10.position)
    if s.game.replays > 99:
        screen.blit(reel100.image, reel100.position)
   
    screen.blit(bg_gi, (503,334), pygame.Rect(503,334,66,357))
    screen.blit(bg_gi, (503,0), pygame.Rect(503,0,66,313))
#    screen.blit(bg_gi, (458,334), pygame.Rect(458,334,44,357))
#    screen.blit(bg_gi, (458,0), pygame.Rect(458,0,44,313))
    
    if s.game.name.position >= 1:
        p = [382,358]
        screen.blit(letter_e, p)
    if s.game.name.position >= 2:
        p = [428,356]
        screen.blit(letter_n, p)
    if s.game.name.position >= 3:
        p = [488,354]
        screen.blit(letter_t, p)
    if s.game.name.position >= 4:
        p = [540,357]
        screen.blit(letter_r, p)
    if s.game.name.position >= 5:
        p = [584,352]
        screen.blit(letter_y, p)

   

    if s.game.tilt.status == False:
        if 1 in s.game.selection:
            p = [16,746]
            screen.blit(selection, p)
        if 2 in s.game.selection:
            p = [15,866]
            screen.blit(selection, p)
        if 3 in s.game.selection:
            p = [151,867]
            screen.blit(selection, p)
        if 4 in s.game.selection:
            p = [292,870]
            screen.blit(selection, p)
        if 5 in s.game.selection:
            p = [432,868]
            screen.blit(selection, p)
        if 6 in s.game.selection:
            p = [568,867]
            screen.blit(selection, p)
        if 7 in s.game.selection:
            p = [568,744]
            screen.blit(selection, p)

        if s.game.coin.position == 1:
            p = [1,700]
            screen.blit(odds, p)
        if s.game.coin.position == 2:
            p = [2,652]
            screen.blit(odds, p)
        if s.game.coin.position == 3:
            p = [1,603]
            screen.blit(odds, p)
        if s.game.coin.position == 4:
            p = [2,550]
            screen.blit(odds, p)

        if s.game.odds.position == 1:
            p = [128,442]
            screen.blit(type_image, p)
        if s.game.odds.position == 2:
            p = [192,464]
            screen.blit(type_image, p)
        if s.game.odds.position == 3:
            p = [252,484]
            screen.blit(type_image, p)
        if s.game.odds.position == 4:
            p = [310,505]
            screen.blit(type_image, p)
        if s.game.odds.position == 5:
            p = [366,528]
            screen.blit(type_image, p)

        if s.game.pennant.status == True:
            p = [162,294]
            screen.blit(feature, p)
        if s.game.left.status == True:
            p = [56,290]
            screen.blit(left, p)
        if s.game.right.status == True:
            p = [606,286]
            screen.blit(left, p)

    if s.game.tilt.status == True:
        tilt_position = [189,754]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def selection_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.left.status == False:
        dirty_rects.append(screen.blit(bg_gi, (56,290), pygame.Rect(56,290,52,59)))
    if s.game.right.status == False:
        dirty_rects.append(screen.blit(bg_gi, (606,286), pygame.Rect(606,286,52,59)))

    if 1 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (16,746), pygame.Rect(16,746,137,125)))
    if 2 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (15,866), pygame.Rect(15,866,137,125)))
    if 3 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (151,867), pygame.Rect(151,867,137,125)))
    if 4 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (292,870), pygame.Rect(292,870,137,125)))
    if 5 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (432,868), pygame.Rect(432,868,137,125)))
    if 6 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (568,867), pygame.Rect(568,867,137,125)))
    if 7 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (568,744), pygame.Rect(568,744,137,125)))

    if num in [5,20,30,40]:
        if s.game.left.status == False:
            p = [56,290]
            dirty_rects.append(screen.blit(left, p))
    if num in [0,10,25,35,45]:
        if s.game.right.status == False:
            p = [606,286]
            dirty_rects.append(screen.blit(left, p))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [16,746]
            dirty_rects.append(screen.blit(selection, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [15,866]
            dirty_rects.append(screen.blit(selection, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection:
            p = [151,867]
            dirty_rects.append(screen.blit(selection, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection:
            p = [292,870]
            dirty_rects.append(screen.blit(selection, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection:
            p = [432,868]
            dirty_rects.append(screen.blit(selection, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [568,867]
            dirty_rects.append(screen.blit(selection, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [568,744]
            dirty_rects.append(screen.blit(selection, p))

    pygame.display.update(dirty_rects)
    return

def star_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (128,442), pygame.Rect(128,442,209,12)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (192,464), pygame.Rect(192,464,209,12)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (252,484), pygame.Rect(252,484,209,12)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (310,505), pygame.Rect(310,505,209,12)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (366,528), pygame.Rect(366,528,209,12)))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [128,442]
            dirty_rects.append(screen.blit(type_image, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [192,464]
            dirty_rects.append(screen.blit(type_image, p))
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [252,484]
            dirty_rects.append(screen.blit(type_image, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [310,505]
            dirty_rects.append(screen.blit(type_image, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [366,528]
            dirty_rects.append(screen.blit(type_image, p))

    pygame.display.update(dirty_rects)
    return

