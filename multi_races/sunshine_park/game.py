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
from multi_races.graphics.sunshine_park import *

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

    def sw_coin_active(self, sw):
        self.game.tilt.disengage()
        if self.game.start.status == False:
            if self.game.eb_play.status == False:
                self.game.horseshoe.disengage()
                self.game.clover.disengage()
                self.game.feature.disengage()
                self.game.star.disengage()
                self.game.all_advantages.engage(self.game)
        self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_startButton_active(self, sw):
        if self.game.replays > 0 or self.game.switches.freeplay.is_inactive():
            self.regular_play()
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)
            return
        if self.game.all_advantages.status == False:
            self.game.horseshoe.disengage()
            self.game.clover.disengage()
            self.game.feature.disengage()
            self.game.eb_play.disengage()
            self.game.star.disengage()
            self.game.all_advantages.engage(self.game)
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)
            self.delay(name="startButton", delay=0.1, handler=self.sw_startButton_active, param=sw)

    def regular_play(self):
        self.cancel_delayed(name="replay_step_up")
        self.game.cu = not self.game.cu
        self.game.search_index.disengage()
        self.game.coils.counter.pulse()
        self.game.coils.motor.enable()
        self.game.coils.timing.pulse()
        self.game.search_index.disengage()
        begin = self.game.spotting.position
        self.game.spotting.spin()
        begin2 = self.game.spotting2.position
        self.game.spotting2.spin()
        self.game.mixer1.spin()
        self.game.mixer2.spin()
        self.game.mixer3.spin()
        self.game.mixer4.spin()
        self.game.mixer5.spin()
        if self.game.switches.lane.is_inactive():
            self.game.coils.shutter.enable()
        self.game.replay_counter.reset()
        self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)
        self.game.tilt.disengage()
        if self.game.start.status == False:
            self.game.odds.reset()
            if self.game.wild.position != 21:
                self.game.fan.disengage()
            self.game.wild.reset()
            self.game.clover.disengage()
            self.game.horseshoe.disengage()
            self.game.star.disengage()
            self.game.feature.disengage()
            self.game.hold3.disengage()
            self.game.hold4.disengage()
            self.game.hold5.disengage()
            self.game.left.disengage()
            self.game.right.disengage()
            self.game.left_right.disengage()
            self.game.purse_double.disengage()
            self.game.show_double.disengage()
            self.game.purse_win.disengage()
            self.game.show_win.disengage()
            self.game.pennant.disengage()
            self.game.extra_ball.reset()
            self.game.ball_count.reset()
            self.game.wild.step()
        self.scan_all(begin)
        self.game.reflex.decrease()
        self.replay_step_down()

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
        self.game.eb_play.disengage()
        self.game.all_advantages.engage(self.game)

    # This is really nasty, but it is how we render graphics for each individual hole.

    def sw_purse1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("purse")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_purse2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("purse")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_purse3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("purse")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_purse4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("purse")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_purse5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("purse")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_purse6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("purse")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_purse7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("purse")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_show1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("show")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_show2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("show")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_show3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("show")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_show4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("show")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_show5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("show")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_show6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("show")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_show7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("show")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_place1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("place")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_place2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("place")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_place3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("place")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_place4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("place")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_place5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("place")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_place6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("place")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_place7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("place")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_win1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("win")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_win2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("win")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_win3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("win")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_win4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("win")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_win5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("win")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_win6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("win")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_win7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("win")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_feature_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("feature")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        graphics.sunshine_park.display(self)
        self.tilt_actions()
        self.replay_step_down(self.game.replays)

    def tilt_actions(self):
        self.game.start.disengage()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="replay_step_up")
        self.game.odds.reset()
        self.game.clover.disengage()
        self.game.star.disengage()
        self.game.horseshoe.disengage()
        self.game.eb_play.disengage()
        self.game.wild.reset()
        self.game.feature.disengage()
        self.game.left.disengage()
        self.game.right.disengage()
        self.game.replay_counter.reset()
        self.game.fan.disengage()
        self.game.hold3.disengage()
        self.game.hold4.disengage()
        self.game.hold5.disengage()
        self.game.left_right.disengage()
        self.game.purse_double.disengage()
        self.game.show_double.disengage()
        self.game.purse_win.disengage()
        self.game.show_win.disengage()
        self.game.search_index.disengage()
        self.game.anti_cheat.engage(game)
        self.game.extra_ball.reset()
        self.game.ball_count.reset()
        self.game.tilt.engage(self.game)
        self.game.all_advantages.engage(self.game)
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            self.tilt_actions()

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.sunshine_park.reel1, graphics.sunshine_park.reel10, graphics.sunshine_park.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.sunshine_park.display(self)
                self.delay(name="replay_reset", delay=0.13, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.sunshine_park.reel1, graphics.sunshine_park.reel10, graphics.sunshine_park.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.sunshine_park.display(self)
                self.cancel_delayed(name="replay_reset")
        else:
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.sunshine_park.reel1, graphics.sunshine_park.reel10, graphics.sunshine_park.reel100)
                self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)
            self.game.coils.registerDown.pulse()

    def sw_leftcap_active(self, sw):
        if self.game.left.status == True:
            self.step_wild(21 - self.game.wild.position)

    def sw_rightcap_active(self, sw):
        if self.game.right.status == True:
            self.step_wild(21 - self.game.wild.position)

    def sw_bumpera_active(self, sw):
        if self.game.lettera.status == False:
            self.game.coils.bumperALamp.enable()
            self.game.coils.four_hundred.pulse()
            self.game.lettera.engage(self.game)
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_bumperb_active(self, sw):
        if self.game.letterb.status == False:
            if self.game.lettera.status == True:
                self.game.coils.bumperBLamp.enable()
                self.game.letterb.engage(self.game)
                self.game.coils.four_hundred.pulse()
                self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_bumperc_active(self, sw):
        if self.game.letterc.status == False:
            if self.game.letterb.status == True:
                self.game.coils.bumperCLamp.enable()
                self.game.letterc.engage(self.game)
                self.game.coils.four_hundred.pulse()
                self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def sw_bumperd_active(self, sw):
        if self.game.letterd.status == False:
            if self.game.letterc.status == True:
                self.game.letterd.engage(self.game)
                self.game.coils.four_hundred.pulse()
                self.game.coils.bumperDLamp.enable()
                self.game.abcd.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def replay_step_up(self):
        if self.game.replays < 899:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.sunshine_park.reel1, graphics.sunshine_park.reel10, graphics.sunshine_park.reel100)
        self.game.coils.registerUp.pulse()
        self.game.reflex.increase()
        graphics.sunshine_park.display(self)

    def sw_star_active(self, sw):
        if self.game.start.status == True:
            if self.game.star.status == True and (self.game.replays > 0 or self.game.switches.freeplay.is_active()):
                self.regular_play()
                return
            if self.game.star.status == False:
                self.game.all_advantages.disengage()
                self.game.clover.disengage()
                self.game.horseshoe.disengage()
                self.game.feature.disengage()
                self.game.eb_play.disengage()
                self.game.star.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)
                self.delay(name="star", delay=0.1, handler=self.sw_star_active, param=sw)

    def sw_clover_active(self, sw):
        if self.game.start.status == True:
            if self.game.clover.status == True and (self.game.replays > 0 or self.game.switches.freeplay.is_active()):
                self.regular_play()
                return
            if self.game.clover.status == False:
                self.game.all_advantages.disengage()
                self.game.horseshoe.disengage()
                self.game.feature.disengage()
                self.game.star.disengage()
                self.game.eb_play.disengage()
                self.game.clover.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)
                self.delay(name="clover", delay=0.1, handler=self.sw_clover_active, param=sw)

    def sw_horseshoe_active(self, sw):
        if self.game.switches.clover.is_active() and self.game.switches.flag.is_active():
           self.game.end_run_loop()
           os.system("/home/nbaldridge/proc/multi-races/multi_races/start_game.sh sunshine_park")
        else:
            if self.game.start.status == True:
                if self.game.horseshoe.status == True and (self.game.replays > 0 or self.game.switches.freeplay.is_inactive()):
                    self.regular_play()
                    return
                if self.game.horseshoe.status == False:
                    self.game.all_advantages.disengage()
                    self.game.star.disengage()
                    self.game.feature.disengage()
                    self.game.clover.disengage()
                    self.game.eb_play.disengage()
                    self.game.horseshoe.engage(self.game)
                    self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)
                    self.delay(name="horseshoe", delay=0.1, handler=self.sw_horseshoe_active, param=sw)

    def sw_flag_active(self, sw):
        if self.game.switches.star.is_active() and self.game.switches.horseshoe.is_active():
            self.game.end_run_loop()
            del self.game.proc
            os.system("/home/nbaldridge/proc/multi-races/multi_races/start_game.sh turf_king")
        else:
            if self.game.start.status == True:
                if self.game.feature.status == True and (self.game.replays > 0 or self.game.switches.freeplay.is_inactive()):
                    self.regular_play()
                    return
                if self.game.feature.status == False:
                    self.game.all_advantages.disengage()
                    self.game.star.disengage()
                    self.game.clover.disengage()
                    self.game.horseshoe.disengage()
                    self.game.eb_play.disengage()
                    self.game.feature.engage(self.game)
                    self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)
                    self.delay(name="flag", delay=0.1, handler=self.sw_flag_active, param=sw)

    def sw_extra_ball_active(self, sw):
        if self.game.start.status == False:
            if self.game.eb_play.status == True and (self.game.replays > 0 or self.game.switches.freeplay.is_inactive()):
                self.game.regular_play()
                return
            if self.game.eb_play.status == False:
                self.game.all_advantages.disengage()
                self.game.star.disengage()
                self.game.clover.disengage()
                self.game.horseshoe.disengage()
                self.game.feature.disengage()
                self.game.eb_play.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)
                self.delay(name="eb", delay=0.1, handler=self.sw_extra_ball_active, param=sw)

    def search(self, area):
        if self.game.start.status == False:
            selection = self.game.selection
            if self.game.pennant.status == True and self.game.switches.feature.is_active():
                self.find_winner(selection, "feature")
            else:
                for item in selection: 
                    sw = "self.game.switches.%s%s.is_active()" % (area, item)
                    if eval(sw):
                        self.find_winner(selection, area)

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
                return 192

    def find_winner(self, selection, area):
        if self.game.search_index.status == False and self.game.replays < 899:
            purse = self.get_odds("purse")
            show = self.get_odds("show")
            place = self.get_odds("place")
            win = self.get_odds("win")
            if self.game.abcd.status == "True":
                purse = purse * 2
                show = show * 2
                place = place * 2
                win = win * 2
            if self.game.show_win.status == "True":
                show = win
            if self.game.purse_win.status == "True":
                purse = win
            if self.game.purse_double.status == "True":
                purse = purse * 2
            if self.game.show_double.status == "True":
                show = show * 2
            if area == "feature" and self.game.pennant.status == True:
                if self.game.replay_counter.position < 160:
                    self.game.search_index.engage(self.game)
                    self.winner_replay_step_up(160 - self.game.replay_counter.position)
            if area == "purse":
                if self.game.replay_counter.position < purse:
                    self.game.search_index.engage(self.game)
                    self.winner_replay_step_up(purse - self.game.replay_counter.position)
            elif area == "show":
                if self.game.replay_counter.position < show:
                    self.game.search_index.engage(self.game)
                    self.winner_replay_step_up(show - self.game.replay_counter.position)
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
            self.delay(name="replay_step_up", delay=0.1, handler=self.winner_replay_step_up, param=number)
        else:
            self.game.search_index.disengage()
            if self.game.abcd.status == True:
                self.game.lettera.disengage()
                self.game.letterb.disengage()
                self.game.letterc.disengage()
                self.game.letterd.disengage()
                self.game.abcd.disengage()
                self.game.coils.bumperALamp.disable()
                self.game.coils.bumperBLamp.disable()
                self.game.coils.bumperCLamp.disable()
                self.game.coils.bumperDLamp.disable()
            self.cancel_delayed(name="replay_step_up")

    def reset_clover(self):
        self.game.purse_double.disengage()
        self.game.purse_win.disengage()
        self.game.show_double.disengage()
        self.game.show_win.disengage()

    def odds2_probability(self):
        if self.game.entry.status == False:
            if self.game.trophy.status == False:
                self.game.odds2.step()
            else:
                if self.game.mixer5.position not in [4,7,9,16,19,21,24]:
                    self.game.odds2.step()
        else:
            if self.game.mixer5.position not in [2,8,12,14,20,24]:
                if self.game.trophy.status == False:
                    self.game.odds2.step()
                else:
                    if self.game.mixer5.position not in [4,7,9,16,19,21,24]:
                        self.game.odds2.step()

    def check_eb(self):
        if self.game.spotting2.position in [2,5,1,11,31,6,7,3,43,13,4]:
            self.game.extra_ball.step()

    def scan_all(self, begin):
        if self.game.eb_play.status == False:
            if self.game.all_advantages.status == True or self.game.star.status == True:
                s = self.animate_star_scan([begin, self.game.spotting.position,1])
                if self.game.star.status == True:
                    self.reset_clover()
            if self.game.all_advantages.status == True or self.game.horseshoe.status == True:
                if self.game.fan.status == False:
                    h = self.animate_selection_scan([begin,self.game.spotting.position,1])
                self.reset_clover()
            if self.game.all_advantages.status == True or self.game.clover.status == True:
                i = self.animate_clover_scan([begin,self.game.spotting.position,1])
            if self.game.all_advantages.status == True or self.game.feature.status == True:
                f = self.animate_feature_scan([begin,self.game.spotting.position,1])
            if self.game.spotting.position in [6,15,28,31,40,3]:
                self.game.left_right.engage(self.game)
                if self.game.cu:
                    self.game.left.disengage()
                    self.game.right.engage(self.game)
                else:
                    self.game.right.disengage()
                    self.game.left.engage(self.game)

            #Check Mixer Re
            if self.game.odds.position < 5:
                if self.game.all_advantages.status == True:
                    if self.game.mixer4.position in [5,7,8,12,16,18,20,21,23]:
                        if self.game.horseshoe.status == True:
                            if self.game.spotting2.position in [3,7,24,34,41]:
                                if self.game.purse_win.status == False:
                                    self.check_wild()

                            if self.game.spotting2.position in [1,14,33,48]:
                                if self.game.show_win.status == False:
                                    self.check_wild()
                            if self.game.spotting2.position in [4,10,13,18,23,29,36,45,50]:
                                self.check_wild()
                            if self.game.spotting2.position in [2,8,16,27,38,43,47]:
                                self.check_hold()
                            elif self.game.spotting2.position in [9,32,40]:
                                if self.game.purse_win.status == False:
                                    self.check_hold()
                            elif self.game.spotting2.position in [6,21,44]:
                                if self.game.show_win.status == False:
                                    self.check_hold()
                else:
                    if self.game.horseshoe.status == True:
                        self.check_wild()

            if self.game.odds.position in [5,6]:
                if self.game.mixer3.position not in [1,4,7,9,12,15,17,19,22]:
                    if self.game.all_advantages.status == True:
                        if self.game.mixer4.position in [5,7,8,12,16,18,20,21,23]:
                            if self.game.horseshoe.status == True:
                                if self.game.spotting2.position in [3,7,24,34,41]:
                                    if self.game.purse_win.status == False:
                                        self.check_wild()

                                if self.game.spotting2.position in [1,14,33,48]:
                                    if self.game.show_win.status == False:
                                        self.check_wild()
                                if self.game.spotting2.position in [4,10,13,18,23,29,36,45,50]:
                                    self.check_wild()
                    else:
                        if self.game.horseshoe.status == True:
                            self.check_wild()


            if self.game.odds.position in [7,8]:
                if self.game.mixer3.position in [2,6,8,11,13,16,18,21,24]:
                    if self.game.all_advantages.status == True:
                        if self.game.mixer4.position in [5,7,8,12,16,18,20,21,23]:
                            if self.game.horseshoe.status == True:
                                if self.game.spotting2.position in [3,7,24,34,41]:
                                    if self.game.purse_win.status == False:
                                        self.check_wild()

                                if self.game.spotting2.position in [1,14,33,48]:
                                    if self.game.show_win.status == False:
                                        self.check_wild()
                                if self.game.spotting2.position in [4,10,13,18,23,29,36,45,50]:
                                    self.check_wild()
                    else:
                        if self.game.horseshoe.status == True:
                            self.check_wild()

            if self.game.odds.position in [9,10]:
                if self.game.mixer3.position in [2,6,11,16,21]:
                    if self.game.all_advantages.status == True:
                        if self.game.mixer4.position in [5,7,8,12,16,18,20,21,23]:
                            if self.game.horseshoe.status == True:
                                if self.game.spotting2.position in [3,7,24,34,41]:
                                    if self.game.purse_win.status == False:
                                        self.check_wild()

                                if self.game.spotting2.position in [1,14,33,48]:
                                    if self.game.show_win.status == False:
                                        self.check_wild()
                                if self.game.spotting2.position in [4,10,13,18,23,29,36,45,50]:
                                    self.check_wild()
                    else:
                        if self.game.horseshoe.status == True:
                            self.check_wild()

        else:
            #Scanning for extra balls
            if self.game.mixer2.position not in [2,7,11,14,17,19]:
                if self.game.cu:
                    self.check_eb()


    def check_wild(self):
        if self.game.spotting.position in [1,25,49,26]:
            if self.game.left_right.status == False:
                self.step_wild(1)
            elif self.game.spotting.position == 2:
                self.step_wild(9 - self.game.wild.position)
            elif self.game.spotting.position == 10:
                self.step_wild(13 - self.game.wild.position)
            elif self.game.spotting.position == 13:
                self.step_wild(21 - self.game.wild.position)

    def check_hold(self):
        if self.game.spotting.position % 3 == 0:
            self.game.hold5.engage(self.game)
            return
        else:
            if self.game.cu == True:
                self.game.hold4.engage(self.game)
            else:
                self.game.hold5.engage(self.game)

    def scan_star(self):
	if self.game.odds.position == 0:
	    self.game.odds.step()
            self.game.coils.four_hundred.pulse()
        else:
            self.star_probability()
        self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def animate_star_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.sunshine_park.star_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="star_animation", delay=0.05, handler=self.animate_star_scan, param=args)
        else:
            self.cancel_delayed(name="star_animation")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)
            self.scan_star()
            self.game.coils.motor.disable()

    def star_probability(self):
        initial = False
        if self.game.odds.position < 4:
            self.game.odds.step()
            self.game.coils.four_hundred.pulse()
            initial = True
        if self.check_reflex() == 1:
            #path 1
            if 4 not in self.game.selection:
                if self.game.hold4.status == True:
                    if self.game.hold3.status == True or self.game.hold5.status == True:
                        if [3,5] not in self.game.selection and [3,5] not in self.game.selection2:
                            if self.game.mixer4.position not in [1,5,7,8,12,16,18,20,21,23]:
                                if self.game.spotting2.position in [24,49]:
                                    if self.game.wild.position < 9:
                                        self.game.purse_win.engage(self.game)
                                elif self.game.spotting2.position in [12,37,10,35]:
                                    self.game.purse_win.engage(self.game)
                                if self.game.spotting2.position in [7,16,22,38,47,32,41,47,13]:
                                    self.game.show_win.engage(self.game)
                                elif self.game.spotting2.position in [3,30,28,5]:
                                    if self.game.wild.position < 13:
                                        self.game.show_win.engage(self.game)
                                if initial == False:
                                    self.check_odds()
            #path 2
            if self.game.mixer2.connected_rivet() not in [1,4,8,9,13,16,20,24]:
                if self.game.hold3.status == True or self.game.hold5.status == True:
                    if [3,5] not in self.game.selection and [3,5] not in self.game.selection2:
                        if self.game.mixer4.position not in [1,5,7,8,12,16,18,20,21,23]:
                            if self.game.spotting2.position in [24,49]:
                                if self.game.wild.position < 9:
                                    self.game.purse_win.engage(self.game)
                            elif self.game.spotting2.position in [12,37,10,35]:
                                self.game.purse_win.engage(self.game)
                            if self.game.spotting2.position in [7,16,22,38,47,32,41,47,13]:
                                self.game.show_win.engage(self.game)
                            elif self.game.spotting2.position in [3,30,28,5]:
                                if self.game.wild.position < 13:
                                    self.game.show_win.engage(self.game)
                            if initial == False:
                                self.check_odds()
                else:
                    if self.game.mixer2.connected_rivet() not in [4,6,9,12,16,18,21,24]:
                        if self.game.mixer4.position not in [1,5,7,8,12,16,18,20,21,23]:
                            if self.game.spotting2.position in [24,49]:
                                if self.game.wild.position < 9:
                                    self.game.purse_win.engage(self.game)
                            elif self.game.spotting2.position in [12,37,10,35]:
                                self.game.purse_win.engage(self.game)
                            if self.game.spotting2.position in [7,16,22,38,47,32,41,47,13]:
                                self.game.show_win.engage(self.game)
                            elif self.game.spotting2.position in [3,30,28,5]:
                                if self.game.wild.position < 13:
                                    self.game.show_win.engage(self.game)
                            if initial == False:
                                self.check_odds()
            #path 3
            if self.game.mixer2.connected_rivet() in [3,7,15,19]:
                if self.game.mixer4.position not in [1,5,7,8,12,16,18,20,21,23]:
                    if self.game.spotting2.position in [24,49]:
                        if self.game.wild.position < 9:
                            self.game.purse_win.engage(self.game)
                    elif self.game.spotting2.position in [12,37,10,35]:
                        self.game.purse_win.engage(self.game)
                    if self.game.spotting2.position in [7,16,22,38,47,32,41,47,13]:
                        self.game.show_win.engage(self.game)
                    elif self.game.spotting2.position in [3,30,28,5]:
                        if self.game.wild.position < 13:
                            self.game.show_win.engage(self.game)
                    if initial == False:
                        self.check_odds()

    def check_odds(self):
        if self.game.fan.status == False:
            if self.game.purse_win.status == False and self.game.show_win.status == False:
                if self.game.odds.position < 4:
                    self.game.odds.step()
                    self.game.coils.four_hundred.pulse()
                    return
                else:
                    if self.game.odds.position == 4:
                        if self.game.spotting2.position in [2,27]:
                            self.check_extra_step()
                    if self.game.odds.position == 5:
                        if self.game.spotting2.position in [1,26]:
                            self.check_extra_step()
                    if self.game.odds.position == 6:
                        if self.game.spotting2.position in [5,30]:
                            self.check_extra_step()
                    if self.game.odds.position == 7:
                        if self.game.spotting2.position in [7,32]:
                            self.check_extra_step()
                    if self.game.odds.position == 8:
                        if self.game.spotting2.position in [10,35]:
                            self.check_extra_step()
                    if self.game.odds.position == 9:
                        if self.game.spotting2.position in [43,18]:
                            self.check_extra_step()
        else:
            if self.game.mixer2.position in [2,5,10,11,14,17,22,23]:
                if self.game.purse_win.status == False and self.game.show_win.status == False:
                    if self.game.odds.position < 4:
                        self.game.odds.step()
                        self.game.coils.four_hundred.pulse()
                        return
                    else:
                        if self.game.odds.position == 4:
                            if self.game.spotting2.position in [2,27]:
                                self.check_extra_step()
                        if self.game.odds.position == 5:
                            if self.game.spotting2.position in [1,26]:
                                self.check_extra_step()
                        if self.game.odds.position == 6:
                            if self.game.spotting2.position in [5,30]:
                                self.check_extra_step()
                        if self.game.odds.position == 7:
                            if self.game.spotting2.position in [7,32]:
                                self.check_extra_step()
                        if self.game.odds.position == 8:
                            if self.game.spotting2.position in [10,35]:
                                self.check_extra_step()
                        if self.game.odds.position == 9:
                            if self.game.spotting2.position in [43,18]:
                                self.check_extra_step()
                else:
                    if self.game.mixer2.position not in [3,5,8,11,15,17,20,23]:
                        if self.game.odds.position < 4:
                            self.game.odds.step()
                            self.game.coils.four_hundred.pulse()
                            return
                        else:
                            if self.game.odds.position == 4:
                                if self.game.spotting2.position in [2,27]:
                                    self.check_extra_step()
                            if self.game.odds.position == 5:
                                if self.game.spotting2.position in [1,26]:
                                    self.check_extra_step()
                            if self.game.odds.position == 6:
                                if self.game.spotting2.position in [5,30]:
                                    self.check_extra_step()
                            if self.game.odds.position == 7:
                                if self.game.spotting2.position in [7,32]:
                                    self.check_extra_step()
                            if self.game.odds.position == 8:
                                if self.game.spotting2.position in [10,35]:
                                    self.check_extra_step()
                            if self.game.odds.position == 9:
                                if self.game.spotting2.position in [43,18]:
                                    self.check_extra_step()

    def check_extra_step(self):
        i = random.randint(0,32)
        if i == 16:
            if self.game.star.status == True:
                s = random.randint(1,6)
                self.step_odds(s)
            else:
                self.game.odds.step()
                self.game.coils.four_hundred.pulse()
        else:
            self.game.odds.step()
            self.game.coils.four_hundred.pulse()

    def step_odds(self, number):
        if number > 0:
            self.game.odds.step()
            self.game.coils.four_hundred.pulse()
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)
            number -= 1
            self.delay(name="step_odds", delay=0.1, handler=self.step_odds, param=number)

    def step_wild(self, number):
        if number > 0:
            self.game.wild.step()
            self.game.coils.four_hundred.pulse()
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)
            number -= 1
            if self.game.wild.position == 21:
                self.game.fan.engage(self.game)
            self.delay(name="step_wild", delay=0.1, handler=self.step_wild, param=number)

    def scan_selection(self):
        self.selection_probability()
        self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def animate_selection_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.sunshine_park.selection_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="selection_animation", delay=0.05, handler=self.animate_selection_scan, param=args)
        else:
            self.cancel_delayed(name="selection_animation")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)
            self.scan_selection()
            self.game.coils.motor.disable()

    def selection_probability(self):
        self.game.selection = []
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

        if self.game.spotting.position % 3 == 0 or self.game.horseshoe.status == True:
            self.selection2_probability()
        if self.game.odds.position < 5:
            self.selection2_probability()
        if self.game.odds.position in [5,6]:
            if self.game.mixer3.position not in [1,4,7,9,12,15,17,19,22]:
                self.selection2_probability()
        if self.game.odds.position in [7,8]:
            if self.game.mixer3.position in [2,6,8,11,13,16,18,21,24]:
                self.selection2_probability()
        if self.game.odds.position in [9,10]:
            if self.game.mixer3.position in [2,6,11,16,21]:
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
        self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def animate_feature_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.sunshine_park.feature_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="feature_animation", delay=0.05, handler=self.animate_feature_scan, param=args)
        else:
            self.cancel_delayed(name="feature_animation")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)
            self.scan_feature()
            self.game.coils.motor.disable()

    def feature_probability(self):
        if self.game.spotting2.position in [2,41,27,16,8,33,23,48]:
            if self.game.spotting2.position in [2,41,27,16]:
                if self.game.feature.status == False:
                    if self.game.mixer3.position == 1:
                        if self.game.mixer4.position in [7,9,20]:
                            self.game.pennant.engage(self.game)
                else:
                    self.game.pennant.engage(self.game)
            else:
                if self.game.feature.status == False:
                    if self.game.mixer3.position == 1:
                        if self.game.mixer4.position in [7,9,20]:
                            self.game.pennant.engage(self.game)
                else:
                    self.game.pennant.engage(self.game)

    def scan_clover(self):
        self.clover_probability()
        self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)

    def animate_clover_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.sunshine_park.clover_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="clover_animation", delay=0.05, handler=self.animate_clover_scan, param=args)
        else:
            self.cancel_delayed(name="clover_animation")
            self.delay(name="display", delay=0.1, handler=graphics.sunshine_park.display, param=self)
            self.scan_clover()
            self.game.coils.motor.disable()

    def clover_probability(self):
        if self.check_reflex() == 1:
            #path 1
            if 4 in self.game.selection:
                if self.game.hold4.status == True:
                    if self.game.hold3.status == True or self.game.hold5.status == True:
                        if [3,5] not in self.game.selection:
                            if self.game.wild.position < 9:
                                if self.game.spotting2.position in [5,7,30,32]:
                                    self.game.purse_double.engage(self.game)
                            else:
                                if self.game.wild.position == 10:
                                    if self.game.spotting2.position in [2,14,23,27,39,48]:
                                        if self.game.purse_win.status == False:
                                            self.game.purse_double.engage(self.game)
                            if self.game.wild.position >= 9 and self.game.wild.position <= 13:
                                if self.game.spotting2.position in [1,15,26,40]:
                                    self.game.show_double.engage(self.game)
                            elif self.game.wild.position >= 13:
                                if self.game.spotting2.position in [6,16,31,41]:
                                    if self.game.show_win.status == False:
                                        self.game.show_double.engage(self.game)
            #path 2
            if self.game.mixer2.connected_rivet() not in [1,4,8,9,13,16,20,24]:
                if self.game.hold3.status == True or self.game.hold5.status == True:
                    if [3,5] not in self.game.selection:
                            if self.game.wild.position < 9:
                                if self.game.spotting2.position in [5,7,30,32]:
                                    self.game.purse_double.engage(self.game)
                            else:
                                if self.game.wild.position == 10:
                                    if self.game.spotting2.position in [2,14,23,27,39,48]:
                                        if self.game.purse_win.status == False:
                                            self.game.purse_double.engage(self.game)
                            if self.game.wild.position >= 9 and self.game.wild.position <= 13:
                                if self.game.spotting2.position in [1,15,26,40]:
                                    self.game.show_double.engage(self.game)
                            elif self.game.wild.position >= 13:
                                if self.game.spotting2.position in [6,16,31,41]:
                                    if self.game.show_win.status == False:
                                        self.game.show_double.engage(self.game)
                else:
                    if self.game.mixer2.connected_rivet() not in [4,6,9,12,16,18,21,24]:
                        if self.game.wild.position < 9:
                            if self.game.spotting2.position in [5,7,30,32]:
                                self.game.purse_double.engage(self.game)
                        else:
                            if self.game.wild.position == 10:
                                if self.game.spotting2.position in [2,14,23,27,39,48]:
                                    if self.game.purse_win.status == False:
                                        self.game.purse_double.engage(self.game)
                        if self.game.wild.position >= 9 and self.game.wild.position <= 13:
                            if self.game.spotting2.position in [1,15,26,40]:
                                self.game.show_double.engage(self.game)
                        elif self.game.wild.position >= 13:
                            if self.game.spotting2.position in [6,16,31,41]:
                                if self.game.show_win.status == False:
                                    self.game.show_double.engage(self.game)
            #path 3
            if self.game.mixer2.connected_rivet() in [3,7,15,19]:
                if self.game.wild.position < 9:
                    if self.game.spotting2.position in [5,7,30,32]:
                        self.game.purse_double.engage(self.game)
                else:
                    if self.game.wild.position == 10:
                        if self.game.spotting2.position in [2,14,23,27,39,48]:
                            if self.game.purse_win.status == False:
                                self.game.purse_double.engage(self.game)
                if self.game.wild.position >= 9 and self.game.wild.position <= 13:
                    if self.game.spotting2.position in [1,15,26,40]:
                        self.game.show_double.engage(self.game)
                elif self.game.wild.position >= 13:
                    if self.game.spotting2.position in [6,16,31,41]:
                        if self.game.show_win.status == False:
                            self.game.show_double.engage(self.game)

    def check_reflex(self):
        if self.game.reflex.connected_rivet() == 5:
            if self.game.abcd.status == False or self.game.mixer1.connected_rivet("sunshine_park") not in [3,10,14,20]:
                return 1
        elif self.game.reflex.connected_rivet() == 4 and self.game.mixer1.connected_rivet("sunshine_park") not in [2,3,4,5,7,9,10,12,15,17,19,20,21,23]:
            if self.game.abcd.status == False or self.game.mixer1.connected_rivet("sunshine_park") not in [3,10,14,20]:
                return 1
        elif self.game.reflex.connected_rivet() == 3 and self.game.mixer1.connected_rivet("sunshine_park") not in [2,5,7,9,12,15,19,23]:
            if self.game.abcd.status == False or self.game.mixer1.connected_rivet("sunshine_park") not in [3,10,14,20]:
                return 1
        elif self.game.reflex.connected_rivet() == 2 and self.game.mixer1.connected_rivet("sunshine_park") not in [5,9,12,15,19,23]:
            if self.game.abcd.status == False or self.game.mixer1.connected_rivet("sunshine_park") not in [3,10,14,20]:
                return 1
        elif self.game.reflex.connected_rivet() == 1 and self.game.mixer1.connected_rivet("sunshine_park") not in [5,9,15,23]:
            if self.game.abcd.status == False or self.game.mixer1.connected_rivet("sunshine_park") not in [3,10,14,20]:
                return 1
        else:
            return 0

    # Define reset as the knock-off, anti-cheat relay disabled, and replay reset enabled.  Motors turn while credits are knocked off.
    # When meter reaches zero and the zero limit switch is hit, turn off motor sound and leave backglass gi on, but with tilt displayed.

    def startup(self):
        self.eb = False
        self.tilt_actions()


