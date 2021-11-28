import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

meter = pygame.image.load('graphics/assets/register_cover.png').convert_alpha()
tilt = pygame.image.load('grandstand/assets/tilt.png').convert_alpha()
all_double = pygame.image.load('grandstand/assets/all_double.png').convert_alpha()
arrow = pygame.image.load('grandstand/assets/arrow.png').convert_alpha()
button = pygame.image.load('grandstand/assets/button.png').convert_alpha()
double_letter = pygame.image.load('grandstand/assets/double_letter.png').convert_alpha()
feature = pygame.image.load('grandstand/assets/feature.png').convert_alpha()
held = pygame.image.load('grandstand/assets/held.png').convert_alpha()
left_cap = pygame.image.load('grandstand/assets/left_cap.png').convert_alpha()
odds = pygame.image.load('grandstand/assets/odds.png').convert_alpha()
place = pygame.image.load('grandstand/assets/place.png').convert_alpha()
purse = pygame.image.load('grandstand/assets/purse.png').convert_alpha()
right_cap = pygame.image.load('grandstand/assets/right_cap.png').convert_alpha()
scores_double = pygame.image.load('grandstand/assets/scores_double.png').convert_alpha()
scores_win = pygame.image.load('grandstand/assets/scores_win.png').convert_alpha()
section = pygame.image.load('grandstand/assets/section.png').convert_alpha()
selection = pygame.image.load('grandstand/assets/selection.png').convert_alpha()
show = pygame.image.load('grandstand/assets/show.png').convert_alpha()
wild = pygame.image.load('grandstand/assets/wild.png').convert_alpha()
win = pygame.image.load('grandstand/assets/win.png').convert_alpha()
bg_menu = pygame.image.load('grandstand/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('grandstand/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('grandstand/assets/backglass_off.png').convert_alpha()

class scorereel():
    """ Score Reels are used to count replays """
    def __init__(self, pos, image):
        self.position = pos
        self.default_y = self.position[1]
        self.image = pygame.image.load(image).convert()

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
    

    if s.game.tilt.status == False:
        if 1 in s.game.selection or s.game.fan.status == True:
            p = [27,686]
            screen.blit(selection, p)
        if 2 in s.game.selection or s.game.fan.status == True:
            p = [27,834]
            screen.blit(selection, p)
        if 3 in s.game.selection or s.game.fan.status == True:
            p = [164,834]
            screen.blit(selection, p)
        if 4 in s.game.selection or s.game.fan.status == True:
            p = [304,835]
            screen.blit(selection, p)
        if 5 in s.game.selection or s.game.fan.status == True:
            p = [441,835]
            screen.blit(selection, p)
        if 6 in s.game.selection or s.game.fan.status == True:
            p = [582,835]
            screen.blit(selection, p)
        if 7 in s.game.selection or s.game.fan.status == True:
            p = [582,682]
            screen.blit(selection, p)

        if s.game.lettera.status == True:
            p = [24,333]
            screen.blit(double_letter, p)
        if s.game.letterb.status == True:
            p = [51,333]
            screen.blit(double_letter, p)
        if s.game.letterc.status == True:
            p = [79,332]
            screen.blit(double_letter, p)
        if s.game.letterd.status == True:
            p = [109,332]
            screen.blit(double_letter, p)
        if s.game.abcd.status == True:
            p = [19,362]
            screen.blit(all_double, p)
        if s.game.clover.status == True:
            p = [329,690]
            screen.blit(button, p)
        if s.game.horseshoe.status == True:
            p = [329,772]
            screen.blit(button, p)
        if s.game.star.status == True:
            p = [331,618]
            screen.blit(button, p)
        if s.game.left.status == True:
            p = [150,768]
            screen.blit(left_cap, p)
        if s.game.right.status == True:
            p = [482,770]
            screen.blit(right_cap, p)
        if s.game.purse_double.status == True:
            p = [158,686]
            screen.blit(scores_double, p)
        if s.game.show_double.status == True:
            p = [392,686]
            screen.blit(scores_double, p)
        if s.game.purse_win.status == True:
            p = [71,625]
            screen.blit(scores_win, p)
        if s.game.show_win.status == True:
            p = [392,625]
            screen.blit(scores_win, p)
        if s.game.pennant.status == True:
            p = [542,258]
            screen.blit(feature, p)
        if s.game.feature.status == True:
            p = [543,298]
            screen.blit(feature, p)
      
        #Odds displays always shown unless tilted
        p = [8,409]
        screen.blit(section, p)
        p = [8,463]
        screen.blit(section, p)
        p = [8,512]
        screen.blit(section, p)
        p = [8,563]
        screen.blit(section, p)

        if s.game.odds.position == 1:
            p = [98,410]
            screen.blit(odds, p)
            p = [98,461]
            screen.blit(odds, p)
            p = [98,511]
            screen.blit(odds, p)
            p = [98,563]
            screen.blit(odds, p)
        if s.game.odds.position == 2:
            p = [158,410]
            screen.blit(odds, p)
            p = [158,461]
            screen.blit(odds, p)
            p = [158,511]
            screen.blit(odds, p)
            p = [158,563]
            screen.blit(odds, p)
        if s.game.odds.position == 3:
            p = [219,410]
            screen.blit(odds, p)
            p = [219,461]
            screen.blit(odds, p)
            p = [219,511]
            screen.blit(odds, p)
            p = [219,563]
            screen.blit(odds, p)
        if s.game.odds.position == 4:
            p = [280,410]
            screen.blit(odds, p)
            p = [280,461]
            screen.blit(odds, p)
            p = [280,511]
            screen.blit(odds, p)
            p = [280,563]
            screen.blit(odds, p)
        if s.game.odds.position == 5:
            p = [341,410]
            screen.blit(odds, p)
            p = [341,461]
            screen.blit(odds, p)
            p = [341,511]
            screen.blit(odds, p)
            p = [341,563]
            screen.blit(odds, p)
        if s.game.odds.position == 6:
            p = [402,410]
            screen.blit(odds, p)
            p = [402,461]
            screen.blit(odds, p)
            p = [402,511]
            screen.blit(odds, p)
            p = [402,563]
            screen.blit(odds, p)
        if s.game.odds.position == 7:
            p = [464,410]
            screen.blit(odds, p)
            p = [464,461]
            screen.blit(odds, p)
            p = [464,511]
            screen.blit(odds, p)
            p = [464,563]
            screen.blit(odds, p)
        if s.game.odds.position == 8:
            p = [524,410]
            screen.blit(odds, p)
            p = [524,461]
            screen.blit(odds, p)
            p = [524,511]
            screen.blit(odds, p)
            p = [524,563]
            screen.blit(odds, p)
        if s.game.odds.position == 9:
            p = [585,410]
            screen.blit(odds, p)
            p = [585,461]
            screen.blit(odds, p)
            p = [585,511]
            screen.blit(odds, p)
            p = [585,563]
            screen.blit(odds, p)
        if s.game.odds.position == 10:
            p = [648,410]
            screen.blit(odds, p)
            p = [648,461]
            screen.blit(odds, p)
            p = [648,511]
            screen.blit(odds, p)
            p = [648,563]
            screen.blit(odds, p)
        if s.game.wild.position in range(0,5):
            p = [34,994]
            screen.blit(wild, p)
        if s.game.wild.position in range(5,10):
            p = [159,996]
            screen.blit(purse, p)
        if s.game.wild.position in range(10,14):
            p = [313,997]
            screen.blit(show, p)
        if s.game.wild.position in range(14,19):
            p = [437,997]
            screen.blit(place, p)
        if s.game.wild.position in range(19,22):
            p = [590,997]
            screen.blit(win, p)

        if s.game.wild.position == 0:
            p = [38,973]
            screen.blit(arrow, p)
        if s.game.wild.position == 1:
            p = [67,973]
            screen.blit(arrow, p)
        if s.game.wild.position == 2:
            p = [99,973]
            screen.blit(arrow, p)
        if s.game.wild.position == 3:
            p = [127,973]
            screen.blit(arrow, p)
        if s.game.wild.position == 4:
            p = [162,973]
            screen.blit(arrow, p)
        if s.game.wild.position == 5:
            p = [192,973]
            screen.blit(arrow, p)
        if s.game.wild.position == 6:
            p = [222,974]
            screen.blit(arrow, p)
        if s.game.wild.position == 7:
            p = [252,974]
            screen.blit(arrow, p)
        if s.game.wild.position == 8:
            p = [282,974]
            screen.blit(arrow, p)
        if s.game.wild.position == 9:
            p = [318,974]
            screen.blit(arrow, p)
        if s.game.wild.position == 10:
            p = [347,974]
            screen.blit(arrow, p)
        if s.game.wild.position == 11:
            p = [376,974]
            screen.blit(arrow, p)
        if s.game.wild.position == 12:
            p = [407,973]
            screen.blit(arrow, p)
        if s.game.wild.position == 13:
            p = [440,973]
            screen.blit(arrow, p)
        if s.game.wild.position == 14:
            p = [471,974]
            screen.blit(arrow, p)
        if s.game.wild.position == 15:
            p = [501,974]
            screen.blit(arrow, p)
        if s.game.wild.position == 16:
            p = [531,974]
            screen.blit(arrow, p)
        if s.game.wild.position == 17:
            p = [562,974]
            screen.blit(arrow, p)
        if s.game.wild.position == 18:
            p = [595,973]
            screen.blit(arrow, p)
        if s.game.wild.position == 19:
            p = [625,973]
            screen.blit(arrow, p)
        if s.game.wild.position == 20:
            p = [656,973]
            screen.blit(arrow, p)

        if s.game.fan.status == True:
            p = [26,780]
            screen.blit(held, p)
            p = [26,928]
            screen.blit(held, p)
            p = [581,930]
            screen.blit(held, p)
            p = [581,780]
            screen.blit(held, p)
        if s.game.hold3.status == True or s.game.fan.status == True:
            p = [164,930]
            screen.blit(held, p)
        if s.game.hold4.status == True or s.game.fan.status == True:
            p = [304,930]
            screen.blit(held, p)
        if s.game.hold5.status == True or s.game.fan.status == True:
            p = [442,930]
            screen.blit(held, p)
            
    if s.game.tilt.status == True:
        tilt_position = [652,258]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def clover_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]
    
    if s.game.purse_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (158,686), pygame.Rect(158,686,163,61)))
    if s.game.show_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (392,686), pygame.Rect(392,686,163,61)))

    if num in [3,15,22,34]:
        p = [158,686]
        dirty_rects.append(screen.blit(scores_double, p))

    if num in [8,19,27,39]:
        p = [392,686]
        dirty_rects.append(screen.blit(scores_double, p))

    pygame.display.update(dirty_rects)
    return

