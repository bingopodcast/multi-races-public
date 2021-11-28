#!/usr/bin/python

import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
import procgame.game, sys, os, random
import procgame.config
import procgame.sound
import pygame

sys.path.insert(0,os.path.pardir)
import multi_races.common.units as units
import multi_races.common.functions as functions
from multi_races.graphics import methods as graphics
#from multi_races.graphics.winner import *

class OneBall(procgame.game.Mode):
    def __init__(self, game):
        super(OneBall, self).__init__(game=game, priority=5)
        self.holes = []
        self.startup()
        self.game.coils.purse.enable()
        self.game.coils.show.enable()
        self.game.coils.place.enable()
        self.game.coils.win.enable()
        self.game.coils.feature.enable()
        self.game.coils.bumperALamp.enable()
        self.game.coils.bumperBLamp.enable()

    def sw_flag_active(self, sw):
		if self.game.switches.star.is_active() and self.game.switches.horseshoe.is_active():
			self.game.end_run_loop()
			del self.game.proc
			os.system("/home/nbaldridge/proc/multi-races/multi_races/start_game.sh winner")

    def sw_coin_active(self, sw):
        self.game.tilt.disengage()
        if self.game.start.status == False:
            self.game.clover.disengage()
            self.game.all_advantages.engage(self.game)
        self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_startButton_active(self, sw):
        if self.game.replays > 0 or self.game.switches.freeplay.is_inactive():
            self.regular_play()
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)
            return
        if self.game.all_advantages.status == False:
            self.game.clover.disengage()
            self.game.all_advantages.engage(self.game)
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)
            self.delay(name="startButton", delay=0.1, handler=self.sw_startButton_active, param=sw)


    #def sw_enter_active(self, sw):
    #    if self.game.switches.startButton.is_active() and self.game.switches.feature.is_active():
    #        self.game.end_run_loop()
    #        os.system("/home/nbaldridge/proc/multi-races/start_game.sh winner")

    def regular_play(self):
        self.cancel_delayed(name="replay_step_up")
        self.game.cu = not self.game.cu
        self.game.search_index.disengage()
        self.game.coils.counter.pulse()
        self.game.coils.motor.enable()
        self.game.coils.timing.pulse()
        self.game.coils.selection.pulse()
        self.game.four_hundred.step()
        self.game.coils.four_hundred.pulse()
        self.game.coin6.step()
        self.game.coin.step()
        begin = self.game.spotting.position
        self.game.spotting.spin()
        begin2 = self.game.spotting2.position
        self.game.spotting2.spin()
        if self.game.switches.lane.is_inactive():
            self.game.coils.shutter.enable()
        self.game.replay_counter.reset()
        self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)
        self.game.tilt.disengage()
        if self.game.start.status == False:
            self.game.odds.reset()
            if self.game.name.position == 6:
                self.game.name.reset()
            self.game.clover.disengage()
            self.game.left.disengage()
            self.game.right.disengage()
            self.game.left_right.disengage()
            if self.game.feature_lite.status == True and self.game.feature_lite_won.status == True:
                self.game.pennant.disengage()
                self.game.feature_lite_won.disengage()
                self.game.feature_lit.disengage()
            else:
                if self.game.feature_lite.status == False:
                    self.game.pennant.disengage()
            if self.game.show_race_won.status == True:
                self.game.show_race_stepper.reset()
                self.game.show_race.disengage()
                self.game.show_race_won.disengage()
            if self.game.place_race_won.status == True:
                self.game.place_race_stepper.reset()
                self.game.place_race_won.disengage()
                self.game.place_race.disengage()
            if self.game.win_race_won.status == True:
                self.game.win_race_stepper.reset()
                self.game.win_race.disengage()
                self.game.win_race_won.disengage()
            self.game.feature_purse.disengage()
            if self.game.left_purse_won.status == True:
                self.game.left_purse.disengage()
                self.game.left_purse_won.disengage()
            if self.game.right_purse_won.status == True:
                self.game.right_purse.disengage()
                self.game.right_purse_won.disengage()
            if self.game.four_place_won.status == True:
                self.game.four_place.disengage()
                self.game.four_place_won.disengage()
            if self.game.four_show_won.status == True:
                self.game.four_show.disengage()
                self.game.four_show_won.disengage()
            if self.game.four_purse_won.status == True:
                self.game.four_purse_won.disengage()
                self.game.four_purse.disengage()
            if self.game.daily_double_won.status == True:
                self.game.daily_double.disengage()
                self.game.daily_double_won.disengage()
            if self.game.purse_win_won.status == True:
                self.game.purse_win.disengage()
                self.game.purse_win_won.disengage()
            if self.game.show_win_won.status == True:
                self.game.show_win.disengage()
                self.game.show_win_won.disengage()
            self.game.hold3.disengage()
            self.game.hold4.disengage()
            self.game.hold5.disengage()
            self.game.fan.disengage()
        self.game.reflex.decrease()
        self.scan_all(begin)
        self.replay_step_down()
        self.game.clover.disengage()
        self.game.all_advantages.engage(self.game)
        if self.game.coin.position == 0:
            self.game.coils.bumperCLamp.enable()
            self.game.coils.bumperDLamp.disable()
        else:
            self.game.coils.bumperCLamp.disable()
            self.game.coils.bumperDLamp.enable()
        self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)
        
    def sw_lane_active(self, sw):
        self.game.start.engage(self.game)

    def sw_smRunout_active_for_10ms(self, sw):
        self.game.coils.shutter.disable()

    def sw_lane_inactive_for_15ms(self, sw):
        self.game.start.disengage()
        self.game.all_advantages.disengage()
        self.game.horseshoe.disengage()
        self.game.feature.disengage()
        self.game.star.disengage()
        self.game.clover.disengage()
        self.game.all_advantages.engage(self.game)

    # This is really nasty, but it is how we render graphics for each individual hole.

    def sw_purse1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("purse")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_purse2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("purse")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_purse3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("purse")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_purse4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("purse")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_purse5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("purse")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_purse6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("purse")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_purse7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("purse")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_show1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("show")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_show2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("show")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_show3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("show")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_show4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("show")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_show5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("show")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_show6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("show")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_show7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("show")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_place1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("place")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_place2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("place")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_place3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("place")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_place4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("place")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_place5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("place")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_place6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("place")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_place7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("place")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_win1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("win")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_win2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("win")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_win3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("win")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_win4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("win")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_win5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("win")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_win6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("win")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_win7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("win")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_feature_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("feature")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        graphics.winner.display(self)
        self.tilt_actions()
        self.replay_step_down(self.game.replays)

    def tilt_actions(self):
        self.game.start.disengage()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="replay_step_up")
        self.game.odds.reset()
        self.game.hold3.disengage()
        self.game.hold4.disengage()
        self.game.hold5.disengage()
        self.game.fan.disengage()
        self.game.clover.disengage()
        self.game.feature.disengage()
        self.game.left.disengage()
        self.game.right.disengage()
        self.game.replay_counter.reset()
        self.game.left_right.disengage()
        self.game.feature_purse.disengage()
        self.game.left_purse.disengage()
        self.game.right_purse.disengage()
        self.game.four_place.disengage()
        self.game.four_show.disengage()
        self.game.four_purse.disengage()
        self.game.daily_double.disengage()
        self.game.purse_win.disengage()
        self.game.show_win.disengage()
        self.game.search_index.disengage()
        self.game.anti_cheat.engage(game)
        self.game.tilt.engage(self.game)
        self.game.all_advantages.engage(self.game)
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            self.tilt_actions()

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.winner.display(self)
                self.delay(name="replay_reset", delay=0.13, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.winner.display(self)
                self.cancel_delayed(name="replay_reset")
        else:
            if self.game.replays > 0:
                self.game.replays -= 1
                self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)
                graphics.winner.display(self)

    def sw_leftcap_active(self, sw):
        if self.game.left.status == True:
            self.game.name.step()
            self.game.coils.four_hundred.pulse()
            if self.game.name.position < 6:
                self.find_winner(self.game.selection, "purse")
            else:
                if self.game.odds.position <= 5:
                    if self.game.replay_counter.position < 40:
                        self.game.search_index.engage(self.game)
                        self.winner_replay_step_up(40 - self.game.replay_counter.position)
                if self.game.odds.position in [6,7]:
                    if self.game.replay_counter.position < 80:
                        self.game.search_index.engage(self.game)
                        self.winner_replay_step_up(80 - self.game.replay_counter.position)
                if self.game.odds.position in [8,9,10]:
                    if self.game.replay_counter.position < 160:
                        self.game.search_index.engage(self.game)
                        self.winner_replay_step_up(160 - self.game.replay_counter.position)
        if self.game.left_purse.status == True and self.game.left_purse_won.status == False:
            self.game.left_purse_won.engage(self.game)
            self.find_winner(self.game.selection, "purse")
        self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_rightcap_active(self, sw):
        if self.game.right.status == True:
            self.game.name.step()
            self.game.coils.four_hundred.pulse()
            if self.game.name.position < 6:
                self.find_winner(self.game.selection, "purse")
            else:
                if self.game.odds.position <= 5:
                    if self.game.replay_counter.position < 40:
                        self.game.search_index.engage(self.game)
                        self.winner_replay_step_up(40 - self.game.replay_counter.position)
                if self.game.odds.position in [6,7]:
                    if self.game.replay_counter.position < 80:
                        self.game.search_index.engage(self.game)
                        self.winner_replay_step_up(80 - self.game.replay_counter.position)
                if self.game.odds.position in [8,9,10]:
                    if self.game.replay_counter.position < 160:
                        self.game.search_index.engage(self.game)
                        self.winner_replay_step_up(160 - self.game.replay_counter.position)
        if self.game.right_purse.status == True and self.game.right_purse_won.status == False:
            self.game.right_purse_won.engage(self.game)
            self.find_winner(self.game.selection, "purse")
        self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_bumpera_active(self, sw):
        if self.game.show_race_won.status == False:
            self.game.show_race_stepper.step()
            self.game.coils.four_hundred.pulse()
            if self.game.show_race_stepper.position == 8:
                self.game.show_race.engage(self.game)
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_bumperb_active(self, sw):
        if self.game.place_race_won.status == False:
            self.game.place_race_stepper.step()
            self.game.coils.four_hundred.pulse()
            if self.game.place_race_stepper.position == 8:
                self.game.place_race.engage(self.game)
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_bumperc_active(self, sw):
        if self.game.coin.position == 0:
            if self.game.win_race_won.status == False:
                self.game.win_race_stepper.step()
                self.game.coils.four_hundred.pulse()
                if self.game.win_race_stepper.position == 8:
                    self.game.win_race.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def sw_bumperd_active(self, sw):
        if self.game.coin.position == 1:
            if self.game.win_race_won.status == False:
                self.game.win_race_stepper.step()
                self.game.coils.four_hundred.pulse()
                if self.game.win_race_stepper.position == 8:
                    self.game.win_race.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def replay_step_up(self):
        if self.game.replays < 899:
            self.game.replays += 1
        self.game.coils.registerUp.pulse()
        self.game.reflex.increase()
        graphics.winner.display(self)

    def sw_clover_active(self, sw):
        if self.game.start.status == True:
            if self.game.clover.status == True and (self.game.replays > 0 or self.game.switches.freeplay.is_inactive()):
                self.regular_play()
                return
            if self.game.clover.status == False:
                self.game.all_advantages.disengage()
                self.game.clover.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)
                self.delay(name="clover", delay=0.1, handler=self.sw_clover_active, param=sw)

    def search(self, area):
        if self.game.start.status == False:
            selection = self.game.selection
            if self.game.pennant.status == True and self.game.switches.feature.is_active():
                self.find_winner(selection, "feature")
                if self.game.feature_lite.status == True:
                    self.game.feature_lite_won.engage(self.game)
            else:
                for item in selection: 
                    sw = "self.game.switches.%s%s.is_active()" % (area, item)
                    if eval(sw):
                        self.find_winner(selection, area)
                if self.game.show_race.status == True:
                    if area == "show":
                        self.find_winner(selection, area)
                        self.game.show_race_won.engage(self.game)
                if self.game.place_race.status == True:
                    if area == "place":
                        self.find_winner(selection, area)
                        self.game.place_race_won.engage(self.game)
                if self.game.win_race.status == True:
                    if area == "win":
                        self.find_winner(selection, area)
                        self.game.win_race_won.engage(self.game)
                if self.game.four_purse.status == True and self.game.four_purse_won.status == False:
                    if self.game.switches.purse4.is_active():
                        self.find_winner(selection, area)
                        self.game.four_purse_won.engage(self.game)
                if self.game.four_show.status == True and self.game.four_show_won.status == False:
                    if self.game.switches.show4.is_active():
                        self.find_winner(selection, area)
                        self.game.four_show_won.engage(self.game)
                if self.game.four_place.status == True and self.game.four_place_won.status == False:
                    if self.game.switches.place4.is_active():
                        self.find_winner(selection, area)
                        self.game.four_place_won.engage(self.game)

    def get_odds(self, section):
        if section == "purse":
            if self.game.odds.position in [1,2]:
                return 3
            elif self.game.odds.position == 3:
                return 5
            elif self.game.odds.position == 4:
                return 8
            elif self.game.odds.position == 5:
                return 12
            elif self.game.odds.position == 6:
                return 16
            elif self.game.odds.position == 7:
                return 24
            elif self.game.odds.position == 8:
                return 32
            elif self.game.odds.position == 9:
                return 48
            elif self.game.odds.position == 10:
                return 64
        elif section == "show":
            if self.game.odds.position == 1:
                return 3
            elif self.game.odds.position == 2:
                return 5
            elif self.game.odds.position == 3:
                return 8
            elif self.game.odds.position == 4:
                return 12
            elif self.game.odds.position == 5:
                return 16
            elif self.game.odds.position == 6:
                return 24
            elif self.game.odds.position == 7:
                return 32
            elif self.game.odds.position == 8:
                return 48
            elif self.game.odds.position == 9:
                return 64
            elif self.game.odds.position == 10:
                return 96
        elif section == "place":
            if self.game.odds.position == 1:
                return 5
            elif self.game.odds.position == 2:
                return 8
            elif self.game.odds.position == 3:
                return 12
            elif self.game.odds.position == 4:
                return 16
            elif self.game.odds.position == 5:
                return 24
            elif self.game.odds.position == 6:
                return 32
            elif self.game.odds.position == 7:
                return 48
            elif self.game.odds.position == 8:
                return 64
            elif self.game.odds.position == 9:
                return 96
            elif self.game.odds.position == 10:
                return 128
        elif section == "win":
            if self.game.odds.position == 1:
                return 8
            elif self.game.odds.position == 2:
                return 12
            elif self.game.odds.position == 3:
                return 16
            elif self.game.odds.position == 4:
                return 24
            elif self.game.odds.position == 5:
                return 32
            elif self.game.odds.position == 6:
                return 48
            elif self.game.odds.position == 7:
                return 64
            elif self.game.odds.position == 8:
                return 96
            elif self.game.odds.position in [9,10]:
                return 160

    def find_winner(self, selection, area):
        if self.game.search_index.status == False and self.game.replays < 899:
            purse = self.get_odds("purse")
            show = self.get_odds("show")
            place = self.get_odds("place")
            win = self.get_odds("win")
            if self.game.show_win.status == True:
                show = win
            if self.game.purse_win.status == True:
                purse = win
            if area == "feature" and self.game.pennant.status == True:
                if self.game.odds.position <= 5:
                    if self.game.replay_counter.position < 40:
                        self.game.search_index.engage(self.game)
                        self.winner_replay_step_up(40 - self.game.replay_counter.position)
                if self.game.odds.position in [6,7]:
                    if self.game.replay_counter.position < 80:
                        self.game.search_index.engage(self.game)
                        self.winner_replay_step_up(80 - self.game.replay_counter.position)
                if self.game.odds.position in [8,9,10]:
                    if self.game.replay_counter.position < 160:
                        self.game.search_index.engage(self.game)
                        self.winner_replay_step_up(160 - self.game.replay_counter.position)
            else:
                if area == "feature":
                    if self.game.feature_purse.status == True and self.game.feature_purse_won.status == False:
                        if self.game.replay_counter.position < purse:
                            self.game.search_index.engage(self.game)
                            self.winner_replay_step_up(purse - self.game.replay_counter.position)
            if area == "purse":
                if self.game.purse_win.status == False:
                    if self.game.replay_counter.position < purse:
                        self.game.search_index.engage(self.game)
                        self.winner_replay_step_up(purse - self.game.replay_counter.position)
                if self.game.purse_win.status == True and self.game.purse_win_won.status == False:
                    if self.game.replay_counter.position < win:
                        self.game.search_index.engage(self.game)
                        self.winner_replay_step_up(win - self.game.replay_counter.position)
            elif area == "show":
                if self.game.show_win.status == False:
                    if self.game.replay_counter.position < show:
                        self.game.search_index.engage(self.game)
                        self.winner_replay_step_up(show - self.game.replay_counter.position)
                if self.game.show_win.status == True and self.game.show_win_won.status == False:
                    if self.game.replay_counter.position < win:
                        self.game.search_index.engage(self.game)
                        self.winner_replay_step_up(win - self.game.replay_counter.position)
            elif area == "place":
                if self.game.replay_counter.position < place:
                    self.game.search_index.engage(self.game)
                    self.winner_replay_step_up(place - self.game.replay_counter.position)
            else:
                if area == "win":
                    if self.game.replay_counter.position < win:
                        self.game.search_index.engage(self.game)
                        self.winner_replay_step_up(win - self.game.replay_counter.position)

    def winner_replay_step_up(self, number):
        if number >= 1:
            self.game.replay_counter.step()
            self.game.coils.four_hundred.pulse()
            number -= 1
            self.replay_step_up()
            if self.game.replays == 899:
                number = 0
            self.delay(name="replay_step_up", delay=0.25, handler=self.winner_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            self.cancel_delayed(name="replay_step_up")

    def scan_all(self, begin):
        if self.game.all_advantages.status == True:
            s = self.animate_star_scan([begin, self.game.spotting.position,1])
        if self.game.all_advantages.status == True:
            self.game.selection = []
            if self.game.hold3.status == True:
                self.game.selection.append(3)
            if self.game.hold4.status == True:
                self.game.selection.append(4)
            if self.game.hold5.status == True:
                self.game.selection.append(5)
            if self.game.fan.status == True:
                self.game.selection.append(1,2,3,4,5,6,7)
            h = self.animate_selection_scan([begin,self.game.spotting.position,1])
        if self.game.clover.status == True:
            i = self.animate_clover_scan([begin,self.game.spotting.position,1])
        if self.game.all_advantages.status == True:
            f = self.animate_feature_scan([begin,self.game.spotting.position,1])

        if self.game.all_advantages.status  == True:
            if self.game.left_right.status == False:
                if self.game.spotting.position in [6,15,28,31,40,3]:
                    self.game.left_right.engage(self.game)
            else:
                if self.game.cu:
                    self.game.left.disengage()
                    self.game.right.engage(self.game)
                else:
                    self.game.right.disengage()
                    self.game.left.engage(self.game)

        #Check Mixer Re
        if self.game.odds.position < 5:
            if self.game.all_advantages.status == True:
                pass
            else:
                pass

        if self.game.odds.position in [5,6]:
            if self.game.all_advantages.status == True:
                pass
            else:
                pass


        if self.game.odds.position in [7,8]:
            if self.game.all_advantages.status == True:
                pass
            else:
                pass

        if self.game.odds.position in [9,10]:
            if self.game.all_advantages.status == True:
                pass
            else:
                pass

    def scan_star(self):
        self.star_probability()
        self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def animate_star_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.winner.star_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="star_animation", delay=0.05, handler=self.animate_star_scan, param=args)
        else:
            self.cancel_delayed(name="star_animation")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)
            self.scan_star()
            self.game.coils.motor.disable()

    def star_probability(self):
        initial = False
        if self.game.odds.position < 2:
            self.game.odds.step()
            self.game.coils.four_hundred.pulse()
            initial = True
        if self.check_reflex() == 1:
            #path 1
            if 4 in self.game.selection:
                if [3,5] not in self.game.selection:
                    if initial == False:
                        self.check_odds()
            #path 2
            if initial == False:
                self.check_odds()
            else:
                if initial == False:
                    self.check_odds()
            #path 3
            if initial == False:
                self.check_odds()

    def check_odds(self):
            if self.game.odds.position < 2:
                self.game.odds.step()
                self.game.coils.four_hundred.pulse()
                return
            else:
                if self.game.odds.position == 2:
                    if self.game.spotting2.position in [3,5,8,12,16,18,22,24,28,30,32,35,39,41,44,47,49]:
                        self.check_extra_step()
                if self.game.odds.position == 3:
                    if self.game.spotting2.position in [5,8,12,15,18,28,30,32,25,29,41,44,47,49]:
                        self.check_extra_step()
                if self.game.odds.position == 4:
                    if self.game.spotting2.position in [8,12,15,18,28,30,32,25,29,41,44,47,49]:
                        self.check_extra_step()
                if self.game.odds.position == 5:
                    if self.game.spotting2.position in [12,15,18,28,30,32,25,29,41,44,47,49]:
                        self.check_extra_step()
                if self.game.odds.position == 6:
                    if self.game.spotting2.position in [12,18,28,30,32,25,29,41,44,47,49]:
                        self.check_extra_step()
                if self.game.odds.position == 7:
                    if self.game.spotting2.position in [18,28,30,32,25,29,41,44,47]:
                        self.check_extra_step()
                if self.game.odds.position == 8:
                    if self.game.spotting2.position in [18,30,32,25,29,44]:
                        self.check_extra_step()
                if self.game.odds.position == 9:
                    if self.game.spotting2.position in [18,32,25,29,44]:
                        self.check_extra_step()

    def check_extra_step(self):
        if self.game.coin6.position == 5:
            if self.game.odds.position < 6:
                self.step_odds(6 - self.game.odds.position)
            elif self.game.odds.position in [6,7]:
                self.step_odds(8 - self.game.odds.position)
            elif self.game.odds.position > 7:
                self.game.odds.step()
                self.game.coils.four_hundred.pulse()
        else:
            self.game.odds.step()
            self.game.coils.four_hundred.pulse()

    def step_odds(self, number):
        if number > 0:
            self.game.odds.step()
            self.game.coils.four_hundred.pulse()
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)
            number -= 1
            self.delay(name="step_odds", delay=0.1, handler=self.step_odds, param=number)

    def step_wild(self, number):
        if number > 0:
            self.game.wild.step()
            self.game.coils.four_hundred.pulse()
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)
            number -= 1
            if self.game.wild.position == 20:
                self.game.fan.engage(self.game)
            self.delay(name="step_wild", delay=0.1, handler=self.step_wild, param=number)

    def scan_selection(self):
        self.selection_probability()
        self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def animate_selection_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.winner.selection_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="selection_animation", delay=0.05, handler=self.animate_selection_scan, param=args)
        else:
            self.cancel_delayed(name="selection_animation")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)
            self.scan_selection()
            self.game.coils.motor.disable()

    def selection_probability(self):
        if self.game.spotting.position in [1,26,8,33,15,40,23,48]:
            self.game.selection.append(1)
        if self.game.spotting.position in [2,27,9,34,16,41,24,49]:
            self.game.selection.append(2)
        if self.game.spotting.position in [3,28,10,35,17,42,25,50,0]:
            self.game.selection.append(3)
        if self.game.spotting.position in [4,29,11,36,18,43]:
            self.game.selection.append(4)
        if self.game.spotting.position in [5,30,12,37,19,44]:
            self.game.selection.append(5)
        if self.game.spotting.position in [6,31,13,38,20,45]:
            self.game.selection.append(6)
        if self.game.spotting.position in [7,32,14,39,21,46,47,22]:
            self.game.selection.append(7)

        if self.game.coin6.position % 3 == 0:
            self.selection2_probability()

    def selection2_probability(self):
        if self.game.spotting.position in [1,26,8,33,15,40,23,48]:
            self.game.selection.append(7)
        if self.game.spotting.position in [2,27,9,34,16,41,24,49]:
            self.game.selection.append(7)
        if self.game.spotting.position in [3,28,10,35,17,42,25,50,0]:
            self.game.selection.append(5)
        if self.game.spotting.position in [4,29,11,36,18,43]:
            self.game.selection.append(4)
        if self.game.spotting.position in [5,30,12,37,19,44]:
            self.game.selection.append(3)
        if self.game.spotting.position in [6,31,13,38,20,45]:
            self.game.selection.append(2)
        if self.game.spotting.position in [7,32,14,39,21,46,47,22]:
            self.game.selection.append(1)

    def scan_feature(self):
        self.feature_probability()
        self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def animate_feature_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.winner.feature_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="feature_animation", delay=0.05, handler=self.animate_feature_scan, param=args)
        else:
            self.cancel_delayed(name="feature_animation")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)
            self.scan_feature()
            self.game.coils.motor.disable()

    def feature_probability(self):
        if self.game.four_hundred.position == 400:
            self.game.pennant.engage(self.game)

    def scan_clover(self):
        self.clover_probability()
        self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)

    def animate_clover_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.winner.clover_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="clover_animation", delay=0.05, handler=self.animate_clover_scan, param=args)
        else:
            self.cancel_delayed(name="clover_animation")
            self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)
            self.scan_clover()
            self.game.coils.motor.disable()

    def clover_probability(self):
        if self.check_reflex() == 1:
            if self.game.spotting2.position in [17,32,45]:
                self.game.feature_purse.engage(self.game)
            if self.game.spotting2.position in [13,22,33]:
                self.game.left_purse.engage(self.game)
            if self.game.spotting2.position in [5,11,27]:
                self.game.right_purse.engage(self.game)
            if self.game.spotting2.position in [9,14,32]:
                self.game.four_place.engage(self.game)
            if self.game.spotting2.position in [1,19,21]:
                self.game.four_show.engage(self.game)
            if self.game.spotting2.position in [2,8,20]:
                self.game.four_purse.engage(self.game)

            if self.game.spotting2.position in [3,49,28,24]:
                self.game.daily_double.engage(self.game)
            if self.game.spotting2.position in [4,46]:
                self.game.purse_win.engage(self.game)
            if self.game.spotting2.position in [7,39]:
                self.game.odds_advance.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)
                if self.game.odds.position < 10:
                    self.game.odds.step()
                    self.game.coils.four_hundred.pulse()
                self.game.odds_advance.disengage()
                self.delay(name="display", delay=0.1, handler=graphics.winner.display, param=self)
            if self.game.spotting2.position in [8,36]:
                self.game.show_win.engage(self.game)
            if self.game.spotting2.position in [15,23,40,48]:
                self.game.feature_lite.engage(self.game)
                self.game.pennant.engage(self.game)
            if self.game.spotting2.position in [18,43,10,26]:
                self.game.hold3.engage(self.game)
                self.game.selection.append(3)
            if self.game.four_hundred.position % 20 == 0:
                if self.game.spotting2.position in [19,44,11,27]:
                    self.game.hold4.engage(self.game)
                    self.game.selection.append(4)
            if self.game.spotting2.position in [20,45,12,28]:
                self.game.hold5.engage(self.game)
                self.game.selection.append(5)
            if self.game.four_hundred.position % 100 == 0:
                self.game.fan.engage(self.game)
                self.game.selection.append(1,2,3,4,5,6,7)

    def check_reflex(self):
        if self.game.reflex.connected_rivet() == 5:
            return 1
        elif self.game.reflex.connected_rivet() == 4:
            return 1
        elif self.game.reflex.connected_rivet() == 3:
            return 1
        elif self.game.reflex.connected_rivet() == 2:
            return 1
        elif self.game.reflex.connected_rivet() == 1:
            return 1
        else:
            return 0

    # Define reset as the knock-off, anti-cheat relay disabled, and replay reset enabled.  Motors turn while credits are knocked off.
    # When meter reaches zero and the zero limit switch is hit, turn off motor sound and leave backglass gi on, but with tilt displayed.

    def startup(self):
        self.eb = False
        self.tilt_actions()


