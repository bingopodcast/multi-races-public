import pygame
import random

pygame.display.set_caption("Multi Races")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])
pygame.mouse.set_visible(False)

type_image = pygame.image.load('trophy/assets/type.png').convert_alpha()
trophy = pygame.image.load('trophy/assets/trophy.png').convert_alpha()
tilt = pygame.image.load('trophy/assets/tilt.png').convert_alpha()
show_win = pygame.image.load('trophy/assets/show_win.png').convert_alpha()
selection = pygame.image.load('trophy/assets/selection.png').convert_alpha()
purse_win = pygame.image.load('trophy/assets/purse_win.png').convert_alpha()
odds = pygame.image.load('trophy/assets/odds.png').convert_alpha()
feature = pygame.image.load('trophy/assets/feature.png').convert_alpha()
horseshoe = pygame.image.load('trophy/assets/horseshoe.png').convert_alpha()
letter_t = pygame.image.load('trophy/assets/letter_t.png').convert_alpha()
letter_r = pygame.image.load('trophy/assets/letter_r.png').convert_alpha()
letter_o = pygame.image.load('trophy/assets/letter_o.png').convert_alpha()
letter_p = pygame.image.load('trophy/assets/letter_p.png').convert_alpha()
letter_h = pygame.image.load('trophy/assets/letter_h.png').convert_alpha()
letter_y = pygame.image.load('trophy/assets/letter_y.png').convert_alpha()
bg_menu = pygame.image.load('trophy/assets/backglass_menu.png').convert_alpha()
bg_gi = pygame.image.load('trophy/assets/backglass_gi.png').convert_alpha()
bg_off = pygame.image.load('trophy/assets/backglass_off.png').convert_alpha()

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

    p = [149,278]
    screen.blit(letter_t, p)
    if s.game.name.position >= 1:
        p = [217,274]
        screen.blit(letter_r, p)
    if s.game.name.position >= 2:
        p = [286,272]
        screen.blit(letter_o, p)
    if s.game.name.position >= 3:
        p = [352,270]
        screen.blit(letter_p, p)
    if s.game.name.position >= 4:
        p = [422,274]
        screen.blit(letter_h, p)
    if s.game.name.position >= 5:
        p = [490,280]
        screen.blit(letter_y, p)

    if s.game.tilt.status == False:
        if 1 in s.game.selection:
            p = [-6,488]
            screen.blit(selection, p)
        if 2 in s.game.selection:
            p = [27,374]
            screen.blit(selection, p)
        if 3 in s.game.selection:
            p = [155,348]
            screen.blit(selection, p)
        if 4 in s.game.selection:
            p = [282,350]
            screen.blit(selection, p)
        if 5 in s.game.selection:
            p = [415,350]
            screen.blit(selection, p)
        if 6 in s.game.selection:
            p = [548,370]
            screen.blit(selection, p)
        if 7 in s.game.selection:
            p = [572,500]
            screen.blit(selection, p)

        if s.game.coin.position == 1:
            p = [85,810]
            screen.blit(odds, p)
        if s.game.coin.position == 2:
            p = [85,750]
            screen.blit(odds, p)
        if s.game.coin.position == 3:
            p = [87,692]
            screen.blit(odds, p)
        if s.game.coin.position == 4:
            p = [90,634]
            screen.blit(odds, p)

        if s.game.odds.position == 1:
            p = [97,952]
            screen.blit(type_image, p)
        if s.game.odds.position == 2:
            p = [167,980]
            screen.blit(type_image, p)
        if s.game.odds.position == 3:
            p = [232,1006]
            screen.blit(type_image, p)
        if s.game.odds.position == 4:
            p = [300,1039]
            screen.blit(type_image, p)
        if s.game.odds.position == 5:
            p = [360,1083]
            screen.blit(type_image, p)

        if s.game.horseshoe.status == True:
            p = [319,482]
            screen.blit(horseshoe, p)

        if s.game.pennant.status == True:
            p = [160,508]
            screen.blit(feature, p)
        if s.game.left.status == True:
            p = [127,550]
            screen.blit(trophy, p)
        if s.game.right.status == True:
            p = [502,549]
            screen.blit(trophy, p)
        if s.game.purse_win.status == True:
            p = [244,562]
            screen.blit(purse_win, p)
        if s.game.show_win.status == True:
            p = [246,594]
            screen.blit(show_win, p)


    if s.game.tilt.status == True:
        tilt_position = [464,508]
        screen.blit(tilt, tilt_position)

    pygame.display.update()

