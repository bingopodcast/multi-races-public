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
from multi_races.graphics.citation import *

class OneBall(procgame.game.Mode):
    def __init__(self, game):
        super(OneBall, self).__init__(game=game, priority=5)
        self.holes = []
        self.startup()
        self.game.sound.register_sound('tilt', "audio/tilt.wav")
        self.game.sound.register_sound('step', "audio/step.wav")


    def sw_coin_active(self, sw):
        self.game.tilt.disengage()
        if self.game.start.status == False:
            self.game.horseshoe.disengage()
            self.game.all_advantages.engage(self.game)
        self.regular_play()
        self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def regular_play(self):
        self.cancel_delayed(name="replay_step_up")
        self.game.cu = not self.game.cu
        self.game.coin.step()
        self.game.search_index.disengage()
        self.game.coils.counter.pulse()
        self.game.coils.motor.enable()
        self.game.coils.timing.pulse()
        begin = self.game.spotting.position
        self.game.spotting.spin()
        if self.game.switches.shutter.is_inactive():
            self.game.coils.shutter.enable()
        self.game.replay_counter.reset()
        self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)
        self.game.tilt.disengage()
        if self.game.start.status == False:
            self.game.odds.reset()
            if self.game.fan.status == True:
                self.game.fan.disengage()
            self.game.clover.disengage()
            self.game.horseshoe.disengage()
            self.game.left.disengage()
            self.game.right.disengage()
            self.game.left_right.disengage()
            self.game.purse_win.disengage()
            self.game.show_win.disengage()
            self.game.pennant.disengage()
        self.scan_all(begin)
        self.game.reflex.decrease()
        self.replay_step_down()
        self.game.horseshoe.disengage()
        self.game.all_advantages.engage(self.game)

    def sw_lane_active(self, sw):
        self.game.start.engage(self.game)

    def sw_smRunout_active_for_10ms(self, sw):
        self.game.coils.shutter.disable()

    def sw_lane_inactive_for_15ms(self, sw):
        self.game.start.disengage()
        self.game.all_advantages.disengage()
        self.game.horseshoe.disengage()
        self.game.clover.disengage()
        self.game.all_advantages.engage(self.game)

    # This is really nasty, but it is how we render graphics for each individual hole.

    def sw_purse1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("purse")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def sw_purse2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("purse")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def sw_purse3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("purse")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def sw_purse4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("purse")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def sw_purse5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("purse")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def sw_purse6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("purse")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def sw_purse7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("purse")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def sw_show1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("show")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def sw_show2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("show")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def sw_show3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("show")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def sw_show4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("show")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def sw_show5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("show")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def sw_show6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("show")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def sw_show7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("show")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def sw_place1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("place")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def sw_place2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("place")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def sw_place3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("place")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def sw_place4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("place")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def sw_place5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("place")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def sw_place6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("place")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def sw_place7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("place")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def sw_win1_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("win")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def sw_win2_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("win")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def sw_win3_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("win")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def sw_win4_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("win")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def sw_win5_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("win")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def sw_win6_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("win")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def sw_win7_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("win")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def sw_feature_active_for_40ms(self, sw):
        if self.game.tilt.status == False and self.game.start.status == False:
            self.search("feature")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)
    
    def sw_replayReset_active(self, sw):
        self.game.anti_cheat.disengage()
        graphics.citation.display(self)
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
        self.game.left.disengage()
        self.game.right.disengage()
        self.game.replay_counter.reset()
        self.game.fan.disengage()
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
        self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def sw_tilt_active(self, sw):
        if self.game.tilt.status == False:
            self.tilt_actions()

    def replay_step_down(self, number=0):
        if number > 0:
            if number > 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.citation.reel1, graphics.citation.reel10, graphics.citation.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.citation.display(self)
                self.delay(name="replay_reset", delay=0.13, handler=self.replay_step_down, param=number)
            elif number == 1:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.citation.reel1, graphics.citation.reel10, graphics.citation.reel100)
                self.game.coils.registerDown.pulse()
                number -= 1
                graphics.citation.display(self)
                self.cancel_delayed(name="replay_reset")
        else:
            if self.game.replays > 0:
                self.game.replays -= 1
                graphics.replay_step_down(self.game.replays, graphics.citation.reel1, graphics.citation.reel10, graphics.citation.reel100)
                self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)
            self.game.coils.registerDown.pulse()

    def sw_leftcap_active(self, sw):
        if self.game.left.status == True:
            self.winner_replay_step_up(4)
            self.game.name.step()
            self.game.coils.four_hundred.pulse()
            if self.game.name.position == 5:
                self.winner_replay_step_up(40)
        self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def sw_rightcap_active(self, sw):
        if self.game.right.status == True:
            self.winner_replay_step_up(4)
            self.game.name.step()
            self.game.coils.four_hundred.pulse()
            if self.game.name.position == 5:
                self.winner_replay_step_up(40)
        self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def sw_bumpera_active(self, sw):
        if self.game.lettera.status == False:
            self.game.coils.bumperALamp.enable()
            self.game.coils.four_hundred.pulse()
            self.game.lettera.engage(self.game)


    def sw_bumperb_active(self, sw):
        if self.game.letterb.status == False:
            if self.game.lettera.status == True:
                self.game.coils.bumperBLamp.enable()
                self.game.coils.four_hundred.pulse()
                self.game.letterb.engage(self.game)

    def sw_bumperc_active(self, sw):
        if self.game.letterc.status == False:
            if self.game.letterb.status == True:
                self.game.coils.bumperCLamp.enable()
                self.game.coils.four_hundred.pulse()
                self.game.letterc.engage(self.game)

    def sw_bumperd_active(self, sw):
        if self.game.letterd.status == False:
            if self.game.letterc.status == True:
                self.game.coils.bumperDLamp.enable()
                self.game.coils.four_hundred.pulse()
                self.game.letterd.engage(self.game)
                self.game.abcd.engage(self.game)

    def replay_step_up(self):
        if self.game.replays < 899:
            self.game.replays += 1
            graphics.replay_step_up(self.game.replays, graphics.citation.reel1, graphics.citation.reel10, graphics.citation.reel100)
        self.game.coils.registerUp.pulse()
        self.game.reflex.increase()
        graphics.citation.display(self)

    def sw_horseshoe_active(self, sw):
        if self.game.switches.clover.is_active() and self.game.switches.flag.is_active():
           self.game.end_run_loop()
           os.system("/home/nbaldridge/proc/multi-races/multi_races/start_game.sh citation")
        else:
            if self.game.horseshoe.status == True and (self.game.replays > 0 or self.game.switches.freeplay.is_active()):
                self.game.regular_play()
                return
            if self.game.horseshoe.status == False:
                self.game.all_advantages.disengage()
                self.game.horseshoe.engage(self.game)
                self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)
                self.delay(name="horseshoe", delay=0.1, handler=self.sw_horseshoe_active, param=sw)

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
                return 160

    def find_winner(self, selection, area):
        if self.game.search_index.status == False and self.game.replays < 899:
            purse = self.get_odds("purse")
            show = self.get_odds("show")
            place = self.get_odds("place")
            win = self.get_odds("win")
            if self.game.abcd.status == True:
                purse = purse * 2
                show = show * 2
                place = place * 2
                win = win * 2
            if self.game.show_win.status == True:
                show = win
            if self.game.purse_win.status == True:
                purse = win
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
            self.delay(name="replay_step_up", delay=0.25, handler=self.winner_replay_step_up, param=number)
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
        self.game.purse_win.disengage()
        self.game.show_win.disengage()

    def check_initial_portioning(self):
        if self.game.coin.position % 3 == 0:
            return True
        if self.game.abcd.status == False:
            if self.game.odds.position <= 6:
                return True
            elif self.game.odds.position in [7,8]:
                if self.game.reflex.connected_rivet() <= 1:
                    return True
            elif self.game.odds.position in [9,10]:
                if self.game.reflex.connected_rivet() <= 3:
                    return True
        else:
            return False

    def scan_all(self, begin):
        if self.game.all_advantages.status == True:
            s = self.animate_star_scan([begin,self.game.spotting.position,1])
            i = self.animate_clover_scan([begin,self.game.spotting.position,1])
            self.game.selection = []
            u = self.animate_selection_scan([begin,self.game.spotting.position,1])
        if self.game.horseshoe.status == True:
            v = self.animate_feature_scan([begin,self.game.spotting.position,1])
            self.check_hold()

        self.game.four_hundred.step()

        if self.game.spotting.position in [37,12]:
            self.game.left_right.engage(self.game)
            if self.game.cu:
                self.game.left.disengage()
                self.game.right.engage(self.game)
            else:
                self.game.right.disengage()
                self.game.left.engage(self.game)

        if self.game.spotting.position in [22, 47]:
            if self.game.four_hundred.position % 20 == 0:
                self.game.pennant.engage(self.game)

    def check_hold(self):
        if self.game.reflex.connected_rivet() >= 2 or self.game.four_hundred.position % 3 == 0.15:
            if self.game.reflex.connected_rivet() <= 4 or self.game.four_hundred.position % 3 == 0.15:
                if self.game.reflex.connected_rivet() <= 1:
                    if self.game.spotting.position == 19:
                        self.game.purse_win.engage(self.game)
                    if self.game.spotting.position == 18:
                        self.game.show_win.engage()

    def scan_star(self):
        self.star_probability()
        self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def animate_star_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.citation.star_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="star_animation", delay=0.05, handler=self.animate_star_scan, param=args)
        else:
            self.cancel_delayed(name="star_animation")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)
            self.scan_star()
            self.game.coils.motor.disable()

    def star_probability(self):
        self.check_odds()

    def check_odds(self):
        p = self.check_initial_portioning()
        if p == True:
            if self.game.odds.position < 4:
                self.game.odds.step()
                self.game.coils.four_hundred.pulse()
                return
            else:
                if self.game.spotting.position == 25:
                    if self.game.odds.position == 3:
                        self.check_extra_step()
                elif self.game.spotting.position == 26:
                    if self.game.odds.position == 4:
                        self.check_extra_step()
                elif self.game.spotting.position == 27:
                    if self.game.odds.position == 5:
                        self.check_extra_step()
                elif self.game.spotting.position == 21:
                    if self.game.odds.position == 6:
                        self.check_extra_step()
                elif self.game.spotting.position == 36:
                    if self.game.odds.position == 7:
                        self.check_extra_step()
                elif self.game.spotting.position == 37:
                    if self.game.odds.position == 8:
                        self.check_extra_step()
                elif self.game.spotting.position == 40:
                    if self.game.four_hundred.position % 5 == 0:
                        if self.game.odds.position in [8,9]:
                            self.check_extra_step()
                elif self.game.spotting.position == 42:
                    if self.game.four_hundred.position % 10 == 0:
                        if self.game.odds.position in [8,9]:
                            self.check_extra_step()

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
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)
            number -= 1
            self.delay(name="step_odds", delay=0.1, handler=self.step_odds, param=number)

    def scan_selection(self):
        self.selection_probability()
        self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def animate_selection_scan(self, args):
        if self.game.fan.status == True:
            self.game.selection = [1,2,3,4,5,6,7]
            return
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.citation.selection_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="selection_animation", delay=0.05, handler=self.animate_selection_scan, param=args)
        else:
            self.cancel_delayed(name="selection_animation")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)
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

    def feature_probability(self):
        if self.game.spotting.position in [2,41,27,16,8,33,23,48]:
            if self.game.spotting.position in [2,41,27,16]:
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


    def scan_feature(self):
        self.feature_probability()
        self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def animate_feature_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.citation.feature_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="feature_animation", delay=0.05, handler=self.animate_feature_scan, param=args)
        else:
            self.cancel_delayed(name="feature_animation")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)
            self.scan_feature()
            self.game.coils.motor.disable()

    def scan_clover(self):
        self.clover_probability()
        self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)

    def animate_clover_scan(self, args):
        start = args[0]
        diff = args[1]
        num = args[2]
        if start + num >= 50:
            start = 0
        if diff >= 0:
            num = num + 1
            graphics.citation.clover_animation([self, start + num])
            self.cancel_delayed(name="display")
            diff = diff - 1
            args = [start,diff,num]
            self.delay(name="clover_animation", delay=0.05, handler=self.animate_clover_scan, param=args)
        else:
            self.cancel_delayed(name="clover_animation")
            self.delay(name="display", delay=0.1, handler=graphics.citation.display, param=self)
            self.scan_clover()
            self.game.coils.motor.disable()

    def check_reflex(self):
        if self.game.reflex.connected_rivet() == 5:
            if self.game.abcd.status == False or self.game.mixer1.connected_rivet("citation") not in [3,10,14,20]:
                return 1
        elif self.game.reflex.connected_rivet() == 4 and self.game.mixer1.connected_rivet("citation") not in [2,3,4,5,7,9,10,12,15,17,19,20,21,23]:
            if self.game.abcd.status == False or self.game.mixer1.connected_rivet("citation") not in [3,10,14,20]:
                return 1
        elif self.game.reflex.connected_rivet() == 3 and self.game.mixer1.connected_rivet("citation") not in [2,5,7,9,12,15,19,23]:
            if self.game.abcd.status == False or self.game.mixer1.connected_rivet("citation") not in [3,10,14,20]:
                return 1
        elif self.game.reflex.connected_rivet() == 2 and self.game.mixer1.connected_rivet("citation") not in [5,9,12,15,19,23]:
            if self.game.abcd.status == False or self.game.mixer1.connected_rivet("citation") not in [3,10,14,20]:
                return 1
        elif self.game.reflex.connected_rivet() == 1 and self.game.mixer1.connected_rivet("citation") not in [5,9,15,23]:
            if self.game.abcd.status == False or self.game.mixer1.connected_rivet("citation") not in [3,10,14,20]:
                return 1
        else:
            return 0

    def clover_probability(self):
        if self.check_reflex() == 1:
            #path 1
            if self.game.number_four.status == False:
                if [3,5] not in self.game.selection:
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
            if self.game.spotting.position == 24 and self.game.odds.position == 3:
                self.game.fan.engage(self.game)
                self.game.selection = [1,2,3,4,5,6,7]
            if self.game.spotting.position == 13 and self.game.odds.position == 2:
                self.game.fan.engage(self.game)
                self.game.selection = [1,2,3,4,5,6,7]

    # Define reset as the knock-off, anti-cheat relay disabled, and replay reset enabled.  Motors turn while credits are knocked off.
    # When meter reaches zero and the zero limit switch is hit, turn off motor sound and leave backglass gi on, but with tilt displayed.

    def startup(self):
        self.eb = False
        self.tilt_actions()


