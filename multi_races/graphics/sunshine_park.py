import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

all_double = pygame.image.load('sunshine_park/assets/all_double.png').convert_alpha()
arrow = pygame.image.load('sunshine_park/assets/arrow.png').convert_alpha()
ball_count = pygame.image.load('sunshine_park/assets/ball_count.png').convert_alpha()
button = pygame.image.load('sunshine_park/assets/button.png').convert_alpha()
double_letter = pygame.image.load('sunshine_park/assets/double_letter.png').convert_alpha()
extra_ball = pygame.image.load('sunshine_park/assets/extra_ball.png').convert_alpha()
feature = pygame.image.load('sunshine_park/assets/feature.png').convert_alpha()
held1 = pygame.image.load('sunshine_park/assets/held1.png').convert_alpha()
held2 = pygame.image.load('sunshine_park/assets/held2.png').convert_alpha()
held3 = pygame.image.load('sunshine_park/assets/held3.png').convert_alpha()
held4 = pygame.image.load('sunshine_park/assets/held4.png').convert_alpha()
held5 = pygame.image.load('sunshine_park/assets/held5.png').convert_alpha()
held6 = pygame.image.load('sunshine_park/assets/held6.png').convert_alpha()
held7 = pygame.image.load('sunshine_park/assets/held7.png').convert_alpha()
left_cap = pygame.image.load('sunshine_park/assets/left_cap.png').convert_alpha()
left_win = pygame.image.load('sunshine_park/assets/left_win.png').convert_alpha()
odds = pygame.image.load('sunshine_park/assets/odds.png').convert_alpha()
place = pygame.image.load('sunshine_park/assets/place.png').convert_alpha()
purse = pygame.image.load('sunshine_park/assets/purse.png').convert_alpha()
right_cap = pygame.image.load('sunshine_park/assets/right_cap.png').convert_alpha()
right_win = pygame.image.load('sunshine_park/assets/right_win.png').convert_alpha()
section = pygame.image.load('sunshine_park/assets/section.png').convert_alpha()
selection1 = pygame.image.load('sunshine_park/assets/selection1.png').convert_alpha()
selection2 = pygame.image.load('sunshine_park/assets/selection2.png').convert_alpha()
selection3 = pygame.image.load('sunshine_park/assets/selection3.png').convert_alpha()
selection4 = pygame.image.load('sunshine_park/assets/selection4.png').convert_alpha()
selection5 = pygame.image.load('sunshine_park/assets/selection5.png').convert_alpha()
selection6 = pygame.image.load('sunshine_park/assets/selection6.png').convert_alpha()
selection7 = pygame.image.load('sunshine_park/assets/selection7.png').convert_alpha()
show = pygame.image.load('sunshine_park/assets/show.png').convert_alpha()
wild = pygame.image.load('sunshine_park/assets/wild.png').convert_alpha()
win = pygame.image.load('sunshine_park/assets/win.png').convert_alpha()
meter = pygame.image.load('graphics/assets/register_cover.png').convert_alpha()
tilt = pygame.image.load('sunshine_park/assets/tilt.png').convert_alpha()
bg_menu = pygame.image.load('sunshine_park/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('sunshine_park/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('sunshine_park/assets/backglass_off.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

reel1 = scorereel([372,341], "graphics/assets/green_reel.png")
reel10 = scorereel([344,341], "graphics/assets/green_reel.png")
reel100 = scorereel([312,341], "graphics/assets/green_reel_zero.png")

def display(s, replays=0, menu=False):
    global screen
    meter_position = [298,328]

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
            p = [56,616]
            screen.blit(selection1, p)
        if 2 in s.game.selection or s.game.fan.status == True:
            p = [52,766]
            screen.blit(selection2, p)
        if 3 in s.game.selection or s.game.fan.status == True:
            p = [204,788]
            screen.blit(selection3, p)
        if 4 in s.game.selection or s.game.fan.status == True:
            p = [326,814]
            screen.blit(selection4, p)
        if 5 in s.game.selection or s.game.fan.status == True:
            p = [455,785]
            screen.blit(selection5, p)
        if 6 in s.game.selection or s.game.fan.status == True:
            p = [603,762]
            screen.blit(selection6, p)
        if 7 in s.game.selection or s.game.fan.status == True:
            p = [612,610]
            screen.blit(selection7, p)

        if s.game.lettera.status == True:
            p = [28,321]
            screen.blit(double_letter, p)
        if s.game.letterb.status == True:
            p = [61,321]
            screen.blit(double_letter, p)
        if s.game.letterc.status == True:
            p = [96,322]
            screen.blit(double_letter, p)
        if s.game.letterd.status == True:
            p = [128,320]
            screen.blit(double_letter, p)
        if s.game.abcd.status == True:
            p = [33,355]
            screen.blit(all_double, p)
        if s.game.clover.status == True:
            p = [338,668]
            screen.blit(button, p)
        if s.game.horseshoe.status == True:
            p = [336,737]
            screen.blit(button, p)
        if s.game.star.status == True:
            p = [336,600]
            screen.blit(button, p)
        if s.game.left.status == True:
            p = [257,734]
            screen.blit(left_cap, p)
        if s.game.right.status == True:
            p = [398,733]
            screen.blit(right_cap, p)
        if s.game.purse_double.status == True:
            p = [154,671]
            screen.blit(left_win, p)
        if s.game.show_double.status == True:
            p = [390,672]
            screen.blit(right_win, p)
        if s.game.purse_win.status == True:
            p = [140,602]
            screen.blit(left_win, p)
        if s.game.show_win.status == True:
            p = [388,604]
            screen.blit(right_win, p)
        if s.game.pennant.status == True:
            p = [624,324]
            screen.blit(feature, p)
      
        #Odds displays always shown unless tilted
        p = [14,404]
        screen.blit(section, p)

        if s.game.odds.position == 1:
            p = [110,405]
            screen.blit(odds, p)
        if s.game.odds.position == 2:
            p = [166,404]
            screen.blit(odds, p)
        if s.game.odds.position == 3:
            p = [228,404]
            screen.blit(odds, p)
        if s.game.odds.position == 4:
            p = [291,402]
            screen.blit(odds, p)
        if s.game.odds.position == 5:
            p = [348,402]
            screen.blit(odds, p)
        if s.game.odds.position == 6:
            p = [410,402]
            screen.blit(odds, p)
        if s.game.odds.position == 7:
            p = [470,401]
            screen.blit(odds, p)
        if s.game.odds.position == 8:
            p = [530,402]
            screen.blit(odds, p)
        if s.game.odds.position == 9:
            p = [591,400]
            screen.blit(odds, p)
        if s.game.odds.position == 10:
            p = [654,400]
            screen.blit(odds, p)
        if s.game.wild.position in range(0,5):
            p = [33,962]
            screen.blit(wild, p)
        if s.game.wild.position in range(5,10):
            p = [164,964]
            screen.blit(purse, p)
        if s.game.wild.position in range(10,14):
            p = [316,964]
            screen.blit(show, p)
        if s.game.wild.position in range(14,19):
            p = [440,964]
            screen.blit(place, p)
        if s.game.wild.position in range(19,22):
            p = [592,960]
            screen.blit(win, p)

        if s.game.wild.position == 1:
            p = [45,938]
            screen.blit(arrow, p)
        if s.game.wild.position == 2:
            p = [76,938]
            screen.blit(arrow, p)
        if s.game.wild.position == 3:
            p = [106,940]
            screen.blit(arrow, p)
        if s.game.wild.position == 4:
            p = [135,938]
            screen.blit(arrow, p)
        if s.game.wild.position == 5:
            p = [170,938]
            screen.blit(arrow, p)
        if s.game.wild.position == 6:
            p = [200,938]
            screen.blit(arrow, p)
        if s.game.wild.position == 7:
            p = [230,938]
            screen.blit(arrow, p)
        if s.game.wild.position == 8:
            p = [259,938]
            screen.blit(arrow, p)
        if s.game.wild.position == 9:
            p = [290,938]
            screen.blit(arrow, p)
        if s.game.wild.position == 10:
            p = [323,938]
            screen.blit(arrow, p)
        if s.game.wild.position == 11:
            p = [352,938]
            screen.blit(arrow, p)
        if s.game.wild.position == 12:
            p = [382,938]
            screen.blit(arrow, p)
        if s.game.wild.position == 13:
            p = [413,937]
            screen.blit(arrow, p)
        if s.game.wild.position == 14:
            p = [445,938]
            screen.blit(arrow, p)
        if s.game.wild.position == 15:
            p = [476,937]
            screen.blit(arrow, p)
        if s.game.wild.position == 16:
            p = [506,938]
            screen.blit(arrow, p)
        if s.game.wild.position == 17:
            p = [535,938]
            screen.blit(arrow, p)
        if s.game.wild.position == 18:
            p = [565,937]
            screen.blit(arrow, p)
        if s.game.wild.position == 19:
            p = [600,937]
            screen.blit(arrow, p)
        if s.game.wild.position == 20:
            p = [628,936]
            screen.blit(arrow, p)
        if s.game.wild.position == 21:
            p = [659,937]
            screen.blit(arrow, p)

        if s.game.fan.status == True:
            p = [86,711]
            screen.blit(held1, p)
            p = [88,857]
            screen.blit(held2, p)
            p = [586,701]
            screen.blit(held6, p)
            p = [582,852]
            screen.blit(held7, p)
        if s.game.hold3.status == True or s.game.fan.status == True:
            p = [215,889]
            screen.blit(held3, p)
        if s.game.hold4.status == True or s.game.fan.status == True:
            p = [336,906]
            screen.blit(held4, p)
        if s.game.hold5.status == True or s.game.fan.status == True:
            p = [448,887]
            screen.blit(held5, p)
           
        if s.game.eb_play.status == True:
            p = [42,1012]
            screen.blit(extra_ball, p)

        if s.game.ball_count.position == 1:
            p = [479,1012]
            screen.blit(ball_count, p)
        if s.game.ball_count.position == 2:
            p = [522,1012]
            screen.blit(ball_count, p)
        if s.game.ball_count.position == 3:
            p = [562,1014]
            screen.blit(ball_count, p)
        if s.game.ball_count.position == 4:
            p = [604,1012]
            screen.blit(ball_count, p)
        if s.game.ball_count.position == 5:
            p = [644,1012]
            screen.blit(ball_count, p)

    if s.game.tilt.status == True:
        tilt_position = [658,236]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def clover_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]
    
    if s.game.purse_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (154,671), pygame.Rect(154,671,189,55)))
    if s.game.show_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (390,672), pygame.Rect(390,672,189,55)))

    if num in [3,15,22,34]:
        p = [154,671]
        dirty_rects.append(screen.blit(left_win, p))

    if num in [8,19,27,39]:
        p = [390,672]
        dirty_rects.append(screen.blit(right_win, p))

    pygame.display.update(dirty_rects)
    return

