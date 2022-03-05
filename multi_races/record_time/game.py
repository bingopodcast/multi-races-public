#!/usr/bin/python

import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
import procgame.game, sys, os, random
import procgame.config
import procgame.sound

sys.path.insert(0,os.path.pardir)
import multi_races.common.units as units
import multi_races.common.functions as functions
from multi_races.graphics import methods as graphics
from multi_races.graphics.record_time import *

class OneBall(procgame.game.Mode):
    def __init__(self, game):
        super(OneBall, self).__init__(game=game, priority=5)
        self.holes = []
        self.startup()


    def sw_coin_active(self, sw):
        self.game.tilt.disengage()
        self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_flag_active(self, sw):
		if self.game.switches.star.is_active() and self.game.switches.horseshoe.is_active():
			self.game.end_run_loop()
			del self.game.proc
			os.system("/home/nbaldridge/proc/multi-races/multi_races/start_game.sh record_time")

    def check_shutter(self, start=0):
        if start == 1:
            if self.game.switches.smRunout.is_active():
                self.game.coils.shutter.disable()
        else:
            if self.game.switches.smRunout.is_inactive():
                self.game.coils.shutter.disable()

    def regular_play(self):
        self.game.payout_number = 0
        self.game.coils.payout.disable()
        self.game.selection = []
        self.game.cu = not self.game.cu
        self.cancel_delayed(name="replay_step_up")
        self.game.search_index.disengage()
        self.game.coils.counter.pulse()
        self.game.coils.motor.enable()
        self.game.coils.timing.pulse()
        self.game.coils.four_hundred.pulse()
        begin = self.game.spotting.position
        self.game.spotting.spin()
        self.game.forty.step()
        if self.game.switches.lane.is_inactive():
            if self.game.switches.rightcap.is_active():
                if self.game.right.status == True:
                    self.game.feature_unit.reset()
            if self.game.switches.leftcap.is_active():
                if self.game.left.status == True:
                    self.game.feature_unit_left.reset()
            if self.game.feature_unit.position == 0:
                self.game.feature_unit.step()
            if self.game.feature_unit_left.position == 0:
                self.game.feature_unit_left.step()
            self.game.coils.shutter.enable()
        self.game.replay_counter.reset()
        self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)
        self.game.tilt.disengage()
        if self.game.start.status == False:
            self.game.coin.reset()
            self.game.odds.reset()
            self.game.left.disengage()
            self.game.right.disengage()
            self.game.left_right.disengage()
            self.game.pennant.disengage()
            self.game.show_section.disengage()
            self.game.place_section.disengage()
            self.game.win_section.disengage()
            self.game.coils.show.disable()
            self.game.coils.place.disable()
            self.game.coils.win.disable()
        self.game.coin.step()
        self.scan_all(begin)
        self.game.reflex.decrease()
        self.replay_step_down()
        if self.game.forty.position == 40:
            self.game.selection = [1,2,3,4,5,6,7]
            self.game.forty.reset()

    def sw_lane_active(self, sw):
        self.game.start.engage(self.game)

    def sw_smRunout_active_for_10ms(self, sw):
        self.game.coils.shutter.disable()

    def sw_lane_inactive_for_1ms(self, sw):
        self.game.start.disengage()

    def sw_leftcap_active(self, sw):
        if self.game.left.status == True:
            m = self.get_multiplier()
            self.winner_replay_step_up(4 * m, True)
            self.game.name.step()
            self.game.coils.four_hundred.pulse()
            if self.game.name.position == 5:
                self.winner_replay_step_up(40 * m, True)
        self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_rightcap_active(self, sw):
        if self.game.right.status == True:
            m = self.get_multiplier()
            self.winner_replay_step_up(4 * m, True)
            self.game.name.step()
            self.game.coils.four_hundred.pulse()
            if self.game.name.position == 5:
                self.winner_replay_step_up(40 * m, True)
        self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_leftcap_active(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("feature")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_rightcap_active(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("feature")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    # This is really nasty, but it is how we render graphics for each individual hole.

    def sw_purse1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("purse")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_purse2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("purse")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_purse3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("purse")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_purse4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("purse")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_purse5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("purse")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_purse6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("purse")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_purse7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("purse")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_show1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("show")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_show2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("show")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_show3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("show")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_show4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("show")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_show5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("show")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_show6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("show")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_show7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("show")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_place1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("place")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_place2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("place")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_place3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("place")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_place4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("place")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_place5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("place")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_place6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("place")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_place7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("place")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_win1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("win")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_win2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("win")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_win3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("win")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_win4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("win")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_win5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("win")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_win6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("win")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_win7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("win")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_feature_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("feature")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        graphics.record_time.display(self)
        self.tilt_actions()
        self.replay_step_down(self.game.replays)

    def tilt_actions(self):
        self.game.payout_number = 0
        self.game.coils.payout.disable()
        self.game.start.disengage()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="replay_step_up")
        self.game.odds.reset()
        self.game.pennant.disengage()
        self.game.left.disengage()
        self.game.right.disengage()
        self.game.replay_counter.reset()
        self.game.left_right.disengage()
        self.game.search_index.disengage()
        self.game.anti_cheat.engage(game)
        self.game.tilt.engage(self.game)
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            self.tilt_actions()

    def sw_odds_active(self, sw):
        self.game.show_section.engage(self.game)

    def sw_trophy_active(self, sw):
        self.game.place_section.engage(self.game)

    def sw_entry_active(self, sw):
        self.game.win_section.engage(self.game)

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.record_time.reel1, graphics.record_time.reel10, graphics.record_time.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.record_time.display(self)
                self.delay(name="replay_reset", delay=0.13, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.record_time.reel1, graphics.record_time.reel10, graphics.record_time.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.record_time.display(self)
                self.cancel_delayed(name="replay_reset")
        else:
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.record_time.reel1, graphics.record_time.reel10, graphics.record_time.reel100)
                self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)
            self.game.coils.registerDown.pulse()

    def replay_step_up(self):
        if self.game.replays < 899:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.record_time.reel1, graphics.record_time.reel10, graphics.record_time.reel100)
        self.game.coils.registerUp.pulse()
        self.game.reflex.increase()
        graphics.record_time.display(self)

    def get_multiplier(self):
        return self.game.coin.position

    def sw_startButton_active(self, sw):
        if self.game.replays > 0 or self.game.switches.freeplay.is_inactive():
            self.regular_play()
            return

    def search(self, area):
        selection = self.game.selection
        allow_continue = False
        if self.game.start.status == False:
            for item in selection: 
                sw = "self.game.switches.%s%s.is_active()" % (area, item)
                if eval(sw):
                    self.find_winner(selection, area)
            if area == "show" and self.game.show_section.status == True:
                self.find_winner(item, area)
            if area == "place" and self.game.place_section.status == True:
                self.find_winner(item, area)
            if area == "win" and self.game.win_section.status == True:
                self.find_winner(item, area)

    def get_odds(self, section):
        if section == "purse":
            if self.game.odds.position in [1,2]:
                return 2
            elif self.game.odds.position == 3:
                return 4
            elif self.game.odds.position == 4:
                return 8
            elif self.game.odds.position == 5:
                return 12
        elif section == "show":
            if self.game.odds.position == 1:
                return 2
            elif self.game.odds.position == 2:
                return 4
            elif self.game.odds.position == 3:
                return 8
            elif self.game.odds.position == 4:
                return 12
            elif self.game.odds.position == 5:
                return 16
        elif section == "place":
            if self.game.odds.position == 1:
                return 4
            elif self.game.odds.position == 2:
                return 8
            elif self.game.odds.position == 3:
                return 12
            elif self.game.odds.position == 4:
                return 16
            elif self.game.odds.position == 5:
                return 20
        elif section == "win":
            if self.game.odds.position == 1:
                return 8
            elif self.game.odds.position == 2:
                return 12
            elif self.game.odds.position == 3:
                return 16
            elif self.game.odds.position == 4:
                return 20
            elif self.game.odds.position == 5:
                return 40

    def find_winner(self, selection, area=None):
        if self.game.search_index.status == False and self.game.replays < 899:
            purse = self.get_odds("purse")
            show = self.get_odds("show")
            place = self.get_odds("place")
            win = self.get_odds("win")
            m = self.get_multiplier()
            if area == "purse":
                if self.game.replay_counter.position < purse:
                    self.game.search_index.engage(self.game)
                    self.winner_replay_step_up(purse * m, True)
            elif area == "show":
                if self.game.replay_counter.position < show:
                    self.game.search_index.engage(self.game)
                    self.winner_replay_step_up(show * m, True)
            elif area == "place":
                if self.game.replay_counter.position < place:
                    self.game.search_index.engage(self.game)
                    self.winner_replay_step_up(place * m, True)
            else:
                if area == "win":
                    if self.game.replay_counter.position < win:
                        self.game.search_index.engage(self.game)
                        self.winner_replay_step_up(win * m, True)

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

    def check_payout(self, number):
        if number >= 2:
            if self.game.switches.paid.is_active():
                number -= 2
                self.delay(name="replay_step_up", delay=0.1, handler=self.winner_replay_step_up, param=number)
            else:
                self.delay(name="check_payout", delay=0.1, handler=self.check_payout, param=number)

    def sw_paid_active(self, sw):
        self.game.payout_number -= 2
        self.game.replay_counter.step()
        self.game.coils.four_hundred.pulse()
        self.game.reflex.increase()
        self.game.replay_counter.step()
        self.game.reflex.increase()
        print self.game.payout_number

    def check_initial_portioning(self):
        return True

    def scan_all(self, begin):
        s = self.animate_star_scan([begin,self.game.spotting.position,1])
        u = self.animate_selection_scan([begin,self.game.spotting.position,1])
        
        self.game.four_hundred.step()

        if self.game.spotting.position in [22, 47]:
            if self.game.four_hundred.position % 20 == 0:
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

        if self.game.spotting.position in [5,6,7,18,20]:
            self.game.feature_unit.engage()

        if self.game.spotting.position in [10,35]:
            self.game.coils.show.enable()
        if self.game.spotting.position in [28,3]:
            self.game.coils.place.enable()
        if self.game.spotting.position in [42,17]:
            self.game.coils.win.enable()

    def scan_star(self):
        self.star_probability()
        self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def animate_star_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        self.game.odds.position = 0
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.record_time.star_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="star_animation", delay=0.05, handler=self.animate_star_scan, param=args)
        else:
            self.cancel_delayed(name="star_animation")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)
            self.scan_star()
            self.game.coils.motor.disable()

    def star_probability(self):
        self.check_odds()

    def check_odds(self):
        if self.game.spotting.position in [5,10,15,20,25,30,35,40,45,50]:
            self.game.odds.position = 1
        if self.game.spotting.position in [4,9,14,19,24,29,34,39,44,49]:
            self.game.odds.position = 2
        if self.game.spotting.position in [3,8,13,18,23,28,33,38,43,48]:
            self.game.odds.position = 3
        if self.game.spotting.position in [2,7,12,17,22,27,32,37,42,47]:
            self.game.odds.position = 4
        if self.game.spotting.position in [1,6,11,16,21,26,31,36,41,46]:
            self.game.odds.position = 5

    def check_extra_step(self):
        i = random.randint(0,32)
        if i == 16:
            s = random.randint(1,6)
            self.step_odds(s)
        else:
            self.game.odds.step()
            self.game.coils.four_hundred.pulse()

    def step_odds(self, number):
        if number > 0:
            self.game.odds.step()
            self.game.coils.four_hundred.pulse()
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)
            number -= 1
            self.delay(name="step_odds", delay=0.1, handler=self.step_odds, param=number)

    def scan_selection(self):
        self.selection_probability()
        self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def animate_selection_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.record_time.selection_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="selection_animation", delay=0.05, handler=self.animate_selection_scan, param=args)
        else:
            self.cancel_delayed(name="selection_animation")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)
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

        if self.game.odds.position >= 4:
            self.game.selection2 = self.selection2_probability()

    def selection2_probability(self):
        if self.game.spotting.position in [1,26,8,33,15,40,23,48]:
            self.game.selection.append(7)
        if self.game.spotting.position in [2,27,9,34,16,41,24,49]:
            self.game.selection.append(6)
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

    def scan_clover(self):
        self.clover_probability()
        self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)

    def animate_clover_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.record_time.clover_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="clover_animation", delay=0.05, handler=self.animate_clover_scan, param=args)
        else:
            self.cancel_delayed(name="clover_animation")
            self.delay(name="display", delay=0.1, handler=graphics.record_time.display, param=self)
            self.scan_clover()
            self.game.coils.motor.disable()

    def clover_probability(self):
        if self.check_reflex() == 1:
            #path 1
            if self.game.number_four.status == False:
                if self.game.hold4.status == True:
                    if self.game.hold5.status == True:
                        if [3,5] not in self.game.selection and [3,5] not in self.game.selection2:
                            if self.game.spotting.position in [5,7,30,32]:
                                self.game.purse_win.engage(self.game)

                            if self.game.spotting.position in [2,14,23,27,39,48]:
                                if self.game.purse_win.status == False:
                                    self.game.purse_win.engage(self.game)
                            if self.game.spotting.position in [1,15,26,40]:
                                self.game.show_win.engage(self.game)
                            if self.game.spotting.position in [6,16,31,41]:
                                if self.game.show_win.status == False:
                                    self.game.show_win.engage(self.game)

    # Define reset as the knock-off, anti-cheat relay disabled, and replay reset enabled.  Motors turn while credits are knocked off.
    # When meter reaches zero and the zero limit switch is hit, turn off motor sound and leave backglass gi on, but with tilt displayed.

    def startup(self):
        self.eb = False
        self.tilt_actions()