class SunshinePark(procgame.game.BasicGame):
    """ Sunshine Park was the last one ball made by Bally """
    def __init__(self, machine_type):
        super(SunshinePark, self).__init__(machine_type)
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

        #Initialize the mixer units
        self.mixer1 = units.Mixer("mixer1", 23)
        r = random.randint(0,23)
        self.mixer1.position = r
        self.mixer2 = units.Mixer("mixer2", 23)
        r = random.randint(0,23)
        self.mixer2.position = r
        self.mixer3 = units.Mixer("mixer3", 23)
        r = random.randint(0,23)
        self.mixer3.position = r
        self.mixer4 = units.Mixer("mixer4", 23)
        r = random.randint(0,23)
        self.mixer4.position = r
        self.mixer5 = units.Mixer("mixer5", 23)
        r = random.randint(0,23)
        self.mixer5.position = r

        self.spotting = units.Spotting("spotting", 50)
        r = random.randint(0,49)
        self.spotting.position = r
        self.spotting2 = units.Spotting("spotting", 50)
        r = random.randint(0,49)
        self.spotting2.position = r

        self.search_index = units.Relay("search_index")

        #Replay Counter
        self.replay_counter = units.Stepper("replay_counter", 300)

        #Initialize stepper units used to keep track of features or timing.
        self.odds = units.Stepper("odds", 10)
        self.wild = units.Stepper("wild", 21)
        self.extra_ball = units.Stepper("extra_ball", 36)
        self.ball_count = units.Stepper("ball_count", 5)

        #Check for status of the replay register zero switch.  If positive
        #and machine is just powered on, this will zero out the replays.
        self.replay_reset = units.Relay("replay_reset")

        #When engage()d, light 6v circuit, and enable game features, scoring,
        #etc. Disengage()d means that the machine is 'soft' tilted.
        self.anti_cheat = units.Relay("anti_cheat")

        #When engage()d, spin.
        self.start = units.Relay("start")

        self.abcd = units.Relay("abcd")
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
        self.eb_play = units.Relay("eb_play")

        self.cu = 0

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
        super(SunshinePark, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')

        main_mode = OneBall(self)
        self.modes.add(main_mode)

game = SunshinePark(machine_type='pdb')
game.reset()
game.run_loop()
