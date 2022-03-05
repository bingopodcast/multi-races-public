#!/usr/bin/python
import pygame
import time
import turf_king, grandstand, futurity, victory_derby, victory_special, winner, photo_finish, old_hilltop, new_daily_races, arlington, derby_41, preakness, sport_page, fairgrounds, pace_maker, grandstand_38, seabiscuit, thistledowns, grand_national, dark_horse, long_shot, hawthorne, jockey_club_41, pimlico, longacres, citation, lexington, special_entry, bally_entry, jockey_special, champion, kentucky, gold_cup, trophy, sunshine_park, favorite, winning_ticket, santa_anita, record_time

def replay_step_up(pos, reel1, reel10, reel100, reel1000=False):
    delta_y = 38

    r1x = reel1.position[0]
    r10x = reel10.position[0]
    r100x = reel100.position[0]
    if reel1000 is not False:
        r1000x = reel1000.position[0]

    if (pos) % 10 == 0 and not (pos) % 100 == 0:
        reel1.position = [r1x,reel1.default_y]
        reel10.position = [r10x,reel10.position[1] - delta_y]
    elif (pos) % 100 == 0 and not (pos) % 1000 == 0:
        reel1.position = [r1x,reel1.default_y]
        reel10.position = [r10x,reel10.default_y]
        reel100.position = [r100x,reel100.position[1] - delta_y]
    elif (pos) % 1000 == 0:
        reel1.position = [r1x,reel1.default_y]
        reel10.position = [r10x,reel10.default_y]
        reel100.position = [r100x,reel100.default_y]
        reel1000.position = [r1000x,reel1000.position[1] - delta_y]
    else:
        reel1.position = [r1x,reel1.position[1] - delta_y]

def replay_step_down(pos, reel1, reel10, reel100, reel1000=False):
    delta_y = 38 

    r1x = reel1.position[0]
    r10x = reel10.position[0]
    r100x = reel100.position[0]
    if reel1000 is not False:
        r1000x = reel1000.position[0]

    if (pos + 1) % 10 == 0 and not (pos + 1) % 100 == 0:
        reel1.position = [r1x,reel1.default_y - delta_y * 9]
        reel10.position = [r10x,reel10.position[1] + delta_y]
    elif (pos + 1) % 100 == 0 and not (pos + 1) % 1000 == 0:
        reel1.position = [r1x,reel1.default_y - delta_y * 9]
        reel10.position = [r10x,reel10.default_y - delta_y * 9]
        reel100.position = [r100x,reel100.position[1] + delta_y]
    elif (pos + 1) % 1000 == 0:
        reel1.position = [r1x,reel1.default_y - delta_y * 9]
        reel10.position = [r10x,reel10.default_y - delta_y * 9]
        reel100.position = [r100x,reel100.default_y - delta_y * 9]
        reel1000.position = [r1000x,reel1000.position[1] + delta_y]
    else:
        if reel1.position[1] != reel1.default_y:
            reel1.position = [r1x,reel1.position[1] + delta_y]