class Citation(procgame.game.BasicGame):
    """ Turf King was one of the last one balls made by Bally """
    def __init__(self, machine_type):
        super(Citation, self).__init__(machine_type)
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
        self.mixer2 = units.Mixer("mixer2", 23)
        self.mixer3 = units.Mixer("mixer3", 23)
        self.mixer4 = units.Mixer("mixer4", 23)

        self.number_four = units.Relay("number_four")

        self.spotting = units.Spotting("spotting", 50)
        r = random.randint(0,49)
        self.spotting.position = r

        self.search_index = units.Relay("search_index")

        #Replay Counter
        self.replay_counter = units.Stepper("replay_counter", 300)

        #Initialize stepper units used to keep track of features or timing.
        self.odds = units.Stepper("odds", 10)
        self.four_hundred = units.Stepper("four_hundred", 400, "citation", "continuous")
        r = random.randint(0,399)
        self.four_hundred.position = r
        self.feature_unit = units.Stepper("feature_unit", 45)
        r = random.randint(0,40)
        self.feature_unit.position = r
        self.coin = units.Stepper("coin", 6, "citation", "continuous")
        self.name = units.Stepper("name", 5)
        r = random.randint(0,4)
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
        self.fan = units.Relay("fan")
        self.all_advantages = units.Relay("all_advantages")
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
        super(Citation, self).reset()
        self.logger = logging.getLogger('game')
        self.load_config('bingo.yaml')

        main_mode = OneBall(self)
        self.modes.add(main_mode)

game = Citation(machine_type='pdb')
game.reset()
game.run_loop()
