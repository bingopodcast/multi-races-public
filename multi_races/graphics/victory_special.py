import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

tilt = pygame.image.load('victory_special/assets/tilt.png').convert_alpha()
dd = pygame.image.load('victory_special/assets/dd.png').convert_alpha()
dd_middle = pygame.image.load('victory_special/assets/dd_middle.png').convert_alpha()
feature = pygame.image.load('victory_special/assets/feature.png').convert_alpha()
flag_left = pygame.image.load('victory_special/assets/flag_left.png').convert_alpha()
flag_right = pygame.image.load('victory_special/assets/flag_right.png').convert_alpha()
horse1 = pygame.image.load('victory_special/assets/horse1.png').convert_alpha()
horse2 = pygame.image.load('victory_special/assets/horse2.png').convert_alpha()
horse3 = pygame.image.load('victory_special/assets/horse3.png').convert_alpha()
horse4 = pygame.image.load('victory_special/assets/horse4.png').convert_alpha()
horse5 = pygame.image.load('victory_special/assets/horse5.png').convert_alpha()
horse6 = pygame.image.load('victory_special/assets/horse6.png').convert_alpha()
horse7 = pygame.image.load('victory_special/assets/horse7.png').convert_alpha()
letter_e = pygame.image.load('victory_special/assets/letter_e.png').convert_alpha()
letter_c = pygame.image.load('victory_special/assets/letter_c.png').convert_alpha()
letter_i = pygame.image.load('victory_special/assets/letter_i.png').convert_alpha()
letter_a = pygame.image.load('victory_special/assets/letter_a.png').convert_alpha()
letter_l = pygame.image.load('victory_special/assets/letter_l.png').convert_alpha()
multiplier_1 = pygame.image.load('victory_special/assets/multiplier_1.png').convert_alpha()
multiplier_2 = pygame.image.load('victory_special/assets/multiplier_2.png').convert_alpha()
multiplier_3 = pygame.image.load('victory_special/assets/multiplier_3.png').convert_alpha()
multiplier_4 = pygame.image.load('victory_special/assets/multiplier_4.png').convert_alpha()
odds = pygame.image.load('victory_special/assets/odds.png').convert_alpha()
section = pygame.image.load('victory_special/assets/section.png').convert_alpha()
selection1 = pygame.image.load('victory_special/assets/selection1.png').convert_alpha()
selection4 = pygame.image.load('victory_special/assets/selection4.png').convert_alpha()
selection7 = pygame.image.load('victory_special/assets/selection7.png').convert_alpha()
dd_win1 = pygame.image.load('victory_special/assets/dd_win1.png').convert_alpha()
dd_win2 = pygame.image.load('victory_special/assets/dd_win2.png').convert_alpha()
bg_menu = pygame.image.load('victory_special/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('victory_special/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('victory_special/assets/backglass_off.png').convert_alpha()


class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert_alpha()

reel1 = scorereel([482,312], "graphics/assets/transparent_reel.png")
reel10 = scorereel([470,312], "graphics/assets/transparent_reel.png")
reel100 = scorereel([458,312], "graphics/assets/transparent_reel.png")

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
        reel1.position[0] = 470
    elif s.game.replays < 100 and s.game.replays > 10:
        reel1.position[0] = 475
    else:
        reel1.position[0] = 482
    screen.blit(reel1.image, reel1.position)
    if s.game.replays > 9 and s.game.replays < 100:
        reel10.position[0] = 458
        screen.blit(reel10.image, reel10.position)
    elif s.game.replays > 100:
        reel10.position[0] = 470
        screen.blit(reel10.image, reel10.position)
    if s.game.replays > 99:
        screen.blit(reel100.image, reel100.position)
   
    screen.blit(bg_gi, (458,334), pygame.Rect(458,334,44,357))
    screen.blit(bg_gi, (458,0), pygame.Rect(458,0,44,313))
    
    if s.game.name.position >= 1:
        p = [414,375]
        screen.blit(letter_e, p)
    if s.game.name.position >= 2:
        p = [468,382]
        screen.blit(letter_c, p)
    if s.game.name.position >= 3:
        p = [528,394]
        screen.blit(letter_i, p)
    if s.game.name.position >= 4:
        p = [557,407]
        screen.blit(letter_a, p)
    if s.game.name.position >= 5:
        p = [621,424]
        screen.blit(letter_l, p)

   

    if s.game.tilt.status == False:
        if 1 in s.game.selection:
            p = [23,555]
            screen.blit(selection1, p)
        if 2 in s.game.selection:
            p = [123,530]
            screen.blit(selection1, p)
        if 3 in s.game.selection:
            p = [218,510]
            screen.blit(selection1, p)
        if 4 in s.game.selection:
            p = [317,484]
            screen.blit(selection4, p)
        if 5 in s.game.selection:
            p = [413,508]
            screen.blit(selection7, p)
        if 6 in s.game.selection:
            p = [508,530]
            screen.blit(selection7, p)
        if 7 in s.game.selection:
            p = [604,556]
            screen.blit(selection7, p)

        p = [84,781]
        screen.blit(section, p)
        p = [79,842]
        screen.blit(section, p)
        p = [79,902]
        screen.blit(section, p)
        p = [79,964]
        screen.blit(section, p)
        if s.game.odds.position == 1:
            p = [556,783]
            screen.blit(odds, p)
            p = [554,844]
            screen.blit(odds, p)
            p = [556,905]
            screen.blit(odds, p)
            p = [556,966]
            screen.blit(odds, p)
        if s.game.odds.position == 2:
            p = [466,782]
            screen.blit(odds, p)
            p = [466,844]
            screen.blit(odds, p)
            p = [466,904]
            screen.blit(odds, p)
            p = [466,966]
            screen.blit(odds, p)
        if s.game.odds.position == 3:
            p = [376,782]
            screen.blit(odds, p)
            p = [377,843]
            screen.blit(odds, p)
            p = [378,904]
            screen.blit(odds, p)
            p = [378,965]
            screen.blit(odds, p)
        if s.game.odds.position == 4:
            p = [289,780]
            screen.blit(odds, p)
            p = [289,842]
            screen.blit(odds, p)
            p = [290,904]
            screen.blit(odds, p)
            p = [290,964]
            screen.blit(odds, p)
        if s.game.odds.position == 5:
            p = [200,780]
            screen.blit(odds, p)
            p = [200,842]
            screen.blit(odds, p)
            p = [200,902]
            screen.blit(odds, p)
            p = [201,964]
            screen.blit(odds, p)

        if s.game.pennant.status == True:
            p = [450,271]
            screen.blit(feature, p)
        if s.game.left.status == True:
            p = [4,383]
            screen.blit(flag_left, p)
        if s.game.right.status == True:
            p = [654,368]
            screen.blit(flag_right, p)

        if s.game.coin.position == 1:
            p = [294,738]
            screen.blit(multiplier_1, p)
        if s.game.coin.position == 2:
            p = [324,722]
            screen.blit(multiplier_2, p)
        if s.game.coin.position == 3:
            p = [366,718]
            screen.blit(multiplier_3, p)
        if s.game.coin.position == 4:
            p = [399,735]
            screen.blit(multiplier_4, p)

        if s.game.dd1 == 1 or s.game.dd2 == 1:
            p = [81,684]
            screen.blit(dd, p)
        if s.game.dd1 == 2 or s.game.dd2 == 2:
            p = [179,662]
            screen.blit(dd, p)
        if s.game.dd1 == 3 or s.game.dd2 == 3:
            p = [273,638]
            screen.blit(dd, p)
        if s.game.dd1 == 4 or s.game.dd2 == 4:
            p = [323,600]
            screen.blit(dd_middle, p)
        if s.game.dd1 == 5 or s.game.dd2 == 5:
            p = [418,639]
            screen.blit(dd, p)
        if s.game.dd1 == 6 or s.game.dd2 == 6:
            p = [516,662]
            screen.blit(dd, p)
        if s.game.dd1 == 7 or s.game.dd2 == 7:
            p = [610,684]
            screen.blit(dd, p)

            
        if s.game.horse1.status == True:
            p = [26,684]
            screen.blit(horse1, p)
        if s.game.horse2.status == True:
            p = [122,661]
            screen.blit(horse2, p)
        if s.game.horse3.status == True:
            p = [220,635]
            screen.blit(horse3, p)
        if s.game.horse4.status == True:
            p = [346,604]
            screen.blit(horse4, p)
        if s.game.horse5.status == True:
            p = [438,640]
            screen.blit(horse5, p)
        if s.game.horse6.status == True:
            p = [528,664]
            screen.blit(horse6, p)
        if s.game.horse7.status == True:
            p = [625,692]
            screen.blit(horse7, p)

        if s.game.daily_double_win1.status == True:
            p = [172,696]
            screen.blit(dd_win1, p)
        if s.game.daily_double_win2.status == True:
            p = [402,698]
            screen.blit(dd_win2, p)

    if s.game.tilt.status == True:
        tilt_position = [582,302]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def selection_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]
    
    if s.game.left.status == False:
        dirty_rects.append(screen.blit(bg_gi, (4,383), pygame.Rect(4,383,81,44)))
    if s.game.right.status == False:
        dirty_rects.append(screen.blit(bg_gi, (654,368), pygame.Rect(654,368,67,43)))

    if 1 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (23,555), pygame.Rect(23,555,98,124)))
    if 2 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (123,530), pygame.Rect(123,530,98,124)))
    if 3 not in s.game.selection or s.game.hold3.status == False:
        dirty_rects.append(screen.blit(bg_gi, (218,510), pygame.Rect(218,510,98,124)))
    if 4 not in s.game.selection or s.game.hold4.status == False:
        dirty_rects.append(screen.blit(bg_gi, (317,484), pygame.Rect(317,484,95,112)))
    if 5 not in s.game.selection or s.game.hold5.status == False:
        dirty_rects.append(screen.blit(bg_gi, (413,508), pygame.Rect(413,508,99,125)))
    if 6 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (508,530), pygame.Rect(508,530,99,125)))
    if 7 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (604,556), pygame.Rect(604,556,99,125)))

    if num in [5,20,30,40]:
        if s.game.left.status == False:
            p = [4,383]
            dirty_rects.append(screen.blit(flag_left, p))
    if num in [0,10,25,35,45]:
        if s.game.right.status == False:
            p = [654,368]
            dirty_rects.append(screen.blit(flag_right, p))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [23,555]
            dirty_rects.append(screen.blit(selection1, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [123,530]
            dirty_rects.append(screen.blit(selection1, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection:
            p = [218,510]
            dirty_rects.append(screen.blit(selection1, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection:
            p = [317,484]
            dirty_rects.append(screen.blit(selection4, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection:
            p = [413,508]
            dirty_rects.append(screen.blit(selection7, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [508,530]
            dirty_rects.append(screen.blit(selection7, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [604,556]
            dirty_rects.append(screen.blit(selection7, p))

    pygame.display.update(dirty_rects)
    return

def star_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]
    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (556,783), pygame.Rect(556,783,88,62)))
        dirty_rects.append(screen.blit(bg_gi, (554,844), pygame.Rect(554,844,88,62)))
        dirty_rects.append(screen.blit(bg_gi, (556,905), pygame.Rect(556,905,88,62)))
        dirty_rects.append(screen.blit(bg_gi, (556,966), pygame.Rect(556,966,88,62)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (466,782), pygame.Rect(466,782,88,62)))
        dirty_rects.append(screen.blit(bg_gi, (466,844), pygame.Rect(466,844,88,62)))
        dirty_rects.append(screen.blit(bg_gi, (466,904), pygame.Rect(466,904,88,62)))
        dirty_rects.append(screen.blit(bg_gi, (466,966), pygame.Rect(466,966,88,62)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (376,782), pygame.Rect(376,782,88,62)))
        dirty_rects.append(screen.blit(bg_gi, (377,843), pygame.Rect(377,843,88,62)))
        dirty_rects.append(screen.blit(bg_gi, (378,904), pygame.Rect(378,904,88,62)))
        dirty_rects.append(screen.blit(bg_gi, (378,965), pygame.Rect(378,965,88,62)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (289,780), pygame.Rect(289,780,88,62)))
        dirty_rects.append(screen.blit(bg_gi, (289,842), pygame.Rect(289,842,88,62)))
        dirty_rects.append(screen.blit(bg_gi, (290,904), pygame.Rect(290,904,88,62)))
        dirty_rects.append(screen.blit(bg_gi, (290,964), pygame.Rect(290,964,88,62)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (200,780), pygame.Rect(200,780,88,62)))
        dirty_rects.append(screen.blit(bg_gi, (200,842), pygame.Rect(200,842,88,62)))
        dirty_rects.append(screen.blit(bg_gi, (200,902), pygame.Rect(200,902,88,62)))
        dirty_rects.append(screen.blit(bg_gi, (201,964), pygame.Rect(201,964,88,62)))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [556,783]
            dirty_rects.append(screen.blit(odds, p))
            p = [554,844]
            dirty_rects.append(screen.blit(odds, p))
            p = [556,905]
            dirty_rects.append(screen.blit(odds, p))
            p = [556,966]
            dirty_rects.append(screen.blit(odds, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [466,782]
            dirty_rects.append(screen.blit(odds, p))
            p = [466,844]
            dirty_rects.append(screen.blit(odds, p))
            p = [466,904]
            dirty_rects.append(screen.blit(odds, p))
            p = [466,966]
            dirty_rects.append(screen.blit(odds, p))
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [376,782]
            dirty_rects.append(screen.blit(odds, p))
            p = [377,843]
            dirty_rects.append(screen.blit(odds, p))
            p = [378,904]
            dirty_rects.append(screen.blit(odds, p))
            p = [378,965]
            dirty_rects.append(screen.blit(odds, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [289,780]
            dirty_rects.append(screen.blit(odds, p))
            p = [289,842]
            dirty_rects.append(screen.blit(odds, p))
            p = [290,904]
            dirty_rects.append(screen.blit(odds, p))
            p = [290,964]
            dirty_rects.append(screen.blit(odds, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [200,780]
            dirty_rects.append(screen.blit(odds, p))
            p = [200,842]
            dirty_rects.append(screen.blit(odds, p))
            p = [200,902]
            dirty_rects.append(screen.blit(odds, p))
            p = [201,964]
            dirty_rects.append(screen.blit(odds, p))

    pygame.display.update(dirty_rects)
    return

