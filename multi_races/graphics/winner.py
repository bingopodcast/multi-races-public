import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

tilt = pygame.image.load('winner/assets/tilt.png').convert_alpha()
added_entries = pygame.image.load('winner/assets/added_entries.png').convert_alpha()
boot = pygame.image.load('winner/assets/boot.png').convert_alpha()
ef_large = pygame.image.load('winner/assets/ef_large.png').convert_alpha()
ef_small = pygame.image.load('winner/assets/ef_small.png').convert_alpha()
eight = pygame.image.load('winner/assets/eight.png').convert_alpha()
eighty = pygame.image.load('winner/assets/eighty.png').convert_alpha()
entry_flash = pygame.image.load('winner/assets/entry_flash.png').convert_alpha()
feature = pygame.image.load('winner/assets/feature.png').convert_alpha()
fifty = pygame.image.load('winner/assets/fifty.png').convert_alpha()
finish = pygame.image.load('winner/assets/finish.png').convert_alpha()
five = pygame.image.load('winner/assets/five.png').convert_alpha()
forty = pygame.image.load('winner/assets/forty.png').convert_alpha()
four = pygame.image.load('winner/assets/four.png').convert_alpha()
home_stretch = pygame.image.load('winner/assets/home_stretch.png').convert_alpha()
nine = pygame.image.load('winner/assets/nine.png').convert_alpha()
ninety = pygame.image.load('winner/assets/ninety.png').convert_alpha()
odds10 = pygame.image.load('winner/assets/odds10.png').convert_alpha()
odds1 = pygame.image.load('winner/assets/odds1.png').convert_alpha()
odds2 = pygame.image.load('winner/assets/odds2.png').convert_alpha()
odds3 = pygame.image.load('winner/assets/odds3.png').convert_alpha()
odds4 = pygame.image.load('winner/assets/odds4.png').convert_alpha()
odds5 = pygame.image.load('winner/assets/odds5.png').convert_alpha()
odds6 = pygame.image.load('winner/assets/odds6.png').convert_alpha()
odds7 = pygame.image.load('winner/assets/odds7.png').convert_alpha()
odds8 = pygame.image.load('winner/assets/odds8.png').convert_alpha()
odds9 = pygame.image.load('winner/assets/odds9.png').convert_alpha()
one_fourth = pygame.image.load('winner/assets/one_fourth.png').convert_alpha()
one_half = pygame.image.load('winner/assets/one_half.png').convert_alpha()
one_hundred = pygame.image.load('winner/assets/one_hundred.png').convert_alpha()
one = pygame.image.load('winner/assets/one.png').convert_alpha()
post = pygame.image.load('winner/assets/post.png').convert_alpha()
racehorse1 = pygame.image.load('winner/assets/racehorse1.png').convert_alpha()
racehorse2 = pygame.image.load('winner/assets/racehorse2.png').convert_alpha()
racehorse3 = pygame.image.load('winner/assets/racehorse3.png').convert_alpha()
race_left = pygame.image.load('winner/assets/race_left.png').convert_alpha()
race_right = pygame.image.load('winner/assets/race_right.png').convert_alpha()
saddle = pygame.image.load('winner/assets/saddle.png').convert_alpha()
section = pygame.image.load('winner/assets/section.png').convert_alpha()
selection1 = pygame.image.load('winner/assets/selection1.png').convert_alpha()
selection2 = pygame.image.load('winner/assets/selection2.png').convert_alpha()
selection3 = pygame.image.load('winner/assets/selection3.png').convert_alpha()
selection4 = pygame.image.load('winner/assets/selection4.png').convert_alpha()
selection5 = pygame.image.load('winner/assets/selection5.png').convert_alpha()
selection6 = pygame.image.load('winner/assets/selection6.png').convert_alpha()
selection7 = pygame.image.load('winner/assets/selection7.png').convert_alpha()
seven = pygame.image.load('winner/assets/seven.png').convert_alpha()
seventy = pygame.image.load('winner/assets/seventy.png').convert_alpha()
six = pygame.image.load('winner/assets/six.png').convert_alpha()
sixty = pygame.image.load('winner/assets/sixty.png').convert_alpha()
special_selection1 = pygame.image.load('winner/assets/special_selection1.png').convert_alpha()
special_selection2 = pygame.image.load('winner/assets/special_selection2.png').convert_alpha()
special_selection3 = pygame.image.load('winner/assets/special_selection3.png').convert_alpha()
special_selection4 = pygame.image.load('winner/assets/special_selection4.png').convert_alpha()
special_selection5 = pygame.image.load('winner/assets/special_selection5.png').convert_alpha()
special_selection6 = pygame.image.load('winner/assets/special_selection6.png').convert_alpha()
ten = pygame.image.load('winner/assets/ten.png').convert_alpha()
thirty = pygame.image.load('winner/assets/thirty.png').convert_alpha()
three_fourths = pygame.image.load('winner/assets/three_fourths.png').convert_alpha()
three = pygame.image.load('winner/assets/three.png').convert_alpha()
twenty = pygame.image.load('winner/assets/twenty.png').convert_alpha()
two_hundred = pygame.image.load('winner/assets/two_hundred.png').convert_alpha()
two = pygame.image.load('winner/assets/two.png').convert_alpha()
feature_purse = pygame.image.load('winner/assets/feature_purse.png').convert_alpha()
boot_purse = pygame.image.load('winner/assets/boot_purse.png').convert_alpha()
saddle_purse = pygame.image.load('winner/assets/saddle_purse.png').convert_alpha()
four_place = pygame.image.load('winner/assets/four_place.png').convert_alpha()
four_show = pygame.image.load('winner/assets/four_show.png').convert_alpha()
four_purse= pygame.image.load('winner/assets/four_purse.png').convert_alpha()
w = pygame.image.load('winner/assets/w.png').convert_alpha()
i = pygame.image.load('winner/assets/i.png').convert_alpha()
n1 = pygame.image.load('winner/assets/n1.png').convert_alpha()
n2 = pygame.image.load('winner/assets/n2.png').convert_alpha()
e = pygame.image.load('winner/assets/e.png').convert_alpha()
r = pygame.image.load('winner/assets/r.png').convert_alpha()
bg_menu = pygame.image.load('winner/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('winner/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('winner/assets/backglass_off.png').convert_alpha()

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
        p = [149,254]
        screen.blit(w, p)
    if s.game.name.position >= 2:
        p = [248,274]
        screen.blit(i, p)
    if s.game.name.position >= 3:
        p = [286,276]
        screen.blit(n1, p)
    if s.game.name.position >= 4:
        p = [363,278]
        screen.blit(n2, p)
    if s.game.name.position >= 5:
        p = [436,270]
        screen.blit(e, p)
    if s.game.name.position >= 6:
        p = [505,258]
        screen.blit(r, p)

    if s.game.tilt.status == False:
        if 1 in s.game.selection:
            p = [8,837]
            screen.blit(selection1, p)
        if 2 in s.game.selection:
            p = [8,709]
            screen.blit(selection2, p)
        if 3 in s.game.selection:
            p = [148,739]
            screen.blit(selection3, p)
        if 4 in s.game.selection:
            p = [288,754]
            screen.blit(selection4, p)
        if 5 in s.game.selection:
            p = [428,739]
            screen.blit(selection5, p)
        if 6 in s.game.selection:
            p = [568,708]
            screen.blit(selection6, p)
        if 7 in s.game.selection:
            p = [568,838]
            screen.blit(selection7, p)

        if s.game.clover.status == True:
            p = [259,996]
            screen.blit(entry_flash, p)
        if s.game.left.status == True:
            p = [14,990]
            screen.blit(boot, p)
        if s.game.right.status == True:
            p = [620,988]
            screen.blit(saddle, p)
        if s.game.feature_purse.status == True:
            p = [148,912]
            screen.blit(feature_purse, p)
        if s.game.left_purse.status == True:
            p = [222,902]
            screen.blit(boot_purse, p)
        if s.game.right_purse.status == True:
            p = [292,895]
            screen.blit(saddle_purse, p)
        if s.game.four_place.status == True:
            p = [359,892]
            screen.blit(four_place, p)
        if s.game.four_show.status == True:
            p = [421,899]
            screen.blit(four_show, p)
        if s.game.four_purse.status == True:
            p = [483,914]
            screen.blit(four_purse, p)
        if s.game.show_win.status == True:
            p = [409,1018]
            screen.blit(ef_small, p)
        if s.game.pennant.status == True:
            p = [620,250]
            screen.blit(feature, p)
        if s.game.daily_double.status == True:
            p = [126,1019]
            screen.blit(ef_large, p)
        if s.game.purse_win.status == True:
            p = [233,1020]
            screen.blit(ef_small, p)
        if s.game.odds_advance.status == True:
            p = [304,1018]
            screen.blit(ef_large, p)
        if s.game.feature_lite.status == True:
            p = [483,1019]
            screen.blit(ef_large, p)
      
        #Odds displays always shown unless tilted
        p = [15,476]
        screen.blit(section, p)
        p = [15,532]
        screen.blit(section, p)
        p = [15,589]
        screen.blit(section, p)
        p = [15,645]
        screen.blit(section, p)

        if s.game.odds.position == 1:
            p = [92,500]
            screen.blit(odds1, p)
            p = [92,555]
            screen.blit(odds1, p)
            p = [92,609]
            screen.blit(odds1, p)
            p = [92,663]
            screen.blit(odds1, p)
        if s.game.odds.position == 2:
            p = [153,513]
            screen.blit(odds2, p)
            p = [153,567]
            screen.blit(odds2, p)
            p = [153,625]
            screen.blit(odds2, p)
            p = [153,677]
            screen.blit(odds2, p)
        if s.game.odds.position == 3:
            p = [214,524]
            screen.blit(odds3, p)
            p = [214,578]
            screen.blit(odds3, p)
            p = [214,634]
            screen.blit(odds3, p)
            p = [214,686]
            screen.blit(odds3, p)
        if s.game.odds.position == 4:
            p = [276,529]
            screen.blit(odds4, p)
            p = [276,583]
            screen.blit(odds4, p)
            p = [276,638]
            screen.blit(odds4, p)
            p = [276,691]
            screen.blit(odds4, p)
        if s.game.odds.position == 5:
            p = [338,531]
            screen.blit(odds5, p)
            p = [338,585]
            screen.blit(odds5, p)
            p = [338,641]
            screen.blit(odds5, p)
            p = [338,693]
            screen.blit(odds5, p)
        if s.game.odds.position == 6:
            p = [398,527]
            screen.blit(odds6, p)
            p = [398,581]
            screen.blit(odds6, p)
            p = [398,639]
            screen.blit(odds6, p)
            p = [398,692]
            screen.blit(odds6, p)
        if s.game.odds.position == 7:
            p = [462,524]
            screen.blit(odds7, p)
            p = [462,578]
            screen.blit(odds7, p)
            p = [462,635]
            screen.blit(odds7, p)
            p = [462,689]
            screen.blit(odds7, p)
        if s.game.odds.position == 8:
            p = [521,517]
            screen.blit(odds8, p)
            p = [521,569]
            screen.blit(odds8, p)
            p = [521,627]
            screen.blit(odds8, p)
            p = [521,682]
            screen.blit(odds8, p)
        if s.game.odds.position == 9:
            p = [583,502]
            screen.blit(odds9, p)
            p = [583,555]
            screen.blit(odds9, p)
            p = [583,613]
            screen.blit(odds9, p)
            p = [583,668]
            screen.blit(odds9, p)
        if s.game.odds.position == 10:
            p = [642,484]
            screen.blit(odds10, p)
            p = [642,540]
            screen.blit(odds10, p)
            p = [642,598]
            screen.blit(odds10, p)
            p = [642,652]
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

    p = [84,348]
    screen.blit(race_left, p)
    p = [75,384]
    screen.blit(race_left, p)
    p = [66,419]
    screen.blit(race_left, p)

    if s.game.show_race_stepper.position == 1:
        p = [178,376]
        screen.blit(racehorse3, p)
    if s.game.show_race_stepper.position == 2:
        p = [229,384]
        screen.blit(racehorse1, p)
    if s.game.show_race_stepper.position == 3:
        p = [284,388]
        screen.blit(racehorse2, p)
    if s.game.show_race_stepper.position == 4:
        p = [338,391]
        screen.blit(racehorse3, p)
    if s.game.show_race_stepper.position == 5:
        p = [393,391]
        screen.blit(racehorse1, p)
    if s.game.show_race_stepper.position == 6:
        p = [448,386]
        screen.blit(racehorse2, p)
    if s.game.show_race_stepper.position == 7:
        p = [497,379]
        screen.blit(racehorse1, p)
    if s.game.show_race_stepper.position == 8:
        p = [539,347]
        screen.blit(race_right, p)

    if s.game.place_race_stepper.position == 1:
        p = [170,411]
        screen.blit(racehorse1, p)
    if s.game.place_race_stepper.position == 2:
        p = [225,419]
        screen.blit(racehorse2, p)
    if s.game.place_race_stepper.position == 3:
        p = [280,424]
        screen.blit(racehorse3, p)
    if s.game.place_race_stepper.position == 4:
        p = [334,425]
        screen.blit(racehorse1, p)
    if s.game.place_race_stepper.position == 5:
        p = [391,424]
        screen.blit(racehorse2, p)
    if s.game.place_race_stepper.position == 6:
        p = [446,418]
        screen.blit(racehorse1, p)
    if s.game.place_race_stepper.position == 7:
        p = [503,413]
        screen.blit(racehorse2, p)
    if s.game.place_race_stepper.position == 8:
        p = [550,381]
        screen.blit(race_right, p)
    
    if s.game.win_race_stepper.position == 1:
        p = [161,445]
        screen.blit(racehorse2, p)
    if s.game.win_race_stepper.position == 2:
        p = [219,453]
        screen.blit(racehorse3, p)
    if s.game.win_race_stepper.position == 3:
        p = [277,459]
        screen.blit(racehorse1, p)
    if s.game.win_race_stepper.position == 4:
        p = [337,461]
        screen.blit(racehorse2, p)
    if s.game.win_race_stepper.position == 5:
        p = [394,459]
        screen.blit(racehorse3, p)
    if s.game.win_race_stepper.position == 6:
        p = [452,454]
        screen.blit(racehorse2, p)
    if s.game.win_race_stepper.position == 7:
        p = [507,448]
        screen.blit(racehorse3, p)
    if s.game.win_race_stepper.position == 8:
        p = [555,417]
        screen.blit(race_right, p)



    if s.game.tilt.status == True:
        tilt_position = [56,257]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def clover_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]
 
    if s.game.feature_purse.status == False:
        dirty_rects.append(screen.blit(bg_gi, (148,912), pygame.Rect(148,912,83,102)))
    if s.game.left_purse.status == False:
        dirty_rects.append(screen.blit(bg_gi, (222,902), pygame.Rect(222,902,83,102)))
    if s.game.right_purse.status == False:
        dirty_rects.append(screen.blit(bg_gi, (292,895), pygame.Rect(292,895,83,93)))
    if s.game.four_place.status == False:
        dirty_rects.append(screen.blit(bg_gi, (359,892), pygame.Rect(359,892,69,93)))
    if s.game.four_show.status == False:
        dirty_rects.append(screen.blit(bg_gi, (421,899), pygame.Rect(421,899,73,105)))
    if s.game.four_purse.status == False:
        dirty_rects.append(screen.blit(bg_gi, (483,914), pygame.Rect(483,914,82,107)))
    if s.game.show_win.status == False:
        dirty_rects.append(screen.blit(bg_gi, (409,1018), pygame.Rect(409,1018,73,67)))
    if s.game.daily_double.status == False:
        dirty_rects.append(screen.blit(bg_gi, (126,1019), pygame.Rect(126,1019,102,68)))
    if s.game.purse_win.status == False:
        dirty_rects.append(screen.blit(bg_gi, (233,1020), pygame.Rect(233,1020,73,67)))
    if s.game.odds_advance.status == False:
        dirty_rects.append(screen.blit(bg_gi, (304,1018), pygame.Rect(304,1018,102,68)))
    if s.game.feature_lite.status == False:
        dirty_rects.append(screen.blit(bg_gi, (483,1019), pygame.Rect(483,1019,102,68)))
    
    if s.game.feature_purse.status == True:
        dirty_rects.append(screen.blit(feature_purse, (148,912), pygame.Rect(148,912,83,102)))
    if s.game.left_purse.status == True:
        dirty_rects.append(screen.blit(boot_purse, (222,902), pygame.Rect(222,902,83,102)))
    if s.game.right_purse.status == True:
        dirty_rects.append(screen.blit(saddle_purse, (292,895), pygame.Rect(292,895,83,93)))
    if s.game.four_place.status == True:
        dirty_rects.append(screen.blit(four_place, (359,892), pygame.Rect(359,892,69,93)))
    if s.game.four_show.status == True:
        dirty_rects.append(screen.blit(four_show, (421,899), pygame.Rect(421,899,73,105)))
    if s.game.four_purse.status == True:
        dirty_rects.append(screen.blit(four_purse, (483,914), pygame.Rect(483,914,82,107)))
 
    if num in [3,15,28,40]:
        if s.game.feature_purse.status == False:
            p = [148,912]
            dirty_rects.append(screen.blit(feature_purse, p))
    if num in [1,10,26,35]:
        if s.game.left_purse.status == False:
            p = [222,902]
            dirty_rects.append(screen.blit(boot_purse, p))
    if num in [5,17,30,42]:
        if s.game.right_purse.status == False:
            p = [292,895]
            dirty_rects.append(screen.blit(saddle_purse, p))
    if num in [6,18,21,43]:
        if s.game.four_place.status == False:
            p = [359,892]
            dirty_rects.append(screen.blit(four_place, p))
    if num in [7,18,31,43]:
        if s.game.four_show.status == False:
            p = [421,899]
            dirty_rects.append(screen.blit(four_show, p))
    if num in [8,19,32,44]:
        if s.game.four_purse.status == False:
            p = [483,914]
            dirty_rects.append(screen.blit(four_purse, p))
    if num in [9,20,33,45]:
        if s.game.show_win.status == False:
            p = [409,1018]
            dirty_rects.append(screen.blit(ef_small, p))
    if num in [10,21,34,46]:
        if s.game.daily_double.status == False:
            p = [126,1019]
            dirty_rects.append(screen.blit(ef_large, p))
    if num in [11,22,35,47]:
        if s.game.purse_win.status == False:
            p = [233,1020]
            dirty_rects.append(screen.blit(ef_small, p))
    if num in [12,23,36,48]:
        if s.game.odds_advance.status == False:
            p = [304,1018]
            dirty_rects.append(screen.blit(ef_large, p))
    if num in [13,24,37,49]:
        if s.game.feature_lite.status == False:
            p = [483,1019]
            dirty_rects.append(screen.blit(ef_large, p))

    if s.game.clover.status == True:
        p = [259,996]
        screen.blit(entry_flash, p)
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
        dirty_rects.append(screen.blit(bg_gi, (14,990), pygame.Rect(14,990,74,71)))
    if s.game.right.status == False:
        dirty_rects.append(screen.blit(bg_gi, (620,988), pygame.Rect(620,988,84,85)))

    if 1 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (8,837), pygame.Rect(8,837,138,144)))
    if 2 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (8,709), pygame.Rect(8,709,138,151)))
    if 3 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (148,739), pygame.Rect(148,739,136,138)))
    if 4 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (288,754), pygame.Rect(288,754,139,128)))
    if 5 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (428,739), pygame.Rect(428,739,138,137)))
    if 6 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (568,708), pygame.Rect(568,708,135,150)))
    if 7 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (568,838), pygame.Rect(568,838,138,143)))

    if num in [5,20,30,40]:
        if s.game.left.status == False:
            p = [14,990]
            dirty_rects.append(screen.blit(boot, p))
    if num in [0,10,25,35,45]:
        if s.game.right.status == False:
            p = [620,988]
            dirty_rects.append(screen.blit(saddle, p))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [8,837]
            dirty_rects.append(screen.blit(selection1, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [8,709]
            dirty_rects.append(screen.blit(selection2, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection:
            p = [148,739]
            dirty_rects.append(screen.blit(selection3, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection:
            p = [288,754]
            dirty_rects.append(screen.blit(selection4, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection:
            p = [428,739]
            dirty_rects.append(screen.blit(selection5, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [568,708]
            dirty_rects.append(screen.blit(selection6, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [568,838]
            dirty_rects.append(screen.blit(selection7, p))

    pygame.display.update(dirty_rects)
    return

def star_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]
    
    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (92,500), pygame.Rect(92,500,60,72)))
        dirty_rects.append(screen.blit(bg_gi, (92,555), pygame.Rect(92,555,60,72)))
        dirty_rects.append(screen.blit(bg_gi, (92,609), pygame.Rect(92,609,60,72)))
        dirty_rects.append(screen.blit(bg_gi, (92,663), pygame.Rect(92,663,60,72)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (153,513), pygame.Rect(153,513,55,60)))
        dirty_rects.append(screen.blit(bg_gi, (153,567), pygame.Rect(153,567,55,60)))
        dirty_rects.append(screen.blit(bg_gi, (153,625), pygame.Rect(153,625,55,60)))
        dirty_rects.append(screen.blit(bg_gi, (153,677), pygame.Rect(153,677,55,60)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (214,524), pygame.Rect(214,524,62,64)))
        dirty_rects.append(screen.blit(bg_gi, (214,578), pygame.Rect(214,578,62,64)))
        dirty_rects.append(screen.blit(bg_gi, (214,634), pygame.Rect(214,634,62,64)))
        dirty_rects.append(screen.blit(bg_gi, (214,686), pygame.Rect(214,686,62,64)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (276,529), pygame.Rect(276,529,59,50)))
        dirty_rects.append(screen.blit(bg_gi, (276,583), pygame.Rect(276,583,59,50)))
        dirty_rects.append(screen.blit(bg_gi, (276,638), pygame.Rect(276,638,59,50)))
        dirty_rects.append(screen.blit(bg_gi, (276,691), pygame.Rect(276,691,59,50)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (338,531), pygame.Rect(338,531,61,58)))
        dirty_rects.append(screen.blit(bg_gi, (338,585), pygame.Rect(338,585,61,58)))
        dirty_rects.append(screen.blit(bg_gi, (338,641), pygame.Rect(338,641,61,58)))
        dirty_rects.append(screen.blit(bg_gi, (338,693), pygame.Rect(338,693,61,58)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (398,527), pygame.Rect(398,527,58,51)))
        dirty_rects.append(screen.blit(bg_gi, (398,581), pygame.Rect(398,581,58,51)))
        dirty_rects.append(screen.blit(bg_gi, (398,639), pygame.Rect(398,639,58,51)))
        dirty_rects.append(screen.blit(bg_gi, (398,692), pygame.Rect(398,692,58,51)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (462,524), pygame.Rect(462,524,60,65)))
        dirty_rects.append(screen.blit(bg_gi, (462,578), pygame.Rect(462,578,60,65)))
        dirty_rects.append(screen.blit(bg_gi, (462,635), pygame.Rect(462,635,60,65)))
        dirty_rects.append(screen.blit(bg_gi, (462,689), pygame.Rect(462,689,60,65)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (521,517), pygame.Rect(521,517,55,62)))
        dirty_rects.append(screen.blit(bg_gi, (521,569), pygame.Rect(521,569,55,62)))
        dirty_rects.append(screen.blit(bg_gi, (521,627), pygame.Rect(521,627,55,62)))
        dirty_rects.append(screen.blit(bg_gi, (521,682), pygame.Rect(521,682,55,62)))
    if s.game.odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (583,502), pygame.Rect(583,502,59,69)))
        dirty_rects.append(screen.blit(bg_gi, (583,555), pygame.Rect(583,555,59,69)))
        dirty_rects.append(screen.blit(bg_gi, (583,613), pygame.Rect(583,613,59,69)))
        dirty_rects.append(screen.blit(bg_gi, (583,668), pygame.Rect(583,668,59,69)))
    if s.game.odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (642,484), pygame.Rect(642,484,56,64)))
        dirty_rects.append(screen.blit(bg_gi, (642,540), pygame.Rect(642,540,56,64)))
        dirty_rects.append(screen.blit(bg_gi, (642,598), pygame.Rect(642,598,56,64)))
        dirty_rects.append(screen.blit(bg_gi, (642,652), pygame.Rect(642,652,56,64)))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [92,500]
            dirty_rects.append(screen.blit(odds1, p))
            p = [92,555]
            dirty_rects.append(screen.blit(odds1, p))
            p = [92,609]
            dirty_rects.append(screen.blit(odds1, p))
            p = [92,663]
            dirty_rects.append(screen.blit(odds1, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [153,513]
            dirty_rects.append(screen.blit(odds2, p))
            p = [153,567]
            dirty_rects.append(screen.blit(odds2, p))
            p = [153,625]
            dirty_rects.append(screen.blit(odds2, p))
            p = [153,677]
            dirty_rects.append(screen.blit(odds2, p))
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [214,524]
            dirty_rects.append(screen.blit(odds3, p))
            p = [214,578]
            dirty_rects.append(screen.blit(odds3, p))
            p = [214,634]
            dirty_rects.append(screen.blit(odds3, p))
            p = [214,686]
            dirty_rects.append(screen.blit(odds3, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [276,529]
            dirty_rects.append(screen.blit(odds4, p))
            p = [276,583]
            dirty_rects.append(screen.blit(odds4, p))
            p = [276,638]
            dirty_rects.append(screen.blit(odds4, p))
            p = [276,691]
            dirty_rects.append(screen.blit(odds4, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [338,531]
            dirty_rects.append(screen.blit(odds5, p))
            p = [338,585]
            dirty_rects.append(screen.blit(odds5, p))
            p = [338,641]
            dirty_rects.append(screen.blit(odds5, p))
            p = [338,693]
            dirty_rects.append(screen.blit(odds5, p))
    if num in [5,15,25,35,45]:
        if s.game.odds.position != 6:
            p = [398,527]
            dirty_rects.append(screen.blit(odds6, p))
            p = [398,581]
            dirty_rects.append(screen.blit(odds6, p))
            p = [398,639]
            dirty_rects.append(screen.blit(odds6, p))
            p = [398,692]
            dirty_rects.append(screen.blit(odds6, p))
    if num in [6,16,26,36,46]:
        if s.game.odds.position != 7:
            p = [462,524]
            dirty_rects.append(screen.blit(odds7, p))
            p = [462,578]
            dirty_rects.append(screen.blit(odds7, p))
            p = [462,635]
            dirty_rects.append(screen.blit(odds7, p))
            p = [462,689]
            dirty_rects.append(screen.blit(odds7, p))
    if num in [7,17,27,37,47]:
        if s.game.odds.position != 8:
            p = [521,517]
            dirty_rects.append(screen.blit(odds8, p))
            p = [521,569]
            dirty_rects.append(screen.blit(odds8, p))
            p = [521,627]
            dirty_rects.append(screen.blit(odds8, p))
            p = [522,682]
            dirty_rects.append(screen.blit(odds8, p))
    if num in [8,18,28,38,48]:
        if s.game.odds.position != 9:
            p = [583,502]
            dirty_rects.append(screen.blit(odds9, p))
            p = [583,555]
            dirty_rects.append(screen.blit(odds9, p))
            p = [583,613]
            dirty_rects.append(screen.blit(odds9, p))
            p = [583,668]
            dirty_rects.append(screen.blit(odds9, p))
    if num in [9,19,29,39,49]:
        if s.game.odds.position != 10:
            p = [642,484]
            dirty_rects.append(screen.blit(odds10, p))
            p = [642,540]
            dirty_rects.append(screen.blit(odds10, p))
            p = [642,598]
            dirty_rects.append(screen.blit(odds10, p))
            p = [642,652]
            dirty_rects.append(screen.blit(odds10, p))

    pygame.display.update(dirty_rects)
    return

