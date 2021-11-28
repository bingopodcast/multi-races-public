import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

tilt = pygame.image.load('photo_finish/assets/tilt.png').convert_alpha()
added_entry = pygame.image.load('photo_finish/assets/added_entry.png').convert_alpha()
boot = pygame.image.load('photo_finish/assets/boot.png').convert_alpha()
eight = pygame.image.load('photo_finish/assets/eight.png').convert_alpha()
eighty = pygame.image.load('photo_finish/assets/eighty.png').convert_alpha()
entry_flash = pygame.image.load('photo_finish/assets/entry_flash.png').convert_alpha()
fifty = pygame.image.load('photo_finish/assets/fifty.png').convert_alpha()
five = pygame.image.load('photo_finish/assets/five.png').convert_alpha()
forty = pygame.image.load('photo_finish/assets/forty.png').convert_alpha()
four = pygame.image.load('photo_finish/assets/four.png').convert_alpha()
nine = pygame.image.load('photo_finish/assets/nine.png').convert_alpha()
ninety = pygame.image.load('photo_finish/assets/ninety.png').convert_alpha()
odds10 = pygame.image.load('photo_finish/assets/odds10.png').convert_alpha()
odds1 = pygame.image.load('photo_finish/assets/odds1.png').convert_alpha()
odds2 = pygame.image.load('photo_finish/assets/odds2.png').convert_alpha()
odds3 = pygame.image.load('photo_finish/assets/odds3.png').convert_alpha()
odds4 = pygame.image.load('photo_finish/assets/odds4.png').convert_alpha()
odds5 = pygame.image.load('photo_finish/assets/odds5.png').convert_alpha()
odds6 = pygame.image.load('photo_finish/assets/odds6.png').convert_alpha()
odds7 = pygame.image.load('photo_finish/assets/odds7.png').convert_alpha()
odds8 = pygame.image.load('photo_finish/assets/odds8.png').convert_alpha()
odds9 = pygame.image.load('photo_finish/assets/odds9.png').convert_alpha()
one_hundred = pygame.image.load('photo_finish/assets/one_hundred.png').convert_alpha()
one = pygame.image.load('photo_finish/assets/one.png').convert_alpha()
racehorse1 = pygame.image.load('photo_finish/assets/racehorse1.png').convert_alpha()
racehorse2 = pygame.image.load('photo_finish/assets/racehorse2.png').convert_alpha()
racehorse3 = pygame.image.load('photo_finish/assets/racehorse3.png').convert_alpha()
saddle = pygame.image.load('photo_finish/assets/saddle.png').convert_alpha()
section = pygame.image.load('photo_finish/assets/section.png').convert_alpha()
selection1 = pygame.image.load('photo_finish/assets/selection1.png').convert_alpha()
selection2 = pygame.image.load('photo_finish/assets/selection2.png').convert_alpha()
selection3 = pygame.image.load('photo_finish/assets/selection3.png').convert_alpha()
selection4 = pygame.image.load('photo_finish/assets/selection4.png').convert_alpha()
selection5 = pygame.image.load('photo_finish/assets/selection5.png').convert_alpha()
selection6 = pygame.image.load('photo_finish/assets/selection6.png').convert_alpha()
selection7 = pygame.image.load('photo_finish/assets/selection7.png').convert_alpha()
seven = pygame.image.load('photo_finish/assets/seven.png').convert_alpha()
seventy = pygame.image.load('photo_finish/assets/seventy.png').convert_alpha()
six = pygame.image.load('photo_finish/assets/six.png').convert_alpha()
sixty = pygame.image.load('photo_finish/assets/sixty.png').convert_alpha()
ten = pygame.image.load('photo_finish/assets/ten.png').convert_alpha()
thirty = pygame.image.load('photo_finish/assets/thirty.png').convert_alpha()
three = pygame.image.load('photo_finish/assets/three.png').convert_alpha()
twenty = pygame.image.load('photo_finish/assets/twenty.png').convert_alpha()
two = pygame.image.load('photo_finish/assets/two.png').convert_alpha()
f = pygame.image.load('photo_finish/assets/f.png').convert_alpha()
i = pygame.image.load('photo_finish/assets/i.png').convert_alpha()
n = pygame.image.load('photo_finish/assets/n.png').convert_alpha()
i2 = pygame.image.load('photo_finish/assets/i2.png').convert_alpha()
letter_s = pygame.image.load('photo_finish/assets/s.png').convert_alpha()
h = pygame.image.load('photo_finish/assets/h.png').convert_alpha()
ef_indicator = pygame.image.load('photo_finish/assets/ef_indicator.png').convert_alpha()
feature = pygame.image.load('photo_finish/assets/feature.png').convert_alpha()
bg_menu = pygame.image.load('photo_finish/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('photo_finish/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('photo_finish/assets/backglass_off.png').convert_alpha()

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
        p = [361,334]
        screen.blit(f, p)
    if s.game.name.position >= 2:
        p = [401,338]
        screen.blit(i, p)
    if s.game.name.position >= 3:
        p = [432,343]
        screen.blit(n, p)
    if s.game.name.position >= 4:
        p = [484,352]
        screen.blit(i2, p)
    if s.game.name.position >= 5:
        p = [513,356]
        screen.blit(letter_s, p)
    if s.game.name.position >= 6:
        p = [556,372]
        screen.blit(h, p)

    if s.game.tilt.status == False:
        if 1 in s.game.selection:
            p = [24,781]
            screen.blit(selection1, p)
        if 2 in s.game.selection:
            p = [82,728]
            screen.blit(selection2, p)
        if 3 in s.game.selection:
            p = [182,694]
            screen.blit(selection3, p)
        if 4 in s.game.selection:
            p = [299,681]
            screen.blit(selection4, p)
        if 5 in s.game.selection:
            p = [397,685]
            screen.blit(selection5, p)
        if 6 in s.game.selection:
            p = [490,722]
            screen.blit(selection6, p)
        if 7 in s.game.selection:
            p = [568,763]
            screen.blit(selection7, p)

        if s.game.clover.status == True:
            p = [301,847]
            screen.blit(entry_flash, p)
        if s.game.left.status == True:
            p = [13,688]
            screen.blit(boot, p)
        if s.game.right.status == True:
            p = [652,693]
            screen.blit(saddle, p)
        if s.game.purse_place_win.status == True:
            p = [360,870]
            screen.blit(ef_indicator, p)
        if s.game.show_place_win.status == True:
            p = [360,910]
            screen.blit(ef_indicator, p)
        if s.game.three.status == True or s.game.four.status == True or s.game.five.status == True:
            p = [360,950]
            screen.blit(ef_indicator, p)
        if s.game.fan.status == True:
            p = [360,990]
            screen.blit(ef_indicator, p)
        if s.game.odds_advance.status == True:
            p = [221,870]
            screen.blit(ef_indicator, p)
        if s.game.show.status == True:
            p = [220,907]
            screen.blit(ef_indicator, p)
        if s.game.place.status == True:
            p = [220,950]
            screen.blit(ef_indicator, p)
        if s.game.win.status == True:
            p = [220,990]
            screen.blit(ef_indicator, p)
        if s.game.pennant.status == True:
            p = [610,334]
            screen.blit(feature, p)
      
        #Odds displays always shown unless tilted
        p = [2,480]
        screen.blit(section, p)
        p = [24,530]
        screen.blit(section, p)
        p = [46,580]
        screen.blit(section, p)
        p = [70,634]
        screen.blit(section, p)

        if s.game.odds.position == 1:
            p = [107,456]
            screen.blit(odds1, p)
            p = [125,511]
            screen.blit(odds1, p)
            p = [142,564]
            screen.blit(odds1, p)
            p = [162,620]
            screen.blit(odds1, p)
        if s.game.odds.position == 2:
            p = [164,444]
            screen.blit(odds2, p)
            p = [179,500]
            screen.blit(odds2, p)
            p = [190,558]
            screen.blit(odds2, p)
            p = [204,616]
            screen.blit(odds2, p)
        if s.game.odds.position == 3:
            p = [226,435]
            screen.blit(odds3, p)
            p = [234,492]
            screen.blit(odds3, p)
            p = [244,549]
            screen.blit(odds3, p)
            p = [252,606]
            screen.blit(odds3, p)
        if s.game.odds.position == 4:
            p = [291,428]
            screen.blit(odds4, p)
            p = [295,488]
            screen.blit(odds4, p)
            p = [299,545]
            screen.blit(odds4, p)
            p = [302,606]
            screen.blit(odds4, p)
        if s.game.odds.position == 5:
            p = [353,428]
            screen.blit(odds5, p)
            p = [353,489]
            screen.blit(odds5, p)
            p = [352,546]
            screen.blit(odds5, p)
            p = [350,603]
            screen.blit(odds5, p)
        if s.game.odds.position == 6:
            p = [410,432]
            screen.blit(odds6, p)
            p = [405,490]
            screen.blit(odds6, p)
            p = [398,549]
            screen.blit(odds6, p)
            p = [397,606]
            screen.blit(odds6, p)
        if s.game.odds.position == 7:
            p = [472,442]
            screen.blit(odds7, p)
            p = [462,496]
            screen.blit(odds7, p)
            p = [452,554]
            screen.blit(odds7, p)
            p = [442,612]
            screen.blit(odds7, p)
        if s.game.odds.position == 8:
            p = [530,454]
            screen.blit(odds8, p)
            p = [516,509]
            screen.blit(odds8, p)
            p = [499,566]
            screen.blit(odds8, p)
            p = [486,624]
            screen.blit(odds8, p)
        if s.game.odds.position == 9:
            p = [586,475]
            screen.blit(odds9, p)
            p = [568,528]
            screen.blit(odds9, p)
            p = [550,583]
            screen.blit(odds9, p)
            p = [528,638]
            screen.blit(odds9, p)
        if s.game.odds.position == 10:
            p = [641,497]
            screen.blit(odds10, p)
            p = [616,552]
            screen.blit(odds10, p)
            p = [595,605]
            screen.blit(odds10, p)
            p = [571,657]
            screen.blit(odds10, p)
           
    if s.game.replays:
        digits = [int(d) for d in list(str(s.game.replays))]
        if len(digits) == 3:
            if digits[0] != 0:
                if digits[0] == 1:
                    p = [346,1064]
                    screen.blit(one_hundred, p)
            if digits[1] != 0:
                if digits[1] == 1:
                    p = [18,1064]
                    screen.blit(ten, p)
                if digits[1] == 2:
                    p = [53,1064]
                    screen.blit(twenty, p)
                if digits[1] == 3:
                    p = [90,1064]
                    screen.blit(thirty, p)
                if digits[1] == 4:
                    p = [126,1064]
                    screen.blit(forty, p)
                if digits[1] == 5:
                    p = [161,1064]
                    screen.blit(fifty, p)
                if digits[1] == 6:
                    p = [199,1064]
                    screen.blit(sixty, p)
                if digits[1] == 7:
                    p = [234,1064]
                    screen.blit(seventy, p)
                if digits[1] == 8:
                    p = [272,1064]
                    screen.blit(eighty, p)
                if digits[1] == 9:
                    p = [308,1064]
                    screen.blit(ninety, p)
            if digits[2] != 0:
                if digits[2] == 1:
                    p = [394,1064]
                    screen.blit(one, p)
                if digits[2] == 2:
                    p = [430,1064]
                    screen.blit(two, p)
                if digits[2] == 3:
                    p = [466,1064]
                    screen.blit(three, p)
                if digits[2] == 4:
                    p = [504,1064]
                    screen.blit(four, p)
                if digits[2] == 5:
                    p = [539,1064]
                    screen.blit(five, p)
                if digits[2] == 6:
                    p = [578,1064]
                    screen.blit(six, p)
                if digits[2] == 7:
                    p = [610,1064]
                    screen.blit(seven, p)
                if digits[2] == 8:
                    p = [648,1064]
                    screen.blit(eight, p)
                if digits[2] == 9:
                    p = [682,1064]
                    screen.blit(nine, p)
        if len(digits) == 2:
            if digits[0] != 0:
                if digits[0] == 1:
                    p = [18,1064]
                    screen.blit(ten, p)
                if digits[0] == 2:
                    p = [53,1064]
                    screen.blit(twenty, p)
                if digits[0] == 3:
                    p = [90,1064]
                    screen.blit(thirty, p)
                if digits[0] == 4:
                    p = [126,1064]
                    screen.blit(forty, p)
                if digits[0] == 5:
                    p = [161,1064]
                    screen.blit(fifty, p)
                if digits[0] == 6:
                    p = [199,1064]
                    screen.blit(sixty, p)
                if digits[0] == 7:
                    p = [234,1064]
                    screen.blit(seventy, p)
                if digits[0] == 8:
                    p = [272,1064]
                    screen.blit(eighty, p)
                if digits[0] == 9:
                    p = [308,1064]
                    screen.blit(ninety, p)
            if digits[1] != 0:
                if digits[1] == 1:
                    p = [394,1064]
                    screen.blit(one, p)
                if digits[1] == 2:
                    p = [430,1064]
                    screen.blit(two, p)
                if digits[1] == 3:
                    p = [466,1064]
                    screen.blit(three, p)
                if digits[1] == 4:
                    p = [504,1064]
                    screen.blit(four, p)
                if digits[1] == 5:
                    p = [539,1064]
                    screen.blit(five, p)
                if digits[1] == 6:
                    p = [578,1064]
                    screen.blit(six, p)
                if digits[1] == 7:
                    p = [610,1064]
                    screen.blit(seven, p)
                if digits[1] == 8:
                    p = [648,1064]
                    screen.blit(eight, p)
                if digits[1] == 9:
                    p = [682,1064]
                    screen.blit(nine, p)
        if len(digits) == 1:
            if digits[0] != 0:
                if digits[0] == 1:
                    p = [394,1064]
                    screen.blit(one, p)
                if digits[0] == 2:
                    p = [430,1064]
                    screen.blit(two, p)
                if digits[0] == 3:
                    p = [466,1064]
                    screen.blit(three, p)
                if digits[0] == 4:
                    p = [504,1064]
                    screen.blit(four, p)
                if digits[0] == 5:
                    p = [539,1064]
                    screen.blit(five, p)
                if digits[0] == 6:
                    p = [578,1064]
                    screen.blit(six, p)
                if digits[0] == 7:
                    p = [610,1064]
                    screen.blit(seven, p)
                if digits[0] == 8:
                    p = [648,1064]
                    screen.blit(eight, p)
                if digits[0] == 9:
                    p = [682,1064]
                    screen.blit(nine, p)

    p = [7,226]
    screen.blit(added_entry, p)
    p = [7,257]
    screen.blit(added_entry, p)
    p = [7,287]
    screen.blit(added_entry, p)

    if s.game.show_race_stepper.position == 1:
        p = [153,226]
        screen.blit(racehorse3, p)
    if s.game.show_race_stepper.position == 2:
        p = [212,226]
        screen.blit(racehorse1, p)
    if s.game.show_race_stepper.position == 3:
        p = [272,226]
        screen.blit(racehorse2, p)
    if s.game.show_race_stepper.position == 4:
        p = [331,226]
        screen.blit(racehorse3, p)
    if s.game.show_race_stepper.position == 5:
        p = [390,226]
        screen.blit(racehorse1, p)
    if s.game.show_race_stepper.position == 6:
        p = [449,226]
        screen.blit(racehorse2, p)
    if s.game.show_race_stepper.position == 7:
        p = [510,226]
        screen.blit(racehorse1, p)
    if s.game.show_race_stepper.position == 8:
        p = [565,226]
        screen.blit(added_entry, p)

    if s.game.place_race_stepper.position == 1:
        p = [153,256]
        screen.blit(racehorse1, p)
    if s.game.place_race_stepper.position == 2:
        p = [212,256]
        screen.blit(racehorse2, p)
    if s.game.place_race_stepper.position == 3:
        p = [272,256]
        screen.blit(racehorse3, p)
    if s.game.place_race_stepper.position == 4:
        p = [331,256]
        screen.blit(racehorse1, p)
    if s.game.place_race_stepper.position == 5:
        p = [390,256]
        screen.blit(racehorse2, p)
    if s.game.place_race_stepper.position == 6:
        p = [449,256]
        screen.blit(racehorse1, p)
    if s.game.place_race_stepper.position == 7:
        p = [510,256]
        screen.blit(racehorse2, p)
    if s.game.place_race_stepper.position == 8:
        p = [565,256]
        screen.blit(added_entry, p)
    
    if s.game.win_race_stepper.position == 1:
        p = [153,284]
        screen.blit(racehorse2, p)
    if s.game.win_race_stepper.position == 2:
        p = [212,284]
        screen.blit(racehorse3, p)
    if s.game.win_race_stepper.position == 3:
        p = [272,284]
        screen.blit(racehorse1, p)
    if s.game.win_race_stepper.position == 4:
        p = [331,284]
        screen.blit(racehorse2, p)
    if s.game.win_race_stepper.position == 5:
        p = [390,284]
        screen.blit(racehorse3, p)
    if s.game.win_race_stepper.position == 6:
        p = [449,284]
        screen.blit(racehorse2, p)
    if s.game.win_race_stepper.position == 7:
        p = [510,284]
        screen.blit(racehorse3, p)
    if s.game.win_race_stepper.position == 8:
        p = [565,284]
        screen.blit(added_entry, p)



    if s.game.tilt.status == True:
        tilt_position = [12,450]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def clover_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]
 
    if s.game.purse_place_win.status == False:
        dirty_rects.append(screen.blit(bg_gi, (360,870), pygame.Rect(360,870,135,36)))
    if s.game.show_place_win.status == False:
        dirty_rects.append(screen.blit(bg_gi, (360,910), pygame.Rect(360,910,135,36)))
    if s.game.three.status == False and s.game.four.status == False and s.game.five.status == False:
        dirty_rects.append(screen.blit(bg_gi, (360,950), pygame.Rect(360,950,135,36)))
    if s.game.fan.status == False:
        dirty_rects.append(screen.blit(bg_gi, (360,990), pygame.Rect(360,990,135,36)))
    if s.game.odds_advance.status == False:
        dirty_rects.append(screen.blit(bg_gi, (221,870), pygame.Rect(221,870,135,36)))
    if s.game.show.status == False:
        dirty_rects.append(screen.blit(bg_gi, (220,907), pygame.Rect(220,907,135,36)))
    if s.game.place.status == False:
        dirty_rects.append(screen.blit(bg_gi, (220,950), pygame.Rect(220,950,135,36)))
    if s.game.win.status == False:
        dirty_rects.append(screen.blit(bg_gi, (220,990), pygame.Rect(220,990,135,36)))
 
    if num in [3,15,28,40]:
        if s.game.purse_place_win.status == False:
            p = [360,870]
            dirty_rects.append(screen.blit(ef_indicator, p))
    if num in [1,10,26,35]:
        if s.game.show_place_win.status == False:
            p = [360,910]
            dirty_rects.append(screen.blit(ef_indicator, p))
    if num in [5,17,30,42]:
        if s.game.three.status == False and s.game.four.status == False and s.game.five.status == False:
            p = [360,950]
            dirty_rects.append(screen.blit(ef_indicator, p))
    if num in [6,18,21,43]:
        if s.game.fan.status == False:
            p = [360,990]
            dirty_rects.append(screen.blit(ef_indicator, p))
    if num in [7,18,31,43]:
        if s.game.odds_advance.status == False:
            p = [221,870]
            dirty_rects.append(screen.blit(ef_indicator, p))
    if num in [8,19,32,44]:
        if s.game.show.status == False:
            p = [220,907]
            dirty_rects.append(screen.blit(ef_indicator, p))
    if num in [9,20,33,45]:
        if s.game.place.status == False:
            p = [220,950]
            dirty_rects.append(screen.blit(ef_indicator, p))
    if num in [10,21,34,46]:
        if s.game.win.status == False:
            p = [220,990]
            dirty_rects.append(screen.blit(ef_indicator, p))

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
        dirty_rects.append(screen.blit(bg_gi, (610,334), pygame.Rect(610,334,85,28)))
   
    if num in [7,25,32,44]:
        if s.game.pennant.status == False:
            p = [610,334]
            dirty_rects.append(screen.blit(feature, p))

    pygame.display.update(dirty_rects)
    return

