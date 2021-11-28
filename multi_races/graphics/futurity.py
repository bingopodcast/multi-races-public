import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert_alpha()
tilt = pygame.image.load('futurity/assets/tilt.png').convert_alpha()
all_double = pygame.image.load('futurity/assets/all_double.png').convert_alpha()
arrow = pygame.image.load('futurity/assets/arrow.png').convert_alpha()
button = pygame.image.load('futurity/assets/button.png').convert_alpha()
double_letter = pygame.image.load('futurity/assets/double_letter.png').convert_alpha()
futurity_arrow = pygame.image.load('futurity/assets/futurity_arrow.png').convert_alpha()
held_next = pygame.image.load('futurity/assets/held_next.png').convert_alpha()
held_number = pygame.image.load('futurity/assets/held_number.png').convert_alpha()
feature = pygame.image.load('futurity/assets/feature.png').convert_alpha()
held = pygame.image.load('futurity/assets/held.png').convert_alpha()
left_cap = pygame.image.load('futurity/assets/left_cap.png').convert_alpha()
next_odds = pygame.image.load('futurity/assets/next_odds.png').convert_alpha()
odds = pygame.image.load('futurity/assets/odds.png').convert_alpha()
place = pygame.image.load('futurity/assets/place.png').convert_alpha()
purse = pygame.image.load('futurity/assets/purse.png').convert_alpha()
right_cap = pygame.image.load('futurity/assets/right_cap.png').convert_alpha()
scores_double = pygame.image.load('futurity/assets/scores_double.png').convert_alpha()
scores_win = pygame.image.load('futurity/assets/scores_win.png').convert_alpha()
section = pygame.image.load('futurity/assets/section.png').convert_alpha()
selection = pygame.image.load('futurity/assets/selection.png').convert_alpha()
show = pygame.image.load('futurity/assets/show.png').convert_alpha()
trophy = pygame.image.load('futurity/assets/trophy.png').convert_alpha()
wild = pygame.image.load('futurity/assets/wild.png').convert_alpha()
win = pygame.image.load('futurity/assets/win.png').convert_alpha()
bg_menu = pygame.image.load('futurity/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('futurity/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('futurity/assets/backglass_off.png').convert_alpha()
next_odds = pygame.image.load('futurity/assets/next_odds.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([628,322], "graphics/assets/green_reel.png")
reel10 = scorereel([600,322], "graphics/assets/green_reel.png")
reel100 = scorereel([572,322], "graphics/assets/green_reel_zero.png")

def display(s, replays=0, menu=False):
    global screen

    meter_position = [555,310]

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
            p = [30,700]
            screen.blit(selection, p)
        if 2 in s.game.selection or s.game.fan.status == True:
            p = [30,820]
            screen.blit(selection, p)
        if 3 in s.game.selection or s.game.fan.status == True:
            p = [162,820]
            screen.blit(selection, p)
        if 4 in s.game.selection or s.game.fan.status == True:
            p = [292,817]
            screen.blit(selection, p)
        if 5 in s.game.selection or s.game.fan.status == True:
            p = [427,819]
            screen.blit(selection, p)
        if 6 in s.game.selection or s.game.fan.status == True:
            p = [562,820]
            screen.blit(selection, p)
        if 7 in s.game.selection or s.game.fan.status == True:
            p = [561,699]
            screen.blit(selection, p)

        if s.game.lettera.status == True:
            p = [38,318]
            screen.blit(double_letter, p)
        if s.game.letterb.status == True:
            p = [68,318]
            screen.blit(double_letter, p)
        if s.game.letterc.status == True:
            p = [96,318]
            screen.blit(double_letter, p)
        if s.game.letterd.status == True:
            p = [123,318]
            screen.blit(double_letter, p)
        if s.game.abcd.status == True:
            p = [34,345]
            screen.blit(all_double, p)
        if s.game.clover.status == True:
            p = [219,637]
            screen.blit(button, p)
            p = [451,635]
            screen.blit(button, p)
        if s.game.horseshoe.status == True:
            p = [333,692]
            screen.blit(button, p)
        if s.game.star.status == True:
            p = [334,647]
            screen.blit(button, p)
        if s.game.left.status == True:
            p = [255,685]
            screen.blit(left_cap, p)
        if s.game.right.status == True:
            p = [398,686]
            screen.blit(right_cap, p)
        if s.game.purse_double.status == True:
            p = [17,636]
            screen.blit(scores_double, p)
        if s.game.show_double.status == True:
            p = [505,635]
            screen.blit(scores_double, p)
        if s.game.purse_win.status == True:
            p = [26,589]
            screen.blit(scores_win, p)
        if s.game.show_win.status == True:
            p = [456,587]
            screen.blit(scores_win, p)
        if s.game.pennant.status == True:
            p = [166,310]
            screen.blit(feature, p)
        if s.game.feature.status == True:
            p = [172,348]
            screen.blit(feature, p)
      
        #Odds displays always shown unless tilted
        p = [13,430]
        screen.blit(section, p)
        p = [14,470]
        screen.blit(section, p)
        p = [14,508]
        screen.blit(section, p)
        p = [14,549]
        screen.blit(section, p)

        if s.game.odds.position == 1:
            p = [116,429]
            screen.blit(odds, p)
            p = [114,469]
            screen.blit(odds, p)
            p = [115,509]
            screen.blit(odds, p)
            p = [115,549]
            screen.blit(odds, p)
        if s.game.odds.position == 2:
            p = [173,428]
            screen.blit(odds, p)
            p = [173,469]
            screen.blit(odds, p)
            p = [173,509]
            screen.blit(odds, p)
            p = [174,549]
            screen.blit(odds, p)
        if s.game.odds.position == 3:
            p = [232,428]
            screen.blit(odds, p)
            p = [232,472]
            screen.blit(odds, p)
            p = [232,509]
            screen.blit(odds, p)
            p = [232,547]
            screen.blit(odds, p)
        if s.game.odds.position == 4:
            p = [289,430]
            screen.blit(odds, p)
            p = [290,470]
            screen.blit(odds, p)
            p = [289,510]
            screen.blit(odds, p)
            p = [290,550]
            screen.blit(odds, p)
        if s.game.odds.position == 5:
            p = [348,430]
            screen.blit(odds, p)
            p = [348,470]
            screen.blit(odds, p)
            p = [347,509]
            screen.blit(odds, p)
            p = [347,549]
            screen.blit(odds, p)
        if s.game.odds.position == 6:
            p = [405,430]
            screen.blit(odds, p)
            p = [407,470]
            screen.blit(odds, p)
            p = [406,509]
            screen.blit(odds, p)
            p = [406,549]
            screen.blit(odds, p)
        if s.game.odds.position == 7:
            p = [464,430]
            screen.blit(odds, p)
            p = [464,470]
            screen.blit(odds, p)
            p = [464,509]
            screen.blit(odds, p)
            p = [464,549]
            screen.blit(odds, p)
        if s.game.odds.position == 8:
            p = [522,430]
            screen.blit(odds, p)
            p = [522,470]
            screen.blit(odds, p)
            p = [522,509]
            screen.blit(odds, p)
            p = [522,549]
            screen.blit(odds, p)
        if s.game.odds.position == 9:
            p = [582,430]
            screen.blit(odds, p)
            p = [582,470]
            screen.blit(odds, p)
            p = [582,509]
            screen.blit(odds, p)
            p = [582,549]
            screen.blit(odds, p)
        if s.game.odds.position == 10:
            p = [641,430]
            screen.blit(odds, p)
            p = [641,470]
            screen.blit(odds, p)
            p = [641,509]
            screen.blit(odds, p)
            p = [641,549]
            screen.blit(odds, p)
        if s.game.wild.position in range(0,5):
            p = [43,959]
            screen.blit(wild, p)
        if s.game.wild.position in range(5,10):
            p = [166,959]
            screen.blit(purse, p)
        if s.game.wild.position in range(10,14):
            p = [314,959]
            screen.blit(show, p)
        if s.game.wild.position in range(14,19):
            p = [436,959]
            screen.blit(place, p)
        if s.game.wild.position in range(19,22):
            p = [587,959]
            screen.blit(win, p)

        if s.game.wild.position == 0:
            p = [46,937]
            screen.blit(arrow, p)
        if s.game.wild.position == 1:
            p = [76,937]
            screen.blit(arrow, p)
        if s.game.wild.position == 2:
            p = [106,937]
            screen.blit(arrow, p)
        if s.game.wild.position == 3:
            p = [135,937]
            screen.blit(arrow, p)
        if s.game.wild.position == 4:
            p = [166,937]
            screen.blit(arrow, p)
        if s.game.wild.position == 5:
            p = [196,937]
            screen.blit(arrow, p)
        if s.game.wild.position == 6:
            p = [226,937]
            screen.blit(arrow, p)
        if s.game.wild.position == 7:
            p = [256,937]
            screen.blit(arrow, p)
        if s.game.wild.position == 8:
            p = [284,937]
            screen.blit(arrow, p)
        if s.game.wild.position == 9:
            p = [317,937]
            screen.blit(arrow, p)
        if s.game.wild.position == 10:
            p = [347,937]
            screen.blit(arrow, p)
        if s.game.wild.position == 11:
            p = [375,937]
            screen.blit(arrow, p)
        if s.game.wild.position == 12:
            p = [404,937]
            screen.blit(arrow, p)
        if s.game.wild.position == 13:
            p = [436,937]
            screen.blit(arrow, p)
        if s.game.wild.position == 14:
            p = [467,937]
            screen.blit(arrow, p)
        if s.game.wild.position == 15:
            p = [495,937]
            screen.blit(arrow, p)
        if s.game.wild.position == 16:
            p = [525,937]
            screen.blit(arrow, p)
        if s.game.wild.position == 17:
            p = [555,937]
            screen.blit(arrow, p)
        if s.game.wild.position == 18:
            p = [586,937]
            screen.blit(arrow, p)
        if s.game.wild.position == 19:
            p = [617,937]
            screen.blit(arrow, p)
        if s.game.wild.position == 20:
            p = [646,937]
            screen.blit(arrow, p)

        if s.game.fan.status == True:
            p = [31,783]
            screen.blit(held, p)
            p = [30,903]
            screen.blit(held, p)
            p = [560,903]
            screen.blit(held, p)
            p = [559,783]
            screen.blit(held, p)
        if s.game.hold3.status == True or s.game.fan.status == True:
            p = [163,903]
            screen.blit(held, p)
        if s.game.hold4.status == True or s.game.fan.status == True:
            p = [294,903]
            screen.blit(held, p)
        if s.game.hold5.status == True or s.game.fan.status == True:
            p = [426,903]
            screen.blit(held, p)

        if s.game.odds2.position >= 1:
            p = [276,347]
            screen.blit(next_odds, p)
            if s.game.odds2.position == 1:
                p = [133,408]
                screen.blit(futurity_arrow, p)
            if s.game.odds2.position == 2:
                p = [194,408]
                screen.blit(futurity_arrow, p)
            if s.game.odds2.position == 3:
                p = [251,408]
                screen.blit(futurity_arrow, p)
            if s.game.odds2.position == 4:
                p = [307,408]
                screen.blit(futurity_arrow, p)
            if s.game.odds2.position == 5:
                p = [366,408]
                screen.blit(futurity_arrow, p)
            if s.game.odds2.position == 6:
                p = [426,408]
                screen.blit(futurity_arrow, p)
            if s.game.odds2.position == 7:
                p = [484,408]
                screen.blit(futurity_arrow, p)
            if s.game.odds2.position == 8:
                p = [541,408]
                screen.blit(futurity_arrow, p)
            if s.game.odds2.position == 9:
                p = [600,408]
                screen.blit(futurity_arrow, p)
        
        if s.game.trophy.status == True:
            p = [262,590]
            screen.blit(trophy, p)
    
        if s.game.entry.status == True:
            p = [190,736]
            screen.blit(held_next, p)
            if s.game.number_three.status == True:
                p = [210,784]
                screen.blit(held_number, p)
            if s.game.number_four.status == True:
                p = [342,784]
                screen.blit(held_number, p)
            if s.game.number_five.status == True:
                p = [476,784]
                screen.blit(held_number, p)

    if s.game.tilt.status == True:
        tilt_position = [54,269]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def clover_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]
    
    if s.game.purse_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (17,636), pygame.Rect(17,636,196,45)))
    if s.game.show_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (505,635), pygame.Rect(505,635,196,45)))

    if num in [3,15,22,34]:
        p = [17,636]
        dirty_rects.append(screen.blit(scores_double, p))

    if num in [8,19,27,39]:
        p = [505,635]
        dirty_rects.append(screen.blit(scores_double, p))

    pygame.display.update(dirty_rects)
    return

