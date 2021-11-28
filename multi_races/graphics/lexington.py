import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

tilt = pygame.image.load('lexington/assets/tilt.png').convert_alpha()
button = pygame.image.load('lexington/assets/button.png').convert_alpha()
left_cap = pygame.image.load('lexington/assets/left.png').convert_alpha()
odds = pygame.image.load('lexington/assets/odds.png').convert_alpha()
right_cap = pygame.image.load('lexington/assets/right.png').convert_alpha()
scores_win = pygame.image.load('lexington/assets/scores_win.png').convert_alpha()
section = pygame.image.load('lexington/assets/section.png').convert_alpha()
selection = pygame.image.load('lexington/assets/selection.png').convert_alpha()
lexi = pygame.image.load('lexington/assets/lexi.png').convert_alpha()
letter_n = pygame.image.load('lexington/assets/letter_n.png').convert_alpha()
letter_g = pygame.image.load('lexington/assets/letter_g.png').convert_alpha()
letter_t = pygame.image.load('lexington/assets/letter_t.png').convert_alpha()
letter_o = pygame.image.load('lexington/assets/letter_o.png').convert_alpha()
letter_n2 = pygame.image.load('lexington/assets/letter_n2.png').convert_alpha()
bg_menu = pygame.image.load('lexington/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('lexington/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('lexington/assets/backglass_off.png').convert_alpha()

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
    
    p = [150,250]
    screen.blit(lexi, p)
    if s.game.name.position >= 1:
        p = [389,278]
        screen.blit(letter_n, p)
    if s.game.name.position >= 2:
        p = [449,272]
        screen.blit(letter_g, p)
    if s.game.name.position >= 3:
        p = [508,262]
        screen.blit(letter_t, p)
    if s.game.name.position >= 4:
        p = [568,254]
        screen.blit(letter_o, p)
    if s.game.name.position >= 5:
        p = [623,253]
        screen.blit(letter_n2, p)

    if s.game.tilt.status == False:

        if 1 in s.game.selection or s.game.fan.status == True:
            p = [33,684]
            screen.blit(selection, p)
        if 2 in s.game.selection or s.game.fan.status == True:
            p = [31,842]
            screen.blit(selection, p)
        if 3 in s.game.selection or s.game.fan.status == True:
            p = [168,840]
            screen.blit(selection, p)
        if 4 in s.game.selection or s.game.fan.status == True:
            p = [305,838]
            screen.blit(selection, p)
        if 5 in s.game.selection or s.game.fan.status == True:
            p = [440,840]
            screen.blit(selection, p)
        if 6 in s.game.selection or s.game.fan.status == True:
            p = [577,840]
            screen.blit(selection, p)
        if 7 in s.game.selection or s.game.fan.status == True:
            p = [576,690]
            screen.blit(selection, p)

        if s.game.horseshoe.status == True:
            p = [345,678]
            screen.blit(button, p)
        if s.game.left.status == True:
            p = [191,684]
            screen.blit(left_cap, p)
        if s.game.right.status == True:
            p = [490,684]
            screen.blit(right_cap, p)
        if s.game.purse_win.status == True:
            p = [213,740]
            screen.blit(scores_win, p)
        if s.game.show_win.status == True:
            p = [208,779]
            screen.blit(scores_win, p)
      
        #Odds displays always shown unless tilted
        p = [26,444]
        screen.blit(section, p)

        if s.game.odds.position == 1:
            p = [120,443]
            screen.blit(odds, p)
        if s.game.odds.position == 2:
            p = [180,444]
            screen.blit(odds, p)
        if s.game.odds.position == 3:
            p = [240,444]
            screen.blit(odds, p)
        if s.game.odds.position == 4:
            p = [298,446]
            screen.blit(odds, p)
        if s.game.odds.position == 5:
            p = [360,445]
            screen.blit(odds, p)
        if s.game.odds.position == 6:
            p = [417,446]
            screen.blit(odds, p)
        if s.game.odds.position == 7:
            p = [474,446]
            screen.blit(odds, p)
        if s.game.odds.position == 8:
            p = [534,444]
            screen.blit(odds, p)
        if s.game.odds.position == 9:
            p = [594,444]
            screen.blit(odds, p)
        if s.game.odds.position == 10:
            p = [652,444]
            screen.blit(odds, p)

    if s.game.tilt.status == True:
        tilt_position = [193,639]
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
        dirty_rects.append(screen.blit(bg_gi, (191,684), pygame.Rect(191,684,58,40)))
    if s.game.right.status == False:
        dirty_rects.append(screen.blit(bg_gi, (490,684), pygame.Rect(490,684,56,39)))

    if 1 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (33,684), pygame.Rect(33,684,131,143)))
    if 2 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (31,842), pygame.Rect(31,842,131,143)))
    if 3 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (168,840), pygame.Rect(168,840,131,143)))
    if 4 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (305,838), pygame.Rect(305,838,131,143)))
    if 5 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (440,840), pygame.Rect(440,840,131,143)))
    if 6 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (577,840), pygame.Rect(577,840,131,143)))
    if 7 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (576,690), pygame.Rect(576,690,131,143)))

    if num in [5,20,30,40]:
        if s.game.left.status == False:
            p = [191,684]
            dirty_rects.append(screen.blit(left_cap, p))
    if num in [0,10,25,35,45]:
        if s.game.right.status == False:
            p = [490,684]
            dirty_rects.append(screen.blit(right_cap, p))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [33,684]
            dirty_rects.append(screen.blit(selection, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [31,842]
            dirty_rects.append(screen.blit(selection, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection:
            p = [168,840]
            dirty_rects.append(screen.blit(selection, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection:
            p = [305,838]
            dirty_rects.append(screen.blit(selection, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection:
            p = [440,840]
            dirty_rects.append(screen.blit(selection, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [577,840]
            dirty_rects.append(screen.blit(selection, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [576,690]
            dirty_rects.append(screen.blit(selection, p))

    pygame.display.update(dirty_rects)
    return

def star_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]


    if s.game.purse_win.status == False:
        dirty_rects.append(screen.blit(bg_gi, (213,740), pygame.Rect(213,740,326,50)))
    if s.game.show_win.status == False:
        dirty_rects.append(screen.blit(bg_gi, (208,779), pygame.Rect(208,779,326,50)))

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (120,443), pygame.Rect(120,443,60,223)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (180,444), pygame.Rect(180,444,60,223)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (240,444), pygame.Rect(240,444,60,223)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (298,446), pygame.Rect(298,446,60,223)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (360,445), pygame.Rect(360,445,60,223)))
    if s.game.odds.position != 6:
        dirty_rects.append(screen.blit(bg_gi, (417,446), pygame.Rect(417,446,60,223)))
    if s.game.odds.position != 7:
        dirty_rects.append(screen.blit(bg_gi, (474,446), pygame.Rect(474,446,60,223)))
    if s.game.odds.position != 8:
        dirty_rects.append(screen.blit(bg_gi, (534,444), pygame.Rect(534,444,60,223)))
    if s.game.odds.position != 9:
        dirty_rects.append(screen.blit(bg_gi, (594,444), pygame.Rect(594,444,60,223)))
    if s.game.odds.position != 10:
        dirty_rects.append(screen.blit(bg_gi, (652,444), pygame.Rect(652,444,60,223)))

    if num in [8,10,16,18,20,22,28,35,37,40,42,46,49]:
        if s.game.purse_win.status == False:
            p = [213,740]
            dirty_rects.append(screen.blit(scores_win, p))
    if num in [2,4,17,25,32,36,41,44,48]:
        if s.game.show_win.status == False:
            p = [208,779]
            dirty_rects.append(screen.blit(scores_win, p))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [120,443]
            dirty_rects.append(screen.blit(odds, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [180,444]
            dirty_rects.append(screen.blit(odds, p))
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [240,444]
            dirty_rects.append(screen.blit(odds, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [298,446]
            dirty_rects.append(screen.blit(odds, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [360,445]
            dirty_rects.append(screen.blit(odds, p))
    if num in [5,15,25,35,45]:
        if s.game.odds.position != 6:
            p = [417,446]
            dirty_rects.append(screen.blit(odds, p))
    if num in [6,16,26,36,46]:
        if s.game.odds.position != 7:
            p = [474,446]
            dirty_rects.append(screen.blit(odds, p))
    if num in [7,17,27,37,47]:
        if s.game.odds.position != 8:
            p = [534,444]
            dirty_rects.append(screen.blit(odds, p))
    if num in [8,18,28,38,48]:
        if s.game.odds.position != 9:
            p = [594,444]
            dirty_rects.append(screen.blit(odds, p))
    if num in [9,19,29,39,49]:
        if s.game.odds.position != 10:
            p = [652,444]
            dirty_rects.append(screen.blit(odds, p))

    pygame.display.update(dirty_rects)
    return

