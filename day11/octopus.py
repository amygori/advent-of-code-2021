class Octopus:
    def __init__(self, energy_level, x, y):
        self.energy_level = energy_level
        self.x = x  # horizontal (num)
        self.y = y  # vertical (line)
        if self.y > 0:
            self.up = (self.x, self.y - 1)
        else:
            self.up = None
        if self.x < 9:
            self.right = (self.x + 1, self.y)
        else:
            self.right = None
        if self.x < 9 and self.y < 9:
            self.diag_down_right = (self.x + 1, self.y + 1)
        else:
            self.diag_down_right = None
        if self.y < 9:
            self.down = (self.x, self.y + 1)
        else:
            self.down = None
        if self.x > 0 and self.y < 9:
            self.diag_down_left = (self.x - 1, self.y + 1)
        else:
            self.diag_down_left = None
        if self.x > 0:
            self.left = (self.x - 1, self.y)
        else:
            self.left = None
        if self.y > 0 and self.x > 0:
            self.diag_up_left = (self.x - 1, self.y - 1)
        else:
            self.diag_up_left = None
        if self.x < 9 and self.y > 0:
            self.diag_up_right = (self.x + 1, self.y - 1)
        else:
            self.diag_up_right = None
        self.flashed = False
        self.flashed_on_step = None

    def __repr__(self):
        return f"<🐙 ({self.x}, {self.y}) energy={self.energy_level} flashed={self.flashed}>"

    def increase_energy_level(self, step):
        self.energy_level += 1

    def flash(self, step):
        if self.flashed_on_step == step:
            return
        self.flashed = True
        self.flashed_on_step = step

    def reset_flashed_state(self):
        self.flashed = False

    def reset_energy_level(self):
        self.energy_level = 0

    def flashed_on_this_step(self, step):
        return self.flashed and (step == self.flashed_on_step)

    @property
    def adjacents(self):
        return [
            self.up,
            self.diag_up_right,
            self.right,
            self.diag_down_right,
            self.down,
            self.diag_down_left,
            self.left,
            self.diag_up_left,
        ]
