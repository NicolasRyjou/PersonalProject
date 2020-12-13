

class Handling:

    def __init__(self):
        self.output = ''

    def move(self, command_name, which_arm):

        if command_name == "Move_Right":
            self.output = 'r'

        if command_name == "Move_Left":
            self.output = 'l'

        print("{} is an Unknown command\nPossible commands:{}, {}".format(
            command_name, "BASE_MOVE_LEFT", "BASE_MOVE_RIGHT")
        )

        if not which_arm:
            print("Please specify which arm you want to move")
        else:
            if which_arm == 1:
                if command_name == "PULL_UP":
                    self.output = 'a'
                elif command_name == "PULL_DOWN":
                    self.output = 's'
            if which_arm == 2:
                if command_name == "PULL_UP":
                    self.output = 'd'
                elif command_name == "PULL_DOWN":
                    self.output = 'f'
            if which_arm == 3:
                if command_name == "PULL_UP":
                    self.output = 'g'
                elif command_name == "PULL_DOWN":
                    self.output = 'h'

    def grip_arm(self, bool_claws):
        if not bool_claws:
            self.output = 'c'
        elif bool_claws:
            self.output = 'o'

    def rotor_grip_arm(self, command_name):
        if command_name == "Move_Left":
            self.output = 'j'
        elif command_name == "Move_Right":
            self.output = 'b'

    def special_commands(self, command):
        if command == "hc04_restart":
            self.output = 'n'
        if command == "360_action":
            self.output = 'z'
        if command == "throw_action":
            self.output = 'x'
        if command == "shake_action":
            self.output = 'c'
