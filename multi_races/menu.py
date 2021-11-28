#!/usr/bin/python

import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
import pinproc
import procgame.game, sys, os
import procgame.config
import pygame
import time
import thread
import procgame.sound

sys.path.insert(0,os.path.pardir)
from graphics import methods as graphics
from common import units

#pygame.init()
pygame.display.set_caption("Multi Bingo")
screen = pygame.display.set_mode((0,0))
screen.fill([0,0,0])

class Menu(procgame.game.BasicGame):
    """ This menu lets you select games to play """
    def __init__(self, machine_type):
        super(Menu, self).__init__(machine_type)

    def reset(self, selection, select):
        super(Menu, self).reset()
        self.load_config('bingo.yaml')
        mainmenu = MainMenu(self, selection, select)
        self.modes.add(mainmenu)
        self.logger = logging.getLogger('game')

class MainMenu(procgame.game.Mode):
    def __init__(self, game, selection, select):
        super(MainMenu, self).__init__(game=game, priority=5)
        self.game.replays = 0
        self.game.select = select
        self.game.selection = selection
   
        self.holes = []
        self.holes2 = []

        self.tilt = units.Relay("tilt")

        selection[select]
        __import__("graphics.%s" % (selection[select]))
        g = "graphics.%s.display(self,0,True)" % (selection[select])
        eval(g)


    def sw_startButton_active(self, sw):
        #self.game.end_run_loop()
        #os.system("/home/nbaldridge/proc/multi-races/multi_races/start_game.sh %s" % self.game.selection[self.game.select])
	del self.game.proc
        try:
            s = self.game.select
            t = thread.start_new(__import__("%s.game" % (self.game.selection[self.game.select])))
            if t.isAlive():
                t.join()

        except:

            g = (__import__("%s.game" % (self.game.selection[self.game.select])))

            t = thread.start_new(eval(g))
            self.game.end_run_loop()
            if t.isAlive():
                t.join()
        self.game.reset(self.game.selection, self.game.select)

    def sw_star_active(self, sw):
        if self.game.select != 1:
            self.game.select -= 1
            self.game.selection[self.game.select]
            __import__("graphics.%s" % (self.game.selection[self.game.select]))
            g = "graphics.%s.display(self,0,True)" % (self.game.selection[self.game.select])
            eval(g)
            os.system("sshpass -p raspberry ssh pi@10.0.0.51 /home/pi/ic.sh %s &" % (self.game.selection[self.game.select]))
            os.system("sshpass -p raspberry ssh pi@10.0.0.52 /home/pi/sc.sh %s &" % (self.game.selection[self.game.select]))

    def sw_star_active_for_400ms(self, sw):
        if self.game.select != 1:
            self.game.select -= 1
            self.game.selection[self.game.select]

            __import__("graphics.%s" % (self.game.selection[self.game.select]))
            g = "graphics.%s.display(self,0,True)" % (self.game.selection[self.game.select])
            eval(g)
            os.system("sshpass -p raspberry ssh pi@10.0.0.51 /home/pi/ic.sh %s &" % (self.game.selection[self.game.select]))
            os.system("sshpass -p raspberry ssh pi@10.0.0.52 /home/pi/sc.sh %s &" % (self.game.selection[self.game.select]))
            self.delay(name="left", delay=0.1, handler=self.sw_star_active_for_400ms, param=sw)

    def sw_flag_active(self, sw):
        if self.game.select != len(self.game.selection):
            self.game.select += 1
            self.game.selection[self.game.select]
            __import__("graphics.%s" % (self.game.selection[self.game.select]))
            g = "graphics.%s.display(self,0,True)" % (self.game.selection[self.game.select])
            eval(g)
	    os.system("sshpass -p raspberry ssh pi@10.0.0.51 /home/pi/ic.sh %s &" % (self.game.selection[self.game.select]))
	    os.system("sshpass -p raspberry ssh pi@10.0.0.52 /home/pi/sc.sh %s &" % (self.game.selection[self.game.select]))

    def sw_flag_active_for_400ms(self, sw):
        if self.game.select != len(self.game.selection):
            self.game.select += 1
            self.game.selection[self.game.select]
            __import__("graphics.%s" % (self.game.selection[self.game.select]))
            g = "graphics.%s.display(self,0,True)" % (self.game.selection[self.game.select])
            eval(g)
	    os.system("sshpass -p raspberry ssh pi@10.0.0.51 /home/pi/ic.sh %s &" % (self.game.selection[self.game.select]))
	    os.system("sshpass -p raspberry ssh pi@10.0.0.52 /home/pi/sc.sh %s &" % (self.game.selection[self.game.select]))
        self.delay(name="right", delay=0.1, handler=self.sw_flag_active_for_400ms, param=sw)

def main(sel):

    selection = {}
    selection[1] = "preakness"
    selection[2] = "fairgrounds"
    selection[3] = "arlington"
    selection[4] = "sport_page"
    selection[5] = "winning_ticket",
    selection[6] = "grandstand_38",
    selection[7] = "thistledowns",
    selection[8] = "seabiscuit",
    selection[9] = "hawthorne",
    selection[10] = "pace_maker",
    selection[11] = "grand_national",
    selection[12] = "dark_horse",
    selection[13] = "long_shot",
    selection[14] = "jockey_club_41",
    selection[15] = "derby_41"
    selection[16] = "pimlico"
    selection[17] = "longacres"
    selection[18] = "victory_derby"
    selection[19] = "victory_special"
    selection[20] = "new_daily_races"
    selection[21] = "bally_entry"
    selection[22] = "special_entry"
    selection[23] = "jockey_special"
    selection[24] = "gold_cup"
    selection[25] = "trophy"
    selection[26] = "favorite"
    selection[27] = "photo_finish"
    selection[28] = "citation"
    selection[29] = "lexington"
    selection[30] = "champion"
    selection[31] = "kentucky"
    selection[32] = "grandstand"
    selection[33] = "turf_king"
    selection[34] = "winner"
    selection[35] = "futurity"
    selection[36] = "old_hilltop"
    selection[37] = "sunshine_park"

    for i in range(1,38):
        if sel in selection[i]:
            select = i
            break

    os.system("sshpass -p raspberry ssh pi@10.0.0.51 /home/pi/ic.sh %s &" % (selection[select]))
    os.system("sshpass -p raspberry ssh pi@10.0.0.52 /home/pi/sc.sh %s &" % (selection[select]))

    game = Menu(machine_type='pdb')
    game.reset(selection, select)
    game.run_loop()
    
if __name__ == "__main__":
    main(sys.argv[1])