class Winner(procgame.game.BasicGame):
    """ Turf King was one of the last one balls made by Bally """
    def __init__(self, machine_type):
        super(Winner, self).__init__(machine_type)
        pygame.mixer.pre_init(44100,-16,2,512)
        self.sound = procgame.sound.SoundController(self)
        self.sound.set_volume(1.0)
        # NOTE: trough_count only counts the number of switches present in the  trough.  It does _not_ count
        #       the number of balls present.   In this game, there  should  be  1  ball.
        self.trough_count = 1

        # Subclass my units unique to this game -  modifications must be made to set up mixers and steppers unique to the game
        # NOTE: 'top' positions are indexed using a 0 index, so the top on a 24 position unit is actually 23.

        # Initialize reflex(es) and mixers unique to this game
        self.reflex = units.Reflex("primary", 100)

        self.coin = units.Stepper("coin", 1, "winner", "continuous")
        self.coin6 = units.Stepper("coin6", 5, "winner", "continuous")
        self.four_hundred = units.Stepper("four_hundred", 400, "victory_derby", "continuous")

        self.spotting = units.Spotting("spotting", 50)
        r = random.randint(0,49)
        self.spotting.position = r
        self.spotting2 = units.Spotting("spotting", 50)
        r = random.randint(0,49)
        self.spotting2.position = r

        self.search_index = units.Relay("search_index")

        self.name = units.Stepper("name", 6)

        self.win_race = units.Relay("win_race")
        self.win_race_won = units.Relay("win_race_won")
        self.win_race_stepper = units.Stepper("win_race_stepper", 8)
        self.show_race = units.Relay("show_race")
        self.show_race_won = units.Relay("show_race_won")
        self.show_race_stepper = units.Stepper("show_race_stepper", 8)
        self.place_race = units.Relay("place_race")
        self.place_race_won = units.Relay("place_race_won")
        self.place_race_stepper = units.Stepper("place_race_stepper", 8)

        #Replay Counter
        self.replay_counter = units.Stepper("replay_counter", 300)

        #Initialize stepper units used to keep track of features or timing.
        self.odds = units.Stepper("odds", 10)

        #Check for status of the replay register zero switch.  If positive
        #and machine is just powered on, this will zero out the replays.
        self.replay_reset = units.Relay("replay_reset")

        #When engage()d, light 6v circuit, and enable game features, scoring,
        #etc. Disengage()d means that the machine is 'soft' tilted.
        self.anti_cheat = units.Relay("anti_cheat")

        #When engage()d, spin.
        self.start = units.Relay("start")

        self.clover = units.Relay("clover")
        self.all_advantages = units.Relay("all_advantages")
        self.fan = units.Relay("fan")
        self.feature = units.Relay("feature")
        self.hold3 = units.Relay("hold3")
        self.hold4 = units.Relay("hold4")
        self.hold5 = units.Relay("hold5")
        self.horseshoe = units.Relay("horseshoe")
        self.star = units.Relay("star")
        self.left = units.Relay("left")
        self.right = units.Relay("right")
        self.left_right = units.Relay("left_right")
        self.lettera = units.Relay("lettera")
        self.letterb = units.Relay("letterb")
        self.letterc = units.Relay("letterc")
        self.letterd = units.Relay("letterd")
        self.purse_double = units.Relay("purse_double")
        self.show_double = units.Relay("show_double")
        self.purse_win = units.Relay("purse_win")
        self.show_win = units.Relay("show_win")
        self.pennant = units.Relay("pennant")

        self.feature_purse = units.Relay("feature_purse")
        self.left_purse = units.Relay("left_purse")
        self.right_purse = units.Relay("right_purse")
        self.four_place = units.Relay("four_place")
        self.four_show = units.Relay("four_show")
        self.four_purse = units.Relay("four_purse")
        self.daily_double = units.Relay("daily_double")
        self.purse_win = units.Relay("purse_win")
        self.show_win = units.Relay("show_win")
        self.odds_advance = units.Relay("odds_advance")
        self.feature_purse_won = units.Relay("feature_purse_won")
        self.left_purse_won = units.Relay("left_purse_won")
        self.right_purse_won = units.Relay("right_purse_won")
        self.four_purse_won = units.Relay("four_purse_won")
        self.four_show_won = units.Relay("four_show_won")
        self.four_place_won = units.Relay("four_place_won")
        self.daily_double_won = units.Relay("daily_double_won")
        self.purse_win_won = units.Relay("purse_win_won")
        self.show_win_won = units.Relay("show_win_won")
        self.feature_lite = units.Relay("feature_lite")
        self.feature_lite_won = units.Relay("feature_lite_won")

        self.cu = 0

        r = random.randint(0,4)
        self.name.position = r

        r = random.randint(0,7)
        self.place_race_stepper.position = r

        r = random.randint(0,7)
        self.show_race_stepper.position = r
        
        r = random.randint(0,7)
        self.win_race_stepper.position = r

        #Tilt is separate from anti-cheat in that the trip will move the shutter
        #when the game is tilted with 1st ball in the lane.  Also prevents you
        #from picking back up by killing the anti-cheat.  Can be engaged by
        #tilt bob, slam tilt switches, or timer at 39th step.
        #Immediately kills motors.
        self.tilt = units.Relay("tilt")

        self.replays = 0
        self.returned = False
        self.selection = [1]

    def reset(self):
        super(Winner, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')

        main_mode = OneBall(self)
        self.modes.add(main_mode)

game = Winner(machine_type='pdb')
game.reset()
game.run_loop()
