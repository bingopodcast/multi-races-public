import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

tilt = pygame.image.load('old_hilltop/assets/tilt.png').convert_alpha()
added_entries = pygame.image.load('old_hilltop/assets/added_entries.png').convert_alpha()
boot = pygame.image.load('old_hilltop/assets/boot.png').convert_alpha()
ef_large = pygame.image.load('old_hilltop/assets/ef_large.png').convert_alpha()
ef_small = pygame.image.load('old_hilltop/assets/ef_small.png').convert_alpha()
eight = pygame.image.load('old_hilltop/assets/eight.png').convert_alpha()
eighty = pygame.image.load('old_hilltop/assets/eighty.png').convert_alpha()
entry_flash = pygame.image.load('old_hilltop/assets/entry_flash.png').convert_alpha()
feature = pygame.image.load('old_hilltop/assets/feature.png').convert_alpha()
fifty = pygame.image.load('old_hilltop/assets/fifty.png').convert_alpha()
five = pygame.image.load('old_hilltop/assets/five.png').convert_alpha()
forty = pygame.image.load('old_hilltop/assets/forty.png').convert_alpha()
four = pygame.image.load('old_hilltop/assets/four.png').convert_alpha()
nine = pygame.image.load('old_hilltop/assets/nine.png').convert_alpha()
ninety = pygame.image.load('old_hilltop/assets/ninety.png').convert_alpha()
odds10 = pygame.image.load('old_hilltop/assets/odds10.png').convert_alpha()
odds1 = pygame.image.load('old_hilltop/assets/odds1.png').convert_alpha()
odds2 = pygame.image.load('old_hilltop/assets/odds2.png').convert_alpha()
odds3 = pygame.image.load('old_hilltop/assets/odds3.png').convert_alpha()
odds4 = pygame.image.load('old_hilltop/assets/odds4.png').convert_alpha()
odds5 = pygame.image.load('old_hilltop/assets/odds5.png').convert_alpha()
odds6 = pygame.image.load('old_hilltop/assets/odds6.png').convert_alpha()
odds7 = pygame.image.load('old_hilltop/assets/odds7.png').convert_alpha()
odds8 = pygame.image.load('old_hilltop/assets/odds8.png').convert_alpha()
odds9 = pygame.image.load('old_hilltop/assets/odds9.png').convert_alpha()
one_hundred = pygame.image.load('old_hilltop/assets/one_hundred.png').convert_alpha()
one = pygame.image.load('old_hilltop/assets/one.png').convert_alpha()
racehorse1 = pygame.image.load('old_hilltop/assets/racehorse1.png').convert_alpha()
racehorse2 = pygame.image.load('old_hilltop/assets/racehorse2.png').convert_alpha()
racehorse3 = pygame.image.load('old_hilltop/assets/racehorse3.png').convert_alpha()
saddle = pygame.image.load('old_hilltop/assets/saddle.png').convert_alpha()
section = pygame.image.load('old_hilltop/assets/section.png').convert_alpha()
selection1 = pygame.image.load('old_hilltop/assets/selection1.png').convert_alpha()
selection2 = pygame.image.load('old_hilltop/assets/selection2.png').convert_alpha()
selection3 = pygame.image.load('old_hilltop/assets/selection3.png').convert_alpha()
selection4 = pygame.image.load('old_hilltop/assets/selection4.png').convert_alpha()
selection5 = pygame.image.load('old_hilltop/assets/selection5.png').convert_alpha()
selection6 = pygame.image.load('old_hilltop/assets/selection6.png').convert_alpha()
selection7 = pygame.image.load('old_hilltop/assets/selection7.png').convert_alpha()
seven = pygame.image.load('old_hilltop/assets/seven.png').convert_alpha()
seventy = pygame.image.load('old_hilltop/assets/seventy.png').convert_alpha()
six = pygame.image.load('old_hilltop/assets/six.png').convert_alpha()
sixty = pygame.image.load('old_hilltop/assets/sixty.png').convert_alpha()
parlay1 = pygame.image.load('old_hilltop/assets/parlay1.png').convert_alpha()
parlay2 = pygame.image.load('old_hilltop/assets/parlay2.png').convert_alpha()
parlay3 = pygame.image.load('old_hilltop/assets/parlay3.png').convert_alpha()
parlay4 = pygame.image.load('old_hilltop/assets/parlay4.png').convert_alpha()
parlay5 = pygame.image.load('old_hilltop/assets/parlay5.png').convert_alpha()
parlay6 = pygame.image.load('old_hilltop/assets/parlay6.png').convert_alpha()
ten = pygame.image.load('old_hilltop/assets/ten.png').convert_alpha()
thirty = pygame.image.load('old_hilltop/assets/thirty.png').convert_alpha()
three = pygame.image.load('old_hilltop/assets/three.png').convert_alpha()
twenty = pygame.image.load('old_hilltop/assets/twenty.png').convert_alpha()
two_hundred = pygame.image.load('old_hilltop/assets/two_hundred.png').convert_alpha()
two = pygame.image.load('old_hilltop/assets/two.png').convert_alpha()
h = pygame.image.load('old_hilltop/assets/h.png').convert_alpha()
i = pygame.image.load('old_hilltop/assets/i.png').convert_alpha()
ll = pygame.image.load('old_hilltop/assets/ll.png').convert_alpha()
t = pygame.image.load('old_hilltop/assets/t.png').convert_alpha()
o = pygame.image.load('old_hilltop/assets/o.png').convert_alpha()
p_name = pygame.image.load('old_hilltop/assets/p.png').convert_alpha()
bg_menu = pygame.image.load('old_hilltop/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('old_hilltop/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('old_hilltop/assets/backglass_off.png').convert_alpha()

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
   
    if s.game.name.position >= 1:
        p = [172,287]
        screen.blit(h, p)
    if s.game.name.position >= 2:
        p = [236,294]
        screen.blit(i, p)
    if s.game.name.position >= 3:
        p = [279,294]
        screen.blit(ll, p)
    if s.game.name.position >= 4:
        p = [362,302]
        screen.blit(t, p)
    if s.game.name.position >= 5:
        p = [431,298]
        screen.blit(o, p)
    if s.game.name.position >= 6:
        p = [504,286]
        screen.blit(p_name, p)

    if s.game.tilt.status == False:
        if 1 in s.game.selection:
            p = [18,836]
            screen.blit(selection1, p)
        if 2 in s.game.selection:
            p = [16,711]
            screen.blit(selection2, p)
        if 3 in s.game.selection:
            p = [165,737]
            screen.blit(selection3, p)
        if 4 in s.game.selection:
            p = [303,750]
            screen.blit(selection4, p)
        if 5 in s.game.selection:
            p = [442,743]
            screen.blit(selection5, p)
        if 6 in s.game.selection:
            p = [580,716]
            screen.blit(selection6, p)
        if 7 in s.game.selection:
            p = [580,840]
            screen.blit(selection7, p)

        if s.game.clover.status == True:
            p = [264,984]
            screen.blit(entry_flash, p)
        if s.game.left.status == True:
            p = [36,975]
            screen.blit(boot, p)
        if s.game.right.status == True:
            p = [632,986]
            screen.blit(saddle, p)
        if s.game.show_win.status == True:
            p = [418,1011]
            screen.blit(ef_small, p)
        if s.game.pennant.status == True:
            p = [620,216]
            screen.blit(feature, p)
        if s.game.daily_double.status == True:
            p = [136,1013]
            screen.blit(ef_large, p)
        if s.game.purse_win.status == True:
            p = [242,1010]
            screen.blit(ef_small, p)
        if s.game.odds_advance.status == True:
            p = [312,1010]
            screen.blit(ef_large, p)
        if s.game.feature_lite.status == True:
            p = [490,1008]
            screen.blit(ef_large, p)
      
        #Odds displays always shown unless tilted
        p = [22,484]
        screen.blit(section, p)
        p = [22,540]
        screen.blit(section, p)
        p = [22,595]
        screen.blit(section, p)
        p = [22,648]
        screen.blit(section, p)

        if s.game.odds.position == 1:
            p = [101,509]
            screen.blit(odds1, p)
            p = [101,562]
            screen.blit(odds1, p)
            p = [102,616]
            screen.blit(odds1, p)
            p = [102,668]
            screen.blit(odds1, p)
        if s.game.odds.position == 2:
            p = [160,523]
            screen.blit(odds2, p)
            p = [162,576]
            screen.blit(odds2, p)
            p = [162,626]
            screen.blit(odds2, p)
            p = [162,679]
            screen.blit(odds2, p)
        if s.game.odds.position == 3:
            p = [221,532]
            screen.blit(odds3, p)
            p = [222,584]
            screen.blit(odds3, p)
            p = [222,636]
            screen.blit(odds3, p)
            p = [222,688]
            screen.blit(odds3, p)
        if s.game.odds.position == 4:
            p = [282,538]
            screen.blit(odds4, p)
            p = [282,590]
            screen.blit(odds4, p)
            p = [282,642]
            screen.blit(odds4, p)
            p = [282,692]
            screen.blit(odds4, p)
        if s.game.odds.position == 5:
            p = [342,540]
            screen.blit(odds5, p)
            p = [341,592]
            screen.blit(odds5, p)
            p = [341,642]
            screen.blit(odds5, p)
            p = [341,694]
            screen.blit(odds5, p)
        if s.game.odds.position == 6:
            p = [401,538]
            screen.blit(odds6, p)
            p = [401,590]
            screen.blit(odds6, p)
            p = [401,642]
            screen.blit(odds6, p)
            p = [401,692]
            screen.blit(odds6, p)
        if s.game.odds.position == 7:
            p = [461,532]
            screen.blit(odds7, p)
            p = [462,584]
            screen.blit(odds7, p)
            p = [462,636]
            screen.blit(odds7, p)
            p = [462,686]
            screen.blit(odds7, p)
        if s.game.odds.position == 8:
            p = [521,520]
            screen.blit(odds8, p)
            p = [521,571]
            screen.blit(odds8, p)
            p = [521,619]
            screen.blit(odds8, p)
            p = [521,675]
            screen.blit(odds8, p)
        if s.game.odds.position == 9:
            p = [582,501]
            screen.blit(odds9, p)
            p = [582,556]
            screen.blit(odds9, p)
            p = [582,608]
            screen.blit(odds9, p)
            p = [582,661]
            screen.blit(odds9, p)
        if s.game.odds.position == 10:
            p = [644,481]
            screen.blit(odds10, p)
            p = [642,536]
            screen.blit(odds10, p)
            p = [644,591]
            screen.blit(odds10, p)
            p = [644,645]
            screen.blit(odds10, p)
           
    if s.game.replays:
        digits = [int(d) for d in list(str(s.game.replays))]
        if len(digits) == 3:
            if digits[0] != 0:
                if digits[0] == 1:
                    p = [305,199]
                    screen.blit(one_hundred, p)
                if digits[0] == 2:
                    p = [382,199]
                    screen.blit(two_hundred, p)
            if digits[1] != 0:
                if digits[1] == 1:
                    p = [16,199]
                    screen.blit(ten, p)
                if digits[1] == 2:
                    p = [48,199]
                    screen.blit(twenty, p)
                if digits[1] == 3:
                    p = [80,199]
                    screen.blit(thirty, p)
                if digits[1] == 4:
                    p = [111,199]
                    screen.blit(forty, p)
                if digits[1] == 5:
                    p = [144,199]
                    screen.blit(fifty, p)
                if digits[1] == 6:
                    p = [177,199]
                    screen.blit(sixty, p)
                if digits[1] == 7:
                    p = [208,199]
                    screen.blit(seventy, p)
                if digits[1] == 8:
                    p = [239,199]
                    screen.blit(eighty, p)
                if digits[1] == 9:
                    p = [272,199]
                    screen.blit(ninety, p)
            if digits[2] != 0:
                if digits[2] == 1:
                    p = [428,199]
                    screen.blit(one, p)
                if digits[2] == 2:
                    p = [460,199]
                    screen.blit(two, p)
                if digits[2] == 3:
                    p = [493,199]
                    screen.blit(three, p)
                if digits[2] == 4:
                    p = [524,199]
                    screen.blit(four, p)
                if digits[2] == 5:
                    p = [557,199]
                    screen.blit(five, p)
                if digits[2] == 6:
                    p = [588,199]
                    screen.blit(six, p)
                if digits[2] == 7:
                    p = [619,199]
                    screen.blit(seven, p)
                if digits[2] == 8:
                    p = [651,199]
                    screen.blit(eight, p)
                if digits[2] == 9:
                    p = [683,199]
                    screen.blit(nine, p)
        if len(digits) == 2:
            if digits[0] != 0:
                if digits[0] == 1:
                    p = [16,199]
                    screen.blit(ten, p)
                if digits[0] == 2:
                    p = [48,199]
                    screen.blit(twenty, p)
                if digits[0] == 3:
                    p = [80,199]
                    screen.blit(thirty, p)
                if digits[0] == 4:
                    p = [111,199]
                    screen.blit(forty, p)
                if digits[0] == 5:
                    p = [144,199]
                    screen.blit(fifty, p)
                if digits[0] == 6:
                    p = [177,199]
                    screen.blit(sixty, p)
                if digits[0] == 7:
                    p = [208,199]
                    screen.blit(seventy, p)
                if digits[0] == 8:
                    p = [239,199]
                    screen.blit(eighty, p)
                if digits[0] == 9:
                    p = [272,199]
                    screen.blit(ninety, p)
            if digits[1] != 0:
                if digits[1] == 1:
                    p = [428,199]
                    screen.blit(one, p)
                if digits[1] == 2:
                    p = [460,199]
                    screen.blit(two, p)
                if digits[1] == 3:
                    p = [493,199]
                    screen.blit(three, p)
                if digits[1] == 4:
                    p = [524,199]
                    screen.blit(four, p)
                if digits[1] == 5:
                    p = [557,199]
                    screen.blit(five, p)
                if digits[1] == 6:
                    p = [588,199]
                    screen.blit(six, p)
                if digits[1] == 7:
                    p = [619,199]
                    screen.blit(seven, p)
                if digits[1] == 8:
                    p = [651,199]
                    screen.blit(eight, p)
                if digits[1] == 9:
                    p = [683,199]
                    screen.blit(nine, p)
        if len(digits) == 1:
            if digits[0] != 0:
                if digits[0] == 1:
                    p = [428,199]
                    screen.blit(one, p)
                if digits[0] == 2:
                    p = [460,199]
                    screen.blit(two, p)
                if digits[0] == 3:
                    p = [493,199]
                    screen.blit(three, p)
                if digits[0] == 4:
                    p = [524,199]
                    screen.blit(four, p)
                if digits[0] == 5:
                    p = [557,199]
                    screen.blit(five, p)
                if digits[0] == 6:
                    p = [588,199]
                    screen.blit(six, p)
                if digits[0] == 7:
                    p = [619,199]
                    screen.blit(seven, p)
                if digits[0] == 8:
                    p = [651,199]
                    screen.blit(eight, p)
                if digits[0] == 9:
                    p = [683,199]
                    screen.blit(nine, p)

    p = [88,361]
    screen.blit(added_entries, p)
    p = [80,394]
    screen.blit(added_entries, p)
    p = [73,427]
    screen.blit(added_entries, p)

    if s.game.show_race_stepper.position == 1:
        p = [180,390]
        screen.blit(racehorse3, p)
    if s.game.show_race_stepper.position == 2:
        p = [232,398]
        screen.blit(racehorse1, p)
    if s.game.show_race_stepper.position == 3:
        p = [286,406]
        screen.blit(racehorse2, p)
    if s.game.show_race_stepper.position == 4:
        p = [338,407]
        screen.blit(racehorse3, p)
    if s.game.show_race_stepper.position == 5:
        p = [390,404]
        screen.blit(racehorse1, p)
    if s.game.show_race_stepper.position == 6:
        p = [444,399]
        screen.blit(racehorse2, p)
    if s.game.show_race_stepper.position == 7:
        p = [497,394]
        screen.blit(racehorse1, p)
    if s.game.show_race_stepper.position == 8:
        p = [544,352]
        screen.blit(pygame.transform.flip(added_entries, False, True), p)

    if s.game.place_race_stepper.position == 1:
        p = [172,424]
        screen.blit(racehorse1, p)
    if s.game.place_race_stepper.position == 2:
        p = [228,432]
        screen.blit(racehorse2, p)
    if s.game.place_race_stepper.position == 3:
        p = [283,438]
        screen.blit(racehorse3, p)
    if s.game.place_race_stepper.position == 4:
        p = [338,438]
        screen.blit(racehorse1, p)
    if s.game.place_race_stepper.position == 5:
        p = [392,436]
        screen.blit(racehorse2, p)
    if s.game.place_race_stepper.position == 6:
        p = [446,431]
        screen.blit(racehorse1, p)
    if s.game.place_race_stepper.position == 7:
        p = [502,422]
        screen.blit(racehorse2, p)
    if s.game.place_race_stepper.position == 8:
        p = [547,390]
        screen.blit(pygame.transform.flip(added_entries, False, True), p)
    
    if s.game.win_race_stepper.position == 1:
        p = [167,462]
        screen.blit(racehorse2, p)
    if s.game.win_race_stepper.position == 2:
        p = [222,469]
        screen.blit(racehorse3, p)
    if s.game.win_race_stepper.position == 3:
        p = [281,474]
        screen.blit(racehorse1, p)
    if s.game.win_race_stepper.position == 4:
        p = [336,474]
        screen.blit(racehorse2, p)
    if s.game.win_race_stepper.position == 5:
        p = [394,473]
        screen.blit(racehorse3, p)
    if s.game.win_race_stepper.position == 6:
        p = [451,468]
        screen.blit(racehorse2, p)
    if s.game.win_race_stepper.position == 7:
        p = [506,459]
        screen.blit(racehorse3, p)
    if s.game.win_race_stepper.position == 8:
        p = [558,423]
        screen.blit(pygame.transform.flip(added_entries, False, True), p)

    if s.game.parlay.position >= 1:
        p = [170,922]
        screen.blit(parlay1, p)
    if s.game.parlay.position >= 2:
        p = [239,908]
        screen.blit(parlay2, p)
    if s.game.parlay.position >= 3:
        p = [300,901]
        screen.blit(parlay3, p)
    if s.game.parlay.position >= 4:
        p = [371,904]
        screen.blit(parlay4, p)
    if s.game.parlay.position >= 5:
        p = [428,910]
        screen.blit(parlay5, p)
    if s.game.parlay.position >= 6:
        p = [497,923]
        screen.blit(parlay6, p)

    if s.game.tilt.status == True:
        tilt_position = [96,227]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def clover_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]
 
    if s.game.show_win.status == False:
        dirty_rects.append(screen.blit(bg_gi, (418,1011), pygame.Rect(418,1011,60,61)))
    if s.game.daily_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (136,1013), pygame.Rect(136,1013,95,61)))
    if s.game.purse_win.status == False:
        dirty_rects.append(screen.blit(bg_gi, (242,1010), pygame.Rect(242,1010,60,61)))
    if s.game.odds_advance.status == False:
        dirty_rects.append(screen.blit(bg_gi, (312,1010), pygame.Rect(312,1010,95,61)))
    if s.game.feature_lite.status == False:
        dirty_rects.append(screen.blit(bg_gi, (490,1008), pygame.Rect(490,1008,95,61)))
    
    if num in [9,20,33,45]:
        if s.game.show_win.status == False:
            p = [418,1011]
            dirty_rects.append(screen.blit(ef_small, p))
    if num in [10,21,34,46]:
        if s.game.daily_double.status == False:
            p = [136,1013]
            dirty_rects.append(screen.blit(ef_large, p))
    if num in [11,22,35,47]:
        if s.game.purse_win.status == False:
            p = [242,1010]
            dirty_rects.append(screen.blit(ef_small, p))
    if num in [12,23,36,48]:
        if s.game.odds_advance.status == False:
            p = [312,1010]
            dirty_rects.append(screen.blit(ef_large, p))
    if num in [13,24,37,49]:
        if s.game.feature_lite.status == False:
            p = [490,1008]
            dirty_rects.append(screen.blit(ef_large, p))

    pygame.display.update(dirty_rects)
    return