def selection_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]

    if s.game.left.status == False:
        dirty_rects.append(screen.blit(bg_gi, (127,550), pygame.Rect(127,550,68,93)))
    if s.game.right.status == False:
        dirty_rects.append(screen.blit(bg_gi, (502,549), pygame.Rect(502,549,68,93)))

    if 1 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (-6,488), pygame.Rect(-6,488,134,128)))
    if 2 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (27,374), pygame.Rect(27,374,134,128)))
    if 3 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (155,348), pygame.Rect(155,348,134,128)))
    if 4 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (282,350), pygame.Rect(282,350,134,128)))
    if 5 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (415,350), pygame.Rect(415,350,134,128)))
    if 6 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (548,370), pygame.Rect(548,370,134,128)))
    if 7 not in s.game.selection:
        dirty_rects.append(screen.blit(bg_gi, (572,500), pygame.Rect(572,500,134,128)))

    if num in [5,20,30,40]:
        if s.game.left.status == False:
            p = [127,550]
            dirty_rects.append(screen.blit(trophy, p))
    if num in [0,10,25,35,45]:
        if s.game.right.status == False:
            p = [502,549]
            dirty_rects.append(screen.blit(trophy, p))

    if num in [0,10,20,30,40,50]:
        if 1 not in s.game.selection:
            p = [-6,488]
            dirty_rects.append(screen.blit(selection, p))
    if num in [1,11,21,31,41]:
        if 2 not in s.game.selection:
            p = [27,374]
            dirty_rects.append(screen.blit(selection, p))
    if num in [2,12,22,32,42]:
        if 3 not in s.game.selection:
            p = [155,348]
            dirty_rects.append(screen.blit(selection, p))
    if num in [3,13,23,33,43]:
        if 4 not in s.game.selection:
            p = [282,350]
            dirty_rects.append(screen.blit(selection, p))
    if num in [4,14,24,34,44]:
        if 5 not in s.game.selection:
            p = [415,350]
            dirty_rects.append(screen.blit(selection, p))
    if num in [5,15,25,35,45]:
        if 6 not in s.game.selection:
            p = [548,370]
            dirty_rects.append(screen.blit(selection, p))
    if num in [6,16,26,36,46]:
        if 7 not in s.game.selection:
            p = [572,500]
            dirty_rects.append(screen.blit(selection, p))

    pygame.display.update(dirty_rects)

def clover_animation(args):
    return

def feature_animation(args):
    return

def star_animation(args):
    global screen

    dirty_rects = []
    s = args[0]
    num = args[1]
    
    if s.game.purse_win.status == False:
        dirty_rects.append(screen.blit(bg_gi, (244,562), pygame.Rect(244,562,216,23)))
    if s.game.show_win.status == False:
        dirty_rects.append(screen.blit(bg_gi, (246,594), pygame.Rect(246,594,226,25)))

    if s.game.odds.position != 1:
        dirty_rects.append(screen.blit(bg_gi, (97,952), pygame.Rect(97,952,225,13)))
    if s.game.odds.position != 2:
        dirty_rects.append(screen.blit(bg_gi, (167,980), pygame.Rect(167,980,225,13)))
    if s.game.odds.position != 3:
        dirty_rects.append(screen.blit(bg_gi, (232,1006), pygame.Rect(232,1006,225,13)))
    if s.game.odds.position != 4:
        dirty_rects.append(screen.blit(bg_gi, (300,1039), pygame.Rect(300,1039,225,13)))
    if s.game.odds.position != 5:
        dirty_rects.append(screen.blit(bg_gi, (360,1083), pygame.Rect(360,1083,225,13)))

    if num in [8,10,16,18,20,22,28,35,37,40,42,46,49]:
        if s.game.purse_win.status == False:
            p = [244,562]
            dirty_rects.append(screen.blit(purse_win, p))
    if num in [2,4,17,25,32,36,41,44,48]:
        if s.game.show_win.status == False:
            p = [246,594]
            dirty_rects.append(screen.blit(show_win, p))

    if num in [0,10,20,30,40,50]:
        if s.game.odds.position != 1:
            p = [97,952]
            dirty_rects.append(screen.blit(type_image, p))
    if num in [1,11,21,31,41]:
        if s.game.odds.position != 2:
            p = [167,980]
            dirty_rects.append(screen.blit(type_image, p))
    if num in [2,12,22,32,42]:
        if s.game.odds.position != 3:
            p = [232,1006]
            dirty_rects.append(screen.blit(type_image, p))
    if num in [3,13,23,33,43]:
        if s.game.odds.position != 4:
            p = [300,1039]
            dirty_rects.append(screen.blit(type_image, p))
    if num in [4,14,24,34,44]:
        if s.game.odds.position != 5:
            p = [360,1083]
            dirty_rects.append(screen.blit(type_image, p))

    pygame.display.update(dirty_rects)
    return