def selection_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.left.status == False:
        dirty_rects.append(screen.blit(bg_gi, (13,688), pygame.Rect(13,688,50,48)))
    if s.game.right.status == False:
        dirty_rects.append(screen.blit(bg_gi, (652,693), pygame.Rect(652,693,49,47)))

    if 1 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (24,781), pygame.Rect(24,781,120,135)))
    if 2 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (82,728), pygame.Rect(82,728,141,145)))
    if 3 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (182,694), pygame.Rect(182,694,125,142)))
    if 4 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (299,681), pygame.Rect(299,681,86,141)))
    if 5 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (397,685), pygame.Rect(397,685,100,142)))
    if 6 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (490,722), pygame.Rect(490,722,117,137)))
    if 7 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (568,763), pygame.Rect(568,763,131,139)))

    if num in [5,20,30,40]:
        if s.game.left.status == False:
            p = [13,688]
            dirty_rects.append(screen.blit(boot, p))
    if num in [0,10,25,35,45]:
        if s.game.right.status == False:
            p = [652,693]
            dirty_rects.append(screen.blit(saddle, p))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [24,781]
            dirty_rects.append(screen.blit(selection1, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [82,728]
            dirty_rects.append(screen.blit(selection2, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection:
            p = [182,694]
            dirty_rects.append(screen.blit(selection3, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection:
            p = [299,681]
            dirty_rects.append(screen.blit(selection4, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection:
            p = [397,685]
            dirty_rects.append(screen.blit(selection5, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [490,722]
            dirty_rects.append(screen.blit(selection6, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [568,763]
            dirty_rects.append(screen.blit(selection7, p))

    pygame.display.update(dirty_rects)
    return

def star_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]
 
    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (107,456), pygame.Rect(107,456,61,72)))
        dirty_rects.append(screen.blit(bg_gi, (125,511), pygame.Rect(125,511,61,72)))
        dirty_rects.append(screen.blit(bg_gi, (142,564), pygame.Rect(142,564,61,72)))
        dirty_rects.append(screen.blit(bg_gi, (162,620), pygame.Rect(162,620,61,72)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (164,444), pygame.Rect(164,444,60,69)))
        dirty_rects.append(screen.blit(bg_gi, (179,500), pygame.Rect(179,500,60,69)))
        dirty_rects.append(screen.blit(bg_gi, (190,558), pygame.Rect(190,558,60,69)))
        dirty_rects.append(screen.blit(bg_gi, (204,616), pygame.Rect(204,616,60,69)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (226,435), pygame.Rect(226,435,57,63)))
        dirty_rects.append(screen.blit(bg_gi, (234,492), pygame.Rect(234,492,57,63)))
        dirty_rects.append(screen.blit(bg_gi, (244,549), pygame.Rect(244,549,57,63)))
        dirty_rects.append(screen.blit(bg_gi, (252,606), pygame.Rect(252,606,57,63)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (291,428), pygame.Rect(291,428,49,61)))
        dirty_rects.append(screen.blit(bg_gi, (295,488), pygame.Rect(295,488,49,61)))
        dirty_rects.append(screen.blit(bg_gi, (299,545), pygame.Rect(299,545,49,61)))
        dirty_rects.append(screen.blit(bg_gi, (302,606), pygame.Rect(302,606,49,61)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (353,428), pygame.Rect(353,428,49,61)))
        dirty_rects.append(screen.blit(bg_gi, (353,489), pygame.Rect(353,489,49,61)))
        dirty_rects.append(screen.blit(bg_gi, (352,546), pygame.Rect(352,546,49,61)))
        dirty_rects.append(screen.blit(bg_gi, (350,603), pygame.Rect(350,603,49,61)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (410,432), pygame.Rect(410,432,53,61)))
        dirty_rects.append(screen.blit(bg_gi, (405,490), pygame.Rect(405,490,53,61)))
        dirty_rects.append(screen.blit(bg_gi, (398,549), pygame.Rect(398,549,53,61)))
        dirty_rects.append(screen.blit(bg_gi, (397,606), pygame.Rect(397,606,53,61)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (472,442), pygame.Rect(472,442,56,65)))
        dirty_rects.append(screen.blit(bg_gi, (462,496), pygame.Rect(462,496,56,65)))
        dirty_rects.append(screen.blit(bg_gi, (452,554), pygame.Rect(452,554,56,65)))
        dirty_rects.append(screen.blit(bg_gi, (442,612), pygame.Rect(442,612,56,65)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (530,454), pygame.Rect(530,454,57,69)))
        dirty_rects.append(screen.blit(bg_gi, (516,509), pygame.Rect(516,509,57,69)))
        dirty_rects.append(screen.blit(bg_gi, (499,566), pygame.Rect(499,566,57,69)))
        dirty_rects.append(screen.blit(bg_gi, (486,624), pygame.Rect(486,624,57,69)))
    if s.game.odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (586,475), pygame.Rect(586,475,57,69)))
        dirty_rects.append(screen.blit(bg_gi, (568,528), pygame.Rect(568,528,57,69)))
        dirty_rects.append(screen.blit(bg_gi, (550,583), pygame.Rect(550,583,57,69)))
        dirty_rects.append(screen.blit(bg_gi, (528,638), pygame.Rect(528,638,57,69)))
    if s.game.odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (641,497), pygame.Rect(641,497,73,78)))
        dirty_rects.append(screen.blit(bg_gi, (616,552), pygame.Rect(616,552,73,78)))
        dirty_rects.append(screen.blit(bg_gi, (595,605), pygame.Rect(595,605,73,78)))
        dirty_rects.append(screen.blit(bg_gi, (571,657), pygame.Rect(571,657,73,78)))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [107,456]
            dirty_rects.append(screen.blit(odds1, p))
            p = [125,511]
            dirty_rects.append(screen.blit(odds1, p))
            p = [142,564]
            dirty_rects.append(screen.blit(odds1, p))
            p = [162,620]
            dirty_rects.append(screen.blit(odds1, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [164,444]
            dirty_rects.append(screen.blit(odds2, p))
            p = [179,500]
            dirty_rects.append(screen.blit(odds2, p))
            p = [190,558]
            dirty_rects.append(screen.blit(odds2, p))
            p = [204,616]
            dirty_rects.append(screen.blit(odds2, p))
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [226,435]
            dirty_rects.append(screen.blit(odds3, p))
            p = [234,492]
            dirty_rects.append(screen.blit(odds3, p))
            p = [244,549]
            dirty_rects.append(screen.blit(odds3, p))
            p = [252,606]
            dirty_rects.append(screen.blit(odds3, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [291,428]
            dirty_rects.append(screen.blit(odds4, p))
            p = [295,488]
            dirty_rects.append(screen.blit(odds4, p))
            p = [299,545]
            dirty_rects.append(screen.blit(odds4, p))
            p = [302,606]
            dirty_rects.append(screen.blit(odds4, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [353,428]
            dirty_rects.append(screen.blit(odds5, p))
            p = [353,489]
            dirty_rects.append(screen.blit(odds5, p))
            p = [352,546]
            dirty_rects.append(screen.blit(odds5, p))
            p = [350,603]
            dirty_rects.append(screen.blit(odds5, p))
    if num in [5,15,25,35,45]:
        if s.game.odds.position != 6:
            p = [410,432]
            dirty_rects.append(screen.blit(odds6, p))
            p = [405,490]
            dirty_rects.append(screen.blit(odds6, p))
            p = [398,549]
            dirty_rects.append(screen.blit(odds6, p))
            p = [397,606]
            dirty_rects.append(screen.blit(odds6, p))
    if num in [6,16,26,36,46]:
        if s.game.odds.position != 7:
            p = [472,442]
            dirty_rects.append(screen.blit(odds7, p))
            p = [462,496]
            dirty_rects.append(screen.blit(odds7, p))
            p = [452,554]
            dirty_rects.append(screen.blit(odds7, p))
            p = [442,612]
            dirty_rects.append(screen.blit(odds7, p))
    if num in [7,17,27,37,47]:
        if s.game.odds.position != 8:
            p = [530,454]
            dirty_rects.append(screen.blit(odds8, p))
            p = [516,509]
            dirty_rects.append(screen.blit(odds8, p))
            p = [499,566]
            dirty_rects.append(screen.blit(odds8, p))
            p = [486,624]
            dirty_rects.append(screen.blit(odds8, p))
    if num in [8,18,28,38,48]:
        if s.game.odds.position != 9:
            p = [586,475]
            dirty_rects.append(screen.blit(odds9, p))
            p = [568,528]
            dirty_rects.append(screen.blit(odds9, p))
            p = [550,583]
            dirty_rects.append(screen.blit(odds9, p))
            p = [528,638]
            dirty_rects.append(screen.blit(odds9, p))
    if num in [9,19,29,39,49]:
        if s.game.odds.position != 10:
            p = [641,497]
            dirty_rects.append(screen.blit(odds10, p))
            p = [616,552]
            dirty_rects.append(screen.blit(odds10, p))
            p = [595,605]
            dirty_rects.append(screen.blit(odds10, p))
            p = [571,657]
            dirty_rects.append(screen.blit(odds10, p))

    pygame.display.update(dirty_rects)
    return

