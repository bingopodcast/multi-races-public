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
from multi_races.graphics.jockey_club import *

class OneBall(procgame.game.Mode):
    def __init__(self, game):
        super(OneBall, self).__init__(game=game, priority=5)
        self.holes = []
        self.startup()
        self.game.sound.register_sound('tilt', "audio/tilt.wav")
        self.game.sound.register_sound('step', "audio/step.wav")


    def sw_coin_active(self, sw):
        self.game.tilt.disengage()
        self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def sw_enter_active(self, sw):
        if self.game.switches.startButton.is_active() and self.game.switches.feature.is_active():
            self.game.end_run_loop()
            os.system("/home/nbaldridge/proc/multi-races/start_game.sh jockey_club")

    def check_shutter(self, start=0):
        if start == 1:
            if self.game.switches.smRunout.is_active():
                if self.game.switches.shutter.is_active():
                    self.game.coils.shutter.disable()
        else:
            if self.game.switches.shutter.is_inactive():
                if self.game.switches.smRunout.is_active():
                    self.game.coils.shutter.disable()

    def regular_play(self):
        self.cancel_delayed(name="replay_step_up")
        self.game.search_index.disengage()
        self.game.coils.counter.pulse()
        self.game.coils.motor.pulse(40)
        self.game.spotting.spin()
        if self.game.switches.shutter.is_inactive():
            self.game.coils.shutter.enable()
        self.game.replay_counter.reset()
        self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)
        self.game.tilt.disengage()
        if self.game.start.status == False:
            self.game.coin.reset()
            self.game.odds.reset()
            if self.game.name.position == 5:
                self.game.name.reset()
            self.game.clover.disengage()
            self.game.horseshoe.disengage()
            self.game.hold4.disengage()
            self.game.hold5.disengage()
            self.game.left.disengage()
            self.game.right.disengage()
            self.game.left_right.disengage()
            self.game.purse_win.disengage()
            self.game.show_win.disengage()
            self.game.pennant.disengage()
        self.game.coin.step()
        self.scan_all()
        self.game.reflex.decrease()
        self.replay_step_down()

    def sw_lane_active(self):
        self.game.start.engage(self.game)

    def sw_smRunout_active_for_1ms(self, sw):
        if self.game.start.status == True:
            self.check_shutter(1)
        else:
            self.check_shutter()

    def sw_gate_inactive_for_1ms(self, sw):
        self.game.start.disengage()
        self.game.horseshoe.disengage()
        self.game.clover.disengage()
        if self.game.switches.shutter.is_active():
            self.game.coils.shutter.enable()
        self.game.sound.play('tilt')

    # This is really nasty, but it is how we render graphics for each individual hole.

    def sw_purse1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search()
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def sw_purse2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search()
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def sw_purse3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search()
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def sw_purse4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search()
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def sw_purse5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search()
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def sw_purse6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search()
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def sw_purse7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search()
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def sw_show1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search()
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def sw_show2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search()
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def sw_show3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search()
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def sw_show4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search()
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def sw_show5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search()
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def sw_show6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search()
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def sw_show7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search()
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def sw_place1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search()
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def sw_place2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search()
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def sw_place3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search()
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def sw_place4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search()
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def sw_place5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search()
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def sw_place6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search()
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def sw_place7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search()
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def sw_win1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search()
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def sw_win2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search()
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def sw_win3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search()
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def sw_win4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search()
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def sw_win5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search()
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def sw_win6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search()
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def sw_win7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search()
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        graphics.jockey_club.display(self)
        self.tilt_actions()
        self.replay_step_down(self.game.replays)

    def tilt_actions(self):
        self.game.start.disengage()
        self.cancel_delayed(name="replay_reset")
        self.cancel_delayed(name="replay_step_up")
        self.game.odds.reset()
        self.game.clover.disengage()
        self.game.horseshoe.disengage()
        self.game.all_advantages.disengage()
        self.game.feature.disengage()
        self.game.left.disengage()
        self.game.right.disengage()
        self.game.replay_counter.reset()
        self.game.hold4.disengage()
        self.game.hold5.disengage()
        self.game.abcd.disengage()
        self.game.left_right.disengage()
        self.game.purse_win.disengage()
        self.game.show_win.disengage()
        self.game.search_index.disengage()
        self.game.anti_cheat.engage(game)
        self.game.tilt.engage(self.game)
        self.game.sound.stop_music()
        self.game.sound.play('tilt')
        # displays "Tilt" on the backglass, you have to recoin.
        self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            self.tilt_actions()

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.jockey_club.reel1, graphics.jockey_club.reel10, graphics.jockey_club.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.jockey_club.display(self)
                self.delay(name="replay_reset", delay=0.13, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.jockey_club.reel1, graphics.jockey_club.reel10, graphics.jockey_club.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.jockey_club.display(self)
                self.cancel_delayed(name="replay_reset")
        else:
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.jockey_club.reel1, graphics.jockey_club.reel10, graphics.jockey_club.reel100)
                self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)
            self.game.coils.registerDown.pulse()

    def sw_leftcap_active(self, sw):
        if self.game.left.status == True:
            m = self.get_multiplier()
            self.winner_replay_step_up(3 * m)
            self.game.name.step()
            if self.game.name.position == 5:
                self.winner_replay_step_up(40 * m)

    def sw_rightcap_active(self, sw):
        if self.game.right.status == True:
            m = self.get_multiplier()
            self.winner_replay_step_up(3 * m)
            self.game.name.step()
            if self.game.name.position == 5:
                self.winner_replay_step_up(40 * m)

    def get_multiplier(self):
            return self.game.coin.position + 1

    def sw_bumpera_active(self, sw):
        if self.game.lettera.status == False:
            self.game.lettera.engage(self.game)

    def sw_bumperb_active(self, sw):
        if self.game.letterb.status == False:
            if self.game.lettera.status == True:
                self.game.letterb.engage(self.game)

    def sw_bumperc_active(self, sw):
        if self.game.letterc.status == False:
            if self.game.letterb.status == True:
                self.game.letterc.engage(self.game)

    def sw_bumperd_active(self, sw):
        if self.game.letterd.status == False:
            if self.game.letterc.status == True:
                self.game.letterd.engage(self.game)
                self.game.abcd.engage(self.game)
                self.game.search_index.engage(self.game)
                self.winner_replay_step_up(self.game.feature_unit.position * 20)

    def replay_step_up(self):
        if self.game.replays < 899:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.jockey_club.reel1, graphics.jockey_club.reel10, graphics.jockey_club.reel100)
        self.game.coils.registerUp.pulse()
        self.game.reflex.increase()
        graphics.jockey_club.display(self)

    def sw_clover_active(self, sw):
        if self.game.clover.status == True and (self.game.replays > 0 or self.game.switches.freeplay.is_active()):
            self.game.regular_play()
            return
        if self.game.clover.status == False:
            self.game.horseshoe.disengage()
            self.game.clover.engage(self.game)
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)
            self.delay(name="clover", delay=0.1, handler=self.sw_clover_active, param=sw)

    def sw_horseshoe_active(self, sw):
        if self.game.horseshoe.status == True and (self.game.replays > 0 or self.game.switches.freeplay.is_active()):
            self.game.regular_play()
            return
        if self.game.horseshoe.status == False:
            self.game.clover.disengage()
            self.game.horseshoe.engage(self.game)
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)
            self.delay(name="horseshoe", delay=0.1, handler=self.sw_horseshoe_active, param=sw)

    def search(self):
        selection = self.game.selection
        selection2 = self.game.selection2
        if sw_%s_is_active() % (selection):
            self.find_winner(selection)
        if sw_%s_is_active() % (selection2):
            self.find_winner(selection2)

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
                return 20
            elif self.game.odds.position == 8:
                return 40
        elif section == "show":
            if self.game.odds.position == 1:
                return 6
            elif self.game.odds.position == 2:
                return 6
            elif self.game.odds.position == 3:
                return 10
            elif self.game.odds.position == 4:
                return 16
            elif self.game.odds.position == 5:
                return 24
            elif self.game.odds.position == 6:
                return 32
            elif self.game.odds.position == 7:
                return 40
            elif self.game.odds.position == 8:
                return 80
        elif section == "place":
            if self.game.odds.position == 1:
                return 9
            elif self.game.odds.position == 2:
                return 9
            elif self.game.odds.position == 3:
                return 15
            elif self.game.odds.position == 4:
                return 24
            elif self.game.odds.position == 5:
                return 36
            elif self.game.odds.position == 6:
                return 48
            elif self.game.odds.position == 7:
                return 60
            elif self.game.odds.position == 8:
                return 120
        elif section == "win":
            if self.game.odds.position == 1:
                return 12
            elif self.game.odds.position == 2:
                return 12
            elif self.game.odds.position == 3:
                return 20
            elif self.game.odds.position == 4:
                return 32
            elif self.game.odds.position == 5:
                return 48
            elif self.game.odds.position == 6:
                return 64
            elif self.game.odds.position == 7:
                return 80
            elif self.game.odds.position == 8:
                return 160

    def find_winner(self, selection):
        if self.game.search_index.status == False and self.game.replays < 899:
            purse = self.get_odds("purse")
            show = self.get_odds("show")
            place = self.get_odds("place")
            win = self.get_odds("win")
            if self.game.show_win.status == "True":
                show = win
            if self.game.purse_win.status == "True":
                purse = win
            if selection[:1] == "feature" and self.game.pennant.status == True:
                m = self.get_multiplier()
                self.game.search_index.engage(self.game)
                self.winner_replay_step_up(40 * m)
            if selection[:1] == "purse" or selection2[:1] == "purse":
                m = self.get_multiplier()
                if self.game.replay_counter.position < purse:
                    self.game.search_index.engage(self.game)
                    self.winner_replay_step_up(purse * m)
            elif selection[:1] == "show" or selection2[:1] == "show":
                if self.game.replay_counter.position < show:
                    self.game.search_index.engage(self.game)
                    self.winner_replay_step_up(show * m)
            elif selection[:1] == "place" or selection2[:1] == "place":
                if self.game.replay_counter.position < place:
                    self.game.search_index.engage(self.game)
                    self.winner_replay_step_up(place * m)
            else:
                if selection[:1] == "win" or selection2[:1] == "win":
                    if self.game.replay_counter.position < win:
                        self.game.search_index.engage(self.game)
                        self.winner_replay_step_up(win * m)

    def winner_replay_step_up(self, number):
        if number >= 2:
            self.game.replay_counter.step()
            self.game.coils.payout.enable()
            self.replay_step_up()
            self.check_payout(number)
        else:
            self.game.coils.payout.disable()
            self.game.search_index.disengage()
            if self.game.abcd.status == True:
                self.game.lettera.disengage()
                self.game.letterb.disengage()
                self.game.letterc.disengage()
                self.game.letterd.disengage()
                self.game.abcd.disengage()
            self.cancel_delayed(name="replay_step_up")
            self.search()
            self.timeout_actions()

    def reset_clover(self):
        self.game.purse_win.disengage()
        self.game.show_win.disengage()

    def check_initial_portioning(self):
        return True

    def scan_all(self):
        if self.game.clover.status == True:
            s = self.animate_star_scan()
            t = self.animate_clover_scan()
            u = self.animate_selection_scan()
        if self.game.horseshoe.status == True:
            v = self.animate_feature_scan()
            w = self.animate_win_scan()
            self.check_hold()

        self.game.four_hundred.step()

        if self.game.four_hundred.position == 0:
            self.game.feature_unit.step()

        if self.game.spotting.position in [37,12]:
            self.game.left_right.engage(self.game)
            if self.game.cu:
                self.game.left.disengage()
                self.game.right.engage(self.game)
            else:
                self.game.right.disengage()
                self.game.left.engage(self.game)

        if self.game.spotting.position in [22, 47]:
            if self.game.four_hundred % 20 == 0:
                self.game.pennant.engage(self.game)

    def check_hold(self):
        if self.game.four_hundred.position % 3 == 0.15:
            if self.game.spotting.position in [33,34]:
                if self.game.cu:
                    self.game.hold3.engage(self.game)
                    self.game.hold5.engage(self.game)
                else:
                    self.game.hold4.engage(self.game)

    def scan_star(self):
        self.star_probability()
        self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def animate_star_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.jockey_club.star_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="star_animation", delay=0.05, handler=self.animate_star_scan, param=args)
        else:
            self.cancel_delayed(name="star_animation")
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)
            self.scan_star()

    def star_probability(self):
        self.check_odds()

    def check_odds(self):
        p = self.check_initial_portioning()
        if p == True:
            if self.game.spotting.position in [0,3,5,10,15,25,28,30,35,40,45]:
                self.game.odds.position = 0
            if self.game.spotting.position in [1,2,4,7,11,12,19,22,26,27,32,37,43,44]:
                self.game.odds.position = 1
            if self.game.spotting.position in [6,8,9,13,14,21,23,31,34,38,46,48]:
                self.game.odds.position = 2
            if self.game.spotting.position in [16,24,41]:
                self.game.odds.position = 3
            if self.game.spotting.position in [17,42]:
                self.game.odds.position = 4
            if self.game.spotting.position in [49,39]:
                self.game.odds.position = 5
            if self.game.spotting.position in [20,33]:
                self.game.odds.position = 6
            if self.game.spotting.position in [18,29]:
                self.game.odds.position = 7
            if self.game.spotting.position in [36,47]:
                self.game.odds.position = 8

    def check_extra_step(self):
        i = random.randint(0,32)
        if i == 16:
            s = random.randint(1,6)
            self.step_odds(s)
        else:
            self.game.odds.step()

    def step_odds(self, number):
        if number > 0:
            self.game.odds.step()
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)
            number -= 1
            self.delay(name="step_odds", delay=0.1, handler=self.step_odds, param=number)

    def scan_selection(self):
        self.selection_probability()
        self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def animate_selection_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.jockey_club.selection_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="selection_animation", delay=0.05, handler=self.animate_selection_scan, param=args)
        else:
            self.cancel_delayed(name="selection_animation")
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)
            self.scan_selection()

    def selection_probability(self):
        if self.game.spotting.position in [1,26,8,33,15,40,23,48]:
            self.game.selection = 1
        if self.game.spotting.position in [2,27,9,34,16,41,24,49]:
            self.game.selection = 2
        if self.game.spotting.position in [3,28,10,35,17,42,25,50,0]:
            self.game.selection = 3
        if self.game.spotting.position in [4,29,11,36,18,43]:
            self.game.selection = 4
        if self.game.spotting.position in [5,30,12,37,19,44]:
            self.game.selection = 5
        if self.game.spotting.position in [6,31,13,38,20,45]:
            self.game.selection = 6
        if self.game.spotting.position in [7,32,14,39,21,46,47,22]:
            self.game.selection = 7

        if self.game.coin.position % 3 == 0 or self.game.horseshoe.status == True:
            self.game.selection2 = self.selection2_probability()
        if self.game.odds.position < 5:
            self.game.selection2 = self.selection2_probability()
        if self.game.odds.position in [5,6]:
            self.game.selection2 = self.selection2_probability()
        if self.game.odds.position in [7,8]:
            self.game.selection2 = self.selection2_probability()
        if self.game.odds.position in [9,10]:
            self.game.selection2 = self.selection2_probability()

    def selection2_probability(self):
        if self.game.spotting.position in [1,26,8,33,15,40,23,48]:
            self.game.selection = 7
        if self.game.spotting.position in [2,27,9,34,16,41,24,49]:
            self.game.selection = 6
        if self.game.spotting.position in [3,28,10,35,17,42,25,50,0]:
            self.game.selection = 5
        if self.game.spotting.position in [4,29,11,36,18,43]:
            self.game.selection = 4
        if self.game.spotting.position in [5,30,12,37,19,44]:
            self.game.selection = 3
        if self.game.spotting.position in [6,31,13,38,20,45]:
            self.game.selection = 2
        if self.game.spotting.position in [7,32,14,39,21,46,47,22]:
            self.game.selection = 1

    def scan_feature(self):
        self.feature_probability()
        self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def animate_feature_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.jockey_club.feature_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="feature_animation", delay=0.05, handler=self.animate_feature_scan, param=args)
        else:
            self.cancel_delayed(name="feature_animation")
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)
            self.scan_feature()

    def scan_clover(self):
        self.clover_probability()
        self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)

    def animate_clover_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.jockey_club.clover_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="clover_animation", delay=0.05, handler=self.animate_clover_scan, param=args)
        else:
            self.cancel_delayed(name="clover_animation")
            self.delay(name="display", delay=0.1, handler=graphics.jockey_club.display, param=self)
            self.scan_clover()

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


