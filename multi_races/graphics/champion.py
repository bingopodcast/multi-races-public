import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

tilt = pygame.image.load('champion/assets/tilt.png').convert_alpha()
arrow = pygame.image.load('champion/assets/arrow.png').convert_alpha()
feature = pygame.image.load('champion/assets/feature.png').convert_alpha()
horseshoe = pygame.image.load('champion/assets/horseshoe.png').convert_alpha()
odds = pygame.image.load('champion/assets/odds.png').convert_alpha()
place = pygame.image.load('champion/assets/place.png').convert_alpha()
purse = pygame.image.load('champion/assets/purse.png').convert_alpha()
scores_double = pygame.image.load('champion/assets/scores_double.png').convert_alpha()
scores_win = pygame.image.load('champion/assets/scores_win.png').convert_alpha()
section = pygame.image.load('champion/assets/section.png').convert_alpha()
selection = pygame.image.load('champion/assets/selection.png').convert_alpha()
show = pygame.image.load('champion/assets/show.png').convert_alpha()
trophy = pygame.image.load('champion/assets/trophy.png').convert_alpha()
wild = pygame.image.load('champion/assets/wild.png').convert_alpha()
win = pygame.image.load('champion/assets/win.png').convert_alpha()
bg_menu = pygame.image.load('champion/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('champion/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('champion/assets/backglass_off.png').convert_alpha()
meter = pygame.image.load('graphics/assets/register_cover.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert_alpha()

reel1 = scorereel([380,344], "graphics/assets/green_reel.png")
reel10 = scorereel([350,344], "graphics/assets/green_reel.png")
reel100 = scorereel([322,344], "graphics/assets/green_reel.png")


def display(s, replays=0, menu=False):
    global screen
    meter_position = [306,332]
    screen.blit(reel1.image, reel1.position)
    screen.blit(reel10.image, reel10.position)
    screen.blit(reel100.image, reel100.position)
    screen.blit(meter, meter_position)

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

        if 1 in s.game.selection or s.game.fan.status == True:
            p = [13,738]
            screen.blit(selection, p)
        if 2 in s.game.selection or s.game.fan.status == True:
            p = [12,606]
            screen.blit(selection, p)
        if 3 in s.game.selection or s.game.fan.status == True:
            p = [162,606]
            screen.blit(selection, p)
        if 4 in s.game.selection or s.game.fan.status == True:
            p = [308,606]
            screen.blit(selection, p)
        if 5 in s.game.selection or s.game.fan.status == True:
            p = [456,606]
            screen.blit(selection, p)
        if 6 in s.game.selection or s.game.fan.status == True:
            p = [602,606]
            screen.blit(selection, p)
        if 7 in s.game.selection or s.game.fan.status == True:
            p = [603,738]
            screen.blit(selection, p)

        if s.game.horseshoe.status == True:
            p = [341,745]
            screen.blit(horseshoe, p)
        if s.game.clover.status == True:
            p = [340,938]
            screen.blit(horseshoe, p)
        if s.game.left.status == True:
            p = [1,926]
            screen.blit(trophy, p)
        if s.game.right.status == True:
            p = [616,923]
            screen.blit(trophy, p)
        if s.game.purse_win.status == True:
            p = [138,801]
            screen.blit(scores_win, p)
        if s.game.show_win.status == True:
            p = [439,802]
            screen.blit(scores_win, p)
        if s.game.purse_double.status == True:
            p = [98,964]
            screen.blit(scores_double, p)
        if s.game.show_double.status == True:
            p = [428,965]
            screen.blit(scores_double, p)
      
        #Odds displays always shown unless tilted
        p = [17,400]
        screen.blit(section, p)

        if s.game.odds.position == 1:
            p = [105,400]
            screen.blit(odds, p)
        if s.game.odds.position == 2:
            p = [164,401]
            screen.blit(odds, p)
        if s.game.odds.position == 3:
            p = [225,402]
            screen.blit(odds, p)
        if s.game.odds.position == 4:
            p = [287,403]
            screen.blit(odds, p)
        if s.game.odds.position == 5:
            p = [347,403]
            screen.blit(odds, p)
        if s.game.odds.position == 6:
            p = [409,403]
            screen.blit(odds, p)
        if s.game.odds.position == 7:
            p = [468,404]
            screen.blit(odds, p)
        if s.game.odds.position == 8:
            p = [529,405]
            screen.blit(odds, p)
        if s.game.odds.position == 9:
            p = [589,407]
            screen.blit(odds, p)
        if s.game.odds.position == 10:
            p = [649,406]
            screen.blit(odds, p)

        if s.game.wild.position == 1:
            p = [9,874]
            screen.blit(arrow, p)
        if s.game.wild.position == 2:
            p = [37,874]
            screen.blit(arrow, p)
        if s.game.wild.position == 3:
            p = [68,875]
            screen.blit(arrow, p)
        if s.game.wild.position == 4:
            p = [97,875]
            screen.blit(arrow, p)
        if s.game.wild.position == 5:
            p = [146,873]
            screen.blit(arrow, p)
        if s.game.wild.position == 6:
            p = [178,874]
            screen.blit(arrow, p)
        if s.game.wild.position == 7:
            p = [209,874]
            screen.blit(arrow, p)
        if s.game.wild.position == 8:
            p = [238,874]
            screen.blit(arrow, p)
        if s.game.wild.position == 9:
            p = [268,875]
            screen.blit(arrow, p)
        if s.game.wild.position == 10:
            p = [320,875]
            screen.blit(arrow, p)
        if s.game.wild.position == 11:
            p = [350,875]
            screen.blit(arrow, p)
        if s.game.wild.position == 12:
            p = [380,875]
            screen.blit(arrow, p)
        if s.game.wild.position == 13:
            p = [410,874]
            screen.blit(arrow, p)
        if s.game.wild.position == 14:
            p = [461,874]
            screen.blit(arrow, p)
        if s.game.wild.position == 15:
            p = [491,874]
            screen.blit(arrow, p)
        if s.game.wild.position == 16:
            p = [521,874]
            screen.blit(arrow, p)
        if s.game.wild.position == 17:
            p = [551,874]
            screen.blit(arrow, p)
        if s.game.wild.position == 18:
            p = [582,873]
            screen.blit(arrow, p)
        if s.game.wild.position == 19:
            p = [631,873]
            screen.blit(arrow, p)
        if s.game.wild.position == 20:
            p = [660,871]
            screen.blit(arrow, p)
        if s.game.wild.position == 21:
            p = [690,872]
            screen.blit(arrow, p)

        if s.game.wild.position < 5:
            p = [6,898]
            screen.blit(wild, p)
        if s.game.wild.position >= 10 and s.game.wild.position < 14:
            p = [149,899]
            screen.blit(purse, p)
        if s.game.wild.position >= 14 and s.game.wild.position < 19:
            p = [323,900]
            screen.blit(show, p)
        if s.game.wild.position >= 19 and s.game.wild.position < 22:
            p = [462,899]
            screen.blit(place, p)
        if s.game.wild.position >= 22:
            p = [621,897]
            screen.blit(win, p)
        if s.game.pennant.status == True:
            p = [113,357]
            screen.blit(feature, p)

    if s.game.tilt.status == True:
        tilt_position = [535,360]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def clover_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.purse_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (98,964), pygame.Rect(98,964,198,70)))
    if s.game.show_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (428,965), pygame.Rect(428,965,198,70)))

    if num in [5,20,30,40,15]:
        if s.game.show_double.status == False:
            p = [430,965]
            dirty_rects.append(screen.blit(scores_double, p))
    if num in [0,10,25,35,45]:
        if s.game.purse_double.status == False:
            p = [98,964]
            dirty_rects.append(screen.blit(scores_double, p))

    pygame.display.update()
    return

