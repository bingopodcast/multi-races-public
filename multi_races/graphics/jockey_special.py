import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

tilt = pygame.image.load('jockey_special/assets/tilt.png').convert_alpha()
feature = pygame.image.load('jockey_special/assets/feature.png').convert_alpha()
left = pygame.image.load('jockey_special/assets/left.png').convert_alpha()
right = pygame.image.load('jockey_special/assets/right.png').convert_alpha()
purse_win = pygame.image.load('jockey_special/assets/purse_win.png').convert_alpha()
show_win = pygame.image.load('jockey_special/assets/show_win.png').convert_alpha()
horseshoe = pygame.image.load('jockey_special/assets/horseshoe.png').convert_alpha()
odds = pygame.image.load('jockey_special/assets/odds.png').convert_alpha()
type_image = pygame.image.load('jockey_special/assets/type.png').convert_alpha()
letter_s = pygame.image.load('jockey_special/assets/letter_s.png').convert_alpha()
letter_p = pygame.image.load('jockey_special/assets/letter_p.png').convert_alpha()
letter_e = pygame.image.load('jockey_special/assets/letter_e.png').convert_alpha()
letter_c = pygame.image.load('jockey_special/assets/letter_c.png').convert_alpha()
letter_i = pygame.image.load('jockey_special/assets/letter_i.png').convert_alpha()
letter_a = pygame.image.load('jockey_special/assets/letter_a.png').convert_alpha()
letter_l = pygame.image.load('jockey_special/assets/letter_l.png').convert_alpha()
selection1 = pygame.image.load('jockey_special/assets/selection1.png').convert_alpha()
selection2 = pygame.image.load('jockey_special/assets/selection2.png').convert_alpha()
selection3 = pygame.image.load('jockey_special/assets/selection3.png').convert_alpha()
selection4 = pygame.image.load('jockey_special/assets/selection4.png').convert_alpha()
selection5 = pygame.image.load('jockey_special/assets/selection5.png').convert_alpha()
selection6 = pygame.image.load('jockey_special/assets/selection6.png').convert_alpha()
selection7 = pygame.image.load('jockey_special/assets/selection7.png').convert_alpha()
bg_menu = pygame.image.load('jockey_special/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('jockey_special/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('jockey_special/assets/backglass_off.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert_alpha()

reel1 = scorereel([511,444], "graphics/assets/transparent_reel.png")
reel10 = scorereel([501,444], "graphics/assets/transparent_reel.png")
reel100 = scorereel([491,444], "graphics/assets/transparent_reel.png")

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
   
    screen.blit(bg_gi, (491,470), pygame.Rect(491,470,66,500))
    screen.blit(bg_gi, (491,0), pygame.Rect(491,0,66,440))
#    screen.blit(bg_gi, (458,334), pygame.Rect(458,334,44,357))
#    screen.blit(bg_gi, (458,0), pygame.Rect(458,0,44,313))
    
    if s.game.name.position >= 1:
        p = [351,288]
        screen.blit(letter_s, p)
    if s.game.name.position >= 2:
        p = [408,289]
        screen.blit(letter_p, p)
    if s.game.name.position >= 3:
        p = [458,303]
        screen.blit(letter_e, p)
    if s.game.name.position >= 4:
        p = [512,321]
        screen.blit(letter_c, p)
    if s.game.name.position >= 5:
        p = [558,338]
        screen.blit(letter_i, p)
    if s.game.name.position >= 6:
        p = [587,358]
        screen.blit(letter_a, p)
    if s.game.name.position >= 7:
        p = [634,385]
        screen.blit(letter_l, p)

   

    if s.game.tilt.status == False:
        if 1 in s.game.selection:
            p = [10,750]
            screen.blit(selection1, p)
        if 2 in s.game.selection:
            p = [23,893]
            screen.blit(selection2, p)
        if 3 in s.game.selection:
            p = [164,898]
            screen.blit(selection3, p)
        if 4 in s.game.selection:
            p = [314,889]
            screen.blit(selection4, p)
        if 5 in s.game.selection:
            p = [414,898]
            screen.blit(selection5, p)
        if 6 in s.game.selection:
            p = [563,903]
            screen.blit(selection6, p)
        if 7 in s.game.selection:
            p = [618,756]
            screen.blit(selection7, p)

        if s.game.coin.position == 1:
            p = [6,689]
            screen.blit(odds, p)
        if s.game.coin.position == 2:
            p = [7,635]
            screen.blit(odds, p)
        if s.game.coin.position == 3:
            p = [6,582]
            screen.blit(odds, p)
        if s.game.coin.position == 4:
            p = [6,528]
            screen.blit(odds, p)

        if s.game.odds.position == 1:
            p = [120,772]
            screen.blit(type_image, p)
        if s.game.odds.position == 2:
            p = [189,802]
            screen.blit(type_image, p)
        if s.game.odds.position == 3:
            p = [249,832]
            screen.blit(type_image, p)
        if s.game.odds.position == 4:
            p = [317,862]
            screen.blit(type_image, p)
        if s.game.odds.position == 5:
            p = [375,882]
            screen.blit(type_image, p)

        if s.game.horseshoe.status == True:
            p = [332,348]
            screen.blit(horseshoe, p)

        if s.game.pennant.status == True:
            p = [606,249]
            screen.blit(feature, p)
        if s.game.left.status == True:
            p = [12,457]
            screen.blit(left, p)
        if s.game.right.status == True:
            p = [621,463]
            screen.blit(right, p)
        if s.game.purse_win.status == True:
            p = [259,418]
            screen.blit(purse_win, p)
        if s.game.show_win.status == True:
            p = [263,450]
            screen.blit(show_win, p)


    if s.game.tilt.status == True:
        tilt_position = [182,443]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def selection_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.left.status == False:
        dirty_rects.append(screen.blit(bg_gi, (12,457), pygame.Rect(12,457,98,70)))
    if s.game.right.status == False:
        dirty_rects.append(screen.blit(bg_gi, (621,463), pygame.Rect(621,463,102,61)))

    if 1 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (10,750), pygame.Rect(10,750,103,149)))
    if 2 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (23,893), pygame.Rect(23,893,145,141)))
    if 3 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (164,898), pygame.Rect(164,898,145,136)))
    if 4 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (314,889), pygame.Rect(314,889,112,149)))
    if 5 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (414,898), pygame.Rect(414,898,148,138)))
    if 6 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (563,903), pygame.Rect(563,903,142,145)))
    if 7 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (618,756), pygame.Rect(618,756,98,151)))

    if num in [5,20,30,40]:
        if s.game.left.status == False:
            p = [12,457]
            dirty_rects.append(screen.blit(left, p))
    if num in [0,10,25,35,45]:
        if s.game.right.status == False:
            p = [621,463]
            dirty_rects.append(screen.blit(right, p))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [10,750]
            dirty_rects.append(screen.blit(selection1, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [23,893]
            dirty_rects.append(screen.blit(selection2, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection:
            p = [164,898]
            dirty_rects.append(screen.blit(selection3, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection:
            p = [314,889]
            dirty_rects.append(screen.blit(selection4, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection:
            p = [414,898]
            dirty_rects.append(screen.blit(selection5, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [563,903]
            dirty_rects.append(screen.blit(selection6, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [618,756]
            dirty_rects.append(screen.blit(selection7, p))

    pygame.display.update(dirty_rects)
    return

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
        dirty_rects.append(screen.blit(bg_gi, (259,418), pygame.Rect(259,418,210,20)))
    if s.game.show_win.status == False:
        dirty_rects.append(screen.blit(bg_gi, (263,450), pygame.Rect(263,450,207,21)))

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (120,772), pygame.Rect(120,772,209,12)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (189,802), pygame.Rect(189,802,209,12)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (249,832), pygame.Rect(249,832,209,12)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (317,862), pygame.Rect(317,862,209,12)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (375,882), pygame.Rect(375,882,209,12)))

    if num in [8,10,16,18,20,22,28,35,37,40,42,46,49]:
        if s.game.purse_win.status == False:
            p = [259,418]
            dirty_rects.append(screen.blit(purse_win, p))
    if num in [2,4,17,25,32,36,41,44,48]:
        if s.game.show_win.status == False:
            p = [263,450]
            dirty_rects.append(screen.blit(show_win, p))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [120,772]
            dirty_rects.append(screen.blit(type_image, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [189,802]
            dirty_rects.append(screen.blit(type_image, p))
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [249,832]
            dirty_rects.append(screen.blit(type_image, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [317,862]
            dirty_rects.append(screen.blit(type_image, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [375,882]
            dirty_rects.append(screen.blit(type_image, p))

    pygame.display.update(dirty_rects)
    return

