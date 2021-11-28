import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

tilt = pygame.image.load('victory_derby/assets/tilt.png').convert_alpha()
dd = pygame.image.load('victory_derby/assets/dd.png').convert_alpha()
dd_middle = pygame.image.load('victory_derby/assets/dd_middle.png').convert_alpha()
feature = pygame.image.load('victory_derby/assets/feature.png').convert_alpha()
flag_left = pygame.image.load('victory_derby/assets/flag_left.png').convert_alpha()
flag_right = pygame.image.load('victory_derby/assets/flag_right.png').convert_alpha()
horse1 = pygame.image.load('victory_derby/assets/horse1.png').convert_alpha()
horse2 = pygame.image.load('victory_derby/assets/horse2.png').convert_alpha()
horse3 = pygame.image.load('victory_derby/assets/horse3.png').convert_alpha()
horse4 = pygame.image.load('victory_derby/assets/horse4.png').convert_alpha()
horse5 = pygame.image.load('victory_derby/assets/horse5.png').convert_alpha()
horse6 = pygame.image.load('victory_derby/assets/horse6.png').convert_alpha()
horse7 = pygame.image.load('victory_derby/assets/horse7.png').convert_alpha()
letter_d = pygame.image.load('victory_derby/assets/letter_d.png').convert_alpha()
letter_e = pygame.image.load('victory_derby/assets/letter_e.png').convert_alpha()
letter_r = pygame.image.load('victory_derby/assets/letter_r.png').convert_alpha()
letter_b = pygame.image.load('victory_derby/assets/letter_b.png').convert_alpha()
letter_y = pygame.image.load('victory_derby/assets/letter_y.png').convert_alpha()
multiplier_1 = pygame.image.load('victory_derby/assets/multiplier_1.png').convert_alpha()
multiplier_2 = pygame.image.load('victory_derby/assets/multiplier_2.png').convert_alpha()
multiplier_3 = pygame.image.load('victory_derby/assets/multiplier_3.png').convert_alpha()
multiplier_4 = pygame.image.load('victory_derby/assets/multiplier_4.png').convert_alpha()
odds = pygame.image.load('victory_derby/assets/odds.png').convert_alpha()
section = pygame.image.load('victory_derby/assets/section.png').convert_alpha()
selection1 = pygame.image.load('victory_derby/assets/selection1.png').convert_alpha()
selection4 = pygame.image.load('victory_derby/assets/selection4.png').convert_alpha()
selection7 = pygame.image.load('victory_derby/assets/selection7.png').convert_alpha()
dd_win1 = pygame.image.load('victory_derby/assets/dd_win1.png').convert_alpha()
dd_win2 = pygame.image.load('victory_derby/assets/dd_win2.png').convert_alpha()
bg_menu = pygame.image.load('victory_derby/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('victory_derby/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('victory_derby/assets/backglass_off.png').convert_alpha()

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
        p = [414,388]
        screen.blit(letter_d, p)
    if s.game.name.position >= 2:
        p = [464,394]
        screen.blit(letter_e, p)
    if s.game.name.position >= 3:
        p = [508,402]
        screen.blit(letter_r, p)
    if s.game.name.position >= 4:
        p = [556,414]
        screen.blit(letter_b, p)
    if s.game.name.position >= 5:
        p = [604,430]
        screen.blit(letter_y, p)

   

    if s.game.tilt.status == False:
        if 1 in s.game.selection:
            p = [23,567]
            screen.blit(selection1, p)
        if 2 in s.game.selection:
            p = [122,544]
            screen.blit(selection1, p)
        if 3 in s.game.selection:
            p = [219,522]
            screen.blit(selection1, p)
        if 4 in s.game.selection:
            p = [314,497]
            screen.blit(selection4, p)
        if 5 in s.game.selection:
            p = [408,520]
            screen.blit(selection7, p)
        if 6 in s.game.selection:
            p = [502,541]
            screen.blit(selection7, p)
        if 7 in s.game.selection:
            p = [601,565]
            screen.blit(selection7, p)

        p = [76,791]
        screen.blit(section, p)
        p = [76,848]
        screen.blit(section, p)
        p = [76,913]
        screen.blit(section, p)
        p = [76,973]
        screen.blit(section, p)
        if s.game.odds.position == 1:
            p = [552,788]
            screen.blit(odds, p)
            p = [552,850]
            screen.blit(odds, p)
            p = [552,912]
            screen.blit(odds, p)
            p = [552,974]
            screen.blit(odds, p)
        if s.game.odds.position == 2:
            p = [462,788]
            screen.blit(odds, p)
            p = [462,850]
            screen.blit(odds, p)
            p = [462,912]
            screen.blit(odds, p)
            p = [462,974]
            screen.blit(odds, p)
        if s.game.odds.position == 3:
            p = [374,788]
            screen.blit(odds, p)
            p = [374,850]
            screen.blit(odds, p)
            p = [374,912]
            screen.blit(odds, p)
            p = [374,974]
            screen.blit(odds, p)
        if s.game.odds.position == 4:
            p = [286,788]
            screen.blit(odds, p)
            p = [286,850]
            screen.blit(odds, p)
            p = [286,912]
            screen.blit(odds, p)
            p = [286,974]
            screen.blit(odds, p)
        if s.game.odds.position == 5:
            p = [196,788]
            screen.blit(odds, p)
            p = [196,850]
            screen.blit(odds, p)
            p = [196,912]
            screen.blit(odds, p)
            p = [196,974]
            screen.blit(odds, p)

        if s.game.pennant.status == True:
            p = [444,282]
            screen.blit(feature, p)
        if s.game.left.status == True:
            p = [0,396]
            screen.blit(flag_left, p)
        if s.game.right.status == True:
            p = [652,378]
            screen.blit(flag_right, p)

        if s.game.coin.position == 1:
            p = [290,746]
            screen.blit(multiplier_1, p)
        if s.game.coin.position == 2:
            p = [320,730]
            screen.blit(multiplier_2, p)
        if s.game.coin.position == 3:
            p = [361,724]
            screen.blit(multiplier_3, p)
        if s.game.coin.position == 4:
            p = [393,742]
            screen.blit(multiplier_4, p)

        if s.game.dd1 == 1:
            p = [81,694]
            screen.blit(dd, p)
        if s.game.dd1 == 2:
            p = [181,672]
            screen.blit(dd, p)
        if s.game.dd1 == 3:
            p = [276,648]
            screen.blit(dd, p)
        if s.game.dd1 == 4:
            p = [323,610]
            screen.blit(dd_middle, p)
        if s.game.dd2 == 5:
            p = [416,650]
            screen.blit(dd, p)
        if s.game.dd2 == 6:
            p = [510,672]
            screen.blit(dd, p)
        if s.game.dd2 == 7:
            p = [606,693]
            screen.blit(dd, p)

            
        if s.game.horse1.status == True:
            p = [20,694]
            screen.blit(horse1, p)
        if s.game.horse2.status == True:
            p = [120,671]
            screen.blit(horse2, p)
        if s.game.horse3.status == True:
            p = [218,645]
            screen.blit(horse3, p)
        if s.game.horse4.status == True:
            p = [342,614]
            screen.blit(horse4, p)
        if s.game.horse5.status == True:
            p = [432,645]
            screen.blit(horse5, p)
        if s.game.horse6.status == True:
            p = [520,670]
            screen.blit(horse6, p)
        if s.game.horse7.status == True:
            p = [618,698]
            screen.blit(horse7, p)

        if s.game.daily_double_win1.status == True:
            p = [166,706]
            screen.blit(dd_win1, p)
        if s.game.daily_double_win2.status == True:
            p = [396,706]
            screen.blit(dd_win2, p)

    if s.game.tilt.status == True:
        tilt_position = [626,310]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def selection_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.left.status == False:
        dirty_rects.append(screen.blit(bg_gi, (0,396), pygame.Rect(0,396,81,44)))
    if s.game.right.status == False:
        dirty_rects.append(screen.blit(bg_gi, (652,378), pygame.Rect(652,378,67,43)))

    if 1 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (23,567), pygame.Rect(23,567,98,124)))
    if 2 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (122,544), pygame.Rect(122,544,98,124)))
    if 3 not in s.game.selection or s.game.hold3.status == False:
        dirty_rects.append(screen.blit(bg_gi, (219,522), pygame.Rect(219,522,98,124)))
    if 4 not in s.game.selection or s.game.hold4.status == False:
        dirty_rects.append(screen.blit(bg_gi, (314,497), pygame.Rect(314,497,95,112)))
    if 5 not in s.game.selection or s.game.hold5.status == False:
        dirty_rects.append(screen.blit(bg_gi, (408,520), pygame.Rect(408,520,99,125)))
    if 6 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (502,541), pygame.Rect(502,541,99,125)))
    if 7 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (601,565), pygame.Rect(601,565,99,125)))

    if num in [5,20,30,40]:
        if s.game.left.status == False:
            p = [0,396]
            dirty_rects.append(screen.blit(flag_left, p))
    if num in [0,10,25,35,45]:
        if s.game.right.status == False:
            p = [652,378]
            dirty_rects.append(screen.blit(flag_right, p))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [23,567]
            dirty_rects.append(screen.blit(selection1, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [122,544]
            dirty_rects.append(screen.blit(selection1, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection:
            p = [219,522]
            dirty_rects.append(screen.blit(selection1, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection:
            p = [314,497]
            dirty_rects.append(screen.blit(selection4, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection:
            p = [408,520]
            dirty_rects.append(screen.blit(selection7, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [502,541]
            dirty_rects.append(screen.blit(selection7, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [601,565]
            dirty_rects.append(screen.blit(selection7, p))

    pygame.display.update(dirty_rects)
    return

def star_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (552,788), pygame.Rect(552,788,88,62)))
        dirty_rects.append(screen.blit(bg_gi, (552,850), pygame.Rect(552,850,88,62)))
        dirty_rects.append(screen.blit(bg_gi, (552,912), pygame.Rect(552,912,88,62)))
        dirty_rects.append(screen.blit(bg_gi, (552,974), pygame.Rect(552,974,88,62)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (462,788), pygame.Rect(462,788,88,62)))
        dirty_rects.append(screen.blit(bg_gi, (462,850), pygame.Rect(462,850,88,62)))
        dirty_rects.append(screen.blit(bg_gi, (462,912), pygame.Rect(462,912,88,62)))
        dirty_rects.append(screen.blit(bg_gi, (462,974), pygame.Rect(462,974,88,62)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (374,788), pygame.Rect(374,788,88,62)))
        dirty_rects.append(screen.blit(bg_gi, (374,850), pygame.Rect(374,850,88,62)))
        dirty_rects.append(screen.blit(bg_gi, (374,912), pygame.Rect(374,912,88,62)))
        dirty_rects.append(screen.blit(bg_gi, (374,974), pygame.Rect(374,974,88,62)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (286,788), pygame.Rect(286,788,88,62)))
        dirty_rects.append(screen.blit(bg_gi, (286,850), pygame.Rect(286,850,88,62)))
        dirty_rects.append(screen.blit(bg_gi, (286,912), pygame.Rect(286,912,88,62)))
        dirty_rects.append(screen.blit(bg_gi, (286,974), pygame.Rect(286,974,88,62)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (196,788), pygame.Rect(196,788,88,62)))
        dirty_rects.append(screen.blit(bg_gi, (196,850), pygame.Rect(196,850,88,62)))
        dirty_rects.append(screen.blit(bg_gi, (196,912), pygame.Rect(196,912,88,62)))
        dirty_rects.append(screen.blit(bg_gi, (196,974), pygame.Rect(196,974,88,62)))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [552,788]
            dirty_rects.append(screen.blit(odds, p))
            p = [552,850]
            dirty_rects.append(screen.blit(odds, p))
            p = [552,912]
            dirty_rects.append(screen.blit(odds, p))
            p = [552,974]
            dirty_rects.append(screen.blit(odds, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [462,788]
            dirty_rects.append(screen.blit(odds, p))
            p = [462,850]
            dirty_rects.append(screen.blit(odds, p))
            p = [462,912]
            dirty_rects.append(screen.blit(odds, p))
            p = [462,974]
            dirty_rects.append(screen.blit(odds, p))
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [374,788]
            dirty_rects.append(screen.blit(odds, p))
            p = [374,850]
            dirty_rects.append(screen.blit(odds, p))
            p = [374,912]
            dirty_rects.append(screen.blit(odds, p))
            p = [374,974]
            dirty_rects.append(screen.blit(odds, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [286,788]
            dirty_rects.append(screen.blit(odds, p))
            p = [286,850]
            dirty_rects.append(screen.blit(odds, p))
            p = [286,912]
            dirty_rects.append(screen.blit(odds, p))
            p = [286,974]
            dirty_rects.append(screen.blit(odds, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [196,788]
            dirty_rects.append(screen.blit(odds, p))
            p = [196,850]
            dirty_rects.append(screen.blit(odds, p))
            p = [196,912]
            dirty_rects.append(screen.blit(odds, p))
            p = [196,974]
            dirty_rects.append(screen.blit(odds, p))

    pygame.display.update(dirty_rects)
    return