def special_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]
       
    if s.game.trophy.status == False:
        dirty_rects.append(screen.blit(bg_gi, (262,590), pygame.Rect(262,590,189,58)))
    if s.game.entry.status == False:
        dirty_rects.append(screen.blit(bg_gi, (190,736), pygame.Rect(190,736,343,46)))
    if s.game.number_three.status == False:
        dirty_rects.append(screen.blit(bg_gi, (210,784), pygame.Rect(210,784,35,32)))
    if s.game.number_four.status == False:
        dirty_rects.append(screen.blit(bg_gi, (342,784), pygame.Rect(342,784,35,32)))
    if s.game.number_five.status == False:
        dirty_rects.append(screen.blit(bg_gi, (476,784), pygame.Rect(476,784,35,32)))
    if s.game.odds2.position < 1:
        dirty_rects.append(screen.blit(bg_gi, (276,347), pygame.Rect(276,347,166,54)))
    if s.game.odds2.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (133,408), pygame.Rect(133,408,22,20)))
    if s.game.odds2.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (194,408), pygame.Rect(194,408,22,20)))
    if s.game.odds2.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (251,408), pygame.Rect(251,408,22,20)))
    if s.game.odds2.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (307,408), pygame.Rect(308,408,22,20)))
    if s.game.odds2.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (366,408), pygame.Rect(366,408,22,20)))
    if s.game.odds2.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (426,408), pygame.Rect(426,408,22,20)))
    if s.game.odds2.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (484,408), pygame.Rect(484,408,22,20)))
    if s.game.odds2.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (541,408), pygame.Rect(541,408,22,20)))
    if s.game.odds2.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (600,408), pygame.Rect(600,408,22,20)))

    if num in [2,7,18,20,22,30,44,49]:
        if s.game.trophy.status == False:
            p = [262,590]
            dirty_rects.append(screen.blit(trophy, p))
    if num in [1,5,10,12,24,28,34,39,45]:
        if s.game.entry.status == False:
            p = [190,736]
            dirty_rects.append(screen.blit(held_next, p))
        if num in [1,12,34]:
            if s.game.number_three.status == False:
                p = [210,784]
                dirty_rects.append(screen.blit(held_number, p))
        if num in [5,24,39]:
            if s.game.number_four.status == False:
                p = [342,784]
                dirty_rects.append(screen.blit(held_number, p))
        if num in [10,28,45]:
            if s.game.number_five.status == False:
                p = [476,784]
                dirty_rects.append(screen.blit(held_number, p))

    if num in [3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38,39,40,41,43,44,45,46,47,48,49,50,0,10,20,30,40,1,11,21,31,41]:
        if num in [3,7,0,14,18,11,25,36,47,49]:
            if s.game.odds2.position < 1:
                p = [276,347]
                dirty_rects.append(screen.blit(next_odds, p))
        
        if num in [3,13,23,33,43]:
            if s.game.odds2.position != 1:
                p = [133,408]
                dirty_rects.append(screen.blit(futurity_arrow, p))
        if num in [4,14,24,34,44]:
            if s.game.odds2.position != 2:
                p = [194,408]
                dirty_rects.append(screen.blit(futurity_arrow, p))
        if num in [5,15,25,35,45]:
            if s.game.odds2.position != 3:
                p = [251,408]
                dirty_rects.append(screen.blit(futurity_arrow, p))
        if num in [6,16,26,36,46]:
            if s.game.odds2.position != 4:
                p = [307,408]
                dirty_rects.append(screen.blit(futurity_arrow, p))
        if num in [7,17,27,37,47]:
            if s.game.odds2.position != 5:
                p = [366,408]
                dirty_rects.append(screen.blit(futurity_arrow, p))
        if num in [8,18,28,38,48]:
            if s.game.odds2.position != 6:
                p = [426,408]
                dirty_rects.append(screen.blit(futurity_arrow, p))
        if num in [9,19,29,39,49]:
            if s.game.odds2.position != 7:
                p = [484,408]
                dirty_rects.append(screen.blit(futurity_arrow, p))
        if num in [0,10,20,30,40,50]:
            if s.game.odds2.position != 8:
                p = [541,408]
                dirty_rects.append(screen.blit(futurity_arrow, p))
        if num in [1,11,21,31,41]:
            if s.game.odds2.position != 9:
                p = [600,408]
                dirty_rects.append(screen.blit(futurity_arrow, p))
 
    pygame.display.update(dirty_rects)
    return
            