def feature_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.pennant.status == False:
        dirty_rects.append(screen.blit(bg_gi, (624,324), pygame.Rect(624,324,67,37)))
   
    if num in [7,25,32,44]:
        if s.game.pennant.status == False:
            p = [624,324]
            dirty_rects.append(screen.blit(feature, p))

    pygame.display.update(dirty_rects)
    return

def selection_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]
 
    if s.game.left.status == False:
        dirty_rects.append(screen.blit(bg_gi, (257,734), pygame.Rect(257,734,72,52)))
    if s.game.right.status == False:
        dirty_rects.append(screen.blit(bg_gi, (398,733), pygame.Rect(398,733,70,50)))

        if 1 in s.game.selection or s.game.fan.status == True:
            p = [56,616]
            screen.blit(selection1, p)
        if 2 in s.game.selection or s.game.fan.status == True:
            p = [52,766]
            screen.blit(selection2, p)
        if 3 in s.game.selection or s.game.fan.status == True:
            p = [204,788]
            screen.blit(selection3, p)
        if 4 in s.game.selection or s.game.fan.status == True:
            p = [326,814]
            screen.blit(selection4, p)
        if 5 in s.game.selection or s.game.fan.status == True:
            p = [455,785]
            screen.blit(selection5, p)
        if 6 in s.game.selection or s.game.fan.status == True:
            p = [603,762]
            screen.blit(selection6, p)
        if 7 in s.game.selection or s.game.fan.status == True:
            p = [612,610]
            screen.blit(selection7, p)

    if num in [5,20,30,40]:
        if s.game.left.status == False:
            p = [257,734]
            dirty_rects.append(screen.blit(left_cap, p))
    if num in [0,10,25,35,45]:
        if s.game.right.status == False:
            p = [398,733]
            dirty_rects.append(screen.blit(right_cap, p))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [56,616]
            dirty_rects.append(screen.blit(selection1, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [52,766]
            dirty_rects.append(screen.blit(selection2, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection or s.game.hold3.status == False:
            p = [204,788]
            dirty_rects.append(screen.blit(selection3, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection or s.game.hold4.status == False:
            p = [326,814]
            dirty_rects.append(screen.blit(selection4, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection or s.game.hold5.status == False:
            p = [455,785]
            dirty_rects.append(screen.blit(selection5, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [603,762]
            dirty_rects.append(screen.blit(selection6, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [612,610]
            dirty_rects.append(screen.blit(selection7, p))

    pygame.display.update(dirty_rects)
    return

def star_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.purse_win.status == False:
        dirty_rects.append(screen.blit(bg_gi, (140,602), pygame.Rect(140,602,189,55)))
    if s.game.show_win.status == False:
        dirty_rects.append(screen.blit(bg_gi, (388,604), pygame.Rect(388,604,199,51)))


    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (110,405), pygame.Rect(110,405,59,188)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (166,404), pygame.Rect(166,404,59,188)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (228,404), pygame.Rect(228,404,59,188)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (291,402), pygame.Rect(291,402,59,188)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (348,402), pygame.Rect(348,402,59,188)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (410,402), pygame.Rect(410,402,59,188)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (470,401), pygame.Rect(470,401,59,188)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (530,402), pygame.Rect(530,402,59,188)))
    if s.game.odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (591,400), pygame.Rect(591,400,59,188)))
    if s.game.odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (654,400), pygame.Rect(654,400,59,188)))

    if num in [8,10,16,18,20,22,28,35,37,40,42,46,49]:
        if s.game.purse_win.status == False:
            p = [140,602]
            dirty_rects.append(screen.blit(left_win, p))
    if num in [2,4,17,25,32,36,41,44,48]:
        if s.game.show_win.status == False:
            p = [388,604]
            dirty_rects.append(screen.blit(right_win, p))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [110,405]
            dirty_rects.append(screen.blit(odds, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [166,404]
            dirty_rects.append(screen.blit(odds, p))
    
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [228,404]
            dirty_rects.append(screen.blit(odds, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [291,402]
            dirty_rects.append(screen.blit(odds, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [348,402]
            dirty_rects.append(screen.blit(odds, p))
    if num in [5,15,25,35,45]:
        if s.game.odds.position != 6:
            p = [410,402]
            dirty_rects.append(screen.blit(odds, p))
    if num in [6,16,26,36,46]:
        if s.game.odds.position != 7:
            p = [470,401]
            dirty_rects.append(screen.blit(odds, p))
    if num in [7,17,27,37,47]:
        if s.game.odds.position != 8:
            p = [530,402]
            dirty_rects.append(screen.blit(odds, p))
    if num in [8,18,28,38,48]:
        if s.game.odds.position != 9:
            p = [591,400]
            dirty_rects.append(screen.blit(odds, p))
    if num in [9,19,29,39,49]:
        if s.game.odds.position != 10:
            p = [654,400]
            dirty_rects.append(screen.blit(odds, p))

    pygame.display.update(dirty_rects)
    return

