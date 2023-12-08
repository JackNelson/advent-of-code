class Ship:
    def __init__(self, compass_dir="N", waypoint=(0, 0)):

        self.horz_dist = 0
        self.vert_dist = 0
        self.horz_dir = ""
        self.vert_dir = ""

        self.horz_waypoint = waypoint[0]
        self.vert_waypoint = waypoint[1]
        self.update_horz_waypoint_dir()
        self.update_vert_waypoint_dir()

        self.compass_dir = compass_dir
        self.init_compass()

        self.nav_waypoint_dict = {
            "N": (1, self.update_vert_waypoint),
            "S": (-1, self.update_vert_waypoint),
            "E": (1, self.update_horz_waypoint),
            "W": (-1, self.update_horz_waypoint),
            "R": (1, self.rotate_waypoint),
            "L": (-1, self.rotate_waypoint),
            "F": (1, self.move_toward_waypoint),
        }

        self.nav_dict = {
            "N": (1, self.update_vert_dist),
            "S": (-1, self.update_vert_dist),
            "E": (1, self.update_horz_dist),
            "W": (-1, self.update_horz_dist),
            "R": (1, self.update_compass),
            "L": (-1, self.update_compass),
            "F": (1, self.move_forward),
        }

    def init_compass(self):
        """maps direction in degrees to compass direction (0 deg = 'N')"""

        d = {"N": 0, "E": 90, "S": 180, "W": 270}

        self.compass = d[self.compass_dir]

    def update_compass(self, val):
        """updates compass in degrees"""

        self.compass += val

        if self.compass < 0:
            self.compass += 360
        elif self.compass >= 360:
            self.compass -= 360

        self.update_compass_dir()

    def update_compass_dir(self):
        """updates compass direction to compass in degrees (0 deg = 'N')"""

        d = {0: "N", 90: "E", 180: "S", 270: "W"}

        self.compass_dir = d[self.compass]

    def rotate_waypoint(self, val):
        """rotates the waypoint based on rotation in degrees"""

        # save current compass, waypoint for later use
        tmp_compass_dir = self.compass_dir
        tmp_horz_waypoint = self.horz_waypoint
        tmp_vert_waypoint = self.vert_waypoint

        # rotate compass
        self.update_compass(val)

        # update waypoint based on new compass direction
        if self.compass_dir == "E":
            self.horz_waypoint = tmp_vert_waypoint
            self.vert_waypoint = -1 * tmp_horz_waypoint

        elif self.compass_dir == "S":
            self.horz_waypoint *= -1
            self.vert_waypoint *= -1

        elif self.compass_dir == "W":
            self.horz_waypoint = -1 * tmp_vert_waypoint
            self.vert_waypoint = tmp_horz_waypoint

        else:
            pass

        # reset the waypoint directions
        self.update_horz_waypoint_dir()
        self.update_vert_waypoint_dir()

        # reset the compass
        self.compass_dir = tmp_compass_dir
        self.init_compass()

    def update_horz_dist(self, val):
        """updates horizontal distance traveled"""

        self.horz_dist += val
        self.update_horz_dir()

    def update_vert_dist(self, val):
        """updates vertical distance traveled"""

        self.vert_dist += val
        self.update_vert_dir()

    def update_horz_dir(self):
        """updates horizontal direction of distance traveled"""

        if self.horz_dist < 0:
            self.horz_dir = "W"
        elif self.horz_dist > 0:
            self.horz_dir = "E"
        else:
            self.horz_dir = ""

    def update_vert_dir(self):
        """updates vertical direction of distance traveled"""

        if self.vert_dist < 0:
            self.vert_dir = "S"
        elif self.vert_dist > 0:
            self.vert_dir = "N"
        else:
            self.vert_dir = ""

    def update_horz_waypoint(self, val):
        """updates the horizontal waypoint"""

        self.horz_waypoint += val
        self.update_horz_waypoint_dir()

    def update_vert_waypoint(self, val):
        """updates the vertical waypoint"""

        self.vert_waypoint += val
        self.update_vert_waypoint_dir()

    def update_horz_waypoint_dir(self):
        """updates the horizontal direction of waypoint"""

        if self.horz_waypoint < 0:
            self.horz_waypoint_dir = "W"
        elif self.horz_waypoint > 0:
            self.horz_waypoint_dir = "E"
        else:
            self.horz_dir = ""

    def update_vert_waypoint_dir(self):
        """updates the vertical direction of waypoint"""

        if self.vert_waypoint < 0:
            self.vert_waypoint_dir = "S"
        elif self.vert_waypoint > 0:
            self.vert_waypoint_dir = "N"
        else:
            self.vert_dir = ""

    def move_forward(self, val):
        """updates distance in direction of compass"""

        self.move(self.compass_dir, val)

    def move_toward_waypoint(self, val):
        """updates distance in direction of waypoint"""

        self.update_horz_dist(val * self.horz_waypoint)
        self.update_vert_dist(val * self.vert_waypoint)

    def update_command_val(self, command, val):
        """updates command values depending on command"""

        return val * self.nav_dict[command][0]

    def get_command_func(self, command):
        """gets the function relative to command"""

        return self.nav_dict[command][1]

    def move(self, command, val):
        """move using the compass assumptions"""

        func = self.get_command_func(command)
        val = self.update_command_val(command, val)

        func(val)

    def update_waypoint_command_val(self, command, val):
        """updates waypoint command values depending on command"""

        return val * self.nav_waypoint_dict[command][0]

    def get_waypoint_command_func(self, command):
        """gets the waypoint function relative to command"""

        return self.nav_waypoint_dict[command][1]

    def waypoint_move(self, command, val):
        """move using the waypoint direction"""

        func = self.get_waypoint_command_func(command)
        val = self.update_waypoint_command_val(command, val)

        func(val)

    def print_status(self):
        """prints current location compared to starting point"""

        print(
            f"{self.horz_dir}{abs(self.horz_dist)}, {self.vert_dir}{abs(self.vert_dist)}"
        )

    def print_waypoint(self):
        """prints current waypoint status"""

        print(
            f"{self.horz_waypoint_dir}{abs(self.horz_waypoint)}, {self.vert_waypoint_dir}{abs(self.vert_waypoint)}"
        )

    def calc_manhattan_dist(self):
        """calculates the manhattan distance based on the distance traveled"""

        return abs(self.horz_dist) + abs(self.vert_dist)


with open("data/day12.txt", "r") as f:
    data = [x.replace("\n", "") for x in f.readlines()]

print("Part A: \n")
compass_dir = input("What direction is the ship initially pointing? (N,S,E,W): ")
ferry = Ship(compass_dir=compass_dir)

for instruction in data:
    command = instruction[0]
    val = int(instruction[1:])

    ferry.move(command, val)

ferry.print_status()
print(f"Final Manhattan distance: {ferry.calc_manhattan_dist()}")

print("\nPart B: \n")
waypoint_horz = int(input("What is the waypoint horizontal distance? (-W/+E) "))
waypoint_vert = int(input("What is the waypoint vertical distance? (-S/+N) "))
ferry = Ship(waypoint=(waypoint_horz, waypoint_vert))

for instruction in data:
    command = instruction[0]
    val = int(instruction[1:])

    ferry.waypoint_move(command, val)

ferry.print_status()
print(f"Final Manhattan distance: {ferry.calc_manhattan_dist()}")