class RecordTime(procgame.game.BasicGame):
    """ Turf King was one of the last one balls made by Bally """
    def __init__(self, machine_type):
        super(RecordTime, self).__init__(machine_type)
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

        self.spotting = units.Spotting("spotting", 50)
        r = random.randint(0,49)
        self.spotting.position = r

        self.search_index = units.Relay("search_index")

        #Replay Counter
        self.replay_counter = units.Stepper("replay_counter", 300)

        #Initialize stepper units used to keep track of features or timing.
        self.odds = units.Stepper("odds", 5)
        self.four_hundred = units.Stepper("four_hundred", 400, "record_time", "continuous")
        r = random.randint(0,399)
        self.four_hundred.position = r
        self.feature_unit = units.Relay("feature_unit")
        self.coin = units.Stepper("coin", 10)
        self.name = units.Stepper("name", 5)
        r = random.randint(0,4)
        self.name.position = r

        self.payout_number = 0
        self.cu = 1

        #Check for status of the replay register zero switch.  If positive
        #and machine is just powered on, this will zero out the replays.
        self.replay_reset = units.Relay("replay_reset")

        #When engage()d, light 6v circuit, and enable game features, scoring,
        #etc. Disengage()d means that the machine is 'soft' tilted.
        self.anti_cheat = units.Relay("anti_cheat")

        #When engage()d, spin.
        self.start = units.Relay("start")

        self.left = units.Relay("left")
        self.right = units.Relay("right")
        self.left_right = units.Relay("left_right")
        self.purse_win = units.Relay("purse_win")
        self.show_win = units.Relay("show_win")
        self.pennant = units.Relay("pennant")

        self.show_section = units.Relay("show_section")
        self.place_section = units.Relay("place_section")
        self.win_section = units.Relay("win_section")
        
        self.forty = units.Stepper("forty", 40)

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
        super(RecordTime, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')

        main_mode = OneBall(self)
        self.modes.add(main_mode)

game = RecordTime(machine_type='pdb')
game.reset()
game.run_loop()
