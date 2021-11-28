import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

tilt = pygame.image.load('citation/assets/tilt.png').convert_alpha()
button = pygame.image.load('citation/assets/button.png').convert_alpha()
left_cap = pygame.image.load('citation/assets/left.png').convert_alpha()
odds = pygame.image.load('citation/assets/odds.png').convert_alpha()
right_cap = pygame.image.load('citation/assets/right.png').convert_alpha()
scores_win = pygame.image.load('citation/assets/scores_win.png').convert_alpha()
section = pygame.image.load('citation/assets/section.png').convert_alpha()
selection = pygame.image.load('citation/assets/selection.png').convert_alpha()
cit = pygame.image.load('citation/assets/cit.png').convert_alpha()
letter_a = pygame.image.load('citation/assets/letter_a.png').convert_alpha()
letter_t = pygame.image.load('citation/assets/letter_t.png').convert_alpha()
letter_i = pygame.image.load('citation/assets/letter_i.png').convert_alpha()
letter_o = pygame.image.load('citation/assets/letter_o.png').convert_alpha()
letter_n = pygame.image.load('citation/assets/letter_n.png').convert_alpha()
bg_menu = pygame.image.load('citation/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('citation/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('citation/assets/backglass_off.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert_alpha()

reel1 = scorereel([494,371], "graphics/assets/transparent_reel.png")
reel10 = scorereel([484,371], "graphics/assets/transparent_reel.png")
reel100 = scorereel([474,371], "graphics/assets/transparent_reel.png")


def display(s, replays=0, menu=False):
    global screen
    meter_position = [300,350]

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
        reel1.position[0] = 484
    elif s.game.replays < 100 and s.game.replays > 10:
        reel1.position[0] = 489
    else:
        reel1.position[0] = 494
    screen.blit(reel1.image, reel1.position)
    if s.game.replays > 9 and s.game.replays < 100:
        reel10.position[0] = 479
        screen.blit(reel10.image, reel10.position)
    elif s.game.replays > 100:
        reel10.position[0] = 484
        screen.blit(reel10.image, reel10.position)
    if s.game.replays > 99:
        screen.blit(reel100.image, reel100.position)
   
    screen.blit(bg_gi, (474,401), pygame.Rect(474,401,44,337))
    screen.blit(bg_gi, (474,0), pygame.Rect(474,0,44,360))

    p = [141,258]
    screen.blit(cit, p)
    if s.game.name.position >= 1:
        p = [316,282]
        screen.blit(letter_a, p)
    if s.game.name.position >= 2:
        p = [382,280]
        screen.blit(letter_t, p)
    if s.game.name.position >= 3:
        p = [449,274]
        screen.blit(letter_i, p)
    if s.game.name.position >= 4:
        p = [501,268]
        screen.blit(letter_o, p)
    if s.game.name.position >= 5:
        p = [560,258]
        screen.blit(letter_n, p)

    if s.game.tilt.status == False:

        if 1 in s.game.selection or s.game.fan.status == True:
            p = [15,680]
            screen.blit(selection, p)
        if 2 in s.game.selection or s.game.fan.status == True:
            p = [18,836]
            screen.blit(selection, p)
        if 3 in s.game.selection or s.game.fan.status == True:
            p = [153,836]
            screen.blit(selection, p)
        if 4 in s.game.selection or s.game.fan.status == True:
            p = [295,838]
            screen.blit(selection, p)
        if 5 in s.game.selection or s.game.fan.status == True:
            p = [435,837]
            screen.blit(selection, p)
        if 6 in s.game.selection or s.game.fan.status == True:
            p = [573,838]
            screen.blit(selection, p)
        if 7 in s.game.selection or s.game.fan.status == True:
            p = [576,684]
            screen.blit(selection, p)

        if s.game.horseshoe.status == True:
            p = [334,676]
            screen.blit(button, p)
        if s.game.left.status == True:
            p = [177,685]
            screen.blit(left_cap, p)
        if s.game.right.status == True:
            p = [492,686]
            screen.blit(right_cap, p)
        if s.game.purse_win.status == True:
            p = [200,779]
            screen.blit(scores_win, p)
        if s.game.show_win.status == True:
            p = [200,742]
            screen.blit(scores_win, p)
      
        #Odds displays always shown unless tilted
        p = [14,444]
        screen.blit(section, p)

        if s.game.odds.position == 1:
            p = [108,442]
            screen.blit(odds, p)
        if s.game.odds.position == 2:
            p = [168,442]
            screen.blit(odds, p)
        if s.game.odds.position == 3:
            p = [228,442]
            screen.blit(odds, p)
        if s.game.odds.position == 4:
            p = [289,442]
            screen.blit(odds, p)
        if s.game.odds.position == 5:
            p = [351,442]
            screen.blit(odds, p)
        if s.game.odds.position == 6:
            p = [412,442]
            screen.blit(odds, p)
        if s.game.odds.position == 7:
            p = [472,442]
            screen.blit(odds, p)
        if s.game.odds.position == 8:
            p = [532,442]
            screen.blit(odds, p)
        if s.game.odds.position == 9:
            p = [593,442]
            screen.blit(odds, p)
        if s.game.odds.position == 10:
            p = [654,445]
            screen.blit(odds, p)

    if s.game.tilt.status == True:
        tilt_position = [184,368]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def clover_animation(args):
    return

def feature_animation(args):
    return

def selection_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.left.status == False:
        dirty_rects.append(screen.blit(bg_gi, (177,685), pygame.Rect(177,685,58,40)))
    if s.game.right.status == False:
        dirty_rects.append(screen.blit(bg_gi, (492,686), pygame.Rect(492,686,56,39)))

    if 1 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (15,680), pygame.Rect(15,680,131,143)))
    if 2 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (18,836), pygame.Rect(18,836,131,143)))
    if 3 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (153,836), pygame.Rect(153,836,131,143)))
    if 4 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (295,838), pygame.Rect(295,838,131,143)))
    if 5 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (435,837), pygame.Rect(435,837,131,143)))
    if 6 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (573,838), pygame.Rect(573,838,131,143)))
    if 7 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (576,684), pygame.Rect(576,684,131,143)))

    if num in [5,20,30,40]:
        if s.game.left.status == False:
            p = [177,685]
            dirty_rects.append(screen.blit(left_cap, p))
    if num in [0,10,25,35,45]:
        if s.game.right.status == False:
            p = [492,686]
            dirty_rects.append(screen.blit(right_cap, p))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [15,680]
            dirty_rects.append(screen.blit(selection, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [18,836]
            dirty_rects.append(screen.blit(selection, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection:
            p = [153,836]
            dirty_rects.append(screen.blit(selection, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection:
            p = [295,838]
            dirty_rects.append(screen.blit(selection, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection:
            p = [435,837]
            dirty_rects.append(screen.blit(selection, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [573,838]
            dirty_rects.append(screen.blit(selection, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [576,684]
            dirty_rects.append(screen.blit(selection, p))

    pygame.display.update(dirty_rects)
    return

def star_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]


    if s.game.purse_win.status == False:
        dirty_rects.append(screen.blit(bg_gi, (200,779), pygame.Rect(200,779,326,50)))
    if s.game.show_win.status == False:
        dirty_rects.append(screen.blit(bg_gi, (200,742), pygame.Rect(200,742,326,50)))

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (108,442), pygame.Rect(108,442,60,223)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (168,442), pygame.Rect(168,442,60,223)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (228,442), pygame.Rect(228,442,60,223)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (289,442), pygame.Rect(289,442,60,223)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (351,442), pygame.Rect(351,442,60,223)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (412,442), pygame.Rect(412,442,60,223)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (472,442), pygame.Rect(472,442,60,223)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (532,442), pygame.Rect(532,442,60,223)))
    if s.game.odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (593,442), pygame.Rect(593,442,60,223)))
    if s.game.odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (654,445), pygame.Rect(654,445,60,223)))

    if num in [8,10,16,18,20,22,28,35,37,40,42,46,49]:
        if s.game.purse_win.status == False:
            p = [200,779]
            dirty_rects.append(screen.blit(scores_win, p))
    if num in [2,4,17,25,32,36,41,44,48]:
        if s.game.show_win.status == False:
            p = [200,742]
            dirty_rects.append(screen.blit(scores_win, p))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [108,442]
            dirty_rects.append(screen.blit(odds, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [168,442]
            dirty_rects.append(screen.blit(odds, p))
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [228,442]
            dirty_rects.append(screen.blit(odds, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [289,442]
            dirty_rects.append(screen.blit(odds, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [351,442]
            dirty_rects.append(screen.blit(odds, p))
    if num in [5,15,25,35,45]:
        if s.game.odds.position != 6:
            p = [412,442]
            dirty_rects.append(screen.blit(odds, p))
    if num in [6,16,26,36,46]:
        if s.game.odds.position != 7:
            p = [472,442]
            dirty_rects.append(screen.blit(odds, p))
    if num in [7,17,27,37,47]:
        if s.game.odds.position != 8:
            p = [532,442]
            dirty_rects.append(screen.blit(odds, p))
    if num in [8,18,28,38,48]:
        if s.game.odds.position != 9:
            p = [593,442]
            dirty_rects.append(screen.blit(odds, p))
    if num in [9,19,29,39,49]:
        if s.game.odds.position != 10:
            p = [654,445]
            dirty_rects.append(screen.blit(odds, p))

    pygame.display.update(dirty_rects)
    return

