import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert_alpha()
tilt = pygame.image.load('turf_king/assets/tilt.png').convert_alpha()
all_double = pygame.image.load('turf_king/assets/all_double.png').convert_alpha()
arrow = pygame.image.load('turf_king/assets/arrow.png').convert_alpha()
button = pygame.image.load('turf_king/assets/button.png').convert_alpha()
double_letter = pygame.image.load('turf_king/assets/double_letter.png').convert_alpha()
feature = pygame.image.load('turf_king/assets/feature.png').convert_alpha()
held = pygame.image.load('turf_king/assets/held.png').convert_alpha()
left_cap = pygame.image.load('turf_king/assets/left_cap.png').convert_alpha()
odds = pygame.image.load('turf_king/assets/odds.png').convert_alpha()
place = pygame.image.load('turf_king/assets/place.png').convert_alpha()
purse = pygame.image.load('turf_king/assets/purse.png').convert_alpha()
right_cap = pygame.image.load('turf_king/assets/right_cap.png').convert_alpha()
scores_double = pygame.image.load('turf_king/assets/scores_double.png').convert_alpha()
scores_win = pygame.image.load('turf_king/assets/scores_win.png').convert_alpha()
section = pygame.image.load('turf_king/assets/section.png').convert_alpha()
selection = pygame.image.load('turf_king/assets/selection.png').convert_alpha()
show = pygame.image.load('turf_king/assets/show.png').convert_alpha()
wild = pygame.image.load('turf_king/assets/wild.png').convert_alpha()
win = pygame.image.load('turf_king/assets/win.png').convert_alpha()
bg_menu = pygame.image.load('turf_king/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('turf_king/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('turf_king/assets/backglass_off.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([373,360], "graphics/assets/green_reel.png")
reel10 = scorereel([345,360], "graphics/assets/green_reel.png")
reel100 = scorereel([317,360], "graphics/assets/green_reel_zero.png")

def display(s, replays=0, menu=False):
    global screen
    meter_position = [300,350]

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
            p = [32,684]
            screen.blit(selection, p)
        if 2 in s.game.selection or s.game.fan.status == True:
            p = [32,826]
            screen.blit(selection, p)
        if 3 in s.game.selection or s.game.fan.status == True:
            p = [168,826]
            screen.blit(selection, p)
        if 4 in s.game.selection or s.game.fan.status == True:
            p = [306,826]
            screen.blit(selection, p)
        if 5 in s.game.selection or s.game.fan.status == True:
            p = [442,826]
            screen.blit(selection, p)
        if 6 in s.game.selection or s.game.fan.status == True:
            p = [576,826]
            screen.blit(selection, p)
        if 7 in s.game.selection or s.game.fan.status == True:
            p = [577,684]
            screen.blit(selection, p)

        if s.game.lettera.status == True:
            p = [28,349]
            screen.blit(double_letter, p)
        if s.game.letterb.status == True:
            p = [54,349]
            screen.blit(double_letter, p)
        if s.game.letterc.status == True:
            p = [82,350]
            screen.blit(double_letter, p)
        if s.game.letterd.status == True:
            p = [112,350]
            screen.blit(double_letter, p)
        if s.game.abcd.status == True:
            p = [23,378]
            screen.blit(all_double, p)
        if s.game.clover.status == True:
            p = [332,690]
            screen.blit(button, p)
        if s.game.horseshoe.status == True:
            p = [332,768]
            screen.blit(button, p)
        if s.game.star.status == True:
            p = [332,623]
            screen.blit(button, p)
        if s.game.left.status == True:
            p = [156,762]
            screen.blit(left_cap, p)
        if s.game.right.status == True:
            p = [476,764]
            screen.blit(right_cap, p)
        if s.game.purse_double.status == True:
            p = [164,685]
            screen.blit(scores_double, p)
        if s.game.show_double.status == True:
            p = [392,684]
            screen.blit(scores_double, p)
        if s.game.purse_win.status == True:
            p = [74,628]
            screen.blit(scores_win, p)
        if s.game.show_win.status == True:
            p = [391,628]
            screen.blit(scores_win, p)
        if s.game.pennant.status == True:
            p = [540,279]
            screen.blit(feature, p)
        if s.game.feature.status == True:
            p = [538,320]
            screen.blit(feature, p)
      
        #Odds displays always shown unless tilted
        p = [12,424]
        screen.blit(section, p)
        p = [12,474]
        screen.blit(section, p)
        p = [12,523]
        screen.blit(section, p)
        p = [14,569]
        screen.blit(section, p)

        if s.game.odds.position == 1:
            p = [102,424]
            screen.blit(odds, p)
            p = [102,474]
            screen.blit(odds, p)
            p = [102,523]
            screen.blit(odds, p)
            p = [103,569]
            screen.blit(odds, p)
        if s.game.odds.position == 2:
            p = [162,424]
            screen.blit(odds, p)
            p = [162,474]
            screen.blit(odds, p)
            p = [162,523]
            screen.blit(odds, p)
            p = [163,569]
            screen.blit(odds, p)
        if s.game.odds.position == 3:
            p = [222,424]
            screen.blit(odds, p)
            p = [222,474]
            screen.blit(odds, p)
            p = [222,523]
            screen.blit(odds, p)
            p = [223,569]
            screen.blit(odds, p)
        if s.game.odds.position == 4:
            p = [282,424]
            screen.blit(odds, p)
            p = [282,474]
            screen.blit(odds, p)
            p = [282,523]
            screen.blit(odds, p)
            p = [283,569]
            screen.blit(odds, p)
        if s.game.odds.position == 5:
            p = [342,424]
            screen.blit(odds, p)
            p = [342,474]
            screen.blit(odds, p)
            p = [342,523]
            screen.blit(odds, p)
            p = [343,569]
            screen.blit(odds, p)
        if s.game.odds.position == 6:
            p = [400,424]
            screen.blit(odds, p)
            p = [400,474]
            screen.blit(odds, p)
            p = [400,523]
            screen.blit(odds, p)
            p = [400,569]
            screen.blit(odds, p)
        if s.game.odds.position == 7:
            p = [461,424]
            screen.blit(odds, p)
            p = [461,474]
            screen.blit(odds, p)
            p = [461,523]
            screen.blit(odds, p)
            p = [462,569]
            screen.blit(odds, p)
        if s.game.odds.position == 8:
            p = [521,424]
            screen.blit(odds, p)
            p = [521,474]
            screen.blit(odds, p)
            p = [521,523]
            screen.blit(odds, p)
            p = [522,569]
            screen.blit(odds, p)
        if s.game.odds.position == 9:
            p = [581,424]
            screen.blit(odds, p)
            p = [581,474]
            screen.blit(odds, p)
            p = [581,523]
            screen.blit(odds, p)
            p = [582,569]
            screen.blit(odds, p)
        if s.game.odds.position == 10:
            p = [642,424]
            screen.blit(odds, p)
            p = [642,474]
            screen.blit(odds, p)
            p = [642,523]
            screen.blit(odds, p)
            p = [643,569]
            screen.blit(odds, p)
        if s.game.wild.position in range(0,5):
            p = [38,981]
            screen.blit(wild, p)
        if s.game.wild.position in range(5,10):
            p = [161,980]
            screen.blit(purse, p)
        if s.game.wild.position in range(10,14):
            p = [314,980]
            screen.blit(show, p)
        if s.game.wild.position in range(14,19):
            p = [435,980]
            screen.blit(place, p)
        if s.game.wild.position in range(19,22):
            p = [586,982]
            screen.blit(win, p)

        if s.game.wild.position == 0:
            p = [46,960]
            screen.blit(arrow, p)
        if s.game.wild.position == 1:
            p = [74,960]
            screen.blit(arrow, p)
        if s.game.wild.position == 2:
            p = [104,960]
            screen.blit(arrow, p)
        if s.game.wild.position == 3:
            p = [134,958]
            screen.blit(arrow, p)
        if s.game.wild.position == 4:
            p = [166,958]
            screen.blit(arrow, p)
        if s.game.wild.position == 5:
            p = [198,958]
            screen.blit(arrow, p)
        if s.game.wild.position == 6:
            p = [226,958]
            screen.blit(arrow, p)
        if s.game.wild.position == 7:
            p = [257,958]
            screen.blit(arrow, p)
        if s.game.wild.position == 8:
            p = [286,958]
            screen.blit(arrow, p)
        if s.game.wild.position == 9:
            p = [319,958]
            screen.blit(arrow, p)
        if s.game.wild.position == 10:
            p = [347,958]
            screen.blit(arrow, p)
        if s.game.wild.position == 11:
            p = [378,958]
            screen.blit(arrow, p)
        if s.game.wild.position == 12:
            p = [408,958]
            screen.blit(arrow, p)
        if s.game.wild.position == 13:
            p = [439,960]
            screen.blit(arrow, p)
        if s.game.wild.position == 14:
            p = [469,960]
            screen.blit(arrow, p)
        if s.game.wild.position == 15:
            p = [498,960]
            screen.blit(arrow, p)
        if s.game.wild.position == 16:
            p = [528,959]
            screen.blit(arrow, p)
        if s.game.wild.position == 17:
            p = [558,960]
            screen.blit(arrow, p)
        if s.game.wild.position == 18:
            p = [592,960]
            screen.blit(arrow, p)
        if s.game.wild.position == 19:
            p = [622,960]
            screen.blit(arrow, p)
        if s.game.wild.position == 20:
            p = [653,960]
            screen.blit(arrow, p)

        if s.game.fan.status == True:
            p = [34,774]
            screen.blit(held, p)
            p = [34,918]
            screen.blit(held, p)
            p = [578,918]
            screen.blit(held, p)
            p = [577,774]
            screen.blit(held, p)
        if s.game.hold3.status == True or s.game.fan.status == True:
            p = [170,916]
            screen.blit(held, p)
        if s.game.hold4.status == True or s.game.fan.status == True:
            p = [307,916]
            screen.blit(held, p)
        if s.game.hold5.status == True or s.game.fan.status == True:
            p = [441,916]
            screen.blit(held, p)
            
    if s.game.tilt.status == True:
        tilt_position = [646,282]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def clover_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]
    
    if s.game.purse_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (164,685), pygame.Rect(164,685,163,61)))
    if s.game.show_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (392,684), pygame.Rect(392,684,163,61)))

    if num in [3,15,22,34]:
        p = [164,685]
        dirty_rects.append(screen.blit(scores_double, p))

    if num in [8,19,27,39]:
        p = [392,684]
        dirty_rects.append(screen.blit(scores_double, p))

    pygame.display.update(dirty_rects)
    return