def feature_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.purse_win.status == False:
        dirty_rects.append(screen.blit(bg_gi, (138,801), pygame.Rect(138,801,147,60)))
    if s.game.show_win.status == False:
        dirty_rects.append(screen.blit(bg_gi, (439,802), pygame.Rect(439,802,147,60)))
    if s.game.fan.status == False:
        dirty_rects.append(screen.blit(bg_gi, (289,804), pygame.Rect(289,804,198,70)))

    if num in [14,6,8,23,32]:
        if s.game.purse_win.status == False:
            p = [138,801]
            dirty_rects.append(screen.blit(scores_win, p))
    if num in [4,7,17,19,21,28]:
        if s.game.show_win.status == False:
            p = [439,802]
            dirty_rects.append(screen.blit(scores_win, p))
    if num in [3,7,9,13,22]:
        if s.game.fan.status == False:
            p = [289,804]
            dirty_rects.append(screen.blit(scores_win, p))

    pygame.display.update()
    return

def selection_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.left.status == False:
        dirty_rects.append(screen.blit(bg_gi, (1,926), pygame.Rect(1,926,99,105)))
    if s.game.right.status == False:
        dirty_rects.append(screen.blit(bg_gi, (616,923), pygame.Rect(616,923,99,105)))

    if 1 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (13,738), pygame.Rect(13,738,119,123)))
    if 2 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (12,606), pygame.Rect(12,606,119,123)))
    if 3 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (162,606), pygame.Rect(162,606,119,123)))
    if 4 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (308,606), pygame.Rect(308,606,119,123)))
    if 5 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (456,606), pygame.Rect(456,606,119,123)))
    if 6 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (602,606), pygame.Rect(602,606,119,123)))
    if 7 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (603,738), pygame.Rect(603,738,119,123)))

    if num in [5,20,30,40]:
        if s.game.left.status == False:
            p = [1,926]
            dirty_rects.append(screen.blit(trophy, p))
    if num in [0,10,25,35,45]:
        if s.game.right.status == False:
            p = [616,923]
            dirty_rects.append(screen.blit(trophy, p))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [13,738]
            dirty_rects.append(screen.blit(selection, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [12,606]
            dirty_rects.append(screen.blit(selection, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection:
            p = [162,606]
            dirty_rects.append(screen.blit(selection, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection:
            p = [308,606]
            dirty_rects.append(screen.blit(selection, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection:
            p = [456,606]
            dirty_rects.append(screen.blit(selection, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [602,606]
            dirty_rects.append(screen.blit(selection, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [603,738]
            dirty_rects.append(screen.blit(selection, p))

    pygame.display.update(dirty_rects)
    return

def star_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (105,400), pygame.Rect(105,400,61,206)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (164,401), pygame.Rect(164,401,61,206)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (225,402), pygame.Rect(225,402,61,206)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (287,403), pygame.Rect(287,403,61,206)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (347,403), pygame.Rect(347,403,61,206)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (409,403), pygame.Rect(409,403,61,206)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (468,404), pygame.Rect(468,404,61,206)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (529,405), pygame.Rect(529,405,61,206)))
    if s.game.odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (589,407), pygame.Rect(589,407,61,206)))
    if s.game.odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (649,406), pygame.Rect(649,406,61,206)))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [105,400]
            dirty_rects.append(screen.blit(odds, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [164,401]
            dirty_rects.append(screen.blit(odds, p))
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [225,402]
            dirty_rects.append(screen.blit(odds, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [287,403]
            dirty_rects.append(screen.blit(odds, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [347,403]
            dirty_rects.append(screen.blit(odds, p))
    if num in [5,15,25,35,45]:
        if s.game.odds.position != 6:
            p = [409,403]
            dirty_rects.append(screen.blit(odds, p))
    if num in [6,16,26,36,46]:
        if s.game.odds.position != 7:
            p = [468,404]
            dirty_rects.append(screen.blit(odds, p))
    if num in [7,17,27,37,47]:
        if s.game.odds.position != 8:
            p = [529,405]
            dirty_rects.append(screen.blit(odds, p))
    if num in [8,18,28,38,48]:
        if s.game.odds.position != 9:
            p = [589,407]
            dirty_rects.append(screen.blit(odds, p))
    if num in [9,19,29,39,49]:
        if s.game.odds.position != 10:
            p = [649,406]
            dirty_rects.append(screen.blit(odds, p))

    pygame.display.update(dirty_rects)
    return