def feature_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.pennant.status == False:
        dirty_rects.append(screen.blit(bg_gi, (542,258), pygame.Rect(542,258,62,34)))
   
    if num in [7,25,32,44]:
        if s.game.pennant.status == False:
            p = [542,258]
            dirty_rects.append(screen.blit(feature, p))

    pygame.display.update(dirty_rects)
    return

def selection_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.left.status == False:
        dirty_rects.append(screen.blit(bg_gi, (150,768), pygame.Rect(150,768,86,55)))
    if s.game.right.status == False:
        dirty_rects.append(screen.blit(bg_gi, (482,770), pygame.Rect(482,770,84,51)))

    if 1 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (27,686), pygame.Rect(27,686,107,90)))
    if 2 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (27,834), pygame.Rect(27,834,107,90)))
    if 3 not in s.game.selection or s.game.hold3.status == False:
        dirty_rects.append(screen.blit(bg_gi, (164,834), pygame.Rect(164,834,107,90)))
    if 4 not in s.game.selection or s.game.hold4.status == False:
        dirty_rects.append(screen.blit(bg_gi, (304,835), pygame.Rect(304,835,107,90)))
    if 5 not in s.game.selection or s.game.hold5.status == False:
        dirty_rects.append(screen.blit(bg_gi, (441,835), pygame.Rect(441,835,107,90)))
    if 6 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (582,835), pygame.Rect(582,835,107,90)))
    if 7 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (582,682), pygame.Rect(582,682,107,90)))

    if num in [5,20,30,40]:
        if s.game.left.status == False:
            p = [150,768]
            dirty_rects.append(screen.blit(left_cap, p))
    if num in [0,10,25,35,45]:
        if s.game.right.status == False:
            p = [482,770]
            dirty_rects.append(screen.blit(right_cap, p))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [27,686]
            dirty_rects.append(screen.blit(selection, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [27,834]
            dirty_rects.append(screen.blit(selection, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection or s.game.hold3.status == False:
            p = [164,834]
            dirty_rects.append(screen.blit(selection, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection or s.game.hold4.status == False:
            p = [304,835]
            dirty_rects.append(screen.blit(selection, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection or s.game.hold5.status == False:
            p = [441,835]
            dirty_rects.append(screen.blit(selection, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [582,835]
            dirty_rects.append(screen.blit(selection, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [582,682]
            dirty_rects.append(screen.blit(selection, p))

    pygame.display.update(dirty_rects)
    return

def star_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.purse_win.status == False:
        dirty_rects.append(screen.blit(bg_gi, (71,625), pygame.Rect(71,625,247,39)))
    if s.game.show_win.status == False:
        dirty_rects.append(screen.blit(bg_gi, (392,625), pygame.Rect(392,625,247,39)))

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (98,410), pygame.Rect(98,410,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (98,461), pygame.Rect(98,461,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (98,511), pygame.Rect(98,511,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (98,563), pygame.Rect(98,563,61,49)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (158,410), pygame.Rect(158,410,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (158,461), pygame.Rect(158,461,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (158,511), pygame.Rect(158,511,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (158,563), pygame.Rect(158,563,61,49)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (219,410), pygame.Rect(219,410,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (219,461), pygame.Rect(219,461,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (219,511), pygame.Rect(219,511,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (219,563), pygame.Rect(219,563,61,49)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (280,410), pygame.Rect(280,410,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (280,461), pygame.Rect(280,461,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (280,511), pygame.Rect(280,511,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (280,563), pygame.Rect(280,563,61,49)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (341,410), pygame.Rect(341,410,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (341,461), pygame.Rect(341,461,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (341,511), pygame.Rect(341,511,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (341,563), pygame.Rect(341,563,61,49)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (402,410), pygame.Rect(402,410,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (402,461), pygame.Rect(402,461,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (402,511), pygame.Rect(402,511,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (402,563), pygame.Rect(402,563,61,49)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (464,410), pygame.Rect(464,410,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (464,461), pygame.Rect(464,461,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (464,511), pygame.Rect(464,511,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (464,563), pygame.Rect(464,563,61,49)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (524,410), pygame.Rect(524,410,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (524,461), pygame.Rect(524,461,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (524,511), pygame.Rect(524,511,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (524,563), pygame.Rect(524,563,61,49)))
    if s.game.odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (585,410), pygame.Rect(585,410,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (585,461), pygame.Rect(585,461,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (585,511), pygame.Rect(585,511,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (585,563), pygame.Rect(585,563,61,49)))
    if s.game.odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (648,410), pygame.Rect(648,410,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (648,461), pygame.Rect(648,461,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (648,511), pygame.Rect(648,511,61,49)))
        dirty_rects.append(screen.blit(bg_gi, (648,563), pygame.Rect(648,563,61,49)))

    if num in [8,10,16,18,20,22,28,35,37,40,42,46,49]:
        if s.game.purse_win.status == False:
            p = [71,625]
            dirty_rects.append(screen.blit(scores_win, p))
    if num in [2,4,17,25,32,36,41,44,48]:
        if s.game.show_win.status == False:
            p = [392,625]
            dirty_rects.append(screen.blit(scores_win, p))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [98,410]
            dirty_rects.append(screen.blit(odds, p))
            p = [98,461]
            dirty_rects.append(screen.blit(odds, p))
            p = [98,511]
            dirty_rects.append(screen.blit(odds, p))
            p = [98,563]
            dirty_rects.append(screen.blit(odds, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [158,410]
            dirty_rects.append(screen.blit(odds, p))
            p = [158,461]
            dirty_rects.append(screen.blit(odds, p))
            p = [158,511]
            dirty_rects.append(screen.blit(odds, p))
            p = [158,563]
            dirty_rects.append(screen.blit(odds, p))
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [219,410]
            dirty_rects.append(screen.blit(odds, p))
            p = [219,461]
            dirty_rects.append(screen.blit(odds, p))
            p = [219,511]
            dirty_rects.append(screen.blit(odds, p))
            p = [219,563]
            dirty_rects.append(screen.blit(odds, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [280,410]
            dirty_rects.append(screen.blit(odds, p))
            p = [280,461]
            dirty_rects.append(screen.blit(odds, p))
            p = [280,511]
            dirty_rects.append(screen.blit(odds, p))
            p = [280,563]
            dirty_rects.append(screen.blit(odds, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [341,410]
            dirty_rects.append(screen.blit(odds, p))
            p = [341,461]
            dirty_rects.append(screen.blit(odds, p))
            p = [341,511]
            dirty_rects.append(screen.blit(odds, p))
            p = [341,563]
            dirty_rects.append(screen.blit(odds, p))
    if num in [5,15,25,35,45]:
        if s.game.odds.position != 6:
            p = [402,410]
            dirty_rects.append(screen.blit(odds, p))
            p = [402,461]
            dirty_rects.append(screen.blit(odds, p))
            p = [402,511]
            dirty_rects.append(screen.blit(odds, p))
            p = [402,563]
            dirty_rects.append(screen.blit(odds, p))
    if num in [6,16,26,36,46]:
        if s.game.odds.position != 7:
            p = [464,410]
            dirty_rects.append(screen.blit(odds, p))
            p = [464,461]
            dirty_rects.append(screen.blit(odds, p))
            p = [464,511]
            dirty_rects.append(screen.blit(odds, p))
            p = [464,563]
            dirty_rects.append(screen.blit(odds, p))
    if num in [7,17,27,37,47]:
        if s.game.odds.position != 8:
            p = [524,410]
            dirty_rects.append(screen.blit(odds, p))
            p = [524,461]
            dirty_rects.append(screen.blit(odds, p))
            p = [524,511]
            dirty_rects.append(screen.blit(odds, p))
            p = [524,563]
            dirty_rects.append(screen.blit(odds, p))
    if num in [8,18,28,38,48]:
        if s.game.odds.position != 9:
            p = [585,410]
            dirty_rects.append(screen.blit(odds, p))
            p = [585,461]
            dirty_rects.append(screen.blit(odds, p))
            p = [585,511]
            dirty_rects.append(screen.blit(odds, p))
            p = [585,563]
            dirty_rects.append(screen.blit(odds, p))
    if num in [9,19,29,39,49]:
        if s.game.odds.position != 10:
            p = [648,410]
            dirty_rects.append(screen.blit(odds, p))
            p = [648,461]
            dirty_rects.append(screen.blit(odds, p))
            p = [648,511]
            dirty_rects.append(screen.blit(odds, p))
            p = [648,563]
            dirty_rects.append(screen.blit(odds, p))

    pygame.display.update(dirty_rects)
    return