def feature_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.pennant.status == False:
        dirty_rects.append(screen.blit(bg_gi, (620,250), pygame.Rect(620,250,43,29)))
   
    if num in [7,25,32,44]:
        if s.game.pennant.status == False:
            p = [620,250]
            dirty_rects.append(screen.blit(feature, p))

    pygame.display.update(dirty_rects)
    return

def selection_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.left.status == False:
        dirty_rects.append(screen.blit(bg_gi, (36,975), pygame.Rect(36,975,44,71)))
    if s.game.right.status == False:
        dirty_rects.append(screen.blit(bg_gi, (632,986), pygame.Rect(632,986,72,68)))

    if 1 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (18,836), pygame.Rect(18,836,119,125)))
    if 2 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (16,711), pygame.Rect(16,711,121,129)))
    if 3 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (165,737), pygame.Rect(165,737,108,121)))
    if 4 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (303,750), pygame.Rect(303,750,109,118)))
    if 5 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (442,743), pygame.Rect(442,743,107,120)))
    if 6 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (580,716), pygame.Rect(580,716,115,131)))
    if 7 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (580,840), pygame.Rect(580,840,120,127)))

    if num in [5,20,30,40]:
        if s.game.left.status == False:
            p = [36,975]
            dirty_rects.append(screen.blit(boot, p))
    if num in [0,10,25,35,45]:
        if s.game.right.status == False:
            p = [632,986]
            dirty_rects.append(screen.blit(saddle, p))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [18,836]
            dirty_rects.append(screen.blit(selection1, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [16,711]
            dirty_rects.append(screen.blit(selection2, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection:
            p = [165,737]
            dirty_rects.append(screen.blit(selection3, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection:
            p = [303,750]
            dirty_rects.append(screen.blit(selection4, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection:
            p = [442,743]
            dirty_rects.append(screen.blit(selection5, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [580,716]
            dirty_rects.append(screen.blit(selection6, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [580,840]
            dirty_rects.append(screen.blit(selection7, p))

    pygame.display.update(dirty_rects)
    return

def star_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]
    
    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (101,509), pygame.Rect(101,509,57,58)))
        dirty_rects.append(screen.blit(bg_gi, (101,562), pygame.Rect(101,562,57,58)))
        dirty_rects.append(screen.blit(bg_gi, (102,616), pygame.Rect(102,616,57,58)))
        dirty_rects.append(screen.blit(bg_gi, (102,668), pygame.Rect(102,668,57,58)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (160,523), pygame.Rect(160,523,57,54)))
        dirty_rects.append(screen.blit(bg_gi, (162,576), pygame.Rect(162,576,57,54)))
        dirty_rects.append(screen.blit(bg_gi, (162,626), pygame.Rect(162,626,57,54)))
        dirty_rects.append(screen.blit(bg_gi, (162,679), pygame.Rect(162,679,57,54)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (221,532), pygame.Rect(221,532,55,51)))
        dirty_rects.append(screen.blit(bg_gi, (222,584), pygame.Rect(222,584,55,51)))
        dirty_rects.append(screen.blit(bg_gi, (222,636), pygame.Rect(222,636,55,51)))
        dirty_rects.append(screen.blit(bg_gi, (222,688), pygame.Rect(222,688,55,51)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (282,538), pygame.Rect(282,538,54,49)))
        dirty_rects.append(screen.blit(bg_gi, (282,590), pygame.Rect(282,590,54,49)))
        dirty_rects.append(screen.blit(bg_gi, (282,642), pygame.Rect(282,642,54,49)))
        dirty_rects.append(screen.blit(bg_gi, (282,692), pygame.Rect(282,692,54,49)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (342,540), pygame.Rect(342,540,52,46)))
        dirty_rects.append(screen.blit(bg_gi, (341,592), pygame.Rect(341,592,52,46)))
        dirty_rects.append(screen.blit(bg_gi, (341,642), pygame.Rect(341,642,52,46)))
        dirty_rects.append(screen.blit(bg_gi, (341,694), pygame.Rect(341,694,52,46)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (401,538), pygame.Rect(401,538,56,48)))
        dirty_rects.append(screen.blit(bg_gi, (401,590), pygame.Rect(401,590,56,48)))
        dirty_rects.append(screen.blit(bg_gi, (401,642), pygame.Rect(401,642,56,48)))
        dirty_rects.append(screen.blit(bg_gi, (401,692), pygame.Rect(401,692,56,48)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (461,532), pygame.Rect(461,532,55,51)))
        dirty_rects.append(screen.blit(bg_gi, (462,584), pygame.Rect(462,584,55,51)))
        dirty_rects.append(screen.blit(bg_gi, (462,636), pygame.Rect(462,636,55,51)))
        dirty_rects.append(screen.blit(bg_gi, (462,686), pygame.Rect(462,686,55,51)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (521,520), pygame.Rect(521,520,53,57)))
        dirty_rects.append(screen.blit(bg_gi, (521,571), pygame.Rect(521,571,53,57)))
        dirty_rects.append(screen.blit(bg_gi, (521,619), pygame.Rect(521,619,53,57)))
        dirty_rects.append(screen.blit(bg_gi, (521,675), pygame.Rect(521,675,53,57)))
    if s.game.odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (582,501), pygame.Rect(582,501,57,59)))
        dirty_rects.append(screen.blit(bg_gi, (582,556), pygame.Rect(582,556,57,59)))
        dirty_rects.append(screen.blit(bg_gi, (582,608), pygame.Rect(582,608,57,59)))
        dirty_rects.append(screen.blit(bg_gi, (582,661), pygame.Rect(582,661,57,59)))
    if s.game.odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (644,481), pygame.Rect(644,481,56,61)))
        dirty_rects.append(screen.blit(bg_gi, (642,536), pygame.Rect(642,536,56,61)))
        dirty_rects.append(screen.blit(bg_gi, (644,591), pygame.Rect(644,591,56,61)))
        dirty_rects.append(screen.blit(bg_gi, (644,645), pygame.Rect(644,645,56,61)))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [101,509]
            dirty_rects.append(screen.blit(odds1, p))
            p = [101,562]
            dirty_rects.append(screen.blit(odds1, p))
            p = [102,616]
            dirty_rects.append(screen.blit(odds1, p))
            p = [102,668]
            dirty_rects.append(screen.blit(odds1, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [160,523]
            dirty_rects.append(screen.blit(odds2, p))
            p = [162,576]
            dirty_rects.append(screen.blit(odds2, p))
            p = [162,626]
            dirty_rects.append(screen.blit(odds2, p))
            p = [162,679]
            dirty_rects.append(screen.blit(odds2, p))
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [221,532]
            dirty_rects.append(screen.blit(odds3, p))
            p = [222,584]
            dirty_rects.append(screen.blit(odds3, p))
            p = [222,636]
            dirty_rects.append(screen.blit(odds3, p))
            p = [222,688]
            dirty_rects.append(screen.blit(odds3, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [282,538]
            dirty_rects.append(screen.blit(odds4, p))
            p = [282,590]
            dirty_rects.append(screen.blit(odds4, p))
            p = [282,642]
            dirty_rects.append(screen.blit(odds4, p))
            p = [282,692]
            dirty_rects.append(screen.blit(odds4, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [342,540]
            dirty_rects.append(screen.blit(odds5, p))
            p = [341,592]
            dirty_rects.append(screen.blit(odds5, p))
            p = [341,642]
            dirty_rects.append(screen.blit(odds5, p))
            p = [341,694]
            dirty_rects.append(screen.blit(odds5, p))
    if num in [5,15,25,35,45]:
        if s.game.odds.position != 6:
            p = [401,538]
            dirty_rects.append(screen.blit(odds6, p))
            p = [401,590]
            dirty_rects.append(screen.blit(odds6, p))
            p = [401,642]
            dirty_rects.append(screen.blit(odds6, p))
            p = [401,692]
            dirty_rects.append(screen.blit(odds6, p))
    if num in [6,16,26,36,46]:
        if s.game.odds.position != 7:
            p = [461,532]
            dirty_rects.append(screen.blit(odds7, p))
            p = [462,584]
            dirty_rects.append(screen.blit(odds7, p))
            p = [462,636]
            dirty_rects.append(screen.blit(odds7, p))
            p = [462,686]
            dirty_rects.append(screen.blit(odds7, p))
    if num in [7,17,27,37,47]:
        if s.game.odds.position != 8:
            p = [521,520]
            dirty_rects.append(screen.blit(odds8, p))
            p = [521,571]
            dirty_rects.append(screen.blit(odds8, p))
            p = [521,619]
            dirty_rects.append(screen.blit(odds8, p))
            p = [522,675]
            dirty_rects.append(screen.blit(odds8, p))
    if num in [8,18,28,38,48]:
        if s.game.odds.position != 9:
            p = [582,501]
            dirty_rects.append(screen.blit(odds9, p))
            p = [582,556]
            dirty_rects.append(screen.blit(odds9, p))
            p = [582,608]
            dirty_rects.append(screen.blit(odds9, p))
            p = [582,661]
            dirty_rects.append(screen.blit(odds9, p))
    if num in [9,19,29,39,49]:
        if s.game.odds.position != 10:
            p = [644,481]
            dirty_rects.append(screen.blit(odds10, p))
            p = [642,536]
            dirty_rects.append(screen.blit(odds10, p))
            p = [644,591]
            dirty_rects.append(screen.blit(odds10, p))
            p = [644,645]
            dirty_rects.append(screen.blit(odds10, p))

    pygame.display.update(dirty_rects)
    return

