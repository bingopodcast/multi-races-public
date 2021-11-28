import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

type_image = pygame.image.load('gold_cup/assets/type.png').convert_alpha()
trophy = pygame.image.load('gold_cup/assets/trophy.png').convert_alpha()
tilt = pygame.image.load('gold_cup/assets/tilt.png').convert_alpha()
show_win = pygame.image.load('gold_cup/assets/show_win.png').convert_alpha()
selection = pygame.image.load('gold_cup/assets/selection.png').convert_alpha()
purse_win = pygame.image.load('gold_cup/assets/purse_win.png').convert_alpha()
odds = pygame.image.load('gold_cup/assets/odds.png').convert_alpha()
feature = pygame.image.load('gold_cup/assets/feature.png').convert_alpha()
horseshoe = pygame.image.load('gold_cup/assets/horseshoe.png').convert_alpha()
letter_g = pygame.image.load('gold_cup/assets/letter_g.png').convert_alpha()
letter_o = pygame.image.load('gold_cup/assets/letter_o.png').convert_alpha()
letter_l = pygame.image.load('gold_cup/assets/letter_l.png').convert_alpha()
letter_d = pygame.image.load('gold_cup/assets/letter_d.png').convert_alpha()
letter_c = pygame.image.load('gold_cup/assets/letter_c.png').convert_alpha()
letter_u = pygame.image.load('gold_cup/assets/letter_u.png').convert_alpha()
letter_p = pygame.image.load('gold_cup/assets/letter_p.png').convert_alpha()
bg_menu = pygame.image.load('gold_cup/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('gold_cup/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('gold_cup/assets/backglass_off.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert_alpha()

reel1 = scorereel([511,500], "graphics/assets/transparent_reel.png")
reel10 = scorereel([501,500], "graphics/assets/transparent_reel.png")
reel100 = scorereel([491,500], "graphics/assets/transparent_reel.png")

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
        reel1.position[0] = 501
    elif s.game.replays < 100 and s.game.replays > 10:
        reel1.position[0] = 506
    else:
        reel1.position[0] = 511
    screen.blit(reel1.image, reel1.position)
    if s.game.replays > 9 and s.game.replays < 100:
        reel10.position[0] = 495
        screen.blit(reel10.image, reel10.position)
    elif s.game.replays > 100:
        reel10.position[0] = 501
        screen.blit(reel10.image, reel10.position)
    if s.game.replays > 99:
        screen.blit(reel100.image, reel100.position)
   
    screen.blit(bg_gi, (491,535), pygame.Rect(491,535,66,500))
    screen.blit(bg_gi, (491,0), pygame.Rect(491,0,66,490))
#    screen.blit(bg_gi, (458,334), pygame.Rect(458,334,44,357))
#    screen.blit(bg_gi, (458,0), pygame.Rect(458,0,44,313))
   

    p = [106,259]
    screen.blit(letter_g, p)
    p = [172,254]
    screen.blit(letter_o, p)
    if s.game.name.position >= 1:
        p = [233,241]
        screen.blit(letter_l, p)
    if s.game.name.position >= 2:
        p = [299,237]
        screen.blit(letter_d, p)
    if s.game.name.position >= 3:
        p = [431,242]
        screen.blit(letter_c, p)
    if s.game.name.position >= 4:
        p = [499,244]
        screen.blit(letter_u, p)
    if s.game.name.position >= 5:
        p = [562,254]
        screen.blit(letter_p, p)

    if s.game.tilt.status == False:
        if 1 in s.game.selection:
            p = [16,485]
            screen.blit(selection, p)
        if 2 in s.game.selection:
            p = [50,343]
            screen.blit(selection, p)
        if 3 in s.game.selection:
            p = [176,318]
            screen.blit(selection, p)
        if 4 in s.game.selection:
            p = [301,322]
            screen.blit(selection, p)
        if 5 in s.game.selection:
            p = [425,319]
            screen.blit(selection, p)
        if 6 in s.game.selection:
            p = [547,339]
            screen.blit(selection, p)
        if 7 in s.game.selection:
            p = [586,480]
            screen.blit(selection, p)

        if s.game.coin.position == 1:
            p = [112,848]
            screen.blit(odds, p)
        if s.game.coin.position == 2:
            p = [112,782]
            screen.blit(odds, p)
        if s.game.coin.position == 3:
            p = [111,717]
            screen.blit(odds, p)
        if s.game.coin.position == 4:
            p = [113,650]
            screen.blit(odds, p)

        if s.game.odds.position == 1:
            p = [121,936]
            screen.blit(type_image, p)
        if s.game.odds.position == 2:
            p = [182,962]
            screen.blit(type_image, p)
        if s.game.odds.position == 3:
            p = [247,988]
            screen.blit(type_image, p)
        if s.game.odds.position == 4:
            p = [313,1015]
            screen.blit(type_image, p)
        if s.game.odds.position == 5:
            p = [378,1051]
            screen.blit(type_image, p)

        if s.game.horseshoe.status == True:
            p = [335,474]
            screen.blit(horseshoe, p)

        if s.game.pennant.status == True:
            p = [176,507]
            screen.blit(feature, p)
        if s.game.left.status == True:
            p = [153,559]
            screen.blit(trophy, p)
        if s.game.right.status == True:
            p = [508,557]
            screen.blit(trophy, p)
        if s.game.purse_win.status == True:
            p = [248,573]
            screen.blit(purse_win, p)
        if s.game.show_win.status == True:
            p = [258,611]
            screen.blit(show_win, p)


    if s.game.tilt.status == True:
        tilt_position = [645,220]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def selection_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.left.status == False:
        dirty_rects.append(screen.blit(bg_gi, (153,559), pygame.Rect(153,559,63,83)))
    if s.game.right.status == False:
        dirty_rects.append(screen.blit(bg_gi, (508,557), pygame.Rect(508,557,63,83)))

    if 1 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (16,485), pygame.Rect(16,485,132,146)))
    if 2 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (50,343), pygame.Rect(50,343,132,146)))
    if 3 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (176,318), pygame.Rect(176,318,132,146)))
    if 4 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (301,322), pygame.Rect(301,322,132,146)))
    if 5 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (425,319), pygame.Rect(425,319,132,146)))
    if 6 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (547,339), pygame.Rect(547,339,132,146)))
    if 7 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (586,480), pygame.Rect(586,480,132,146)))

    if num in [5,20,30,40]:
        if s.game.left.status == False:
            p = [153,559]
            dirty_rects.append(screen.blit(trophy, p))
    if num in [0,10,25,35,45]:
        if s.game.right.status == False:
            p = [508,557]
            dirty_rects.append(screen.blit(trophy, p))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [16,485]
            dirty_rects.append(screen.blit(selection, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [50,343]
            dirty_rects.append(screen.blit(selection, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection:
            p = [176,318]
            dirty_rects.append(screen.blit(selection, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection:
            p = [301,322]
            dirty_rects.append(screen.blit(selection, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection:
            p = [425,319]
            dirty_rects.append(screen.blit(selection, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [547,339]
            dirty_rects.append(screen.blit(selection, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [586,480]
            dirty_rects.append(screen.blit(selection, p))

    pygame.display.update(dirty_rects)

def clover_animation(args):
    return

def feature_animation(args):
    return

def star_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]
    
    if s.game.purse_win.status == False:
        dirty_rects.append(screen.blit(bg_gi, (248,573), pygame.Rect(248,573,216,22)))
    if s.game.show_win.status == False:
        dirty_rects.append(screen.blit(bg_gi, (258,611), pygame.Rect(258,611,202,22)))

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (121,936), pygame.Rect(121,936,209,12)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (182,962), pygame.Rect(182,962,209,12)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (247,988), pygame.Rect(247,988,209,12)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (313,1015), pygame.Rect(313,1015,209,12)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (378,1051), pygame.Rect(378,1051,209,12)))

    if num in [8,10,16,18,20,22,28,35,37,40,42,46,49]:
        if s.game.purse_win.status == False:
            p = [248,573]
            dirty_rects.append(screen.blit(purse_win, p))
    if num in [2,4,17,25,32,36,41,44,48]:
        if s.game.show_win.status == False:
            p = [258,611]
            dirty_rects.append(screen.blit(show_win, p))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [121,936]
            dirty_rects.append(screen.blit(type_image, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [182,962]
            dirty_rects.append(screen.blit(type_image, p))
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [247,988]
            dirty_rects.append(screen.blit(type_image, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [313,1015]
            dirty_rects.append(screen.blit(type_image, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [378,1051]
            dirty_rects.append(screen.blit(type_image, p))

    pygame.display.update(dirty_rects)
    return

