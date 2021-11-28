import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

tilt = pygame.image.load('new_daily_races/assets/tilt.png').convert_alpha()
feature = pygame.image.load('new_daily_races/assets/feature.png').convert_alpha()
races1 = pygame.image.load('new_daily_races/assets/races1.png').convert_alpha()
races2 = pygame.image.load('new_daily_races/assets/races2.png').convert_alpha()
races3 = pygame.image.load('new_daily_races/assets/races3.png').convert_alpha()
races4 = pygame.image.load('new_daily_races/assets/races4.png').convert_alpha()
races5 = pygame.image.load('new_daily_races/assets/races5.png').convert_alpha()
a = pygame.image.load('new_daily_races/assets/a.png').convert_alpha()
b = pygame.image.load('new_daily_races/assets/b.png').convert_alpha()
c = pygame.image.load('new_daily_races/assets/c.png').convert_alpha()
d = pygame.image.load('new_daily_races/assets/d.png').convert_alpha()
paddock = pygame.image.load('new_daily_races/assets/paddock.png').convert_alpha()
multiple = pygame.image.load('new_daily_races/assets/multiple.png').convert_alpha()
odds = pygame.image.load('new_daily_races/assets/odds.png').convert_alpha()
section = pygame.image.load('new_daily_races/assets/section.png').convert_alpha()
selection = pygame.image.load('new_daily_races/assets/selection.png').convert_alpha()
bg_menu = pygame.image.load('new_daily_races/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('new_daily_races/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('new_daily_races/assets/backglass_off.png').convert_alpha()


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
        p = [368,310]
        screen.blit(races1, p)
    if s.game.name.position >= 2:
        p = [430,320]
        screen.blit(races2, p)
    if s.game.name.position >= 3:
        p = [492,329]
        screen.blit(races3, p)
    if s.game.name.position >= 4:
        p = [550,344]
        screen.blit(races4, p)
    if s.game.name.position >= 5:
        p = [604,368]
        screen.blit(races5, p)

   

    if s.game.tilt.status == False:
        if 1 in s.game.selection:
            p = [8,572]
            screen.blit(selection, p)
        if 2 in s.game.selection:
            p = [8,749]
            screen.blit(selection, p)
        if 3 in s.game.selection:
            p = [153,814]
            screen.blit(selection, p)
        if 4 in s.game.selection:
            p = [295,836]
            screen.blit(selection, p)
        if 5 in s.game.selection:
            p = [439,818]
            screen.blit(selection, p)
        if 6 in s.game.selection:
            p = [586,754]
            screen.blit(selection, p)
        if 7 in s.game.selection:
            p = [590,581]
            screen.blit(selection, p)

        p = [146,476]
        screen.blit(section, p)
        p = [146,536]
        screen.blit(section, p)
        p = [146,594]
        screen.blit(section, p)
        p = [146,650]
        screen.blit(section, p)
        if s.game.odds.position == 1:
            p = [521,476]
            screen.blit(odds, p)
            p = [521,536]
            screen.blit(odds, p)
            p = [521,594]
            screen.blit(odds, p)
            p = [521,652]
            screen.blit(odds, p)
        if s.game.odds.position == 2:
            p = [456,476]
            screen.blit(odds, p)
            p = [456,536]
            screen.blit(odds, p)
            p = [456,594]
            screen.blit(odds, p)
            p = [456,652]
            screen.blit(odds, p)
        if s.game.odds.position == 3:
            p = [393,476]
            screen.blit(odds, p)
            p = [393,536]
            screen.blit(odds, p)
            p = [393,594]
            screen.blit(odds, p)
            p = [393,652]
            screen.blit(odds, p)
        if s.game.odds.position == 4:
            p = [330,476]
            screen.blit(odds, p)
            p = [330,536]
            screen.blit(odds, p)
            p = [330,594]
            screen.blit(odds, p)
            p = [330,652]
            screen.blit(odds, p)
        if s.game.odds.position == 5:
            p = [266,476]
            screen.blit(odds, p)
            p = [266,536]
            screen.blit(odds, p)
            p = [266,594]
            screen.blit(odds, p)
            p = [266,652]
            screen.blit(odds, p)

        if s.game.pennant.status == True:
            p = [7,533]
            screen.blit(feature, p)
        if s.game.left.status == True:
            p = [10,296]
            screen.blit(paddock, p)
        if s.game.right.status == True:
            p = [650,296]
            screen.blit(paddock, p)

        if s.game.coin.position == 1:
            p = [255,410]
            screen.blit(multiple, p)
        if s.game.coin.position == 2:
            p = [312,410]
            screen.blit(multiple, p)
        if s.game.coin.position == 3:
            p = [368,410]
            screen.blit(multiple, p)
        if s.game.coin.position == 4:
            p = [425,410]
            screen.blit(multiple, p)

        if s.game.lettera.status == True:
            p = [30,468]
            screen.blit(a, p)
        if s.game.letterb.status == True:
            p = [84,468]
            screen.blit(b, p)
        if s.game.letterc.status == True:
            p = [606,468]
            screen.blit(c, p)
        if s.game.letterd.status == True:
            p = [663,468]
            screen.blit(d, p)

    if s.game.tilt.status == True:
        tilt_position = [616,536]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def selection_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.left.status == False:
        dirty_rects.append(screen.blit(bg_gi, (10,296), pygame.Rect(10,296,71,91)))
    if s.game.right.status == False:
        dirty_rects.append(screen.blit(bg_gi, (650,296), pygame.Rect(650,296,71,91)))

    if 1 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (8,572), pygame.Rect(8,572,129,154)))
    if 2 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (8,749), pygame.Rect(8,749,129,154)))
    if 3 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (153,814), pygame.Rect(153,814,129,154)))
    if 4 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (295,836), pygame.Rect(295,836,129,154)))
    if 5 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (439,818), pygame.Rect(439,818,129,154)))
    if 6 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (586,754), pygame.Rect(586,754,129,154)))
    if 7 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (590,581), pygame.Rect(590,581,129,154)))

    if num in [5,20,30,40]:
        if s.game.left.status == False:
            p = [10,296]
            dirty_rects.append(screen.blit(paddock, p))
    if num in [0,10,25,35,45]:
        if s.game.right.status == False:
            p = [650,296]
            dirty_rects.append(screen.blit(paddock, p))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [8,572]
            dirty_rects.append(screen.blit(selection, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [8,749]
            dirty_rects.append(screen.blit(selection, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection:
            p = [153,814]
            dirty_rects.append(screen.blit(selection, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection:
            p = [295,836]
            dirty_rects.append(screen.blit(selection, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection:
            p = [439,818]
            dirty_rects.append(screen.blit(selection, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [586,754]
            dirty_rects.append(screen.blit(selection, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [590,581]
            dirty_rects.append(screen.blit(selection, p))

    pygame.display.update(dirty_rects)
    return

def star_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (523,478), pygame.Rect(523,478,60,58)))
        dirty_rects.append(screen.blit(bg_gi, (523,539), pygame.Rect(523,539,60,58)))
        dirty_rects.append(screen.blit(bg_gi, (523,597), pygame.Rect(523,597,60,58)))
        dirty_rects.append(screen.blit(bg_gi, (523,653), pygame.Rect(523,653,60,58)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (458,478), pygame.Rect(458,478,60,58)))
        dirty_rects.append(screen.blit(bg_gi, (458,539), pygame.Rect(458,539,60,58)))
        dirty_rects.append(screen.blit(bg_gi, (458,597), pygame.Rect(458,597,60,58)))
        dirty_rects.append(screen.blit(bg_gi, (458,653), pygame.Rect(458,653,60,58)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (395,478), pygame.Rect(395,478,60,58)))
        dirty_rects.append(screen.blit(bg_gi, (395,539), pygame.Rect(395,539,60,58)))
        dirty_rects.append(screen.blit(bg_gi, (395,597), pygame.Rect(395,597,60,58)))
        dirty_rects.append(screen.blit(bg_gi, (395,653), pygame.Rect(395,653,60,58)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (332,478), pygame.Rect(332,478,60,58)))
        dirty_rects.append(screen.blit(bg_gi, (332,539), pygame.Rect(332,539,60,58)))
        dirty_rects.append(screen.blit(bg_gi, (332,597), pygame.Rect(332,597,60,58)))
        dirty_rects.append(screen.blit(bg_gi, (332,653), pygame.Rect(332,653,60,58)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (268,478), pygame.Rect(268,478,60,58)))
        dirty_rects.append(screen.blit(bg_gi, (268,539), pygame.Rect(268,539,60,58)))
        dirty_rects.append(screen.blit(bg_gi, (268,597), pygame.Rect(268,597,60,58)))
        dirty_rects.append(screen.blit(bg_gi, (268,653), pygame.Rect(268,653,60,58)))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [523,478]
            dirty_rects.append(screen.blit(odds, p))
            p = [523,539]
            dirty_rects.append(screen.blit(odds, p))
            p = [523,597]
            dirty_rects.append(screen.blit(odds, p))
            p = [523,653]
            dirty_rects.append(screen.blit(odds, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [458,478]
            dirty_rects.append(screen.blit(odds, p))
            p = [458,539]
            dirty_rects.append(screen.blit(odds, p))
            p = [458,597]
            dirty_rects.append(screen.blit(odds, p))
            p = [458,653]
            dirty_rects.append(screen.blit(odds, p))
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [395,478]
            dirty_rects.append(screen.blit(odds, p))
            p = [395,539]
            dirty_rects.append(screen.blit(odds, p))
            p = [395,597]
            dirty_rects.append(screen.blit(odds, p))
            p = [395,653]
            dirty_rects.append(screen.blit(odds, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [332,478]
            dirty_rects.append(screen.blit(odds, p))
            p = [332,539]
            dirty_rects.append(screen.blit(odds, p))
            p = [332,597]
            dirty_rects.append(screen.blit(odds, p))
            p = [332,653]
            dirty_rects.append(screen.blit(odds, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [268,478]
            dirty_rects.append(screen.blit(odds, p))
            p = [268,539]
            dirty_rects.append(screen.blit(odds, p))
            p = [268,597]
            dirty_rects.append(screen.blit(odds, p))
            p = [268,653]
            dirty_rects.append(screen.blit(odds, p))

    pygame.display.update(dirty_rects)
    return