def feature_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.pennant.status == False:
        dirty_rects.append(screen.blit(bg_gi, (166,310), pygame.Rect(166,310,62,34)))
   
    if num in [7,25,32,44]:
        if s.game.pennant.status == False:
            p = [166,310]
            dirty_rects.append(screen.blit(feature, p))

    pygame.display.update(dirty_rects)
    return

def selection_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.left.status == False:
        dirty_rects.append(screen.blit(bg_gi, (255,685), pygame.Rect(255,685,59,32)))
    if s.game.right.status == False:
        dirty_rects.append(screen.blit(bg_gi, (398,686), pygame.Rect(398,686,59,32)))

    if 1 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (30,700), pygame.Rect(30,700,128,90)))
    if 2 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (30,820), pygame.Rect(30,820,128,90)))
    if 3 not in s.game.selection or s.game.hold3.status == False:
        dirty_rects.append(screen.blit(bg_gi, (162,820), pygame.Rect(162,820,128,90)))
    if 4 not in s.game.selection or s.game.hold4.status == False:
        dirty_rects.append(screen.blit(bg_gi, (292,817), pygame.Rect(292,817,128,90)))
    if 5 not in s.game.selection or s.game.hold5.status == False:
        dirty_rects.append(screen.blit(bg_gi, (427,819), pygame.Rect(427,819,128,90)))
    if 6 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (562,820), pygame.Rect(562,820,128,90)))
    if 7 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (561,699), pygame.Rect(561,699,128,90)))

    if num in [5,20,30,40]:
        if s.game.left.status == False:
            p = [255,685]
            dirty_rects.append(screen.blit(left_cap, p))
    if num in [0,10,25,35,45]:
        if s.game.right.status == False:
            p = [398,686]
            dirty_rects.append(screen.blit(right_cap, p))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [30,700]
            dirty_rects.append(screen.blit(selection, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [30,820]
            dirty_rects.append(screen.blit(selection, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection or s.game.hold3.status == False:
            p = [162,820]
            dirty_rects.append(screen.blit(selection, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection or s.game.hold4.status == False:
            p = [292,817]
            dirty_rects.append(screen.blit(selection, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection or s.game.hold5.status == False:
            p = [427,819]
            dirty_rects.append(screen.blit(selection, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [562,820]
            dirty_rects.append(screen.blit(selection, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [561,699]
            dirty_rects.append(screen.blit(selection, p))

    pygame.display.update(dirty_rects)
    return

def star_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.purse_win.status == False:
        dirty_rects.append(screen.blit(bg_gi, (26,589), pygame.Rect(26,589,233,37)))
    if s.game.show_win.status == False:
        dirty_rects.append(screen.blit(bg_gi, (456,587), pygame.Rect(456,587,233,37)))

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (116,429), pygame.Rect(116,429,60,38)))
        dirty_rects.append(screen.blit(bg_gi, (114,469), pygame.Rect(114,469,60,38)))
        dirty_rects.append(screen.blit(bg_gi, (115,509), pygame.Rect(115,509,60,38)))
        dirty_rects.append(screen.blit(bg_gi, (115,549), pygame.Rect(115,549,60,38)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (173,428), pygame.Rect(173,428,60,38)))
        dirty_rects.append(screen.blit(bg_gi, (173,469), pygame.Rect(173,469,60,38)))
        dirty_rects.append(screen.blit(bg_gi, (173,509), pygame.Rect(173,509,60,38)))
        dirty_rects.append(screen.blit(bg_gi, (174,549), pygame.Rect(174,549,60,38)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (232,428), pygame.Rect(232,428,60,38)))
        dirty_rects.append(screen.blit(bg_gi, (232,472), pygame.Rect(232,472,60,38)))
        dirty_rects.append(screen.blit(bg_gi, (232,509), pygame.Rect(232,509,60,38)))
        dirty_rects.append(screen.blit(bg_gi, (232,547), pygame.Rect(232,547,60,38)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (289,430), pygame.Rect(289,430,60,38)))
        dirty_rects.append(screen.blit(bg_gi, (290,470), pygame.Rect(290,470,60,38)))
        dirty_rects.append(screen.blit(bg_gi, (289,510), pygame.Rect(289,510,60,38)))
        dirty_rects.append(screen.blit(bg_gi, (290,550), pygame.Rect(290,550,60,38)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (348,430), pygame.Rect(348,430,60,38)))
        dirty_rects.append(screen.blit(bg_gi, (348,470), pygame.Rect(348,470,60,38)))
        dirty_rects.append(screen.blit(bg_gi, (347,509), pygame.Rect(347,509,60,38)))
        dirty_rects.append(screen.blit(bg_gi, (347,549), pygame.Rect(347,549,60,38)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (405,430), pygame.Rect(405,430,60,38)))
        dirty_rects.append(screen.blit(bg_gi, (407,470), pygame.Rect(407,470,60,38)))
        dirty_rects.append(screen.blit(bg_gi, (406,509), pygame.Rect(406,509,60,38)))
        dirty_rects.append(screen.blit(bg_gi, (406,549), pygame.Rect(406,549,60,38)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (464,430), pygame.Rect(464,430,60,38)))
        dirty_rects.append(screen.blit(bg_gi, (464,470), pygame.Rect(464,470,60,38)))
        dirty_rects.append(screen.blit(bg_gi, (464,509), pygame.Rect(464,509,60,38)))
        dirty_rects.append(screen.blit(bg_gi, (464,549), pygame.Rect(464,549,60,38)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (522,430), pygame.Rect(522,430,60,38)))
        dirty_rects.append(screen.blit(bg_gi, (522,470), pygame.Rect(522,470,60,38)))
        dirty_rects.append(screen.blit(bg_gi, (522,509), pygame.Rect(522,509,60,38)))
        dirty_rects.append(screen.blit(bg_gi, (522,549), pygame.Rect(522,549,60,38)))
    if s.game.odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (582,430), pygame.Rect(582,430,60,38)))
        dirty_rects.append(screen.blit(bg_gi, (582,470), pygame.Rect(582,470,60,38)))
        dirty_rects.append(screen.blit(bg_gi, (582,509), pygame.Rect(582,509,60,38)))
        dirty_rects.append(screen.blit(bg_gi, (582,549), pygame.Rect(582,549,60,38)))
    if s.game.odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (641,430), pygame.Rect(641,430,60,38)))
        dirty_rects.append(screen.blit(bg_gi, (641,470), pygame.Rect(641,470,60,38)))
        dirty_rects.append(screen.blit(bg_gi, (641,509), pygame.Rect(641,509,60,38)))
        dirty_rects.append(screen.blit(bg_gi, (641,549), pygame.Rect(641,549,60,38)))

    if num in [8,10,16,18,20,22,28,35,37,40,42,46,49]:
        if s.game.purse_win.status == False:
            p = [26,589]
            dirty_rects.append(screen.blit(scores_win, p))
    if num in [2,4,17,25,32,36,41,44,48]:
        if s.game.show_win.status == False:
            p = [456,587]
            dirty_rects.append(screen.blit(scores_win, p))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [116,429]
            dirty_rects.append(screen.blit(odds, p))
            p = [114,469]
            dirty_rects.append(screen.blit(odds, p))
            p = [115,509]
            dirty_rects.append(screen.blit(odds, p))
            p = [115,549]
            dirty_rects.append(screen.blit(odds, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [173,428]
            dirty_rects.append(screen.blit(odds, p))
            p = [173,469]
            dirty_rects.append(screen.blit(odds, p))
            p = [173,509]
            dirty_rects.append(screen.blit(odds, p))
            p = [174,549]
            dirty_rects.append(screen.blit(odds, p))
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [232,428]
            dirty_rects.append(screen.blit(odds, p))
            p = [232,472]
            dirty_rects.append(screen.blit(odds, p))
            p = [232,509]
            dirty_rects.append(screen.blit(odds, p))
            p = [232,547]
            dirty_rects.append(screen.blit(odds, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [289,430]
            dirty_rects.append(screen.blit(odds, p))
            p = [290,470]
            dirty_rects.append(screen.blit(odds, p))
            p = [289,510]
            dirty_rects.append(screen.blit(odds, p))
            p = [290,550]
            dirty_rects.append(screen.blit(odds, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [348,430]
            dirty_rects.append(screen.blit(odds, p))
            p = [348,470]
            dirty_rects.append(screen.blit(odds, p))
            p = [347,509]
            dirty_rects.append(screen.blit(odds, p))
            p = [347,549]
            dirty_rects.append(screen.blit(odds, p))
    if num in [5,15,25,35,45]:
        if s.game.odds.position != 6:
            p = [405,430]
            dirty_rects.append(screen.blit(odds, p))
            p = [407,470]
            dirty_rects.append(screen.blit(odds, p))
            p = [406,509]
            dirty_rects.append(screen.blit(odds, p))
            p = [406,549]
            dirty_rects.append(screen.blit(odds, p))
    if num in [6,16,26,36,46]:
        if s.game.odds.position != 7:
            p = [464,430]
            dirty_rects.append(screen.blit(odds, p))
            p = [464,470]
            dirty_rects.append(screen.blit(odds, p))
            p = [464,509]
            dirty_rects.append(screen.blit(odds, p))
            p = [464,549]
            dirty_rects.append(screen.blit(odds, p))
    if num in [7,17,27,37,47]:
        if s.game.odds.position != 8:
            p = [522,430]
            dirty_rects.append(screen.blit(odds, p))
            p = [522,470]
            dirty_rects.append(screen.blit(odds, p))
            p = [522,509]
            dirty_rects.append(screen.blit(odds, p))
            p = [522,549]
            dirty_rects.append(screen.blit(odds, p))
    if num in [8,18,28,38,48]:
        if s.game.odds.position != 9:
            p = [582,430]
            dirty_rects.append(screen.blit(odds, p))
            p = [582,470]
            dirty_rects.append(screen.blit(odds, p))
            p = [582,509]
            dirty_rects.append(screen.blit(odds, p))
            p = [582,549]
            dirty_rects.append(screen.blit(odds, p))
    if num in [9,19,29,39,49]:
        if s.game.odds.position != 10:
            p = [641,430]
            dirty_rects.append(screen.blit(odds, p))
            p = [641,470]
            dirty_rects.append(screen.blit(odds, p))
            p = [641,509]
            dirty_rects.append(screen.blit(odds, p))
            p = [641,549]
            dirty_rects.append(screen.blit(odds, p))

    pygame.display.update(dirty_rects)
    return