class JockeyClub(procgame.game.BasicGame):
    """ Turf King was one of the last one balls made by Bally """
    def __init__(self, machine_type):
        super(JockeyClub, self).__init__(machine_type)
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
        self.odds = units.Stepper("odds", 10)
        self.four_hundred = units.Stepper("four_hundred", 400, "jockey_club", "continuous")
        r = random.randint(0,399)
        self.four_hundred.position = r
        self.feature_unit = units.Stepper("feature_unit", 45)
        r = random.randint(0,44)
        self.feature_unit.position = r
        self.coin = units.Stepper("coin", 4)
        self.name = units.Stepper("name", 5)
        r = random.randint(0,8)
        self.name.position = r


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
        self.hold3 = units.Relay("hold3")
        self.hold4 = units.Relay("hold4")
        self.hold5 = units.Relay("hold5")
        self.horseshoe = units.Relay("horseshoe")
        self.left = units.Relay("left")
        self.right = units.Relay("right")
        self.left_right = units.Relay("left_right")
        self.lettera = units.Relay("lettera")
        self.letterb = units.Relay("letterb")
        self.letterc = units.Relay("letterc")
        self.letterd = units.Relay("letterd")
        self.purse_win = units.Relay("purse_win")
        self.show_win = units.Relay("show_win")
        self.pennant = units.Relay("pennant")

        #Tilt is separate from anti-cheat in that the trip will move the shutter
        #when the game is tilted with 1st ball in the lane.  Also prevents you
        #from picking back up by killing the anti-cheat.  Can be engaged by
        #tilt bob, slam tilt switches, or timer at 39th step.
        #Immediately kills motors.
        self.tilt = units.Relay("tilt")

        self.replays = 0
        self.returned = False
        self.selection = None
        self.selection2 = None

    def reset(self):
        super(JockeyClub, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')

        main_mode = OneBall(self)
        self.modes.add(main_mode)

game = JockeyClub(machine_type='pdb')
game.reset()
game.run_loop()
