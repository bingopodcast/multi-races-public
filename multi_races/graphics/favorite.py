import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

tilt = pygame.image.load('favorite/assets/tilt.png').convert_alpha()
feature_1 = pygame.image.load('favorite/assets/ss1.png').convert_alpha()
feature_2 = pygame.image.load('favorite/assets/ss2.png').convert_alpha()
feature_3 = pygame.image.load('favorite/assets/ss3.png').convert_alpha()
feature_4 = pygame.image.load('favorite/assets/ss4.png').convert_alpha()
feature_5 = pygame.image.load('favorite/assets/ss5.png').convert_alpha()
feature_6 = pygame.image.load('favorite/assets/ss6.png').convert_alpha()
feature_7 = pygame.image.load('favorite/assets/ss7.png').convert_alpha()
feature_8 = pygame.image.load('favorite/assets/ss8.png').convert_alpha()
feature_9 = pygame.image.load('favorite/assets/ss9.png').convert_alpha()
feature_10 = pygame.image.load('favorite/assets/ss10.png').convert_alpha()
feature_20 = pygame.image.load('favorite/assets/ss20.png').convert_alpha()
feature_30 = pygame.image.load('favorite/assets/ss30.png').convert_alpha()
feature_40 = pygame.image.load('favorite/assets/ss40.png').convert_alpha()
multiplier = pygame.image.load('favorite/assets/multiplier.png').convert_alpha()
letter_f = pygame.image.load('favorite/assets/letter_f.png').convert_alpha()
letter_a = pygame.image.load('favorite/assets/letter_a.png').convert_alpha()
letter_v = pygame.image.load('favorite/assets/letter_v.png').convert_alpha()
letter_o = pygame.image.load('favorite/assets/letter_o.png').convert_alpha()
letter_r = pygame.image.load('favorite/assets/letter_r.png').convert_alpha()
letter_i = pygame.image.load('favorite/assets/letter_i.png').convert_alpha()
letter_t = pygame.image.load('favorite/assets/letter_t.png').convert_alpha()
letter_e = pygame.image.load('favorite/assets/letter_e.png').convert_alpha()
bumper_a = pygame.image.load('favorite/assets/bumper_a.png').convert_alpha()
bumper_b = pygame.image.load('favorite/assets/bumper_b.png').convert_alpha()
bumper_c = pygame.image.load('favorite/assets/bumper_c.png').convert_alpha()
bumper_d = pygame.image.load('favorite/assets/bumper_d.png').convert_alpha()
odds = pygame.image.load('favorite/assets/odds.png').convert_alpha()
section = pygame.image.load('favorite/assets/section.png').convert_alpha()
selection1 = pygame.image.load('favorite/assets/selection1.png').convert_alpha()
selection2 = pygame.image.load('favorite/assets/selection2.png').convert_alpha()
selection3 = pygame.image.load('favorite/assets/selection3.png').convert_alpha()
selection4 = pygame.image.load('favorite/assets/selection4.png').convert_alpha()
selection5 = pygame.image.load('favorite/assets/selection5.png').convert_alpha()
selection6 = pygame.image.load('favorite/assets/selection6.png').convert_alpha()
selection7 = pygame.image.load('favorite/assets/selection7.png').convert_alpha()
favorite = pygame.image.load('favorite/assets/favorite.png').convert_alpha()
super_score = pygame.image.load('favorite/assets/super_score.png').convert_alpha()
abcd = pygame.image.load('favorite/assets/abcd.png').convert_alpha()
bg_menu = pygame.image.load('favorite/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('favorite/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('favorite/assets/backglass_off.png').convert_alpha()
ss1 = pygame.image.load('favorite/assets/ss1.png').convert_alpha()
ss2 = pygame.image.load('favorite/assets/ss2.png').convert_alpha()
ss3 = pygame.image.load('favorite/assets/ss3.png').convert_alpha()
ss4 = pygame.image.load('favorite/assets/ss4.png').convert_alpha()
ss5 = pygame.image.load('favorite/assets/ss5.png').convert_alpha()
ss6 = pygame.image.load('favorite/assets/ss6.png').convert_alpha()
ss7 = pygame.image.load('favorite/assets/ss7.png').convert_alpha()
ss8 = pygame.image.load('favorite/assets/ss8.png').convert_alpha()
ss9 = pygame.image.load('favorite/assets/ss9.png').convert_alpha()
ss10 = pygame.image.load('favorite/assets/ss10.png').convert_alpha()
ss20 = pygame.image.load('favorite/assets/ss20.png').convert_alpha()
ss30 = pygame.image.load('favorite/assets/ss30.png').convert_alpha()
ss40 = pygame.image.load('favorite/assets/ss40.png').convert_alpha()
one = pygame.image.load('favorite/assets/one.png').convert_alpha()
two = pygame.image.load('favorite/assets/two.png').convert_alpha()
three = pygame.image.load('favorite/assets/three.png').convert_alpha()
four = pygame.image.load('favorite/assets/four.png').convert_alpha()
five = pygame.image.load('favorite/assets/five.png').convert_alpha()
six = pygame.image.load('favorite/assets/six.png').convert_alpha()
seven = pygame.image.load('favorite/assets/seven.png').convert_alpha()
eight = pygame.image.load('favorite/assets/eight.png').convert_alpha()
nine = pygame.image.load('favorite/assets/nine.png').convert_alpha()
ten = pygame.image.load('favorite/assets/ten.png').convert_alpha()
twenty = pygame.image.load('favorite/assets/twenty.png').convert_alpha()
thirty = pygame.image.load('favorite/assets/thirty.png').convert_alpha()
forty = pygame.image.load('favorite/assets/forty.png').convert_alpha()
fifty = pygame.image.load('favorite/assets/fifty.png').convert_alpha()
sixty = pygame.image.load('favorite/assets/sixty.png').convert_alpha()
seventy = pygame.image.load('favorite/assets/seventy.png').convert_alpha()
eighty = pygame.image.load('favorite/assets/eighty.png').convert_alpha()
ninety = pygame.image.load('favorite/assets/ninety.png').convert_alpha()
one_hundred = pygame.image.load('favorite/assets/one_hundred.png').convert_alpha()
two_hundred = pygame.image.load('favorite/assets/two_hundred.png').convert_alpha()
added_place = pygame.image.load('favorite/assets/added_place.png').convert_alpha()
added_show = pygame.image.load('favorite/assets/added_show.png').convert_alpha()
added_win = pygame.image.load('favorite/assets/added_win.png').convert_alpha()
added_purse = pygame.image.load('favorite/assets/added_purse.png').convert_alpha()
added_x = pygame.image.load('favorite/assets/added_x.png').convert_alpha()
added_y = pygame.image.load('favorite/assets/added_y.png').convert_alpha()
added_z = pygame.image.load('favorite/assets/added_z.png').convert_alpha()

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
        p = [32,280]
        screen.blit(letter_f, p)
    if s.game.name.position >= 2:
        p = [77,270]
        screen.blit(letter_a, p)
    if s.game.name.position >= 3:
        p = [118,264]
        screen.blit(letter_v, p)
    if s.game.name.position >= 4:
        p = [183,262]
        screen.blit(letter_o, p)
    if s.game.name.position >= 5:
        p = [228,263]
        screen.blit(letter_r, p)
    if s.game.name.position >= 6:
        p = [274,266]
        screen.blit(letter_i, p)
    if s.game.name.position >= 7:
        p = [306,269]
        screen.blit(letter_t, p)
    if s.game.name.position == 8:
        p = [348,268]
        screen.blit(letter_e, p)

    if s.game.tilt.status == False:

        if s.game.lettera.status == True:
            p = [546,851]
            screen.blit(bumper_a, p)
        if s.game.letterb.status == True:
            p = [581,850]
            screen.blit(bumper_b, p)
        if s.game.letterc.status == True:
            p = [616,848]
            screen.blit(bumper_c, p)
        if s.game.letterd.status == True:
            p = [650,848]
            screen.blit(bumper_d, p)

        if s.game.feature_unit.position in [1,11,21,31,41]:
            p = [440,305]
            screen.blit(feature_1, p)
        if s.game.feature_unit.position in [2,12,22,32,42]:
            p = [473,302]
            screen.blit(feature_2, p)
        if s.game.feature_unit.position in [3,13,23,33,43]:
            p = [504,298]
            screen.blit(feature_3, p)
        if s.game.feature_unit.position in [4,14,24,34,44]:
            p = [536,296]
            screen.blit(feature_4, p)
        if s.game.feature_unit.position in [5,15,25,35,45]:
            p = [568,293]
            screen.blit(feature_5, p)
        if s.game.feature_unit.position in [6,16,26,36,46]:
            p = [602,293]
            screen.blit(feature_6, p)
        if s.game.feature_unit.position in [7,17,27,37,47]:
            p = [632,288]
            screen.blit(feature_7, p)
        if s.game.feature_unit.position in [8,18,28,38,48]:
            p = [438,338]
            screen.blit(feature_8, p)
        if s.game.feature_unit.position in [9,19,29,39,49]:
            p = [466,334]
            screen.blit(feature_9, p)
        if s.game.feature_unit.position in range(10,20):
            p = [500,332]
            screen.blit(feature_10, p)
        if s.game.feature_unit.position in range(20,30):
            p = [532,326]
            screen.blit(feature_20, p)
        if s.game.feature_unit.position in range(30,40):
            p = [566,330]
            screen.blit(feature_30, p)
        if s.game.feature_unit.position in range(40,50):
            p = [596,324]
            screen.blit(feature_40, p)
        if s.game.feature_unit.position == 50:
            p = [628,324]
            screen.blit(feature_50, p)

        if s.game.pennant.status == True:
            p = [542,199]
            screen.blit(super_score, p)

        if s.game.left.status == True:
            p = [463,226]
            screen.blit(favorite, p)
        if s.game.right.status == True:
            p = [622,218]
            screen.blit(abcd, p)

        if 1 in s.game.selection:
            p = [50,604]
            screen.blit(selection1, p)
        if 2 in s.game.selection:
            p = [28,756]
            screen.blit(selection2, p)
        if 3 in s.game.selection:
            p = [28,902]
            screen.blit(selection3, p)
        if 4 in s.game.selection:
            p = [156,898]
            screen.blit(selection4, p)
        if 5 in s.game.selection:
            p = [299,896]
            screen.blit(selection5, p)
        if 6 in s.game.selection:
            p = [438,898]
            screen.blit(selection6, p)
        if 7 in s.game.selection:
            p = [568,895]
            screen.blit(selection7, p)

        p = [170,574]
        screen.blit(section, p)
        if s.game.odds.position == 1:
            p = [300,570]
            screen.blit(odds, p)
        if s.game.odds.position == 2:
            p = [372,563]
            screen.blit(odds, p)
        if s.game.odds.position == 3:
            p = [444,554]
            screen.blit(odds, p)
        if s.game.odds.position == 4:
            p = [515,550]
            screen.blit(odds, p)
        if s.game.odds.position == 5:
            p = [587,542]
            screen.blit(odds, p)

        if s.game.coin.position == 1:
            p = [667,406]
            screen.blit(multiplier, p)
        if s.game.coin.position == 2:
            p = [667,442]
            screen.blit(multiplier, p)
        if s.game.coin.position == 3:
            p = [667,480]
            screen.blit(multiplier, p)
        if s.game.coin.position == 4:
            p = [667,520]
            screen.blit(multiplier, p)

        if s.game.purse_section.status == True:
            p = [444,366]
            screen.blit(added_purse, p)
        if s.game.show_section.status == True:
            p = [296,378]
            screen.blit(added_show, p)
        if s.game.place_section.status == True:
            p = [142,392]
            screen.blit(added_place, p)
        if s.game.win_section.status == True:
            p = [26,405]
            screen.blit(added_win, p)

        if s.game.horsex.status == True:
            p = [98,476]
            screen.blit(added_x, p)
        if s.game.horsey.status == True:
            p = [306,450]
            screen.blit(added_y, p)
        if s.game.horsez.status == True:
            p = [512,430]
            screen.blit(added_z, p)

    if s.game.replays:
        digits = [int(d) for d in list(str(s.game.replays))]
        if len(digits) == 3:
            if digits[0] != 0:
                if digits[0] == 1:
                    p = [678,1048]
                    screen.blit(one_hundred, p)
            if digits[1] != 0:
                if digits[1] == 1:
                    p = [377,1053]
                    screen.blit(ten, p)
                if digits[1] == 2:
                    p = [414,1052]
                    screen.blit(twenty, p)
                if digits[1] == 3:
                    p = [448,1052]
                    screen.blit(thirty, p)
                if digits[1] == 4:
                    p = [479,1050]
                    screen.blit(forty, p)
                if digits[1] == 5:
                    p = [514,1053]
                    screen.blit(fifty, p)
                if digits[1] == 6:
                    p = [548,1053]
                    screen.blit(sixty, p)
                if digits[1] == 7:
                    p = [580,1050]
                    screen.blit(seventy, p)
                if digits[1] == 8:
                    p = [612,1050]
                    screen.blit(eighty, p)
                if digits[1] == 9:
                    p = [644,1049]
                    screen.blit(ninety, p)
            if digits[2] != 0:
                if digits[2] == 1:
                    p = [82,1056]
                    screen.blit(one, p)
                if digits[2] == 2:
                    p = [112,1055]
                    screen.blit(two, p)
                if digits[2] == 3:
                    p = [148,1054]
                    screen.blit(three, p)
                if digits[2] == 4:
                    p = [182,1056]
                    screen.blit(four, p)
                if digits[2] == 5:
                    p = [214,1054]
                    screen.blit(five, p)
                if digits[2] == 6:
                    p = [250,1054]
                    screen.blit(six, p)
                if digits[2] == 7:
                    p = [284,1054]
                    screen.blit(seven, p)
                if digits[2] == 8:
                    p = [316,1054]
                    screen.blit(eight, p)
                if digits[2] == 9:
                    p = [350,1054]
                    screen.blit(nine, p)
        if len(digits) == 2:
            if digits[0] != 0:
                if digits[0] == 1:
                    p = [377,1053]
                    screen.blit(ten, p)
                if digits[0] == 2:
                    p = [414,1052]
                    screen.blit(twenty, p)
                if digits[0] == 3:
                    p = [448,1052]
                    screen.blit(thirty, p)
                if digits[0] == 4:
                    p = [479,1050]
                    screen.blit(forty, p)
                if digits[0] == 5:
                    p = [514,1053]
                    screen.blit(fifty, p)
                if digits[0] == 6:
                    p = [548,1053]
                    screen.blit(sixty, p)
                if digits[0] == 7:
                    p = [580,1050]
                    screen.blit(seventy, p)
                if digits[0] == 8:
                    p = [612,1050]
                    screen.blit(eighty, p)
                if digits[0] == 9:
                    p = [644,1049]
                    screen.blit(ninety, p)
            if digits[1] != 0:
                if digits[1] == 1:
                    p = [82,1056]
                    screen.blit(one, p)
                if digits[1] == 2:
                    p = [112,1055]
                    screen.blit(two, p)
                if digits[1] == 3:
                    p = [148,1054]
                    screen.blit(three, p)
                if digits[1] == 4:
                    p = [182,1056]
                    screen.blit(four, p)
                if digits[1] == 5:
                    p = [214,1054]
                    screen.blit(five, p)
                if digits[1] == 6:
                    p = [250,1054]
                    screen.blit(six, p)
                if digits[1] == 7:
                    p = [284,1054]
                    screen.blit(seven, p)
                if digits[1] == 8:
                    p = [316,1054]
                    screen.blit(eight, p)
                if digits[1] == 9:
                    p = [350,1054]
                    screen.blit(nine, p)
        if len(digits) == 1:
            if digits[0] != 0:
                if digits[0] == 1:
                    p = [82,1056]
                    screen.blit(one, p)
                if digits[0] == 2:
                    p = [112,1055]
                    screen.blit(two, p)
                if digits[0] == 3:
                    p = [148,1054]
                    screen.blit(three, p)
                if digits[0] == 4:
                    p = [182,1056]
                    screen.blit(four, p)
                if digits[0] == 5:
                    p = [214,1054]
                    screen.blit(five, p)
                if digits[0] == 6:
                    p = [250,1054]
                    screen.blit(six, p)
                if digits[0] == 7:
                    p = [284,1054]
                    screen.blit(seven, p)
                if digits[0] == 8:
                    p = [316,1054]
                    screen.blit(eight, p)
                if digits[0] == 9:
                    p = [350,1054]
                    screen.blit(nine, p)

    if s.game.tilt.status == True:
        tilt_position = [294,197]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def selection_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if 1 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (50,604), pygame.Rect(50,604,73,133)))
    if 2 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (28,756), pygame.Rect(28,756,118,129)))
    if 3 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (28,902), pygame.Rect(28,902,120,129)))
    if 4 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (156,898), pygame.Rect(156,898,122,129)))
    if 5 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (299,896), pygame.Rect(299,896,117,130)))
    if 6 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (438,898), pygame.Rect(438,898,118,125)))
    if 7 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (568,895), pygame.Rect(568,895,115,127)))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [50,604]
            dirty_rects.append(screen.blit(selection1, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [28,756]
            dirty_rects.append(screen.blit(selection2, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection:
            p = [28,902]
            dirty_rects.append(screen.blit(selection3, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection:
            p = [156,898]
            dirty_rects.append(screen.blit(selection4, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection:
            p = [299,896]
            dirty_rects.append(screen.blit(selection5, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [438,898]
            dirty_rects.append(screen.blit(selection6, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [568,895]
            dirty_rects.append(screen.blit(selection7, p))

    pygame.display.update(dirty_rects)
    return

def star_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]
    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (300,570), pygame.Rect(300,570,118,293)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (372,563), pygame.Rect(372,563,118,293)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (444,554), pygame.Rect(444,554,118,293)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (515,550), pygame.Rect(515,550,118,293)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (587,542), pygame.Rect(587,542,118,293)))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [300,570]
            dirty_rects.append(screen.blit(odds, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [372,563]
            dirty_rects.append(screen.blit(odds, p))
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [444,554]
            dirty_rects.append(screen.blit(odds, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [515,550]
            dirty_rects.append(screen.blit(odds, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [587,542]
            dirty_rects.append(screen.blit(odds, p))

    dirty_rects.append(screen.blit(bg_gi, (170,574), pygame.Rect(170,574,174,305)))
    p = [170,574]
    dirty_rects.append(screen.blit(section, p))

    if s.game.coin.position == 4:
        dirty_rects.append(screen.blit(bg_gi, (667,520), pygame.Rect(667,520,42,37)))
        p = [667,520]
        dirty_rects.append(screen.blit(multiplier, p))

    pygame.display.update(dirty_rects)
    return

