import random
import procgame

class Stepper:
    def __init__(self, name, top, gamename=None, t=None):
        self.name = name
        self.position = 0
        self.top = top
        self.t = t
        self.gamename = gamename
    def step(self):
        if self.position != self.top:
            self.position += 1
        else:
            if self.t == "continuous":
                self.position = 0
        return self.position
    def stepdown(self):
        if self.position != 0:
            self.position -= 1
        else:
            if self.t == "continuous":
                self.position = self.top
        return self.position
    def reset(self):
        self.position = 0
        return self.position
    
class Spotting:
    def __init__(self, name, top):
        self.name = name
        self.position = 0
        self.top = top
        self.movement_amount = 0
    def spin(self):
        if self.name == 'flash':
            self.movement_amount = random.randint(7,18)
        else:
            self.movement_amount = random.randint(8,20)
        if self.position + self.movement_amount > self.top:
            self.position = (self.position + self.movement_amount) - self.top
        else: 
            self.position += self.movement_amount
        return self.position
    def connected_rivet(self, gamename=None):
        return self.position

class Motor:
    def __init__(self, name, top):
        self.name = name
        self.position = 0
        self.top = top
        self.movement_amount = 0
    def spin(self):
        self.movement_amount = random.randint(0, self.top)
        if self.position + self.movement_amount > self.top:
            self.position = (self.position + self.movement_amount) - self.top
        else: 
            self.position += self.movement_amount
        return self.position
    def connected_rivet(self, gamename=None):
        return self.position

class Mixer:
    def __init__(self, name, top):
        self.name = name
        self.position = 0
        self.top = top
    def spin(self):
        if self.name != "mixer1":
            if self.name == "mixer2":
                movement_amount = random.randint(3,10)
                if self.position + movement_amount > self.top:
                    self.position = (self.position + movement_amount) - self.top
                else:
                    self.position += movement_amount
            elif self.name == "mixer3":
                movement_amount = random.randint(2,7)
                if self.position + movement_amount > self.top:
                    self.position = (self.position + movement_amount) - self.top
                else:
                    self.position += movement_amount
            elif self.name == "mixer4":
                movement_amount = random.randint(2,9)
                if self.position + movement_amount > self.top:
                    self.position = (self.position + movement_amount) - self.top
                else:
                    self.position += movement_amount
            elif self.name == "mixer5":
                movement_amount = random.randint(2,10)
                if self.position + movement_amount > self.top:
                    self.position = (self.position + movement_amount) - self.top
                else:
                    self.position += movement_amount
        else:
            movement_amount = 1
            if self.position + movement_amount > self.top:
                self.position = 0
            else:
                self.position += movement_amount
        return self.position
    def step(self):
        movement_amount = 1
        if self.position + movement_amount > self.top:
            self.position = 0
        else:
            self.position += movement_amount
    def connected_rivet(self, gamename=None):
        # Here's the sticky part - we have to identify the wire that is connected.  Looking at the schematic of the mixer,
        # it appears that there are three different wires that allow current to pass through the unit.  For Coney Island
        # these wires are 14-3, 15-3 and 18-3. Based on other early Bally mixers, it appears that there are three dead
        # (disconnected) rivets. 0 maps to a dead rivet, 1 maps to 14-3, 2 maps to 15-3 and 3 maps to 18-3. Note that I
        # can only add this to the base Mixer class on games like Coney Island that have a single mixer unit.
        if gamename == "coney_island":
            if self.position % 5 == 0:
                return 0
            elif self.position % 4 == 0:
                return 1
            elif self.position % 3 == 0:
                return 2
            elif self.position % 2 == 0:
                return 3
            else:
                return 3
        else:
            return self.position

class Search:
	def __init__(self, name, top):
            self.name = name
            self.position = 0
            self.top = top
	def spin(self):
            if self.position + 1 > self.top:
                self.position = 0
            else:
                self.position += 1
            return self.position
        def connected_rivet(self):
            return self.position

class Relay:
    def __init__(self, name):
        self.name = name
        self.status = False
    def engage(self, game):
        self.status = True
        return self.status
    def disengage(self):
        self.status = False
        return self.status

class Reflex:
    def __init__(self, name, top):
        self.name = name
        self.position = 100
        self.top = top
    def increase(self):
        self.position += 2
        return self.position
    def decrease(self):
        self.position -= 1
        return self.position
    def connected_rivet(self, max=4):
        # See my mixer comments above - in this case, the mixer has four different rivets. unlike the mixer though, the
        # reflex wll connect up to all four rivets at once.  On the reflex, the last rivet onnected will actually bypass
        # the mixer, so there is no need to check the mixer depending on which rivets are returned.  The mixer will not
        # prevent the step of the EB unit if the reflex is connected on all four rivets.  If the reflex is on only three
        # rivets, the mixer is essentially bypassed, unless the mixer.connected_rivet() == 0.  The reflex can actually
        # step beyond the last rivet, which means that the machine is as tight as it can possibly be - it will be very
        # difficult to get an extra ball. The common feeds into the reflex, and it outputs on the same 14-3, 15-3 and 18-3
        # used by the mixer unit, however, there is also that bypass rivet with wire 21-3.
        if max == 4:
            if self.position > 200:
                return 0
            elif self.position <= 50:
                return 4
            elif self.position <= 100:
                return 3
            elif self.position <= 150:
                return 2
            elif self.position <= 200:
                return 1
        else:
            if self.position > 200:
                return 0
            elif self.position <= 25:
                return 5
            elif self.position <= 65:
                return 4
            elif self.position <= 105:
                return 3
            elif self.position <= 145:
                return 2
            elif self.position <= 200:
                return 1