def feature_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.pennant.status == False:
        dirty_rects.append(screen.blit(bg_gi, (540,279), pygame.Rect(540,279,62,34)))
   
    if num in [7,25,32,44]:
        if s.game.pennant.status == False:
            p = [540,279]
            dirty_rects.append(screen.blit(feature, p))

    pygame.display.update(dirty_rects)
    return

def selection_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.left.status == False:
        dirty_rects.append(screen.blit(bg_gi, (156,762), pygame.Rect(156,762,86,55)))
    if s.game.right.status == False:
        dirty_rects.append(screen.blit(bg_gi, (476,764), pygame.Rect(476,764,84,51)))

    if 1 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (32,684), pygame.Rect(32,684,107,90)))
    if 2 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (32,826), pygame.Rect(32,826,107,90)))
    if 3 not in s.game.selection or s.game.hold3.status == False:
        dirty_rects.append(screen.blit(bg_gi, (168,826), pygame.Rect(168,826,107,90)))
    if 4 not in s.game.selection or s.game.hold4.status == False:
        dirty_rects.append(screen.blit(bg_gi, (306,826), pygame.Rect(306,826,107,90)))
    if 5 not in s.game.selection or s.game.hold5.status == False:
        dirty_rects.append(screen.blit(bg_gi, (442,826), pygame.Rect(442,826,107,90)))
    if 6 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (576,826), pygame.Rect(576,826,107,90)))
    if 7 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (577,684), pygame.Rect(577,684,107,90)))

    if num in [5,20,30,40]:
        if s.game.left.status == False:
            p = [156,762]
            dirty_rects.append(screen.blit(left_cap, p))
    if num in [0,10,25,35,45]:
        if s.game.right.status == False:
            p = [476,764]
            dirty_rects.append(screen.blit(right_cap, p))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [32,684]
            dirty_rects.append(screen.blit(selection, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [32,826]
            dirty_rects.append(screen.blit(selection, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection or s.game.hold3.status == False:
            p = [168,826]
            dirty_rects.append(screen.blit(selection, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection or s.game.hold4.status == False:
            p = [306,826]
            dirty_rects.append(screen.blit(selection, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection or s.game.hold5.status == False:
            p = [442,826]
            dirty_rects.append(screen.blit(selection, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [576,826]
            dirty_rects.append(screen.blit(selection, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [577,684]
            dirty_rects.append(screen.blit(selection, p))

    pygame.display.update(dirty_rects)
    return

def star_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.purse_win.status == False:
        dirty_rects.append(screen.blit(bg_gi, (74,628), pygame.Rect(74,628,247,39)))
    if s.game.show_win.status == False:
        dirty_rects.append(screen.blit(bg_gi, (391,628), pygame.Rect(391,628,247,39)))

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (102,424), pygame.Rect(102,424,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (102,474), pygame.Rect(102,474,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (102,523), pygame.Rect(102,523,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (103,569), pygame.Rect(103,569,61,49)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (162,424), pygame.Rect(162,424,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (162,474), pygame.Rect(162,474,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (162,523), pygame.Rect(162,523,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (163,569), pygame.Rect(163,569,61,49)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (222,424), pygame.Rect(222,424,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (222,474), pygame.Rect(222,474,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (222,523), pygame.Rect(222,523,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (223,569), pygame.Rect(223,569,61,49)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (282,424), pygame.Rect(282,424,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (282,474), pygame.Rect(282,474,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (282,523), pygame.Rect(282,523,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (283,569), pygame.Rect(283,569,61,49)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (342,424), pygame.Rect(342,424,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (342,474), pygame.Rect(342,474,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (342,523), pygame.Rect(342,523,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (343,569), pygame.Rect(343,569,61,49)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (400,424), pygame.Rect(400,424,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (400,474), pygame.Rect(400,474,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (400,523), pygame.Rect(400,523,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (400,569), pygame.Rect(400,569,61,49)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (461,424), pygame.Rect(461,424,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (461,474), pygame.Rect(461,474,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (461,523), pygame.Rect(461,523,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (462,569), pygame.Rect(462,569,61,49)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (521,424), pygame.Rect(521,424,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (521,474), pygame.Rect(521,474,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (521,523), pygame.Rect(521,523,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (522,569), pygame.Rect(522,569,61,49)))
    if s.game.odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (581,424), pygame.Rect(581,424,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (581,474), pygame.Rect(581,474,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (581,523), pygame.Rect(581,523,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (582,569), pygame.Rect(582,569,61,49)))
    if s.game.odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (642,424), pygame.Rect(642,424,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (642,474), pygame.Rect(642,474,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (642,523), pygame.Rect(642,523,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (643,569), pygame.Rect(643,569,61,49)))

    if num in [8,10,16,18,20,22,28,35,37,40,42,46,49]:
        if s.game.purse_win.status == False:
            p = [74,628]
            dirty_rects.append(screen.blit(scores_win, p))
    if num in [2,4,17,25,32,36,41,44,48]:
        if s.game.show_win.status == False:
            p = [391,628]
            dirty_rects.append(screen.blit(scores_win, p))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [102,424]
            dirty_rects.append(screen.blit(odds, p))
            p = [102,474]
            dirty_rects.append(screen.blit(odds, p))
            p = [102,523]
            dirty_rects.append(screen.blit(odds, p))
            p = [103,569]
            dirty_rects.append(screen.blit(odds, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [162,424]
            dirty_rects.append(screen.blit(odds, p))
            p = [162,474]
            dirty_rects.append(screen.blit(odds, p))
            p = [162,523]
            dirty_rects.append(screen.blit(odds, p))
            p = [163,569]
            dirty_rects.append(screen.blit(odds, p))
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [222,424]
            dirty_rects.append(screen.blit(odds, p))
            p = [222,474]
            dirty_rects.append(screen.blit(odds, p))
            p = [222,523]
            dirty_rects.append(screen.blit(odds, p))
            p = [223,569]
            dirty_rects.append(screen.blit(odds, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [282,424]
            dirty_rects.append(screen.blit(odds, p))
            p = [282,474]
            dirty_rects.append(screen.blit(odds, p))
            p = [282,523]
            dirty_rects.append(screen.blit(odds, p))
            p = [283,569]
            dirty_rects.append(screen.blit(odds, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [342,424]
            dirty_rects.append(screen.blit(odds, p))
            p = [342,474]
            dirty_rects.append(screen.blit(odds, p))
            p = [342,523]
            dirty_rects.append(screen.blit(odds, p))
            p = [343,569]
            dirty_rects.append(screen.blit(odds, p))
    if num in [5,15,25,35,45]:
        if s.game.odds.position != 6:
            p = [400,424]
            dirty_rects.append(screen.blit(odds, p))
            p = [400,474]
            dirty_rects.append(screen.blit(odds, p))
            p = [400,523]
            dirty_rects.append(screen.blit(odds, p))
            p = [400,569]
            dirty_rects.append(screen.blit(odds, p))
    if num in [6,16,26,36,46]:
        if s.game.odds.position != 7:
            p = [461,424]
            dirty_rects.append(screen.blit(odds, p))
            p = [461,474]
            dirty_rects.append(screen.blit(odds, p))
            p = [461,523]
            dirty_rects.append(screen.blit(odds, p))
            p = [462,569]
            dirty_rects.append(screen.blit(odds, p))
    if num in [7,17,27,37,47]:
        if s.game.odds.position != 8:
            p = [521,424]
            dirty_rects.append(screen.blit(odds, p))
            p = [521,474]
            dirty_rects.append(screen.blit(odds, p))
            p = [521,523]
            dirty_rects.append(screen.blit(odds, p))
            p = [522,569]
            dirty_rects.append(screen.blit(odds, p))
    if num in [8,18,28,38,48]:
        if s.game.odds.position != 9:
            p = [581,424]
            dirty_rects.append(screen.blit(odds, p))
            p = [581,474]
            dirty_rects.append(screen.blit(odds, p))
            p = [581,523]
            dirty_rects.append(screen.blit(odds, p))
            p = [582,569]
            dirty_rects.append(screen.blit(odds, p))
    if num in [9,19,29,39,49]:
        if s.game.odds.position != 10:
            p = [642,424]
            dirty_rects.append(screen.blit(odds, p))
            p = [642,474]
            dirty_rects.append(screen.blit(odds, p))
            p = [642,523]
            dirty_rects.append(screen.blit(odds, p))
            p = [643,569]
            dirty_rects.append(screen.blit(odds, p))

    pygame.display.update(dirty_rects)
    return

